---
layout: default
---

# nsIUrlListManager #

## Methods ##

### getGethashUrl(tableName) ###
  
Get the gethash url for this table  
  

### registerTable(tableName, updateUrl, gethashUrl) ###
  
Add a table to the list of tables we are managing. The name is a  
string of the format provider_name-semantic_type-table_type.  For  
@param tableName A string of the format  
       provider_name-semantic_type-table_type.  For example,  
       goog-white-enchash or goog-black-url.  
@param updateUrl The URL from which to fetch updates.  
@param gethashUrl The URL from which to fetch hash completions.  
  

#### Parameters ####

<table>

<tr>
<td>tableName</td>
<td>A string of the format  
       provider_name-semantic_type-table_type.  For example,  
       goog-white-enchash or goog-black-url.  
</td>
</tr>

<tr>
<td>tableName</td>
<td>A string of the format  
       provider_name-semantic_type-table_type.  For example,  
       goog-white-enchash or goog-black-url.  
</td>
</tr>

<tr>
<td>tableName</td>
<td>A string of the format  
       provider_name-semantic_type-table_type.  For example,  
       goog-white-enchash or goog-black-url.  
</td>
</tr>

</table>

### enableUpdate(tableName) ###
  
Turn on update checking for a table. I.e., during the next server  
check, download updates for this table.  
  

### disableUpdate(tableName) ###
  
Turn off update checking for a table.  
  

### maybeToggleUpdateChecking() ###
  
Toggle update checking, if necessary.  
  

### safeLookup(key, cb) ###
  
Lookup a key.  Should not raise exceptions.  Calls the callback  
function with a comma-separated list of tables to which the key  
belongs.  
  
