---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsIDebug.idl">Source file</a>
</div>

# nsIDebug #
  
  For use by consumers in scripted languages (JavaScript, Java, Python,  
  Perl, ...).  
  
@note C/C++ consumers who are planning to use the nsIDebug interface with  
  the "@mozilla.org/xpcom;1" contract should use NS_DebugBreak from xpcom  
  glue instead.  
  
  

## Methods ##

### assertion(aStr, aExpr, aFile, aLine) ###
  
Show an assertion and trigger nsIDebug.break().  
  
  
  

#### Parameters ####

<table>

<tr>
<td>aStr</td>
<td>assertion message  
</td>
</tr>

<tr>
<td>aExpr</td>
<td>expression that failed  
</td>
</tr>

<tr>
<td>aFile</td>
<td>file containing assertion  
</td>
</tr>

<tr>
<td>aLine</td>
<td>line number of assertion  
</td>
</tr>

</table>

### warning(aStr, aFile, aLine) ###
  
Show a warning.  
  
  

#### Parameters ####

<table>

<tr>
<td>aStr</td>
<td>warning message  
</td>
</tr>

<tr>
<td>aFile</td>
<td>file containing assertion  
</td>
</tr>

<tr>
<td>aLine</td>
<td>line number of assertion  
</td>
</tr>

</table>

### break(aFile, aLine) ###
  
Request to break into a debugger.  
  
  

#### Parameters ####

<table>

<tr>
<td>aFile</td>
<td>file containing break request  
</td>
</tr>

<tr>
<td>aLine</td>
<td>line number of break request  
</td>
</tr>

</table>

### abort(aFile, aLine) ###
  
Request the process to trigger a fatal abort.  
  
  

#### Parameters ####

<table>

<tr>
<td>aFile</td>
<td>file containing abort request  
</td>
</tr>

<tr>
<td>aLine</td>
<td>line number of abort request  
</td>
</tr>

</table>
