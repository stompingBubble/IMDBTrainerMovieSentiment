import os
import json


class IMDBTrainer():
    def __init__(self, path="aclImdb/train"):
        self.scores = []
        self.data = []
        self.size = 0
        # Load up positive and negative reviews
        for X in ["neg", "pos"]:
            for file in os.listdir( os.path.join( path, X ) ):
                s=file.split("_")
                score = int(s[1].replace(".txt",""))
                if X=="neg":
                    self.scores.append( -1 )
                else:
                    self.scores.append(  1 )
                # read the review..
                data = open( os.path.join( path, X, file ), encoding="utf-8").read()
                self.data.append( data )
                self.size += 1
                
    def train( self, sentiment ):
        
        # Spola fram till start
        for i in range(self.size):
            sentiment.addStringScore(self.data[i], self.scores[i])
        
                
    def test( self, sentiment ):
        count = 0
        correct=0
        uncertain=0
        wrong=0
        badcounter = 0 
        goodcounter = 0
        
        for i in range(self.size):
            
            count += 1
            
            s = sentiment.getStringSentiment(self.data[i])
                
            if ( s < -0.01):
                if self.scores[i] < 0:
                    correct += 1
                else:
                    wrong += 1
            elif ( s > 0.01 ):
                if self.scores[i] > 0:
                    correct += 1
                else:
                    wrong += 1
            else:
                uncertain += 1
        
        print("ಠ_ಠ")
        print("Correct: {}%".format( 100*correct/count ) )
        print("Wrong: {}%".format( 100*wrong/count ) )
        print("Uncertain: {}%".format( 100*uncertain/count ) )
        print("\n(ノಠ ∩ಠ)ノ <NOT GOOD ENOUGH")