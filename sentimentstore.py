
class SentimentStore:
    def __init__(self):
        self.store = {}
        self.timesseen = {}
        self.pos = 0
        self.neg = 0
        self.totalwordcount = 0
        self.wordcount = 0
        self.sentiment_dict = {}
        
    def getNumberOfWords(self):
        return self.wordcount

    def getNumberOfPositiveWords(self):
        return self.pos

    def getNumberOfNegativeWords(self):
        return self.neg

    def getTotalWordCount(self):
        return self.totalwordcount

    def addWordScore(self, word, score):
        self.totalwordcount += 1
        if word not in self.store.keys(): 
            self.store[word] = score 
            self.timesseen[word]=1
            self.wordcount += 1
            if score == 1 :
                self.pos += 1
            else: 
                self.neg += 1
        else: 
            self.store[word]+= score
            self.timesseen[word]+=1
                
        return
        
    def addStringScore(self, string, score):
        words = string.split(" ")
        N = 0
        for i in range(N,len(words)):
            strang = ""
            for wrd in words[i-N:i+1+N]:
                strang += " " + wrd
            
            if len(words[i]) > 3: # ignore short words
                self.addWordScore(strang[1:], score)
        
    def getWordSentiment(self, word):
        if word in self.store.keys():
            return self.store[word]
        return 0
    
    def getWordCount(self, word):
        if word in self.store.keys(): 
            return self.timesseen[word]
        return 0

    def getNormalizedWordSentiment(self, word):
        # This function is important - by normalizing the data we compensate
        # for the fact that some words occurs far more often than others.
        if self.getWordCount(word) != 0:
            return self.getWordSentiment(word) / self.getWordCount(word)
        else:
            return 0


    def getStringSentiment(self, s):
        score = 0
        count = 0
        words = s.split(" ")
        N = 0
        #for word in words:
        for i in range(N, len(words)):
            strang = ""
            for wrd in words[i-N:i+1+N]:
                strang += " " + wrd
                if len(words[i]) > 3: # ignore short words
                    count += 1
                    strang = strang.lower()
                    score += self.getNormalizedWordSentiment(strang[1:])
                
        return score / count 
