from model import model

#calculate probability for a given observation
probability=model.probability([["none","no","on time","attend"]])

print(probability)
