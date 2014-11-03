---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/extensions/spellcheck/idl/mozIPersonalDictionary.idl">Source file</a>
</div>

# mozIPersonalDictionary #
<pre>  
This interface represents a Personal Dictionary.  
  
</pre>
## Methods ##

### load() ###
<pre>  
Load the dictionary  
  
</pre>
### save() ###
<pre>  
Save the dictionary  
  
</pre>
### check(word, lang) ###
<pre>  
Check a unicode string  
  
</pre>
### addWord(word, lang) ###
<pre>  
Add a word to the personal dictionary  
  
</pre>
### removeWord(word, lang) ###
<pre>  
Remove a word from the personal dictionary  
  
</pre>
### ignoreWord(word) ###
<pre>  
Add a word to the ignore all list  
  
</pre>
### endSession() ###
<pre>  
Clear the ignore list  
  
</pre>
### addCorrection(word, correction, lang) ###
<pre>   
These three functions are here in case we want to store previous   
misspellings and return them at the head of the misspell list.  
  
</pre><pre>  
Add a misspelling to the list of corrections  
  
</pre>
### removeCorrection(word, correction, lang) ###
<pre>  
Remove a misspelling from the list of corrections  
  
</pre>
### getCorrection(word, words, count) ###
<pre>  
Get a list of previous corrections for the word  
  
</pre>
## Attributes ##

### wordList ###
<pre>  
Get the (lexicographically sorted) list of words  
  
</pre>