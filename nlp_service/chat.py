import random, json, torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from train import FILE

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json','r') as f:
  intents = json.load(f)

data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

print("Lets chat! tap 'quit' to quit")
while True:
  sentence = input("Insert your question:")
  if sentence == "quit":
    break

  sentence = tokenize(sentence)
  X = bag_of_words(sentence, all_words)
  X = X.reshape(1,X.shape[0])
  X = torch.from_numpy(X)

  output = model(X)
  _, predicted = torch.max(output,dim=1)
  tag = tags[predicted.item()]
  
  probs = torch.softmax(output,dim=1)
  prob = probs[0][predicted.item()]

  if prob.item() > 0.75:
    print(tag)
  else:
    print("I do not understand")
