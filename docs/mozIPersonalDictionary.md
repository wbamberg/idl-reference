---
layout: default
---

# mozIPersonalDictionary #

This interface represents a Personal Dictionary.


## Methods ##

### load ###

Load the dictionary


### save ###

Save the dictionary


### check ###

Check a unicode string


### addWord ###

Add a word to the personal dictionary


### removeWord ###

Remove a word from the personal dictionary


### ignoreWord ###

Add a word to the ignore all list


### endSession ###

Clear the ignore list


### addCorrection ###
 
These three functions are here in case we want to store previous 
misspellings and return them at the head of the misspell list.


Add a misspelling to the list of corrections


### removeCorrection ###

Remove a misspelling from the list of corrections


### getCorrection ###

Get a list of previous corrections for the word


## Attributes ##

### wordList ###

Get the (lexicographically sorted) list of words

