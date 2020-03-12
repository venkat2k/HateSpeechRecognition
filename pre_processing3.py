from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

f = open("intermediatev2.csv", "r")
w = open("temp.csv", "w")

txt = f.read().split("\n")
for line in txt:
    try:
        cur = line.split(",")
        category = cur[0]
        content = cur[1].split(" ")
        out = []
        for x in content:
            out.append(stemmer.stem(x))
        content = " ".join(out)
        w.write(category + "," + content + "\n")
    except:
        pass
