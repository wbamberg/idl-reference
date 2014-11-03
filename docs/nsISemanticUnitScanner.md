---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/intl/lwbrk/nsISemanticUnitScanner.idl">Source file</a>
</div>

# nsISemanticUnitScanner #
  
Provides a language independent way to break UNICODE  
text into meaningful semantic units (e.g. words).  
  

## Methods ##

### start(characterSet) ###
  
start()  
  
Starts up the semantic unit scanner with an optional  
character set, which acts as a hint to optimize the heuristics  
used to determine the language(s) of the processed text.  
  
@param characterSet the character set the text was originally  
                    encoded in (can be NULL)  
  

#### Parameters ####

<table>

<tr>
<td>characterSet</td>
<td>the character set the text was originally  
                    encoded in (can be NULL)  
</td>
</tr>

</table>

### next(text, length, pos, isLastBuffer, begin, end) ###
  
next()  
Get the begin / end offset of the next unit in the current text  
  
@param text the text to be scanned  
@param length the number of characters in the text to be processed  
@param pos the current position  
@param isLastBuffer, the buffer is the last one  
@param begin the begin offset of the next unit   
@param begin the end offset of the next unit   
@return has more unit in the current text  
  

#### Parameters ####

<table>

<tr>
<td>text</td>
<td>the text to be scanned  
</td>
</tr>

<tr>
<td>length</td>
<td>the number of characters in the text to be processed  
</td>
</tr>

<tr>
<td>pos</td>
<td>the current position  
</td>
</tr>

<tr>
<td>isLastBuffer,</td>
<td>the buffer is the last one  
</td>
</tr>

<tr>
<td>begin</td>
<td>the begin offset of the next unit   
</td>
</tr>

<tr>
<td>begin</td>
<td>the end offset of the next unit   
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>has more unit in the current text  
</td>
</tr>

</table>
