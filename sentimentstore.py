
class SentimentStore:
    def __init__(self):
        self.store = {}
        self.pos = 0
        self.neg = 0
        self.totalwordcount = 0
        self.wordcount = 0
        self.words = []
        
    def getNumberOfWords(self):
        return self.wordcount

    def getNumberOfPositiveWords(self):
        return self.pos

    def getNumberOfNegativeWords(self):
        return self.neg

    def getTotalWordCount(self):
        return self.totalwordcount

    def addWordScore(self, word, score):
        self.words.append(word)
        
        self.totalwordcount+=1
        if word not in self.store.keys(): 
            self.store[word] = score
            self.wordcount += 1
        else: 
            self.store[word]+=score

        if score == 1: 
            self.pos += 1
        else: 
            self.neg += 1
        
        return
                
    def addStringScore(self, string, score):
        words = string.split(" ")
        wrdnot = False
        for word in words:
            if len(word) > 3: # ignore short words
                self.addWordScore(word, score)

    def getWordSentiment(self, word):
        if word in self.store.keys():
            return self.store[word] 
        return 0
    
    def getWordCount(self, word):
        if word in self.store.keys(): 
            
            if self.store[word] > 0:
                return self.store[word]
            else:
                return abs(self.store[word])
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
        for word in words:
            if len(word) > 3: # ignore short words
                count += 1
                word = word.lower()
                score += self.getNormalizedWordSentiment(word)
        return score / count
