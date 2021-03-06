from format_intents import searchTree, format_node_patterns
import random, json, torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from train import train

models = []

def init_models(file):
  format_node_patterns(file)
  generate_all_models(file)
  return file
  
def akinator_step(sentence, root_id = 0):
    sentence = tokenize(sentence)
    curr_model = get_model_by_id(root_id)
    X = bag_of_words(sentence, curr_model['all_words'])
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X)

    output = curr_model['model'](X)
    _, predicted = torch.max(output,dim=1)
    tag = curr_model['tags'][predicted.item()]
    
    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.83:
      return tag
    else:
      print("I do not understand")
      return None


def generate_all_models(node):
  data = train(node)

  input_size = data["input_size"]
  hidden_size = data["hidden_size"]
  output_size = data["output_size"]
  all_words = data["all_words"]
  tags = data["tags"]
  model_state = data["model_state"]

  model = NeuralNet(input_size, hidden_size, output_size)
  model.load_state_dict(model_state)
  model.eval()
  models.append({"id":node['id'], "node":node, "model":model, "all_words": all_words, "tags": tags})

  if node['children'] is not None:
    for child in node['children']:
      try:
        if child['children'] is not None:
          generate_all_models(child)
      except:
        pass
  
def get_model_by_id(id):
  for model in models:
    if model['id'] == id:
      return model
  return None

def akinator(sentence, root):
  lowest_id = root["id"]
  found_tag = akinator_step(sentence, lowest_id)
  lowest_node = root
  while found_tag is not None:
    lowest_node = searchTree(root,"tag",found_tag)
    lowest_id = lowest_node['id']
    try:
      if lowest_node['children'] is not None:
        found_tag = akinator_step(sentence, lowest_id)
    except:
      break

  return lowest_node

