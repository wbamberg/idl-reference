---
layout: default
---

# nsIINIParserWriter #

## WRITE_UTF16 ##

Windows and the NSIS installer code sometimes expect INI files to be in
UTF-16 encoding. On Windows only, this flag to writeFile can be used to
change the encoding from its default UTF-8.


## setString ##

Set the value of a string for a particular section and key.


## writeFile ##

Write to the INI file.

