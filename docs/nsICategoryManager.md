---
layout: default
---

# nsICategoryManager #

## getCategoryEntry ##

Get the value for the given category's entry.
@param aCategory The name of the category ("protocol")
@param aEntry The entry you're looking for ("http")
@return The value.


## addCategoryEntry ##

Add an entry to a category.
@param aCategory The name of the category ("protocol")
@param aEntry The entry to be added ("http")
@param aValue The value for the entry ("moz.httprulez.1")
@param aPersist Should this data persist between invocations?
@param aReplace Should we replace an existing entry?
@return Previous entry, if any


## deleteCategoryEntry ##

Delete an entry from the category.
@param aCategory The name of the category ("protocol")
@param aEntry The entry to be added ("http")
@param aPersist Delete persistent data from registry, if present?


## deleteCategory ##

Delete a category and all entries.
@param aCategory The category to be deleted.


## enumerateCategory ##

Enumerate the entries in a category.
@param aCategory The category to be enumerated.
@return a simple enumerator, each result QIs to
        nsISupportsCString.


## enumerateCategories ##

Enumerate all existing categories
@param aCategory The category to be enumerated.
@return a simple enumerator, each result QIs to
        nsISupportsCString.

