---
layout: default
---

# nsIXULStore #
  
The XUL store is used to store information related to a XUL document/application.  
Typically it is used to store the persisted state for the document, such as  
window location, toolbars that are open and nodes that are open and closed in a tree.  
  
The data is serialized to [profile directory]/xulstore.json  
  

## Methods ##

### setValue ###
  
Sets a value in the store.  
  
@param doc - document URI  
@param id - identifier of the node  
@param attr - attribute to store  
@param value - value of the attribute  
  

### hasValue ###
  
Returns true if the store contains a value for attr.  
  
@param doc - URI of the document  
@param id - identifier of the node  
@param attr - attribute  
  

### getValue ###
  
Retrieves a value in the store, or an empty string if it does not exist.  
  
@param doc - document URI  
@param id - identifier of the node  
@param attr - attribute to retrieve  
  
@returns the value of the attribute  
  

### removeValue ###
  
Removes a value in the store.  
  
@param doc - document URI  
@param id - identifier of the node  
@param attr - attribute to remove  
  

### getIDsEnumerator ###
  
Iterates over all of the ids associated with a given document uri that  
have stored data.  
  
@param doc - document URI  
  

### getAttributeEnumerator ###
  
Iterates over all of the attributes associated with a given document uri  
and id that have stored data.  
  
@param doc - document URI  
@param id - identifier of the node  
  
