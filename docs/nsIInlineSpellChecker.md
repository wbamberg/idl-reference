---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/txtsvc/nsIInlineSpellChecker.idl">Source file</a>
</div>

# nsIInlineSpellChecker #

## Methods ##

### init(aEditor) ###

### cleanup(aDestroyingFrames) ###

### spellCheckAfterEditorChange(aAction, aSelection, aPreviousSelectedNode, aPreviousSelectedOffset, aStartNode, aStartOffset, aEndNode, aEndOffset) ###

### spellCheckRange(aSelection) ###

### getMisspelledWord(aNode, aOffset) ###

### replaceWord(aNode, aOffset, aNewword) ###

### addWordToDictionary(aWord) ###

### removeWordFromDictionary(aWord) ###

### ignoreWord(aWord) ###

### ignoreWords(aWordsToIgnore, aCount) ###

### updateCurrentDictionary() ###

## Attributes ##

### spellChecker ###

### enableRealTimeSpell ###

### spellCheckPending ###
