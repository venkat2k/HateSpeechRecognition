import re

f = open("dataset.csv", "r")

txt = f.read()

lines = txt.split("\n")

out = ""
for line in lines:
    x = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",line)
    x = x.lower()
    typ = "YES"
    try:
        if x[0] == '0': typ = "NO"
        if x[0] == '1' or x[0] == '0':
            x = typ + "," + x[1:]
            x = re.sub("\d+", "", x)
            x = re.sub("rt", "", x)
            if x != "\n" and x != " " : out += x + "\n"
    except:
        pass
w = open("temp.csv", "w")
w.write(out)
w.close()
f.close()