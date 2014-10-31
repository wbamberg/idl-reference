---
layout: default
---

# nsIFind #

## Methods ##

### Find(aPatText, aSearchRange, aStartPoint, aEndPoint) ###
  
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
  

#### Parameters ####

<table>

<tr>
<td>aPatText</td>
<td>The text to search for.  
</td>
</tr>

<tr>
<td>aSearchRange</td>
<td>A Range specifying domain of search.  
</td>
</tr>

<tr>
<td>aStartPoint</td>
<td>A Range specifying search start point.  
                    If not collapsed, we'll start from  
                    end (forward) or start (backward).  
</td>
</tr>

<tr>
<td>aEndPoint</td>
<td>A Range specifying search end point.  
                    If not collapsed, we'll end at  
                    end (forward) or start (backward).  
@retval             A range spanning the match that was found (or null).  
</td>
</tr>

</table>

## Attributes ##

### findBackwards ###

### caseSensitive ###

### wordBreaker ###
  
Use "find entire words" mode by setting to a word breaker  
or null, to disable "entire words" mode.  
  
