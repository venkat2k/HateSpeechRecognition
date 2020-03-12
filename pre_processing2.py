from nltk.corpus import stopwords

sw = stopwords.words("english")
l = sw[:]
import re
for word in sw:
    if "'" in word:
        l.append(re.sub("'", "", word))
others = ["u", "ok", "yo", "a", "b", "lol", "lmao", "ur", "amp", "ya", "woof", "my", "this"]
sw = l + others
for x in range(len(sw)):
    sw[x] = " " + sw[x] + " "
sw.extend(["i ", "im ", "yo", "my ", "u ", "this "])
f = open("intermediate.csv", "r")
w = open("temp.csv", "w")
txt = f.read()
for word in sw:
    txt = re.sub(word, " ", txt)
w.write(txt)
