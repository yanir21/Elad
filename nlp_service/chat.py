import random, json, torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from train import train

# print("Lets chat! tap 'quit' to quit")
# while True:
#   sentence = input("Insert your question:")
#   if sentence == "quit":
#     break

models = []

def init():
  with open('intents.json','r') as f:
    file = json.load(f)
  
  generate_all_models(file)
  

def akinator(sentence, root_id = 0):
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

    if prob.item() > 0.75:
      print(tag)
    else:
      print("I do not understand")


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

init()
akinator("I have a problem in my db")
  

  
    

  