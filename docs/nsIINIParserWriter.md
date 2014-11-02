---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIINIParser.idl">Source file</a>
</div>

# nsIINIParserWriter #

## Methods ##

### setString(aSection, aKey, aValue) ###
  
Set the value of a string for a particular section and key.  
  

### writeFile(aINIFile, aFlags) ###
  
Write to the INI file.  
  

## Constants ##

### WRITE_UTF16 ###
  
Windows and the NSIS installer code sometimes expect INI files to be in  
UTF-16 encoding. On Windows only, this flag to writeFile can be used to  
change the encoding from its default UTF-8.  
  
