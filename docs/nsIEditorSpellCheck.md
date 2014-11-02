---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIEditorSpellCheck.idl">Source file</a>
</div>
# nsIEditorSpellCheck #

## Methods ##

### checkCurrentDictionary() ###
  
Call this on any change in installed dictionaries to ensure that the spell  
checker is not using a current dictionary which is no longer available.  
If the current dictionary is no longer available, then pick another one.  
  

### canSpellCheck() ###
  
Returns true if we can enable spellchecking. If there are no available  
dictionaries, this will return false.  
  

### InitSpellChecker(editor, enableSelectionChecking, callback) ###
  
Turns on the spell checker for the given editor. enableSelectionChecking  
set means that we only want to check the current selection in the editor,  
(this controls the behavior of GetNextMisspelledWord). For spellchecking  
clients with no modal UI (such as inline spellcheckers), this flag doesn't  
matter.  Initialization is asynchronous and is not complete until the given  
callback is called.  
  

### GetNextMisspelledWord() ###
  
When interactively spell checking the document, this will return the  
value of the next word that is misspelled. This also computes the  
suggestions which you can get by calling GetSuggestedWord.  
  
@see nsISpellChecker::GetNextMisspelledWord  
  

### GetSuggestedWord() ###
  
Used to get suggestions for the last word that was checked and found to  
be misspelled. The first call will give you the first (best) suggestion.  
Subsequent calls will iterate through all the suggestions, allowing you  
to build a list. When there are no more suggestions, an empty string  
(not a null pointer) will be returned.  
  
@see nsISpellChecker::GetSuggestedWord  
  

### CheckCurrentWord(suggestedWord) ###
  
Check a given word. In spite of the name, this function checks the word  
you give it, returning true if the word is misspelled. If the word is  
misspelled, it will compute the suggestions which you can get from  
GetSuggestedWord().  
  
@see nsISpellChecker::CheckCurrentWord  
  

### ReplaceWord(misspelledWord, replaceWord, allOccurrences) ###
  
Use when modally checking the document to replace a word.  
  
@see nsISpellChecker::CheckCurrentWord  
  

### IgnoreWordAllOccurrences(word) ###
  
@see nsISpellChecker::IgnoreAll  
  

### GetPersonalDictionary() ###
  
Fills an internal list of words added to the personal dictionary. These  
words can be retrieved using GetPersonalDictionaryWord()  
  
@see nsISpellChecker::GetPersonalDictionary  
@see GetPersonalDictionaryWord  
  

### GetPersonalDictionaryWord() ###
  
Used after you call GetPersonalDictionary() to iterate through all the  
words added to the personal dictionary. Will return the empty string when  
there are no more words.  
  

### AddWordToDictionary(word) ###
  
Adds a word to the current personal dictionary.  
  
@see nsISpellChecker::AddWordToDictionary  
  

### RemoveWordFromDictionary(word) ###
  
Removes a word from the current personal dictionary.  
  
@see nsISpellChecker::RemoveWordFromPersonalDictionary  
  

### GetDictionaryList(dictionaryList, count) ###
  
Retrieves a list of the currently available dictionaries. The strings will  
typically be language IDs, like "en-US".  
  
@see mozISpellCheckingEngine::GetDictionaryList  
  

### GetCurrentDictionary() ###
  
@see nsISpellChecker::GetCurrentDictionary  
  

### SetCurrentDictionary(dictionary) ###
  
@see nsISpellChecker::SetCurrentDictionary  
  

### UninitSpellChecker() ###
  
Call this to free up the spell checking object. It will also save the  
current selected language as the default for future use.  
  
If you have called CanSpellCheck but not InitSpellChecker, you can still  
call this function to clear the cached spell check object, and no  
preference saving will happen.  
  

### setFilter(filter) ###
  
Used to filter the content (for example, to skip blockquotes in email from  
spellchecking. Call this before calling InitSpellChecker; calling it  
after initialization will have no effect.  
  
@see nsITextServicesDocument::setFilter  
  

### CheckCurrentWordNoSuggest(suggestedWord) ###
  
Like CheckCurrentWord, checks the word you give it, returning true if it's  
misspelled. This is faster than CheckCurrentWord because it does not  
compute any suggestions.  
  
Watch out: this does not clear any suggestions left over from previous  
calls to CheckCurrentWord, so there may be suggestions, but they will be  
invalid.  
  

### UpdateCurrentDictionary(callback) ###
  
Update the dictionary in use to be sure it corresponds to what the editor  
needs.  The update is asynchronous and is not complete until the given  
callback is called.  
  
