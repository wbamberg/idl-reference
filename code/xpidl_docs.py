import os
import sys
import md

from xpidl import xpidl

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

    def write(self, output):
        md.writeH3(self.signature(), output)
        self.writeDoccomments(output)
        self.writeParams(output)

    def writeParams(self, output):
        params = self.paramGenerator(self.doccomments)
        try:
            first = params.next()
            md.writeH4("Parameters", output)
            md.writeTableStart(output)
            md.writeTableRow([first.name, first.doc], output)
        except StopIteration:
            return
        for param in params:
            md.writeTableRow([first.name, first.doc], output)
        md.writeTableEnd(output)

    def signature(self):
        signature = self.name + "("
        if len(self.spec.params) > 0:
            signature += self.spec.params[0].name
            for param in self.spec.params[1:]:
                signature += ", " + param.name
        signature += ")"
        return signature

    def getParamNameFromLine(self, line):
        return line.split(" ", 1)[0]

    def lineIsEmpty(self, line):
        return not line.rstrip()

    # this function assumes that:
    # - lines starting with @param are the start of param doc blocks
    # - the next complete word after @param is the param name
    # - the rest of that line is param documentation
    # - any subsequent lines are param documentation until
    # the param doc block is ended by any of:
    #    - a new @param line
    #    - an @return line
    #    - an empty line
    #    - the end of the whole comment block
    def paramGenerator(self, doccomments):
        lines = []
        for doccomment in self.doccomments:
            lines += stripComments(doccomment)
        processingParamRightNow = False
        for line in lines:
            if line.startswith("@param"):
                if processingParamRightNow:
                    yield Param(name, doc)
                processingParamRightNow = True
                line = line[len("@param "):]
                name = self.getParamNameFromLine(line)
                doc = line[len(name):].lstrip()
            elif line.startswith("@return") or self.lineIsEmpty(line):
                if processingParamRightNow:
                    yield Param(name, doc)
                processingParamRightNow = False
            else:
                if processingParamRightNow:
                    doc += line
        if processingParamRightNow:
            yield Param(name, doc)

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
        self.filename = filename
        self.name = spec.name
        self.doccomments = spec.doccomments
        self.constants = [Constant(member) for member in spec.members if member.kind == "const"]
        self.methods = [Method(member) for member in spec.members if member.kind == "method"]
        self.attributes = [Attribute(member) for member in spec.members if member.kind == "attribute"]

    def write(self):
        output = md.createFile("../docs/" + self.name + ".md")
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

for dirpath, dirs, files in os.walk("../../gecko-dev"):
    for f in files:
        if f.endswith(".idl"):
            fullname = os.path.join(dirpath, f)
            writeIdlFile(index, fullname)

