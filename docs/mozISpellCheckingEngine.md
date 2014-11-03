---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/extensions/spellcheck/idl/mozISpellCheckingEngine.idl">Source file</a>
</div>

# mozISpellCheckingEngine #
<code>  
This interface represents a SpellChecker.  
  
</code>
## Methods ##

### getDictionaryList(dictionaries, count) ###
<code>  
Get the list of dictionaries  
  
</code>
### check(word) ###
<code>  
check a word  
  
The spellcheck engine will send a notification with  
"spellcheck-dictionary-update" as topic when this changes.  
  
</code>
### suggest(word, suggestions, count) ###
<code>  
get a list of suggestions for a misspelled word  
  
The spellcheck engine will send a notification with  
"spellcheck-dictionary-update" as topic when this changes.  
  
</code>
### loadDictionariesFromDir(dir) ###
<code>  
Load dictionaries from the specified dir  
  
</code>
### addDirectory(dir) ###
<code>  
Add dictionaries from a directory to the spell checker  
  
</code>
### removeDirectory(dir) ###
<code>  
Remove dictionaries from a directory from the spell checker  
  
</code>
## Attributes ##

### dictionary ###
  
The name of the current dictionary. Is either a value from  
getDictionaryList or the empty string if no dictionary is selected.  
Setting this attribute to a value not in getDictionaryList will throw  
NS_ERROR_FILE_NOT_FOUND.  
  
The spellcheck engine will send a notification with  
"spellcheck-dictionary-update" as topic when this changes.  
If the dictionary is changed to no dictionary (the empty string), an  
observer is allowed to set another dictionary before it returns.  
  

### language ###
  
The language this spellchecker is using when checking  
  
The spellcheck engine will send a notification with  
"spellcheck-dictionary-update" as topic when this changes.  
  

### providesPersonalDictionary ###
  
Does the engine provide its own personal dictionary?  
  

### providesWordUtils ###
  
Does the engine provide its own word utils?  
  

### name ###
  
The name of the engine  
  

### copyright ###
   
a string indicating the copyright of the engine  
  

### personalDictionary ###
  
the personal dictionary  
  
