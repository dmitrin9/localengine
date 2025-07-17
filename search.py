import os
from html.parser import HTMLParser

class SearchItems:
    def __init__(self, words):
        self.words=words
        self.topDocsAppearsMost=[] # Top documents all words appear most in.

class Parser(HTMLParser):
    pagedata = []
    def handle_data(self, data):
        self.pagedata.append(data)
    def getpagedata(self):
        return "".join(self.pagedata)

def figureThatShitOut(words, pagedir):
    stuff = {}
    for name in os.listdir(os.path.join(os.getenv("HOME"), pagedir)):
        item = os.path.join(os.getenv("HOME"), pagedir, name)
        if os.path.isdir(item):
            figureThatShitOut(words, os.path.join(pagedir, item))
        if os.path.isfile(item):
            parser = Parser()
            with open(os.path.join(pagedir, item)) as f:
                thing = f.read()
                for c in thing:
                    parser.feed(c.lower())

                for word in words:
                    try:
                        stuff[f.name].append([word, parser.getpagedata().count(word)])
                    except KeyError:
                        stuff[f.name] = []
        else:
            raise RuntimeError(f"{item} is not file or directory. Is it a symlink or device?")
    return stuff

def pageRank(words):
    rank = {}

    searchItems = SearchItems(words)
    datadir = os.path.join(os.getenv("HOME"), "repos/localengine/search")
    for item in os.listdir(os.path.join(os.getenv("HOME"), datadir)):
        print(item)
        thing = figureThatShitOut(words, os.path.join(datadir, item))
        rank[item] = thing
    print(rank)

def search(words):
    rank = pageRank(words)
