---
layout: default
---

# nsIFind #

## Methods ##

### Find ###

Find some text in the current context. The implementation is
responsible for performing the find and highlighting the text.

@param aPatText     The text to search for.
@param aSearchRange A Range specifying domain of search.
@param aStartPoint  A Range specifying search start point.
                    If not collapsed, we'll start from
                    end (forward) or start (backward).
@param aEndPoint    A Range specifying search end point.
                    If not collapsed, we'll end at
                    end (forward) or start (backward).
@retval             A range spanning the match that was found (or null).


## Attributes ##

### findBackwards ###

### caseSensitive ###

### wordBreaker ###

Use "find entire words" mode by setting to a word breaker
or null, to disable "entire words" mode.

