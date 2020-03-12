f = open("training_set.csv", "r")

train_features = []
train_labels = []
txt = f.read().split("\n")
for line in txt:
    feature = line.split(",")
    try:
        train_features.append(feature[1])
        if feature[0] == "YES":
            train_labels.append(1)
        else:
            train_labels.append(0)
    except:
        pass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
import numpy
train_features = numpy.array(train_features)
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.8, stop_words='english')

train_features = TfidfVectorizer.fit_transform(vectorizer, train_features, train_labels)

selector = SelectPercentile(f_classif, percentile=75)
selector.fit(train_features, train_labels)
train_features = selector.transform(train_features).toarray()

from sklearn.naive_bayes import GaussianNB
import numpy as np


test = open("test_set.csv", "r")
test_features = []
test_labels = []
txt = test.read().split("\n")
for line in txt:
    feature = line.split(",")
    try:
        test_features.append(feature[1])
        if feature[0] == "YES":
            test_labels.append(1)
        else:
            test_labels.append(0)
    except:
        pass

test_features = numpy.array(test_features)
test_features = TfidfVectorizer.transform(vectorizer, test_features)

selector = SelectPercentile(f_classif, percentile=75)
selector.fit(test_features, test_labels)
test_features = selector.transform(test_features).toarray()


clf = GaussianNB()
clf.fit(train_features, train_labels)
out = clf.predict(test_features)
total = len(test_features)
correct = 0
for x in range(total):
    if out[x] == test_labels[x]:
        correct += 1
print(correct/total)