---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/modules/libjar/nsIJARURI.idl">Source file</a>
</div>
# nsIJARURI #
  
JAR URLs have the following syntax  
  
jar:<jar-file-uri>!/<jar-entry>  
  
EXAMPLE: jar:http://www.big.com/blue.jar!/ocean.html  
  
The nsIURL methods operate on the <jar-entry> part of the spec.  
  

## Methods ##

### cloneWithJARFile(jarFile) ###
  
Create a clone of the JAR URI with a new root URI (the URI for the  
actual JAR file).  
  

## Attributes ##

### JARFile ###
  
Returns the root URI (the one for the actual JAR file) for this JAR  
(e.g., http://www.big.com/blue.jar).  
  

### JAREntry ###
  
Returns the entry specified for this JAR URI (e.g., "ocean.html").  This  
value may contain %-escaped byte sequences.  
  
