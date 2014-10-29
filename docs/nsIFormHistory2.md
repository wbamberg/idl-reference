---
layout: default
---

# nsIFormHistory2 #

The nsIFormHistory object is a service which holds a set of name/value
pairs.  The names correspond to form field names, and the values correspond
to values the user has submitted.  So, several values may exist for a single
name.

Note: this interface provides no means to access stored values.
Stored values are used by the FormFillController to generate
autocomplete matches.

@deprecated use FormHistory.jsm instead.


## hasEntries ##

Returns true if the form history has any entries.


## addEntry ##

Adds a name and value pair to the form history.


## removeEntry ##

Removes a name and value pair from the form history.


## removeEntriesForName ##

Removes all entries that are paired with a name.


## removeAllEntries ##

Removes all entries in the entire form history.


## nameExists ##

Returns true if there is no entry that is paired with a name.


## entryExists ##

Gets whether a name and value pair exists in the form history.


## removeEntriesByTimeframe ##

Removes entries that were created between the specified times.

@param aBeginTime
       The beginning of the timeframe, in microseconds
@param aEndTime
       The end of the timeframe, in microseconds


## DBConnection ##

Returns the underlying DB connection the form history module is using.

