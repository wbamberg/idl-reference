---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/autocomplete/nsIAutoCompleteResult.idl">Source file</a>
</div>

# nsIAutoCompleteResult #

## Methods ##

### getValueAt(index) ###
<code>  
Get the value of the result at the given index  
  
</code>
### getLabelAt(index) ###
<code>  
This returns the string that is displayed in the dropdown  
  
</code>
### getCommentAt(index) ###
<code>  
Get the comment of the result at the given index  
  
</code>
### getStyleAt(index) ###
<code>  
Get the style hint for the result at the given index  
  
</code>
### getImageAt(index) ###
<code>  
Get the image of the result at the given index  
  
</code>
### getFinalCompleteValueAt(index) ###
<code>  
Get the final value that should be completed when the user confirms  
the match at the given index.  
  
</code>
### removeValueAt(rowIndex, removeFromDb) ###
<code>  
Remove the value at the given index from the autocomplete results.  
If removeFromDb is set to true, the value should be removed from  
persistent storage as well.  
  
</code>
## Attributes ##

### searchString ###
  
The original search string  
  

### searchResult ###
  
The result of the search  
  

### defaultIndex ###
  
Index of the default item that should be entered if none is selected  
  

### errorDescription ###
  
A string describing the cause of a search failure  
  

### matchCount ###
  
The number of matches  
  

### typeAheadResult ###
  
If true, the results will not be displayed in the popup. However,  
if a default index is specified, the default item will still be  
completed in the input.  
  

## Constants ##

### RESULT_IGNORED ###
  
Possible values for the searchResult attribute  
  

### RESULT_FAILURE ###

### RESULT_NOMATCH ###

### RESULT_SUCCESS ###

### RESULT_NOMATCH_ONGOING ###

### RESULT_SUCCESS_ONGOING ###
