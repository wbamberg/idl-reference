---
layout: default
---

# nsIWebVTTListener #
  
Listener for a JS WebVTT parser (vtt.js).  
  

## Methods ##

### onCue(cue) ###
  
Is called when the WebVTTParser successfully parses a WebVTT cue.  
  
@param cue An object representing the data of a parsed WebVTT cue.  
  

#### Parameters ####

<table>

<tr>
<td>cue</td>
<td>An object representing the data of a parsed WebVTT cue.  
</td>
</tr>

</table>

### onRegion(region) ###
  
Is called when the WebVTT parser successfully parses a WebVTT region.  
  
@param region An object representing the data of a parsed  
              WebVTT region.  
  

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
  
Is called when the WebVTT parser encounters a parsing error.  
  
@param error The error code of the ParserError the occured.  
  

#### Parameters ####

<table>

<tr>
<td>error</td>
<td>The error code of the ParserError the occured.  
</td>
</tr>

</table>
