---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/satchel/nsIFormAutoComplete.idl">Source file</a>
</div>

# nsIFormAutoComplete #

## Methods ##

### autoCompleteSearch(aInputName, aSearchString, aField, aPreviousResult) ###
<code>  
Generate results for a form input autocomplete menu synchronously.  
This method is deprecated in favour of autoCompleteSearchAsync.  
  
</code>
### autoCompleteSearchAsync(aInputName, aSearchString, aField, aPreviousResult, aListener) ###
<code>  
Generate results for a form input autocomplete menu asynchronously.  
  
</code>
### stopAutoCompleteSearch() ###
<code>  
If a search is in progress, stop it. Otherwise, do nothing. This is used  
to cancel an existing search, for example, in preparation for a new search.  
  
</code>