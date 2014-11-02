---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/satchel/nsIFormHistory.idl">Source file</a>
</div>

# nsIFormHistory2 #
  
The nsIFormHistory object is a service which holds a set of name/value  
pairs.  The names correspond to form field names, and the values correspond  
to values the user has submitted.  So, several values may exist for a single  
name.  
  
Note: this interface provides no means to access stored values.  
Stored values are used by the FormFillController to generate  
autocomplete matches.  
  
@deprecated use FormHistory.jsm instead.  
  

## Methods ##

### addEntry(name, value) ###
  
Adds a name and value pair to the form history.  
  

### removeEntry(name, value) ###
  
Removes a name and value pair from the form history.  
  

### removeEntriesForName(name) ###
  
Removes all entries that are paired with a name.  
  

### removeAllEntries() ###
  
Removes all entries in the entire form history.  
  

### nameExists(name) ###
  
Returns true if there is no entry that is paired with a name.  
  

### entryExists(name, value) ###
  
Gets whether a name and value pair exists in the form history.  
  

### removeEntriesByTimeframe(aBeginTime, aEndTime) ###
  
Removes entries that were created between the specified times.  
  
@param aBeginTime  
       The beginning of the timeframe, in microseconds  
@param aEndTime  
       The end of the timeframe, in microseconds  
  

#### Parameters ####

<table>

<tr>
<td>aBeginTime</td>
<td>       The beginning of the timeframe, in microseconds  
</td>
</tr>

<tr>
<td>aEndTime</td>
<td>       The end of the timeframe, in microseconds  
</td>
</tr>

</table>

## Attributes ##

### hasEntries ###
  
Returns true if the form history has any entries.  
  

### DBConnection ###
  
Returns the underlying DB connection the form history module is using.  
  
