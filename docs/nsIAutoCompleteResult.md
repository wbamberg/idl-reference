---
layout: default
---

# nsIAutoCompleteResult #

## RESULT_IGNORED ##

Possible values for the searchResult attribute


## RESULT_FAILURE ##

## RESULT_NOMATCH ##

## RESULT_SUCCESS ##

## RESULT_NOMATCH_ONGOING ##

## RESULT_SUCCESS_ONGOING ##

## searchString ##

The original search string


## searchResult ##

The result of the search


## defaultIndex ##

Index of the default item that should be entered if none is selected


## errorDescription ##

A string describing the cause of a search failure


## matchCount ##

The number of matches


## typeAheadResult ##

If true, the results will not be displayed in the popup. However,
if a default index is specified, the default item will still be
completed in the input.


## getValueAt ##

Get the value of the result at the given index


## getLabelAt ##

This returns the string that is displayed in the dropdown


## getCommentAt ##

Get the comment of the result at the given index


## getStyleAt ##

Get the style hint for the result at the given index


## getImageAt ##

Get the image of the result at the given index


## getFinalCompleteValueAt ##

Get the final value that should be completed when the user confirms
the match at the given index.


## removeValueAt ##

Remove the value at the given index from the autocomplete results.
If removeFromDb is set to true, the value should be removed from
persistent storage as well.

