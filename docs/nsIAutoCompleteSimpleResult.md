---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/autocomplete/nsIAutoCompleteSimpleResult.idl">Source file</a>
</div>

# nsIAutoCompleteSimpleResult #
<code>  
This class implements nsIAutoCompleteResult and provides simple methods  
for setting the value and result items. It can be used whenever some basic  
auto complete results are needed that can be pre-generated and filled into  
an array.  
  
</code>
## Methods ##

### setSearchString(aSearchString) ###
<code>  
A writer for the readonly attribute 'searchString' which should contain  
the string that the user typed.  
  
</code>
### setErrorDescription(aErrorDescription) ###
<code>  
A writer for the readonly attribute 'errorDescription'.  
  
</code>
### setDefaultIndex(aDefaultIndex) ###
<code>  
A writer for the readonly attribute 'defaultIndex' which should contain  
the index of the list that will be selected by default (normally 0).  
  
</code>
### setSearchResult(aSearchResult) ###
<code>  
A writer for the readonly attribute 'searchResult' which should contain  
one of the constants nsIAutoCompleteResult.RESULT_* indicating the success  
of the search.  
  
</code>
### setTypeAheadResult(aHidden) ###
<code>  
A writer for the readonly attribute 'typeAheadResult', typically set  
because a result is only intended for type-ahead completion.  
  
</code>
### appendMatch(aValue, aComment, aImage, aStyle, aFinalCompleteValue) ###
<code>  
Appends a match consisting of the given value, comment, image, style and  
the value to use for defaultIndex completion.  
@param aValue  
       The value to autocomplete to  
@param aComment  
       Comment shown in the autocomplete widget to describe this match  
@param aImage  
       Image shown in the autocomplete widget for this match.  
@param aStyle  
       Describes how to style the match in the autocomplete widget  
@param aFinalCompleteValue  
       Value used when the user confirms selecting this match. If not  
       provided, aValue will be used.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aValue</td>
<td>       The value to autocomplete to  
</td>
</tr>

<tr>
<td>aComment</td>
<td>       Comment shown in the autocomplete widget to describe this match  
</td>
</tr>

<tr>
<td>aImage</td>
<td>       Image shown in the autocomplete widget for this match.  
</td>
</tr>

<tr>
<td>aStyle</td>
<td>       Describes how to style the match in the autocomplete widget  
</td>
</tr>

<tr>
<td>aFinalCompleteValue</td>
<td>       Value used when the user confirms selecting this match. If not  
       provided, aValue will be used.  
</td>
</tr>

</table>

### setListener(aListener) ###
<code>  
Sets a listener for changes in the result.  
  
</code>