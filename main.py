import time

print( "Creating sentiment storage:" )


from sentimentstore import SentimentStore
sentiment=SentimentStore()

from imdbtrainer import IMDBTrainer

print("Training:")
movies_train=IMDBTrainer("aclImdb/train")
t0 = time.time()
movies_train.train( sentiment )
t1 = time.time()
print("Training took {:.3f}s".format( t1-t0 ) )

print("")
print("Total word count in dataset: ", sentiment.getTotalWordCount() )
print("Total unique words in dataset: ", sentiment.getNumberOfWords() )
print("Total unique positive words in dataset: ", sentiment.getNumberOfPositiveWords() )
print("Total unique negative words in dataset: ", sentiment.getNumberOfNegativeWords() )
print("")

print("Testing:")
movies_test=IMDBTrainer("aclImdb/test")
t0 = time.time()
movies_test.test( sentiment )
t1 = time.time()
print("Testing took {:.3f}s".format( t1-t0 ) )


