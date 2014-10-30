---
layout: default
---

# mozIStorageRow #

## Methods ##

### getResultByIndex(aIndex) ###
  
Obtains the result of a given column specified by aIndex.  
  
@param aIndex  
       Zero-based index of the result to get from the tuple.  
@returns the result of the specified column.  
  

### getResultByName(aName) ###
  
Obtains the result of a given column specified by aName.  
  
@param aName  
       Name of the result to get from the tuple.  
@returns the result of the specified column.  
@note The name of a result column is the value of the "AS" clause for that  
      column.  If there is no AS clause then the name of the column is  
      unspecified and may change from one release to the next.  
  
