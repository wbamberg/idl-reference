import os
import sys
import md

from xpidl import xpidl

index = md.createFile("../docs/index.md")

def writeDoccomments(doccomments, output):
    for doccomment in doccomments:
        lines = doccomment.splitlines()
        for line in lines:
            line = line.lstrip()
            if line.startswith("/**"):
                line = line[3:]
            if line.startswith("*/"):
                line = line[2:]
            if line.startswith("*"):
                line = line[2:]
            output.write(line + "\n")

def writeInterface(interface):
    name = interface.name
    md.writeMDLink(name, name, index)
    output = md.createFile("../docs/" + name + ".md")
    md.writeH1(name, output)
    if hasattr(interface, "doccomments"):
        writeDoccomments(interface.doccomments, output)
    for member in interface.members:
        if member.kind == "cdata":
            continue
        md.writeH2(member.name, output)
        if hasattr(member, "doccomments"):
            writeDoccomments(member.doccomments, output)

def writeIdlFile(index, filename):
    try:
        p = xpidl.IDLParser(outputdir="generated")
        idl = p.parse(open(filename).read(), filename=filename)
    except:
        print "Couldn't process " + filename
    else:
        for p in idl.productions:
            if p.kind == "interface":
                writeInterface(p)

for dirpath, dirs, files in os.walk("../../gecko-dev"):
    for f in files:
        if f.endswith(".idl"):
            fullname = os.path.join(dirpath, f)
            writeIdlFile(index, fullname)

