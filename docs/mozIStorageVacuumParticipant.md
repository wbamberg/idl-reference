---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/storage/public/mozIStorageVacuumParticipant.idl">Source file</a>
</div>

# mozIStorageVacuumParticipant #
  
This interface contains the information that the Storage service needs to  
vacuum a database.  This interface is created as a service through the  
category manager with the category "vacuum-participant".  
Please see https://developer.mozilla.org/en/mozIStorageVacuumParticipant for  
more information.  
  

## Methods ##

### onBeginVacuum() ###
  
Notifies when a vacuum operation begins.  Listeners should avoid using the  
database till onEndVacuum is received.  
  
  
@note When a vacuum operation starts or ends it will also dispatch a global  
      "heavy-io-task" notification through the observer service with the  
      data argument being either "vacuum-begin" or "vacuum-end".  
  

#### Returns ####

<table>

<tr>
<td>true to proceed with the vacuum, false if the participant wants to  
        opt-out for now, it will be retried later.  Useful when participant  
        is running some other heavy operation that can't be interrupted.  
</td>
</tr>

</table>

### onEndVacuum(aSucceeded) ###
  
Notifies when a vacuum operation ends.  
  
  

#### Parameters ####

<table>

<tr>
<td>aSucceeded</td>
<td>       reports if the vacuum succeeded or failed.  
</td>
</tr>

</table>

## Attributes ##

### expectedDatabasePageSize ###
  
The expected page size in bytes for the database.  The vacuum manager will  
try to correct the page size during idle based on this value.  
  
@note If the database is using the WAL journal mode, the page size won't  
       be changed to the requested value.  See bug 634374.  
@note Valid page size values are powers of 2 between 512 and 65536.  
      The suggested value is mozIStorageConnection::defaultPageSize.  
  

### databaseConnection ###
  
Connection to the database file to be vacuumed.  
  
