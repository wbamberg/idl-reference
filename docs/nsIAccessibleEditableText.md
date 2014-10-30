---
layout: default
---

# nsIAccessibleEditableText #

## Methods ##

### setTextContents ###
  
Replaces the text represented by this object by the given text.  
  

### insertText ###
  
Inserts text at the specified position.  
  
@param text - text that is inserted.  
@param position - index at which to insert the text.  
  

### copyText ###
  
Copies the text range into the clipboard.  
  
@param startPos - start index of the text to moved into the clipboard.  
@param endPos - end index of the text to moved into the clipboard.  
  

### cutText ###
  
Deletes a range of text and copies it to the clipboard.  
  
@param startPos - start index of the text to be deleted.  
@param endOffset - end index of the text to be deleted.  
  

### deleteText ###
  
Deletes a range of text.  
  
@param startPos - start index of the text to be deleted.  
@param endPos - end index of the text to be deleted.  
  

### pasteText ###
  
Pastes text from the clipboard.  
  
@param position - index at which to insert the text from the system  
                  clipboard into the text represented by this object.  
  
