---
layout: default
---

# nsIAnnotationService #

## Methods ##

### setPageAnnotation ###

Sets an annotation, overwriting any previous annotation with the same
URL/name. IT IS YOUR JOB TO NAMESPACE YOUR ANNOTATION NAMES.
Use the form "namespace/value", so your name would be like
"bills_extension/page_state" or "history/thumbnail".

Do not use characters that are not valid in URLs such as spaces, ":",
commas, or most other symbols. You should stick to ASCII letters and
numbers plus "_", "-", and "/".

aExpiration is one of EXPIRE_* above. aFlags should be 0 for now, some
flags will be defined in the future.

NOTE: ALL PAGE ANNOTATIONS WILL GET DELETED WHEN THE PAGE IS REMOVED FROM
HISTORY IF THE PAGE IS NOT BOOKMARKED. This means that if you create an
annotation on an unvisited URI, it will get deleted when the browser
shuts down. Otherwise, URIs can exist in history as annotations but the
user has no way of knowing it, potentially violating their privacy
expectations about actions such as "Clear history".
If there is an important annotation that the user or extension wants to
keep, you should add a bookmark for the page and use an EXPIRE_NEVER
annotation.  This will ensure the annotation exists until the item is
removed by the user.
See EXPIRE_* constants above for further information.

The annotation "favicon" is special. Favicons are stored in the favicon
service, but are special cased in the protocol handler so they look like
annotations. Do not set favicons using this service, it will not work.

Only C++ consumers may use the type-specific methods.

@throws NS_ERROR_ILLEGAL_VALUE if the page or the bookmark doesn't exist.


### setItemAnnotation ###

### setPageAnnotationString ###

@throws NS_ERROR_ILLEGAL_VALUE if the page or the bookmark doesn't exist.


### setItemAnnotationString ###

### setPageAnnotationInt32 ###

Sets an annotation just like setAnnotationString, but takes an Int32 as
input.

@throws NS_ERROR_ILLEGAL_VALUE if the page or the bookmark doesn't exist.


### setItemAnnotationInt32 ###

### setPageAnnotationInt64 ###

Sets an annotation just like setAnnotationString, but takes an Int64 as
input.

@throws NS_ERROR_ILLEGAL_VALUE if the page or the bookmark doesn't exist.


### setItemAnnotationInt64 ###

### setPageAnnotationDouble ###

Sets an annotation just like setAnnotationString, but takes a double as
input.

@throws NS_ERROR_ILLEGAL_VALUE if the page or the bookmark doesn't exist.


### setItemAnnotationDouble ###

### getPageAnnotation ###

Retrieves the value of a given annotation. Throws an error if the
annotation does not exist. C++ consumers may use the type-specific
methods.

The type-specific methods throw if the given annotation is set in
a different type.


### getItemAnnotation ###

### getPageAnnotationString ###

@see getPageAnnotation


### getItemAnnotationString ###

### getPageAnnotationInt32 ###

@see getPageAnnotation


### getItemAnnotationInt32 ###

### getPageAnnotationInt64 ###

@see getPageAnnotation


### getItemAnnotationInt64 ###

### getPageAnnotationDouble ###

@see getPageAnnotation


### getItemAnnotationDouble ###

### getPageAnnotationInfo ###

Retrieves info about an existing annotation.

aType will be one of TYPE_* constansts above

example JS:
  var flags = {}, exp = {}, type = {};
  annotator.getAnnotationInfo(myURI, "foo", flags, exp, type);
  // now you can use 'exp.value' and 'flags.value'


### getItemAnnotationInfo ###

### getPageAnnotationType ###

Retrieves the type of an existing annotation
Use getAnnotationInfo if you need this along with the mime-type etc.

@param aURI
       the uri on which the annotation is set
@param aName
       the annotation name
@return one of the TYPE_* constants above
@throws if the annotation is not set


### getItemAnnotationType ###

### getPagesWithAnnotation ###

Returns a list of all URIs having a given annotation.


### getItemsWithAnnotation ###

### getAnnotationsWithName ###

Returns a list of mozIAnnotation(s), having a given annotation name.

@param name
       The annotation to search for.
@return list of mozIAnnotation objects.


### getPageAnnotationNames ###

Get the names of all annotations for this URI.

example JS:
  var annotations = annotator.getPageAnnotations(myURI, {});


### getItemAnnotationNames ###

### pageHasAnnotation ###

Test for annotation existence.


### itemHasAnnotation ###

### removePageAnnotation ###

Removes a specific annotation. Succeeds even if the annotation is
not found.


### removeItemAnnotation ###

### removePageAnnotations ###

Removes all annotations for the given page/item.
We may want some other similar functions to get annotations with given
flags (once we have flags defined).


### removeItemAnnotations ###

### copyPageAnnotations ###

Copies all annotations from the source to the destination URI/item. If
the destination already has an annotation with the same name as one on
the source, it will be overwritten if aOverwriteDest is set. Otherwise,
the original annotation will be preferred.

All the source annotations will stay as-is. If you don't want them
any more, use removePageAnnotations on that URI.


### copyItemAnnotations ###

### addObserver ###

Adds an annotation observer. The annotation service will keep an owning
reference to the observer object.


### removeObserver ###

Removes an annotaton observer previously registered by addObserver.


## Constants ##

### EXPIRE_SESSION ###

Valid values for aExpiration, which sets the expiration policy for your
annotation. The times for the days, weeks and months policies are
measured since the last visit date of the page in question. These 
will not expire so long as the user keeps visiting the page from time
to time.


### EXPIRE_WEEKS ###

### EXPIRE_MONTHS ###

### EXPIRE_NEVER ###

### EXPIRE_WITH_HISTORY ###

### EXPIRE_DAYS ###

### TYPE_INT32 ###

### TYPE_DOUBLE ###

### TYPE_STRING ###

### TYPE_INT64 ###
