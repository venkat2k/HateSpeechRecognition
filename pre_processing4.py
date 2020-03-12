train = open("training_set.csv", "w")
test = open("test_set.csv", "w")

f = open("temp.csv", "r")

txt = f.read().split("\n")
choices = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
import random

for line in txt:
    if random.choice(choices):
        test.write(line + "\n")
    else:
        train.write(line + "\n")