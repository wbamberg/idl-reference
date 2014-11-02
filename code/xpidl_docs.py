import os
import sys
import md

from parse_comments import parseDoccomments
from xpidl import xpidl

pathSearchPrefix = "../../gecko-dev/"
dxrBase = "http://dxr.mozilla.org/mozilla-central/source/"

index = md.createFile("../index.md", "default_index")

class Attribute(object):
    def __init__(self, spec):
        self.name = spec.name
        self.doccomments = spec.doccomments

    def write(self, output):
        md.writeH3(self.name, output)
        self.writeDoccomments(output)

    def writeDoccomments(self, output):
        for doccomment in self.doccomments:
            processed = stripComments(doccomment)
            for line in processed:
                output.write(line)

class Param(object):
    def __init__(self, name, doc):
        self.name = name
        self.doc = doc

class Method(object):
    def __init__(self, spec):
        self.name = spec.name
        self.spec = spec
        self.doccomments = spec.doccomments
        self.doclines = []
        for doccomment in self.doccomments:
            self.doclines += stripComments(doccomment)

    def write(self, output):
        md.writeH3(self.signature(), output)
        self.writeDoccomments(output)
        parsed = parseDoccomments(self.doclines)
        self.writeParams(parsed.params, output)
        self.writeReturns(parsed.returns, output)

    def writeParams(self, params, output):
        params = iter(params)
        try:
            first = params.next()
            md.writeH4("Parameters", output)
            md.writeTableStart(output)
            md.writeTableRow([first.name, first.doc], output)
        except StopIteration:
            return
        for param in params:
            md.writeTableRow([param.name, param.doc], output)
        md.writeTableEnd(output)

    def writeReturns(self, returns, output):
        if not returns:
            return
        md.writeH4("Returns", output)
        md.writeTableStart(output)
        md.writeTableRow([returns], output)
        md.writeTableEnd(output)

    def writeParams2(self, output):
        params = self.paramGenerator(self.doccomments)
        try:
            first = params.next()
            md.writeH4("Parameters", output)
            md.writeTableStart(output)
            md.writeTableRow([first.name, first.doc], output)
        except StopIteration:
            return
        for param in params:
            md.writeTableRow([param.name, param.doc], output)
        md.writeTableEnd(output)

    def signature(self):
        signature = self.name + "("
        if len(self.spec.params) > 0:
            signature += self.spec.params[0].name
            for param in self.spec.params[1:]:
                signature += ", " + param.name
        signature += ")"
        return signature

    def writeDoccomments(self, output):
        for doccomment in self.doccomments:
            processed = stripComments(doccomment)
            for line in processed:
                output.write(line)

class Constant(object):
    def __init__(self, spec):
        self.name = spec.name
        self.doccomments = spec.doccomments

    def write(self, output):
        md.writeH3(self.name, output)
        self.writeDoccomments(output)

    def writeDoccomments(self, output):
        for doccomment in self.doccomments:
            processed = stripComments(doccomment)
            for line in processed:
                output.write(line)

class Interface(object):
    def __init__(self, filename, spec):
        print spec.name
        self.filename = filename
        self.name = spec.name
        self.doccomments = spec.doccomments
        self.constants = [Constant(member) for member in spec.members if member.kind == "const"]
        self.methods = [Method(member) for member in spec.members if member.kind == "method"]
        self.attributes = [Attribute(member) for member in spec.members if member.kind == "attribute"]

    def write(self):
        output = md.createFile("../docs/" + self.name + ".md")
        output.write("<div id='links'>")
        md.writeHTMLLink("Index", "../index.html", output)
        md.writeHTMLLink("Source file", dxrBase + self.filename[len(pathSearchPrefix):], output)
        output.write("</div>")
        md.writeLineBreak(output)
        md.writeH1(self.name, output)
        self.writeDoccomments(output)
        self.writeMembers("Methods", self.methods, output)
        self.writeMembers("Attributes", self.attributes, output)
        self.writeMembers("Constants", self.constants, output)

    def writeDoccomments(self, output):
        for doccomment in self.doccomments:
            processed = stripComments(doccomment)
            for line in processed:
                output.write(line)

    def writeMembers(self, kind, members, output):
        if len(members) > 0:
            md.writeH2(kind, output)
        for member in members:
            member.write(output)

def stripComments(doccomment):
    processed = []
    lines = doccomment.splitlines()
    for line in lines:
        line = line.lstrip()
        if line.startswith("/**"):
            line = line[3:]
        if line.startswith("*/"):
            line = line[2:]
        if line.startswith("*"):
            line = line[2:]
        line = line + "  \n"
        processed.append(line)
    return processed

def writeIdlFile(index, filename):
    try:
        p = xpidl.IDLParser(outputdir="generated")
        idl = p.parse(open(filename).read(), filename=filename)
    except:
        print "Couldn't process " + filename
    else:
        for p in idl.productions:
            if p.kind == "interface":
                name = p.name
                md.writeMDLink(name, "docs/" + name, index)
                md.writeLineBreak(index)
                interface = Interface(filename, p)
                interface.write()

for dirpath, dirs, files in os.walk(pathSearchPrefix):
    for f in files:
        if f.endswith(".idl"):
            fullname = os.path.join(dirpath, f)
            writeIdlFile(index, fullname)

