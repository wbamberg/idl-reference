---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/extensions/spellcheck/idl/mozIPersonalDictionary.idl">Source file</a>
</div>

# mozIPersonalDictionary #
<code>  
This interface represents a Personal Dictionary.  
  
</code>
## Methods ##

### load() ###
<code>  
Load the dictionary  
  
</code>
### save() ###
<code>  
Save the dictionary  
  
</code>
### check(word, lang) ###
<code>  
Check a unicode string  
  
</code>
### addWord(word, lang) ###
<code>  
Add a word to the personal dictionary  
  
</code>
### removeWord(word, lang) ###
<code>  
Remove a word from the personal dictionary  
  
</code>
### ignoreWord(word) ###
<code>  
Add a word to the ignore all list  
  
</code>
### endSession() ###
<code>  
Clear the ignore list  
  
</code>
### addCorrection(word, correction, lang) ###
<code>   
These three functions are here in case we want to store previous   
misspellings and return them at the head of the misspell list.  
  
</code><code>  
Add a misspelling to the list of corrections  
  
</code>
### removeCorrection(word, correction, lang) ###
<code>  
Remove a misspelling from the list of corrections  
  
</code>
### getCorrection(word, words, count) ###
<code>  
Get a list of previous corrections for the word  
  
</code>
## Attributes ##

### wordList ###
  
Get the (lexicographically sorted) list of words  
  
