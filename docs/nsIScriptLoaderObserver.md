---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsIScriptLoaderObserver.idl">Source file</a>
</div>

# nsIScriptLoaderObserver #

## Methods ##

### scriptAvailable(aResult, aElement, aIsInline, aURI, aLineNo) ###
  
The script is available for evaluation. For inline scripts, this  
method will be called synchronously. For externally loaded scripts,  
this method will be called when the load completes.  
  
@param aResult A result code representing the result of loading  
       a script. If this is a failure code, script evaluation  
       will not occur.  
@param aElement The element being processed.  
@param aIsInline Is this an inline script or externally loaded?  
@param aURI What is the URI of the script (the document URI if  
       it is inline).  
@param aLineNo At what line does the script appear (generally 1  
       if it is a loaded script).  
  

#### Parameters ####

<table>

<tr>
<td>aResult</td>
<td>A result code representing the result of loading  
       a script. If this is a failure code, script evaluation  
       will not occur.  
</td>
</tr>

<tr>
<td>aElement</td>
<td>The element being processed.  
</td>
</tr>

<tr>
<td>aIsInline</td>
<td>Is this an inline script or externally loaded?  
</td>
</tr>

<tr>
<td>aURI</td>
<td>What is the URI of the script (the document URI if  
       it is inline).  
</td>
</tr>

<tr>
<td>aLineNo</td>
<td>At what line does the script appear (generally 1  
       if it is a loaded script).  
</td>
</tr>

</table>

### scriptEvaluated(aResult, aElement, aIsInline) ###
  
The script has been evaluated.  
  
@param aResult A result code representing the success or failure of  
       the script evaluation.  
@param aElement The element being processed.  
@param aIsInline Is this an inline script or externally loaded?  
  

#### Parameters ####

<table>

<tr>
<td>aResult</td>
<td>A result code representing the success or failure of  
       the script evaluation.  
</td>
</tr>

<tr>
<td>aElement</td>
<td>The element being processed.  
</td>
</tr>

<tr>
<td>aIsInline</td>
<td>Is this an inline script or externally loaded?  
</td>
</tr>

</table>
