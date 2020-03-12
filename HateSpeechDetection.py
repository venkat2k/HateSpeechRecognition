from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.naive_bayes import GaussianNB
import numpy
import csv
import re

class HateSpeechDetector:
    def __init__(self, language):
        self.language = language
        self.stopwords = stopwords.words(language)
        self.stemmer = SnowballStemmer(language)

    def read_training_data(self, filename):
        f = open(filename, "r")
        w = open("training_set.csv", "w")
        csv_reader = csv.reader(f)
        self.training_labels = []
        for line in csv_reader:
            try:
                self.training_labels.append(line[0])
                w.write(line[1] + "\n")
            except:
                pass
        w.close()
    def preprocess(self, text, additional = []):
        text = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text)
        self.stopwords += additional
        self.stopwords = list(set(self.stopwords))
        sw = []
        for word in self.stopwords:
            sw.append(" " + word + " ")
            sw.append(word + " ")
        self.stopwords = sw
        for word in self.stopwords:
            text = re.sub(word, "", text)
        # print("before stemming", text)
        stemmed_words = []
        words = text.split(" ")
        for word in words:
            stemmed_words.append(self.stemmer.stem(word))
        text = " ".join(stemmed_words)
        text = text.lower()
        return text
    
    def preprocess_training_set(self, filename, additional = []):
        f = open(filename, "r")
        csv_reader = csv.reader(f)
        self.training_labels = []
        self.stopwords += additional
        self.stopwords = list(set(self.stopwords))
        self.training_features = []
        for line in csv_reader:
            try:
                self.training_labels.append(line[0])
                self.training_features.append((self.preprocess(line[1], additional)))
            except:
                pass
        w.close()
        f.close()

    def train(self):
        self.training_features = []
        self.training_labels = []
        f = open("training_set.csv", "r")
        csv_reader = csv.reader(f)
        for line in csv_reader:
            try:
                self.training_labels.append(line[0])
                self.training_features.append(line[1])
            except:
                pass
        self.training_features = numpy.array(self.training_features)
        self.vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.8, stop_words=self.language)
        self.training_features = TfidfVectorizer.fit_transform(self.vectorizer, self.training_features, self.training_labels)
        self.selector = SelectPercentile(f_classif, percentile=95)
        self.selector.fit(self.training_features, self.training_labels)
        self.training_features = self.selector.transform(self.training_features).toarray()
        self.clf = GaussianNB()
        self.clf.fit(self.training_features, self.training_labels)
    
    def predict(self, text):
        text = self.preprocess(text)
        #print(text)
        test_features = numpy.array([text])
        test_features = TfidfVectorizer.transform(self.vectorizer, test_features)
        selector = SelectPercentile(f_classif, percentile=95)
        selector.fit(test_features, [1])
        test_features = selector.transform(test_features).toarray()
        result = self.clf.predict(test_features)
        return result
        #print(result)


        

        


