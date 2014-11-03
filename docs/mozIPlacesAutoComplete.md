---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/mozIPlacesAutoComplete.idl">Source file</a>
</div>

# mozIPlacesAutoComplete #
<code>  
This interface provides some constants used by the Places AutoComplete  
search provider as well as methods to track opened pages for AutoComplete  
purposes.  
  
</code>
## Methods ##

### registerOpenPage(aURI) ###
<code>  
Mark a page as being currently open.  
  
@note Pages will not be automatically unregistered when Private Browsing  
      mode is entered or exited.  Therefore, consumers MUST unregister or  
      register themselves.  
  
@param aURI  
       The URI to register as an open page.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The URI to register as an open page.  
</td>
</tr>

</table>

### unregisterOpenPage(aURI) ###
<code>  
Mark a page as no longer being open (either by closing the window or tab,  
or by navigating away from that page).  
  
@note Pages will not be automatically unregistered when Private Browsing  
      mode is entered or exited.  Therefore, consumers MUST unregister or  
      register themselves.  
  
@param aURI  
       The URI to unregister as an open page.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The URI to unregister as an open page.  
</td>
</tr>

</table>

## Constants ##

### MATCH_ANYWHERE ###
  
Match anywhere in each searchable term.  
  

### MATCH_BOUNDARY_ANYWHERE ###
  
Match first on word boundaries, and if we do not get enough results, then  
match anywhere in each searchable term.  
  

### MATCH_BOUNDARY ###
  
Match on word boundaries in each searchable term.  
  

### MATCH_BEGINNING ###
  
Match only the beginning of each search term.  
  

### MATCH_ANYWHERE_UNMODIFIED ###
  
Match anywhere in each searchable term without doing any transformation  
or stripping on the underlying data.  
  

### MATCH_BEGINNING_CASE_SENSITIVE ###
  
Match only the beginning of each search term using a case sensitive  
comparator.  
  

### BEHAVIOR_HISTORY ###
  
Search through history.  
  

### BEHAVIOR_BOOKMARK ###
  
Search though bookmarks.  
  

### BEHAVIOR_TAG ###
  
Search through tags.  
  

### BEHAVIOR_TITLE ###
  
Search the title of pages.  
  

### BEHAVIOR_URL ###
  
Search the URL of pages.  
  

### BEHAVIOR_TYPED ###
  
Search for typed pages.  
  

### BEHAVIOR_JAVASCRIPT ###
  
Search javascript: URLs.  
  

### BEHAVIOR_OPENPAGE ###
  
Search for pages that have been marked as being opened, such as a tab  
in a tabbrowser.  
  
