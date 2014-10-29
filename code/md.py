def createFile(name):
    f = open(name, "w")
    f.write("---\nlayout: default\n---\n")
    return f

def writeFront(output):
    output.write("---\n---\n")

def writeMDLink(name, target, output):
   output.write("[" + name + "]" + "(" + target + ".html)\n")

def writeLineBreak(output):
   output.write("\n")

def writeHTMLLink(name, target, output):
   output.write("<a href=\"" + target + "\">" + name + "</a>\n")

def writeH1(content, output):
    output.write("\n# " + content + " #\n")

def writeH2(content, output):
    output.write("\n## " + content + " ##\n")

def writeH3(content, output):
    output.write("\n### " + content + " ###\n")

def writeH4(content, output):
    output.write("\n#### " + content + " ####\n")

def writeTableStart(output):
    output.write("\n<table>\n")

def writeTableEnd(output):
    output.write("\n</table>\n")

def writeTableRow(cells, output):
    output.write("\n<tr>")
    for cell in cells:
        output.write("\n<td>" + cell + "</td>")
    output.write("\n</tr>\n")