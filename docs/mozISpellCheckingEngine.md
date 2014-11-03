---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/extensions/spellcheck/idl/mozISpellCheckingEngine.idl">Source file</a>
</div>

# mozISpellCheckingEngine #
<pre>  
This interface represents a SpellChecker.  
  
</pre>
## Methods ##

### getDictionaryList(dictionaries, count) ###
<pre>  
Get the list of dictionaries  
  
</pre>
### check(word) ###
<pre>  
check a word  
  
The spellcheck engine will send a notification with  
"spellcheck-dictionary-update" as topic when this changes.  
  
</pre>
### suggest(word, suggestions, count) ###
<pre>  
get a list of suggestions for a misspelled word  
  
The spellcheck engine will send a notification with  
"spellcheck-dictionary-update" as topic when this changes.  
  
</pre>
### loadDictionariesFromDir(dir) ###
<pre>  
Load dictionaries from the specified dir  
  
</pre>
### addDirectory(dir) ###
<pre>  
Add dictionaries from a directory to the spell checker  
  
</pre>
### removeDirectory(dir) ###
<pre>  
Remove dictionaries from a directory from the spell checker  
  
</pre>
## Attributes ##

### dictionary ###
<pre>  
The name of the current dictionary. Is either a value from  
getDictionaryList or the empty string if no dictionary is selected.  
Setting this attribute to a value not in getDictionaryList will throw  
NS_ERROR_FILE_NOT_FOUND.  
  
The spellcheck engine will send a notification with  
"spellcheck-dictionary-update" as topic when this changes.  
If the dictionary is changed to no dictionary (the empty string), an  
observer is allowed to set another dictionary before it returns.  
  
</pre>
### language ###
<pre>  
The language this spellchecker is using when checking  
  
The spellcheck engine will send a notification with  
"spellcheck-dictionary-update" as topic when this changes.  
  
</pre>
### providesPersonalDictionary ###
<pre>  
Does the engine provide its own personal dictionary?  
  
</pre>
### providesWordUtils ###
<pre>  
Does the engine provide its own word utils?  
  
</pre>
### name ###
<pre>  
The name of the engine  
  
</pre>
### copyright ###
<pre>   
a string indicating the copyright of the engine  
  
</pre>
### personalDictionary ###
<pre>  
the personal dictionary  
  
</pre>