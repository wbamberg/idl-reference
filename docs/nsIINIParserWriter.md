---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/ds/nsIINIParser.idl">Source file</a>
</div>

# nsIINIParserWriter #

## Methods ##

### setString(aSection, aKey, aValue) ###
<pre>  
Set the value of a string for a particular section and key.  
  
</pre>
### writeFile(aINIFile, aFlags) ###
<pre>  
Write to the INI file.  
  
</pre>
## Constants ##

### WRITE_UTF16 ###
<pre>  
Windows and the NSIS installer code sometimes expect INI files to be in  
UTF-16 encoding. On Windows only, this flag to writeFile can be used to  
change the encoding from its default UTF-8.  
  
</pre>