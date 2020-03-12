from HateSpeechDetection import HateSpeechDetector
import warnings
warnings.filterwarnings("ignore")
tool = HateSpeechDetector("english")
# tool.read_training_data("training_set.csv")
additional = ["u", "ok", "yo", "a", "b", "lol", "lmao", "ur", "amp", "ya", "woof", "my", "this", "i ", "im ", "yo", "my ", "u ", "this "]
#tool.preprocess_training_set("dataset.csv")
tool.train()
# f = open("test_set.csv", "r")
# import csv
# csv_reader = csv.reader(f)
# correct = 0
# total = 0
# for line in csv_reader:
#     try:
#         text = line[1]  
#         if line[0] == tool.predict(text):
#             correct += 1
#         total += 1
#     except:
#         pass
# print(correct / total, correct, total)
#print(tool.preprocess("good morning"))
print(tool.predict("good morning"))
print(tool.predict("you look beautiful. I think you are a queen"))
print(tool.predict("you are ugly"))
print(tool.predict("fuck off bitch"))
print(tool.predict("i hate muslims. I want them to die"))