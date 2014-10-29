---
layout: default
---

# nsICompositionStringSynthesizer #

Stores composition clauses information and caret information for synthesizing
composition string.


## setString ##

Set composition string or committed string.


## ATTR_RAWINPUT ##

## ATTR_SELECTEDRAWTEXT ##

## ATTR_CONVERTEDTEXT ##

## ATTR_SELECTEDCONVERTEDTEXT ##

## appendClause ##

Append a clause.

TODO: Should be able to specify custom clause style.


## setCaret ##

Set caret information.


## dispatchEvent ##

Synthesize composition string with given information by dispatching
a proper event.

If clauses have never been set, this dispatches a commit event.
If clauses are not filled all over the composition string, this throw an
error.

After dispatching event, this clears all the information about the
composition string. So, you can reuse this instance.

