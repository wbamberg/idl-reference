---
layout: default
---

# fuelIAnnotations #

Interface representing a collection of annotations associated
with a bookmark or bookmark folder.


## names ##

Array of the annotation names associated with the owning item


## has ##

Determines if an annotation exists with the given name.
@param   aName
         The name of the annotation
@returns true if an annotation exists with the given name,
         false otherwise.


## get ##

Gets the value of an annotation with the given name.
@param   aName
         The name of the annotation
@returns A variant containing the value of the annotation. Supports
         string, boolean and number.


## set ##

Sets the value of an annotation with the given name.
@param   aName
         The name of the annotation
@param   aValue
         The new value of the annotation. Supports string, boolean
         and number
@param   aExpiration
         The expiration policy for the annotation.
         See nsIAnnotationService.


## remove ##

Removes the named annotation from the owner item.
@param   aName
         The name of annotation.

