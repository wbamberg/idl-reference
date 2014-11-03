---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIINIParser.idl">Source file</a>
</div>

# nsIINIParserWriter #

## Methods ##

### setString(aSection, aKey, aValue) ###
<code>  
Set the value of a string for a particular section and key.  
  
</code>
### writeFile(aINIFile, aFlags) ###
<code>  
Write to the INI file.  
  
</code>
## Constants ##

### WRITE_UTF16 ###
  
Windows and the NSIS installer code sometimes expect INI files to be in  
UTF-16 encoding. On Windows only, this flag to writeFile can be used to  
change the encoding from its default UTF-8.  
  
