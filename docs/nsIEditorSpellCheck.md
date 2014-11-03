---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIEditorSpellCheck.idl">Source file</a>
</div>

# nsIEditorSpellCheck #

## Methods ##

### checkCurrentDictionary() ###
<code>  
Call this on any change in installed dictionaries to ensure that the spell  
checker is not using a current dictionary which is no longer available.  
If the current dictionary is no longer available, then pick another one.  
  
</code>
### canSpellCheck() ###
<code>  
Returns true if we can enable spellchecking. If there are no available  
dictionaries, this will return false.  
  
</code>
### InitSpellChecker(editor, enableSelectionChecking, callback) ###
<code>  
Turns on the spell checker for the given editor. enableSelectionChecking  
set means that we only want to check the current selection in the editor,  
(this controls the behavior of GetNextMisspelledWord). For spellchecking  
clients with no modal UI (such as inline spellcheckers), this flag doesn't  
matter.  Initialization is asynchronous and is not complete until the given  
callback is called.  
  
</code>
### GetNextMisspelledWord() ###
<code>  
When interactively spell checking the document, this will return the  
value of the next word that is misspelled. This also computes the  
suggestions which you can get by calling GetSuggestedWord.  
  
@see nsISpellChecker::GetNextMisspelledWord  
  
</code>
### GetSuggestedWord() ###
<code>  
Used to get suggestions for the last word that was checked and found to  
be misspelled. The first call will give you the first (best) suggestion.  
Subsequent calls will iterate through all the suggestions, allowing you  
to build a list. When there are no more suggestions, an empty string  
(not a null pointer) will be returned.  
  
@see nsISpellChecker::GetSuggestedWord  
  
</code>
### CheckCurrentWord(suggestedWord) ###
<code>  
Check a given word. In spite of the name, this function checks the word  
you give it, returning true if the word is misspelled. If the word is  
misspelled, it will compute the suggestions which you can get from  
GetSuggestedWord().  
  
@see nsISpellChecker::CheckCurrentWord  
  
</code>
### ReplaceWord(misspelledWord, replaceWord, allOccurrences) ###
<code>  
Use when modally checking the document to replace a word.  
  
@see nsISpellChecker::CheckCurrentWord  
  
</code>
### IgnoreWordAllOccurrences(word) ###
<code>  
@see nsISpellChecker::IgnoreAll  
  
</code>
### GetPersonalDictionary() ###
<code>  
Fills an internal list of words added to the personal dictionary. These  
words can be retrieved using GetPersonalDictionaryWord()  
  
@see nsISpellChecker::GetPersonalDictionary  
@see GetPersonalDictionaryWord  
  
</code>
### GetPersonalDictionaryWord() ###
<code>  
Used after you call GetPersonalDictionary() to iterate through all the  
words added to the personal dictionary. Will return the empty string when  
there are no more words.  
  
</code>
### AddWordToDictionary(word) ###
<code>  
Adds a word to the current personal dictionary.  
  
@see nsISpellChecker::AddWordToDictionary  
  
</code>
### RemoveWordFromDictionary(word) ###
<code>  
Removes a word from the current personal dictionary.  
  
@see nsISpellChecker::RemoveWordFromPersonalDictionary  
  
</code>
### GetDictionaryList(dictionaryList, count) ###
<code>  
Retrieves a list of the currently available dictionaries. The strings will  
typically be language IDs, like "en-US".  
  
@see mozISpellCheckingEngine::GetDictionaryList  
  
</code>
### GetCurrentDictionary() ###
<code>  
@see nsISpellChecker::GetCurrentDictionary  
  
</code>
### SetCurrentDictionary(dictionary) ###
<code>  
@see nsISpellChecker::SetCurrentDictionary  
  
</code>
### UninitSpellChecker() ###
<code>  
Call this to free up the spell checking object. It will also save the  
current selected language as the default for future use.  
  
If you have called CanSpellCheck but not InitSpellChecker, you can still  
call this function to clear the cached spell check object, and no  
preference saving will happen.  
  
</code>
### setFilter(filter) ###
<code>  
Used to filter the content (for example, to skip blockquotes in email from  
spellchecking. Call this before calling InitSpellChecker; calling it  
after initialization will have no effect.  
  
@see nsITextServicesDocument::setFilter  
  
</code>
### CheckCurrentWordNoSuggest(suggestedWord) ###
<code>  
Like CheckCurrentWord, checks the word you give it, returning true if it's  
misspelled. This is faster than CheckCurrentWord because it does not  
compute any suggestions.  
  
Watch out: this does not clear any suggestions left over from previous  
calls to CheckCurrentWord, so there may be suggestions, but they will be  
invalid.  
  
</code>
### UpdateCurrentDictionary(callback) ###
<code>  
Update the dictionary in use to be sure it corresponds to what the editor  
needs.  The update is asynchronous and is not complete until the given  
callback is called.  
  
</code>