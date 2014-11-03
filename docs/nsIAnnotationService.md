---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/nsIAnnotationService.idl">Source file</a>
</div>

# nsIAnnotationService #

## Methods ##

### setPageAnnotation(aURI, aName, aValue, aFlags, aExpiration) ###
<pre>  
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
  
</pre>
### setItemAnnotation(aItemId, aName, aValue, aFlags, aExpiration) ###

### setPageAnnotationString(aURI, aName, aValue, aFlags, aExpiration) ###
<pre>  
@throws NS_ERROR_ILLEGAL_VALUE if the page or the bookmark doesn't exist.  
  
</pre>
### setItemAnnotationString(aItemId, aName, aValue, aFlags, aExpiration) ###

### setPageAnnotationInt32(aURI, aName, aValue, aFlags, aExpiration) ###
<pre>  
Sets an annotation just like setAnnotationString, but takes an Int32 as  
input.  
  
@throws NS_ERROR_ILLEGAL_VALUE if the page or the bookmark doesn't exist.  
  
</pre>
### setItemAnnotationInt32(aItemId, aName, aValue, aFlags, aExpiration) ###

### setPageAnnotationInt64(aURI, aName, aValue, aFlags, aExpiration) ###
<pre>  
Sets an annotation just like setAnnotationString, but takes an Int64 as  
input.  
  
@throws NS_ERROR_ILLEGAL_VALUE if the page or the bookmark doesn't exist.  
  
</pre>
### setItemAnnotationInt64(aItemId, aName, aValue, aFlags, aExpiration) ###

### setPageAnnotationDouble(aURI, aName, aValue, aFlags, aExpiration) ###
<pre>  
Sets an annotation just like setAnnotationString, but takes a double as  
input.  
  
@throws NS_ERROR_ILLEGAL_VALUE if the page or the bookmark doesn't exist.  
  
</pre>
### setItemAnnotationDouble(aItemId, aName, aValue, aFlags, aExpiration) ###

### getPageAnnotation(aURI, aName) ###
<pre>  
Retrieves the value of a given annotation. Throws an error if the  
annotation does not exist. C++ consumers may use the type-specific  
methods.  
  
The type-specific methods throw if the given annotation is set in  
a different type.  
  
</pre>
### getItemAnnotation(aItemId, aName) ###

### getPageAnnotationString(aURI, aName) ###
<pre>  
@see getPageAnnotation  
  
</pre>
### getItemAnnotationString(aItemId, aName) ###

### getPageAnnotationInt32(aURI, aName) ###
<pre>  
@see getPageAnnotation  
  
</pre>
### getItemAnnotationInt32(aItemId, aName) ###

### getPageAnnotationInt64(aURI, aName) ###
<pre>  
@see getPageAnnotation  
  
</pre>
### getItemAnnotationInt64(aItemId, aName) ###

### getPageAnnotationDouble(aURI, aName) ###
<pre>  
@see getPageAnnotation  
  
</pre>
### getItemAnnotationDouble(aItemId, aName) ###

### getPageAnnotationInfo(aURI, aName, aFlags, aExpiration, aType) ###
<pre>  
Retrieves info about an existing annotation.  
  
aType will be one of TYPE_* constansts above  
  
example JS:  
  var flags = {}, exp = {}, type = {};  
  annotator.getAnnotationInfo(myURI, "foo", flags, exp, type);  
  // now you can use 'exp.value' and 'flags.value'  
  
</pre>
### getItemAnnotationInfo(aItemId, aName, aFlags, aExpiration, aType) ###

### getPageAnnotationType(aURI, aName) ###
<pre>  
Retrieves the type of an existing annotation  
Use getAnnotationInfo if you need this along with the mime-type etc.  
  
@param aURI  
       the uri on which the annotation is set  
@param aName  
       the annotation name  
@return one of the TYPE_* constants above  
@throws if the annotation is not set  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       the uri on which the annotation is set  
</td>
</tr>

<tr>
<td>aName</td>
<td>       the annotation name  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>one of the TYPE_* constants above  
@throws if the annotation is not set  
</td>
</tr>

</table>

### getItemAnnotationType(aItemId, aName) ###

### getPagesWithAnnotation(name, resultCount, results) ###
<pre>  
Returns a list of all URIs having a given annotation.  
  
</pre>
### getItemsWithAnnotation(name, resultCount, results) ###

### getAnnotationsWithName(name, count, results) ###
<pre>  
Returns a list of mozIAnnotation(s), having a given annotation name.  
  
@param name  
       The annotation to search for.  
@return list of mozIAnnotation objects.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       The annotation to search for.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>list of mozIAnnotation objects.  
</td>
</tr>

</table>

### getPageAnnotationNames(aURI, count, result) ###
<pre>  
Get the names of all annotations for this URI.  
  
example JS:  
  var annotations = annotator.getPageAnnotations(myURI, {});  
  
</pre>
### getItemAnnotationNames(aItemId, count, result) ###

### pageHasAnnotation(aURI, aName) ###
<pre>  
Test for annotation existence.  
  
</pre>
### itemHasAnnotation(aItemId, aName) ###

### removePageAnnotation(aURI, aName) ###
<pre>  
Removes a specific annotation. Succeeds even if the annotation is  
not found.  
  
</pre>
### removeItemAnnotation(aItemId, aName) ###

### removePageAnnotations(aURI) ###
<pre>  
Removes all annotations for the given page/item.  
We may want some other similar functions to get annotations with given  
flags (once we have flags defined).  
  
</pre>
### removeItemAnnotations(aItemId) ###

### copyPageAnnotations(aSourceURI, aDestURI, aOverwriteDest) ###
<pre>  
Copies all annotations from the source to the destination URI/item. If  
the destination already has an annotation with the same name as one on  
the source, it will be overwritten if aOverwriteDest is set. Otherwise,  
the original annotation will be preferred.  
  
All the source annotations will stay as-is. If you don't want them  
any more, use removePageAnnotations on that URI.  
  
</pre>
### copyItemAnnotations(aSourceItemId, aDestItemId, aOverwriteDest) ###

### addObserver(aObserver) ###
<pre>  
Adds an annotation observer. The annotation service will keep an owning  
reference to the observer object.  
  
</pre>
### removeObserver(aObserver) ###
<pre>  
Removes an annotaton observer previously registered by addObserver.  
  
</pre>
## Constants ##

### EXPIRE_SESSION ###
<pre>  
Valid values for aExpiration, which sets the expiration policy for your  
annotation. The times for the days, weeks and months policies are  
measured since the last visit date of the page in question. These   
will not expire so long as the user keeps visiting the page from time  
to time.  
  
</pre>
### EXPIRE_WEEKS ###

### EXPIRE_MONTHS ###

### EXPIRE_NEVER ###

### EXPIRE_WITH_HISTORY ###

### EXPIRE_DAYS ###

### TYPE_INT32 ###

### TYPE_DOUBLE ###

### TYPE_STRING ###

### TYPE_INT64 ###
