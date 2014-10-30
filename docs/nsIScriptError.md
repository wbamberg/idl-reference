---
layout: default
---

# nsIScriptError #

## Methods ##

### init(message, sourceName, sourceLine, lineNumber, columnNumber, flags, category) ###

### initWithWindowID(message, sourceName, sourceLine, lineNumber, columnNumber, flags, category, innerWindowID) ###

## Attributes ##

### errorMessage ###
  
The error message without any context/line number information.  
  
@note nsIConsoleMessage.message will return the error formatted  
      with file/line information.  
  

### sourceName ###

### sourceLine ###

### lineNumber ###

### columnNumber ###

### flags ###

### category ###
  
Categories I know about -  
XUL javascript  
content javascript (both of these from nsDocShell, currently)  
system javascript (errors in JS components and other system JS)  
  

### outerWindowID ###

### innerWindowID ###

### isFromPrivateWindow ###

## Constants ##

### errorFlag ###
 pseudo-flag for default case */  

### warningFlag ###
 message is warning */  

### exceptionFlag ###
 exception was thrown for this case - exception-aware hosts can ignore */  

### strictFlag ###
 error or warning is due to strict option */  
