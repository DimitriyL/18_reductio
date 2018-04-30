import urllib

link = "http://www.gutenberg.org/files/1342/1342-0.txt"
f = urllib.urlopen(link)
myfile = f.read()

wordList = myfile.split()

print wordList

def freqWord(word):
    newList = [w for w in wordList if w == word]
    print newList
    return len(newList)

print freqWord("chair")

def mostCommon():
    
