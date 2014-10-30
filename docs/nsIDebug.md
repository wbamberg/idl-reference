---
layout: default
---

# nsIDebug #
  
  For use by consumers in scripted languages (JavaScript, Java, Python,  
  Perl, ...).  
  
@note C/C++ consumers who are planning to use the nsIDebug interface with  
  the "@mozilla.org/xpcom;1" contract should use NS_DebugBreak from xpcom  
  glue instead.  
  
  

## Methods ##

### assertion ###
  
Show an assertion and trigger nsIDebug.break().  
  
@param aStr assertion message  
@param aExpr expression that failed  
@param aFile file containing assertion  
@param aLine line number of assertion  
  
  

### warning ###
  
Show a warning.  
  
@param aStr warning message  
@param aFile file containing assertion  
@param aLine line number of assertion  
  

### break ###
  
Request to break into a debugger.  
  
@param aFile file containing break request  
@param aLine line number of break request  
  

### abort ###
  
Request the process to trigger a fatal abort.  
  
@param aFile file containing abort request  
@param aLine line number of abort request  
  
