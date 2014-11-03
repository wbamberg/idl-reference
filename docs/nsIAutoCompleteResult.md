---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/autocomplete/nsIAutoCompleteResult.idl">Source file</a>
</div>

# nsIAutoCompleteResult #

## Methods ##

### getValueAt(index) ###
<pre>  
Get the value of the result at the given index  
  
</pre>
### getLabelAt(index) ###
<pre>  
This returns the string that is displayed in the dropdown  
  
</pre>
### getCommentAt(index) ###
<pre>  
Get the comment of the result at the given index  
  
</pre>
### getStyleAt(index) ###
<pre>  
Get the style hint for the result at the given index  
  
</pre>
### getImageAt(index) ###
<pre>  
Get the image of the result at the given index  
  
</pre>
### getFinalCompleteValueAt(index) ###
<pre>  
Get the final value that should be completed when the user confirms  
the match at the given index.  
  
</pre>
### removeValueAt(rowIndex, removeFromDb) ###
<pre>  
Remove the value at the given index from the autocomplete results.  
If removeFromDb is set to true, the value should be removed from  
persistent storage as well.  
  
</pre>
## Attributes ##

### searchString ###
<pre>  
The original search string  
  
</pre>
### searchResult ###
<pre>  
The result of the search  
  
</pre>
### defaultIndex ###
<pre>  
Index of the default item that should be entered if none is selected  
  
</pre>
### errorDescription ###
<pre>  
A string describing the cause of a search failure  
  
</pre>
### matchCount ###
<pre>  
The number of matches  
  
</pre>
### typeAheadResult ###
<pre>  
If true, the results will not be displayed in the popup. However,  
if a default index is specified, the default item will still be  
completed in the input.  
  
</pre>
## Constants ##

### RESULT_IGNORED ###
<pre>  
Possible values for the searchResult attribute  
  
</pre>
### RESULT_FAILURE ###

### RESULT_NOMATCH ###

### RESULT_SUCCESS ###

### RESULT_NOMATCH_ONGOING ###

### RESULT_SUCCESS_ONGOING ###
