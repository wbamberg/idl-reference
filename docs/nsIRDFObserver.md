---
layout: default
---

# nsIRDFObserver #

## Methods ##

### onAssert(aDataSource, aSource, aProperty, aTarget) ###
  
This method is called whenever a new assertion is made  
in the data source  
@param aDataSource the datasource that is issuing  
  the notification.  
@param aSource the subject of the assertion  
@param aProperty the predicate of the assertion  
@param aTarget the object of the assertion  
  

### onUnassert(aDataSource, aSource, aProperty, aTarget) ###
  
This method is called whenever an assertion is removed  
from the data source  
@param aDataSource the datasource that is issuing  
  the notification.  
@param aSource the subject of the assertion  
@param aProperty the predicate of the assertion  
@param aTarget the object of the assertion  
  

### onChange(aDataSource, aSource, aProperty, aOldTarget, aNewTarget) ###
  
This method is called when the object of an assertion  
changes from one value to another.  
@param aDataSource the datasource that is issuing  
  the notification.  
@param aSource the subject of the assertion  
@param aProperty the predicate of the assertion  
@param aOldTarget the old object of the assertion  
@param aNewTarget the new object of the assertion  
  

### onMove(aDataSource, aOldSource, aNewSource, aProperty, aTarget) ###
  
This method is called when the subject of an assertion  
changes from one value to another.  
@param aDataSource the datasource that is issuing  
  the notification.  
@param aOldSource the old subject of the assertion  
@param aNewSource the new subject of the assertion  
@param aProperty the predicate of the assertion  
@param aTarget the object of the assertion  
  

### onBeginUpdateBatch(aDataSource) ###
  
This method is called when a datasource is about to  
send several notifications at once. The observer can  
use this as a cue to optimize its behavior. The observer  
can expect the datasource to call endUpdateBatch() when  
the group of notifications has completed.  
@param aDataSource the datasource that is going to  
  be issuing the notifications.  
  

### onEndUpdateBatch(aDataSource) ###
  
This method is called when a datasource has completed  
issuing a notification group.  
@param aDataSource the datasource that has finished  
  issuing a group of notifications  
  
