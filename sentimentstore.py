#some globals: 
#best is min_lenght = 6 and num_of_words = 2


MIN_LENGHT_OF_STRING = 6
NUM_OF_WORDS_TO_PASS = 3

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

#nltk.download('stopwords')
class SentimentStore:
    def __init__(self):
        self.store = {}
        self.timesseen = {}
        self.pos = 0
        self.neg = 0
        self.totalwordcount = 0
        self.totalwordpaircount = 0
        self.wordcount = 0
        self.stop = self.loadStopWords()
        self.words_store = {} 
        
    def loadStopWords(self): 
        with open('stopwords.txt', 'r') as myfile:
            data=myfile.read()
        return data
    
    def addSoloWordScore(self, word, score):
        self.totalwordcount += 1
        if word not in self.words_store.keys(): 
            self.words_store[word] = score
            self.timesseen[word] = 1
            self.wordcount +=1
            if score >= 1: 
                self.pos += 1
            elif score <1: 
                self.neg += 1
        else: 
            self.words_store[word]+=score
            self.timesseen[word]+=1
    
    def printStopWords(self):
        print(self.stop)
        
    def getTotalWordPairCount(self):
        return self.totalwordpaircount 
    
    def getNumberOfWords(self):
        return self.wordcount

    def getNumberOfPositiveWords(self):
        return self.pos

    def getNumberOfNegativeWords(self):
        return self.neg

    def getTotalWordCount(self):
        return self.totalwordcount

    def addWordScore(self, word, score):
        self.totalwordpaircount += 1
        if word not in self.store.keys(): 
            self.store[word] = score 
            self.timesseen[word]=1
            self.wordcount += 1
            if score >=1 :
                self.pos += 1
            elif score <1:
                self.neg += 1
        else: 
            self.store[word]+= score
            self.timesseen[word]+=1
        return
        
    def addStringScore(self, s, score):
        N = NUM_OF_WORDS_TO_PASS - 1
        s = s.replace("#", "").replace("!", "").replace("-", "").replace("/", "").replace("<br", "").replace(":", "").replace("/>", "").replace(")", "").replace("(", "").replace('"', "").replace("}","").replace(".", "").replace("?", "").replace(",","").replace("\\", "").replace(":", "")
        
        #s = s.replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("0", "")
        words = s.split(" ")
        
        for i in range(N,len(words)):
            strang = ""
                
            if len(words[i]) >0:
                self.addSoloWordScore(words[i], score)
                for wrd in words[i-N:i+1]:
                    strang += " " + wrd
                    
                if len(strang) > MIN_LENGHT_OF_STRING: 
                    strang = strang.lower()
                    self.addWordScore(strang[1:], score)
        
    def getWordSentiment(self, word):
        if word in self.store.keys() :
            return self.store[word]
        elif word in self.words_store.keys():
            return self.words_store[word]
        return 0
    
    def getWordCount(self, word):
        if word in self.store.keys() or word in self.words_store.keys(): 
            return self.timesseen[word]
        return 0

    def getNormalizedWordSentiment(self, word):
        # This function is important - by normalizing the data we compensate
        # for the fact that some words occurs far more often than others.
        if self.getWordCount(word) != 0:
            
            return self.getWordSentiment(word) / self.getWordCount(word)
        else:
            return 0
                
    def getStringSentiment(self, string):
        N = NUM_OF_WORDS_TO_PASS - 1
        string = string.replace("#", "").replace("-", "").replace("/", "").replace("<br", "").replace(":", "").replace("/>", "").replace(")", "").replace("(", "").replace('"', "").replace("}","").replace(".", "").replace("?", "").replace(",","").replace("!", "").replace("\\", "").replace(":", "")
                                       
        #string = string.replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("0", "")
        score = 0
        count = 0
        words = string.split(" ")
        for i in range(N, len(words)):
            strang = ""
            #if len(words[i])> 3: 
             #   score += self.getNormalizedWordSentiment(words[i])
             #this increased to 83.204%?? dont know if it is right
             
            #if len(words[i]) > 3:
            if len(words[i]) > 0:
                
                for wrd in words[i-N:i+1]:
                    strang += " " + wrd
                    
                    
                if len(strang) > MIN_LENGHT_OF_STRING: 
                    count += 1
                    strang = strang.lower()
                    if self.getNormalizedWordSentiment(strang[1:]) == 0: 
                        score += self.getNormalizedWordSentiment(words[i])
                    else: 
                        score += self.getNormalizedWordSentiment(strang[1:]) 
                
        if score == 0: 
            return 0
        
        return score / count 