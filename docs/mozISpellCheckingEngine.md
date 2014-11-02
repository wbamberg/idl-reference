---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/extensions/spellcheck/idl/mozISpellCheckingEngine.idl">Source file</a>
</div>
# mozISpellCheckingEngine #
  
This interface represents a SpellChecker.  
  

## Methods ##

### getDictionaryList(dictionaries, count) ###
  
Get the list of dictionaries  
  

### check(word) ###
  
check a word  
  
The spellcheck engine will send a notification with  
"spellcheck-dictionary-update" as topic when this changes.  
  

### suggest(word, suggestions, count) ###
  
get a list of suggestions for a misspelled word  
  
The spellcheck engine will send a notification with  
"spellcheck-dictionary-update" as topic when this changes.  
  

### loadDictionariesFromDir(dir) ###
  
Load dictionaries from the specified dir  
  

### addDirectory(dir) ###
  
Add dictionaries from a directory to the spell checker  
  

### removeDirectory(dir) ###
  
Remove dictionaries from a directory from the spell checker  
  

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
  
