---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/nsITaggingService.idl">Source file</a>
</div>

# nsITaggingService #

## Methods ##

### tagURI(aURI, aTags) ###
<pre>  
Tags a URL with the given set of tags. Current tags set for the URL  
persist. Tags in aTags which are already set for the given URL are  
ignored.  
  
@param aURI  
       the URL to tag.  
@param aTags  
       Array of tags to set for the given URL.  Each element within the  
       array can be either a tag name (non-empty string) or a concrete  
       itemId of a tag container.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       the URL to tag.  
</td>
</tr>

<tr>
<td>aTags</td>
<td>       Array of tags to set for the given URL.  Each element within the  
       array can be either a tag name (non-empty string) or a concrete  
       itemId of a tag container.  
</td>
</tr>

</table>

### untagURI(aURI, aTags) ###
<pre>  
Removes tags from a URL. Tags from aTags which are not set for the  
given URL are ignored.  
  
@param aURI  
       the URL to un-tag.  
@param aTags  
       Array of tags to unset.  Pass null to remove all tags from the given  
       url.  Each element within the array can be either a tag name  
       (non-empty string) or a concrete itemId of a tag container.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       the URL to un-tag.  
</td>
</tr>

<tr>
<td>aTags</td>
<td>       Array of tags to unset.  Pass null to remove all tags from the given  
       url.  Each element within the array can be either a tag name  
       (non-empty string) or a concrete itemId of a tag container.  
</td>
</tr>

</table>

### getURIsForTag(aTag) ###
<pre>  
Retrieves all URLs tagged with the given tag.  
  
@param aTag  
       tag name  
@returns Array of uris tagged with aTag.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aTag</td>
<td>       tag name  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Array of uris tagged with aTag.  
</td>
</tr>

</table>

### getTagsForURI(aURI, length, aTags) ###
<pre>  
Retrieves all tags set for the given URL.  
  
@param aURI  
       a URL.  
@returns array of tags (sorted by name).  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       a URL.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>array of tags (sorted by name).  
</td>
</tr>

</table>

## Attributes ##

### allTags ###
<pre>  
Retrieves all tags used to tag URIs in the data-base (sorted by name).  
  
</pre>
### hasTags ###
<pre>  
Whether any tags exist.  
  
@note This is faster than allTags.length, since doesn't need to sort tags.  
  
</pre>
## Constants ##

### MAX_TAG_LENGTH ###
<pre>  
Defines the maximal length of a tag. Related to the bug 407821   
(https://bugzilla.mozilla.org/show_bug.cgi?id=407821)   
  
</pre>