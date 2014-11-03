---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/extensions/spellcheck/idl/mozISpellI18NUtil.idl">Source file</a>
</div>

# mozISpellI18NUtil #
<code>  
This interface contains various I18N related code used in various places by the spell checker.  
  
</code>
## Methods ##

### getRootForm(word, type, words, count) ###
<code>  
Given a word return a list of possible root forms of that word  
  
</code>
### fromRootForm(word, iwords, icount, owords, ocount) ###
<code>  
Given a word return a list of possible root forms of that word  
  
</code>
### findNextWord(word, length, offset, begin, end) ###
<code>  
Given a unicode string and an offset, find the beginning and end of the  
next word. begin and end are -1 if there are no words remaining in the   
string. This should really be folded into the Line/WordBreaker.  
  
</code>
## Attributes ##

### language ###
  
The language being used to check spelling  
  

## Constants ##

### kCheck ###

### kSuggest ###
