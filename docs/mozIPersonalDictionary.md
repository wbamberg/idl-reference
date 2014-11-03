---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/extensions/spellcheck/idl/mozIPersonalDictionary.idl">Source file</a>
</div>

# mozIPersonalDictionary #
  
This interface represents a Personal Dictionary.  
  

## Methods ##

### load() ###
  
Load the dictionary  
  

### save() ###
  
Save the dictionary  
  

### check(word, lang) ###
  
Check a unicode string  
  

### addWord(word, lang) ###
  
Add a word to the personal dictionary  
  

### removeWord(word, lang) ###
  
Remove a word from the personal dictionary  
  

### ignoreWord(word) ###
  
Add a word to the ignore all list  
  

### endSession() ###
  
Clear the ignore list  
  

### addCorrection(word, correction, lang) ###
   
These three functions are here in case we want to store previous   
misspellings and return them at the head of the misspell list.  
  
  
Add a misspelling to the list of corrections  
  

### removeCorrection(word, correction, lang) ###
  
Remove a misspelling from the list of corrections  
  

### getCorrection(word, words, count) ###
  
Get a list of previous corrections for the word  
  

## Attributes ##

### wordList ###
  
Get the (lexicographically sorted) list of words  
  
