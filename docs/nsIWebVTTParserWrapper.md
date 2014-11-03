---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/media/webvtt/nsIWebVTTParserWrapper.idl">Source file</a>
</div>

# nsIWebVTTParserWrapper #
<code>  
Interface for a wrapper of a JS WebVTT parser (vtt.js).  
  
</code>
## Methods ##

### loadParser(window) ###
<code>  
Loads the JS WebVTTParser and sets it to use the passed window to create  
VTTRegions and VTTCues. This function must be called before calling  
parse, flush, or watch.  
  
@param window The window that the parser will use to create VTTCues and  
              VTTRegions.  
  
  
</code>
#### Parameters ####

<table>

<tr>
<td>window</td>
<td>The window that the parser will use to create VTTCues and  
              VTTRegions.  
</td>
</tr>

</table>

### parse(data) ###
<code>  
Attempts to parse the stream's data as WebVTT format. When it successfully  
parses a WebVTT region or WebVTT cue it will create a VTTRegion or VTTCue  
object and pass it back to the callee through its callbacks.  
  
@param data   The buffer that contains the WebVTT data received by the  
              Necko consumer so far.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>data</td>
<td>The buffer that contains the WebVTT data received by the  
              Necko consumer so far.  
</td>
</tr>

</table>

### flush() ###
<code>  
Flush indicates that no more data is expected from the stream. As such the  
parser should try to parse any kind of partial data it has.  
  
</code>
### watch(callback) ###
<code>  
Set this parser object to use an nsIWebVTTListener object for its onCue  
and onRegion callbacks.  
  
@param callback The nsIWebVTTListener object that exposes onCue and  
                onRegion callbacks for the parser.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>callback</td>
<td>The nsIWebVTTListener object that exposes onCue and  
                onRegion callbacks for the parser.  
</td>
</tr>

</table>

### convertCueToDOMTree(window, cue) ###
<code>  
Convert the text content of a WebVTT cue to a document fragment so that  
we can display it on the page.  
  
@param window A window object with which the document fragment will be  
              created.  
@param cue    The cue whose content will be converted to a document  
              fragment.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>window</td>
<td>A window object with which the document fragment will be  
              created.  
</td>
</tr>

<tr>
<td>cue</td>
<td>The cue whose content will be converted to a document  
              fragment.  
</td>
</tr>

</table>

### processCues(window, cues, overlay) ###
<code>  
Compute the display state of the VTTCues in cues along with any VTTRegions  
that they might be in. First, it computes the positioning and styling of  
the cues and regions passed and converts them into a DOM tree rooted at  
a containing HTMLDivElement. It then adjusts those computed divs for  
overlap avoidance using the dimensions of 'overlay'. Finally, it adds the  
computed divs to the VTTCues display state property for use later.  
  
@param window  A window object with which it will create the DOM tree  
               and containing div element.  
@param cues    An array of VTTCues who need there display state to be  
               computed.  
@param overlay The HTMLElement that the cues will be displayed within.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>window</td>
<td>A window object with which it will create the DOM tree  
               and containing div element.  
</td>
</tr>

<tr>
<td>cues</td>
<td>An array of VTTCues who need there display state to be  
               computed.  
</td>
</tr>

<tr>
<td>overlay</td>
<td>The HTMLElement that the cues will be displayed within.  
</td>
</tr>

</table>
