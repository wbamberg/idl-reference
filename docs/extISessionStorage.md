---
layout: default
---

# extISessionStorage #

Interface representing a simple storage system


## Methods ##

### has ###

Determines if a storage item exists with the given name.
@param   aName
         The name of an item
@returns true if an item exists with the given name,
         false otherwise.


### set ###

Sets the value of a storage item with the given name.
@param   aName
         The name of an item
@param   aValue
         The value to assign to the item


### get ###

Gets the value of a storage item with the given name. Returns a
default value if the item does not exist.
@param   aName
         The name of an item
@param   aDefaultValue
         The value to return if no item exists with the given name
@returns value of the item or the given default value if no item
         exists with the given name.


## Attributes ##

### events ###

The events object for the storage
supports: "change"

