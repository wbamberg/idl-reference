---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/extensions/spellcheck/idl/mozISpellI18NUtil.idl">Source file</a>
</div>

# mozISpellI18NUtil #
<pre>  
This interface contains various I18N related code used in various places by the spell checker.  
  
</pre>
## Methods ##

### getRootForm(word, type, words, count) ###
<pre>  
Given a word return a list of possible root forms of that word  
  
</pre>
### fromRootForm(word, iwords, icount, owords, ocount) ###
<pre>  
Given a word return a list of possible root forms of that word  
  
</pre>
### findNextWord(word, length, offset, begin, end) ###
<pre>  
Given a unicode string and an offset, find the beginning and end of the  
next word. begin and end are -1 if there are no words remaining in the   
string. This should really be folded into the Line/WordBreaker.  
  
</pre>
## Attributes ##

### language ###
<pre>  
The language being used to check spelling  
  
</pre>
## Constants ##

### kCheck ###

### kSuggest ###
