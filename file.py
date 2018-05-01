import urllib

link = "http://www.gutenberg.org/cache/epub/24336/pg24336.txt"
f = urllib.urlopen(link)
myfile = f.read()

wordList = myfile.split()

#print wordList

def freqWord(word):
    newList = [w for w in wordList if w == word]
    #print newList
    return len(newList)

print 'freqWord(\'English\') = ' + str(freqWord("English"))

def groupFreqWord(groupList):
    newList = [freqWord(w) for w in groupList]
    return reduce((lambda x,y: x+y), newList)

print 'groupFreqWord([\'The\', \'English\', \'are\']) = ' + str(groupFreqWord(['The', 'English', 'are']))

def mostFreqWord():
    return reduce((lambda x, y: x if freqWord(x) > freqWord(y) else y), wordList)

print "Most frequent word: " + mostFreqWord()
