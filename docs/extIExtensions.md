---
layout: default
---

# extIExtensions #
  
Interface representing a list of all installed extensions  
  

## Methods ##

### has(aId) ###
  
Determines if an extension exists with the given id.  
@param   aId  
         The id of an extension  
@returns true if an extension exists with the given id,  
         false otherwise.  
  

### get(aId) ###
  
Gets a extIExtension object for an extension.  
@param   aId  
         The id of an extension  
@returns An extension object or null if no extension exists  
         with the given id.  
  

## Attributes ##

### all ###
  
Array of extIExtension listing all extensions in the application.  
  
