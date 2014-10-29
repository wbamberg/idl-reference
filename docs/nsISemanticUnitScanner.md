---
layout: default
---

# nsISemanticUnitScanner #

Provides a language independent way to break UNICODE
text into meaningful semantic units (e.g. words).


## start ##

start()

Starts up the semantic unit scanner with an optional
character set, which acts as a hint to optimize the heuristics
used to determine the language(s) of the processed text.

@param characterSet the character set the text was originally
                    encoded in (can be NULL)


## next ##

next()
Get the begin / end offset of the next unit in the current text

@param text the text to be scanned
@param length the number of characters in the text to be processed
@param pos the current position
@param isLastBuffer, the buffer is the last one
@param begin the begin offset of the next unit 
@param begin the end offset of the next unit 
@return has more unit in the current text

