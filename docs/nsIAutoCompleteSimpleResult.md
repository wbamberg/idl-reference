---
layout: default
---

# nsIAutoCompleteSimpleResult #
  
This class implements nsIAutoCompleteResult and provides simple methods  
for setting the value and result items. It can be used whenever some basic  
auto complete results are needed that can be pre-generated and filled into  
an array.  
  

## Methods ##

### setSearchString(aSearchString) ###
  
A writer for the readonly attribute 'searchString' which should contain  
the string that the user typed.  
  

### setErrorDescription(aErrorDescription) ###
  
A writer for the readonly attribute 'errorDescription'.  
  

### setDefaultIndex(aDefaultIndex) ###
  
A writer for the readonly attribute 'defaultIndex' which should contain  
the index of the list that will be selected by default (normally 0).  
  

### setSearchResult(aSearchResult) ###
  
A writer for the readonly attribute 'searchResult' which should contain  
one of the constants nsIAutoCompleteResult.RESULT_* indicating the success  
of the search.  
  

### setTypeAheadResult(aHidden) ###
  
A writer for the readonly attribute 'typeAheadResult', typically set  
because a result is only intended for type-ahead completion.  
  

### appendMatch(aValue, aComment, aImage, aStyle, aFinalCompleteValue) ###
  
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
  

### setListener(aListener) ###
  
Sets a listener for changes in the result.  
  
