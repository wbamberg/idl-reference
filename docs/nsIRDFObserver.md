---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFObserver.idl">Source file</a>
</div>

# nsIRDFObserver #

## Methods ##

### onAssert(aDataSource, aSource, aProperty, aTarget) ###
  
This method is called whenever a new assertion is made  
in the data source  
  

#### Parameters ####

<table>

<tr>
<td>aDataSource</td>
<td>the datasource that is issuing  
  the notification.  
</td>
</tr>

<tr>
<td>aSource</td>
<td>the subject of the assertion  
</td>
</tr>

<tr>
<td>aProperty</td>
<td>the predicate of the assertion  
</td>
</tr>

<tr>
<td>aTarget</td>
<td>the object of the assertion  
</td>
</tr>

</table>

### onUnassert(aDataSource, aSource, aProperty, aTarget) ###
  
This method is called whenever an assertion is removed  
from the data source  
  

#### Parameters ####

<table>

<tr>
<td>aDataSource</td>
<td>the datasource that is issuing  
  the notification.  
</td>
</tr>

<tr>
<td>aSource</td>
<td>the subject of the assertion  
</td>
</tr>

<tr>
<td>aProperty</td>
<td>the predicate of the assertion  
</td>
</tr>

<tr>
<td>aTarget</td>
<td>the object of the assertion  
</td>
</tr>

</table>

### onChange(aDataSource, aSource, aProperty, aOldTarget, aNewTarget) ###
  
This method is called when the object of an assertion  
changes from one value to another.  
  

#### Parameters ####

<table>

<tr>
<td>aDataSource</td>
<td>the datasource that is issuing  
  the notification.  
</td>
</tr>

<tr>
<td>aSource</td>
<td>the subject of the assertion  
</td>
</tr>

<tr>
<td>aProperty</td>
<td>the predicate of the assertion  
</td>
</tr>

<tr>
<td>aOldTarget</td>
<td>the old object of the assertion  
</td>
</tr>

<tr>
<td>aNewTarget</td>
<td>the new object of the assertion  
</td>
</tr>

</table>

### onMove(aDataSource, aOldSource, aNewSource, aProperty, aTarget) ###
  
This method is called when the subject of an assertion  
changes from one value to another.  
  

#### Parameters ####

<table>

<tr>
<td>aDataSource</td>
<td>the datasource that is issuing  
  the notification.  
</td>
</tr>

<tr>
<td>aOldSource</td>
<td>the old subject of the assertion  
</td>
</tr>

<tr>
<td>aNewSource</td>
<td>the new subject of the assertion  
</td>
</tr>

<tr>
<td>aProperty</td>
<td>the predicate of the assertion  
</td>
</tr>

<tr>
<td>aTarget</td>
<td>the object of the assertion  
</td>
</tr>

</table>

### onBeginUpdateBatch(aDataSource) ###
  
This method is called when a datasource is about to  
send several notifications at once. The observer can  
use this as a cue to optimize its behavior. The observer  
can expect the datasource to call endUpdateBatch() when  
the group of notifications has completed.  
  

#### Parameters ####

<table>

<tr>
<td>aDataSource</td>
<td>the datasource that is going to  
  be issuing the notifications.  
</td>
</tr>

</table>

### onEndUpdateBatch(aDataSource) ###
  
This method is called when a datasource has completed  
issuing a notification group.  
  

#### Parameters ####

<table>

<tr>
<td>aDataSource</td>
<td>the datasource that has finished  
  issuing a group of notifications  
</td>
</tr>

</table>
