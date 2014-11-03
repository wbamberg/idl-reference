---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/media/webvtt/nsIWebVTTListener.idl">Source file</a>
</div>

# nsIWebVTTListener #
<pre>  
Listener for a JS WebVTT parser (vtt.js).  
  
</pre>
## Methods ##

### onCue(cue) ###
<pre>  
Is called when the WebVTTParser successfully parses a WebVTT cue.  
  
@param cue An object representing the data of a parsed WebVTT cue.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>cue</td>
<td>An object representing the data of a parsed WebVTT cue.  
</td>
</tr>

</table>

### onRegion(region) ###
<pre>  
Is called when the WebVTT parser successfully parses a WebVTT region.  
  
@param region An object representing the data of a parsed  
              WebVTT region.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>region</td>
<td>An object representing the data of a parsed  
              WebVTT region.  
</td>
</tr>

</table>

### onParsingError(errorCode) ###
<pre>  
Is called when the WebVTT parser encounters a parsing error.  
  
@param error The error code of the ParserError the occured.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>error</td>
<td>The error code of the ParserError the occured.  
</td>
</tr>

</table>
