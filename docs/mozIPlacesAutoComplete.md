---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/mozIPlacesAutoComplete.idl">Source file</a>
</div>

# mozIPlacesAutoComplete #
<pre>  
This interface provides some constants used by the Places AutoComplete  
search provider as well as methods to track opened pages for AutoComplete  
purposes.  
  
</pre>
## Methods ##

### registerOpenPage(aURI) ###
<pre>  
Mark a page as being currently open.  
  
@note Pages will not be automatically unregistered when Private Browsing  
      mode is entered or exited.  Therefore, consumers MUST unregister or  
      register themselves.  
  
@param aURI  
       The URI to register as an open page.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>       The URI to register as an open page.  
</td>
</tr>

</table>

### unregisterOpenPage(aURI) ###
<pre>  
Mark a page as no longer being open (either by closing the window or tab,  
or by navigating away from that page).  
  
@note Pages will not be automatically unregistered when Private Browsing  
      mode is entered or exited.  Therefore, consumers MUST unregister or  
      register themselves.  
  
@param aURI  
       The URI to unregister as an open page.  
  
</pre>
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
<pre>  
Match anywhere in each searchable term.  
  
</pre>
### MATCH_BOUNDARY_ANYWHERE ###
<pre>  
Match first on word boundaries, and if we do not get enough results, then  
match anywhere in each searchable term.  
  
</pre>
### MATCH_BOUNDARY ###
<pre>  
Match on word boundaries in each searchable term.  
  
</pre>
### MATCH_BEGINNING ###
<pre>  
Match only the beginning of each search term.  
  
</pre>
### MATCH_ANYWHERE_UNMODIFIED ###
<pre>  
Match anywhere in each searchable term without doing any transformation  
or stripping on the underlying data.  
  
</pre>
### MATCH_BEGINNING_CASE_SENSITIVE ###
<pre>  
Match only the beginning of each search term using a case sensitive  
comparator.  
  
</pre>
### BEHAVIOR_HISTORY ###
<pre>  
Search through history.  
  
</pre>
### BEHAVIOR_BOOKMARK ###
<pre>  
Search though bookmarks.  
  
</pre>
### BEHAVIOR_TAG ###
<pre>  
Search through tags.  
  
</pre>
### BEHAVIOR_TITLE ###
<pre>  
Search the title of pages.  
  
</pre>
### BEHAVIOR_URL ###
<pre>  
Search the URL of pages.  
  
</pre>
### BEHAVIOR_TYPED ###
<pre>  
Search for typed pages.  
  
</pre>
### BEHAVIOR_JAVASCRIPT ###
<pre>  
Search javascript: URLs.  
  
</pre>
### BEHAVIOR_OPENPAGE ###
<pre>  
Search for pages that have been marked as being opened, such as a tab  
in a tabbrowser.  
  
</pre>