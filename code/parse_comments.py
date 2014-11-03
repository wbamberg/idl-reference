import os
import sys

def getNextWordFromLine(line):
    return line.split(" ", 1)[0]

def lineIsEmpty(line):
    return not line.rstrip()

# this generator lets us call
# send() to push a value back in,
# so we can peek at it without
# having to consume it
def generator(lines):
    for l in lines:
       r = yield l
       if r:
           # The first yield is needed because 'send' also
           # yields a value
           yield None
           yield l

def blockIsFinished(line):
    return lineIsEmpty(line) or line.startswith("@param") or line.startswith("@return")

def createParamDoc(line, lines):
    line = line[len("@param"):].lstrip()
    name = getNextWordFromLine(line)
    doc = line[len(name):].lstrip()
    for line in lines:
        if blockIsFinished(line):
           try:
               lines.send(1)
           except StopIteration:
               pass
           return ParamDoc(name, doc)
        else:
            doc += line
    return ParamDoc(name, doc)

def createReturnDoc(line, lines):
    doc = line[len("@return "):].lstrip()
    for line in lines:
        if blockIsFinished(line):
            try:
               lines.send(1)
            except StopIteration:
               pass
            return doc
        else:
            doc += line
    return doc

def parseDoccomments(lines):
    parsed = Parsed()
    linesGenerator = generator(lines)
    for line in linesGenerator:
        if line.lstrip().startswith("@param"):
            param = createParamDoc(line, linesGenerator)
            parsed.params.append(param)
        elif line.lstrip().startswith("@return"):
            parsed.returns = createReturnDoc(line, linesGenerator)
        else:
            parsed.generalDocs += line
    return parsed

class ParamDoc(object):
    def __init__(self, name, doc):
        self.name = name
        self.doc = doc

class Parsed(object):
    def __init__(self):
        self.params = []
        self.returns = ""
        self.generalDocs = []
