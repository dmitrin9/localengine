import os
import re
from html.parser import HTMLParser

def count(string, word):
    pattern = r"\b" + re.escape(word) + r"\b"
    matches = re.findall(pattern, string, re.IGNORECASE)
    return len(matches)

class Parser(HTMLParser):
    pagedata = []
    def handle_data(self, data):
        self.pagedata.append(data)
    def getpagedata(self):
        return "".join(self.pagedata)

def figureThatShitOut(words, pagedir):
    stuff = {}
    totalFreq = 0
    for name in os.listdir(os.path.join(os.getenv("HOME"), pagedir)):
        item = os.path.join(os.getenv("HOME"), pagedir, name)
        if os.path.isfile(item):
            parser = Parser()
            with open(item) as f:
                file = f.read()
                for c in file:
                    parser.feed(c.lower())

            for word in words:
                freq = count(parser.getpagedata(), word)
                totalFreq+=freq
                if freq > 0:
                    print(parser.getpagedata())
                    print(word)
                    print(freq)
                path = item
                stuff[path] = freq
        if os.path.isdir(item):
            shitFiguredOut = figureThatShitOut(words, os.path.join(pagedir, item))
            items = shitFiguredOut
            for item in items:
                stuff[item[0]]=item[1]

    if totalFreq == 0:
        return []
    return list(stuff.items())

def _sortSumRank(unorderedSumRank):
    orderedSumRank = []
    exclude=[]
    for _ in unorderedSumRank:
        highest = ["", 0]
        index=0
        for i, rank in enumerate(unorderedSumRank):
            if rank[1] > highest[1] and i not in exclude:
                highest = rank
                index=i
        exclude.append(index)
        orderedSumRank.append(highest[0])
    return list(orderedSumRank)

def pageRank(words):
    things = []
    datadir = os.path.join(os.getenv("HOME"), "repos/localengine/search")
    for item in os.listdir(os.path.join(os.getenv("HOME"), datadir)):
        shitFiguredOut = figureThatShitOut(words, os.path.join(datadir, item))
        [things.append(thing) for thing in shitFiguredOut]

    orderedSumRank = _sortSumRank(things)
    return orderedSumRank

def search(words):
    return pageRank(words)
