---
layout: default
---

# nsICategoryManager #

## Methods ##

### getCategoryEntry(aCategory, aEntry) ###
  
Get the value for the given category's entry.  
@param aCategory The name of the category ("protocol")  
@param aEntry The entry you're looking for ("http")  
@return The value.  
  

### addCategoryEntry(aCategory, aEntry, aValue, aPersist, aReplace) ###
  
Add an entry to a category.  
@param aCategory The name of the category ("protocol")  
@param aEntry The entry to be added ("http")  
@param aValue The value for the entry ("moz.httprulez.1")  
@param aPersist Should this data persist between invocations?  
@param aReplace Should we replace an existing entry?  
@return Previous entry, if any  
  

### deleteCategoryEntry(aCategory, aEntry, aPersist) ###
  
Delete an entry from the category.  
@param aCategory The name of the category ("protocol")  
@param aEntry The entry to be added ("http")  
@param aPersist Delete persistent data from registry, if present?  
  

### deleteCategory(aCategory) ###
  
Delete a category and all entries.  
@param aCategory The category to be deleted.  
  

### enumerateCategory(aCategory) ###
  
Enumerate the entries in a category.  
@param aCategory The category to be enumerated.  
@return a simple enumerator, each result QIs to  
        nsISupportsCString.  
  

### enumerateCategories() ###
  
Enumerate all existing categories  
@param aCategory The category to be enumerated.  
@return a simple enumerator, each result QIs to  
        nsISupportsCString.  
  
