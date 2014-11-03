---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/js/xpconnect/idl/nsIScriptError.idl">Source file</a>
</div>

# nsIScriptError #

## Methods ##

### init(message, sourceName, sourceLine, lineNumber, columnNumber, flags, category) ###

### initWithWindowID(message, sourceName, sourceLine, lineNumber, columnNumber, flags, category, innerWindowID) ###

## Attributes ##

### errorMessage ###
<pre>  
The error message without any context/line number information.  
  
@note nsIConsoleMessage.message will return the error formatted  
      with file/line information.  
  
</pre>
### sourceName ###

### sourceLine ###

### lineNumber ###

### columnNumber ###

### flags ###

### category ###
<pre>  
Categories I know about -  
XUL javascript  
content javascript (both of these from nsDocShell, currently)  
system javascript (errors in JS components and other system JS)  
  
</pre>
### outerWindowID ###

### innerWindowID ###

### isFromPrivateWindow ###

## Constants ##

### errorFlag ###
<pre> pseudo-flag for default case */  
</pre>
### warningFlag ###
<pre> message is warning */  
</pre>
### exceptionFlag ###
<pre> exception was thrown for this case - exception-aware hosts can ignore */  
</pre>
### strictFlag ###
<pre> error or warning is due to strict option */  
</pre>