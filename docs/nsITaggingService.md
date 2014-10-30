---
layout: default
---

# nsITaggingService #

## Methods ##

### tagURI(aURI, aTags) ###
  
Tags a URL with the given set of tags. Current tags set for the URL  
persist. Tags in aTags which are already set for the given URL are  
ignored.  
  
@param aURI  
       the URL to tag.  
@param aTags  
       Array of tags to set for the given URL.  Each element within the  
       array can be either a tag name (non-empty string) or a concrete  
       itemId of a tag container.  
  

### untagURI(aURI, aTags) ###
  
Removes tags from a URL. Tags from aTags which are not set for the  
given URL are ignored.  
  
@param aURI  
       the URL to un-tag.  
@param aTags  
       Array of tags to unset.  Pass null to remove all tags from the given  
       url.  Each element within the array can be either a tag name  
       (non-empty string) or a concrete itemId of a tag container.  
  

### getURIsForTag(aTag) ###
  
Retrieves all URLs tagged with the given tag.  
  
@param aTag  
       tag name  
@returns Array of uris tagged with aTag.  
  

### getTagsForURI(aURI, length, aTags) ###
  
Retrieves all tags set for the given URL.  
  
@param aURI  
       a URL.  
@returns array of tags (sorted by name).  
  

## Attributes ##

### allTags ###
  
Retrieves all tags used to tag URIs in the data-base (sorted by name).  
  

### hasTags ###
  
Whether any tags exist.  
  
@note This is faster than allTags.length, since doesn't need to sort tags.  
  

## Constants ##

### MAX_TAG_LENGTH ###
  
Defines the maximal length of a tag. Related to the bug 407821   
(https://bugzilla.mozilla.org/show_bug.cgi?id=407821)   
  
