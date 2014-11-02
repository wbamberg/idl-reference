---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/base/nsIContentPrefService.idl">Source file</a>
</div>

# nsIContentPrefObserver #

## Methods ##

### onContentPrefSet(aGroup, aName, aValue) ###
  
Called when a content pref is set to a different value.  
  
@param    aGroup      the group to which the pref belongs, or null  
                      if it's a global pref (applies to all sites)  
@param    aName       the name of the pref that was set  
@param    aValue      the new value of the pref  
  

#### Parameters ####

<table>

<tr>
<td>aGroup</td>
<td>the group to which the pref belongs, or null  
                      if it's a global pref (applies to all sites)  
</td>
</tr>

<tr>
<td>aName</td>
<td>the name of the pref that was set  
</td>
</tr>

<tr>
<td>aValue</td>
<td>the new value of the pref  
</td>
</tr>

</table>

### onContentPrefRemoved(aGroup, aName) ###
  
Called when a content pref is removed.  
  
@param    aGroup      the group to which the pref belongs, or null  
                      if it's a global pref (applies to all sites)  
@param    aName       the name of the pref that was removed  
  

#### Parameters ####

<table>

<tr>
<td>aGroup</td>
<td>the group to which the pref belongs, or null  
                      if it's a global pref (applies to all sites)  
</td>
</tr>

<tr>
<td>aName</td>
<td>the name of the pref that was removed  
</td>
</tr>

</table>
