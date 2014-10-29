---
layout: default
---

# nsIDOMXULContainerElement #

## Methods ##

### appendItem ###

Creates an item for the given label and value and appends it to the
container.

@param aLabel - the label for the new item
@param aValue - the value of the new item


### insertItemAt ###

Creates an item for the given label and value and inserts it into the
container at the specified position.

@param aIndex - the index where the new item will be inserted
@param aLabel - the label for the new item
@param aValue - the value of the new item


### removeItemAt ###

Removes an item from the container.

@param aIndex - index of the item to remove


### getIndexOfItem ###

Returns the index of an item or -1 if the item is not in the container.

@param aItem - the item to determine the index of


### getItemAtIndex ###

Returns the item at a given index or null if the item is not is the
container.

@param aIndex - the index of the item to return


## Attributes ##

### itemCount ###

Returns a count of items in the container.

