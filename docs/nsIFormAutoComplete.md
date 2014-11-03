---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/satchel/nsIFormAutoComplete.idl">Source file</a>
</div>

# nsIFormAutoComplete #

## Methods ##

### autoCompleteSearch(aInputName, aSearchString, aField, aPreviousResult) ###
<pre>  
Generate results for a form input autocomplete menu synchronously.  
This method is deprecated in favour of autoCompleteSearchAsync.  
  
</pre>
### autoCompleteSearchAsync(aInputName, aSearchString, aField, aPreviousResult, aListener) ###
<pre>  
Generate results for a form input autocomplete menu asynchronously.  
  
</pre>
### stopAutoCompleteSearch() ###
<pre>  
If a search is in progress, stop it. Otherwise, do nothing. This is used  
to cancel an existing search, for example, in preparation for a new search.  
  
</pre>