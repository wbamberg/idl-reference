---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsIURIFixup.idl">Source file</a>
</div>

# nsIURIFixup #
  
Interface implemented by objects capable of fixing up strings into URIs  
  

## Methods ##

### createExposableURI(aURI) ###
  
Converts an internal URI (e.g. a wyciwyg URI) into one which we can  
expose to the user, for example on the URL bar.  
  
  

#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>The URI to be converted  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>nsIURI     The converted, exposable URI  
@throws NS_ERROR_MALFORMED_URI when the exposable portion of aURI is malformed  
@throws NS_ERROR_UNKNOWN_PROTOCOL when we can't get a protocol handler service  
        for the URI scheme.  
</td>
</tr>

</table>

### createFixupURI(aURIText, aFixupFlags, aPostData) ###
  
Converts the specified string into a URI, first attempting  
to correct any errors in the syntax or other vagaries. Returns  
a wellformed URI or nullptr if it can't.  
  
  

#### Parameters ####

<table>

<tr>
<td>aURIText</td>
<td>Candidate URI.  
</td>
</tr>

<tr>
<td>aFixupFlags</td>
<td>Flags that govern ways the URI may be fixed up.  
</td>
</tr>

<tr>
<td>aPostData</td>
<td>The POST data to submit with the returned  
                   URI (see nsISearchSubmission).  
</td>
</tr>

</table>

### getFixupURIInfo(aURIText, aFixupFlags, aPostData) ###
  
Same as createFixupURI, but returns information about what it corrected  
(e.g. whether we could rescue the URI or "just" generated a keyword  
search URI instead).  
  
  

#### Parameters ####

<table>

<tr>
<td>aURIText</td>
<td>Candidate URI.  
</td>
</tr>

<tr>
<td>aFixupFlags</td>
<td>Flags that govern ways the URI may be fixed up.  
</td>
</tr>

<tr>
<td>aPostData</td>
<td>The POST data to submit with the returned  
                   URI (see nsISearchSubmission).  
</td>
</tr>

</table>

### keywordToURI(aKeyword, aPostData) ###
  
Converts the specified keyword string into a URI.  Note that it's the  
caller's responsibility to check whether keywords are enabled and  
whether aKeyword is a sensible keyword.  
  
  
@throws NS_ERROR_FAILURE if the resulting URI requires submission of POST  
        data and aPostData is null.  
  

#### Parameters ####

<table>

<tr>
<td>aKeyword</td>
<td>The keyword string to convert into a URI  
</td>
</tr>

<tr>
<td>aPostData</td>
<td>The POST data to submit to the returned URI  
                 (see nsISearchSubmission).  
</td>
</tr>

</table>

## Constants ##

### FIXUP_FLAG_NONE ###
 No fixup flags. */  

### FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP ###
  
Allow the fixup to use a keyword lookup service to complete the URI.  
The fixup object implementer should honour this flag and only perform  
any lengthy keyword (or search) operation if it is set.  
  

### FIXUP_FLAGS_MAKE_ALTERNATE_URI ###
  
Tell the fixup to make an alternate URI from the input URI, for example  
to turn foo into www.foo.com.  
  

### FIXUP_FLAG_REQUIRE_WHITELISTED_HOST ###
  
For an input that may be just a domain with only 1 level (eg, "mozilla"),  
require that the host be whitelisted.  
  
Overridden by FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP.  
  

### FIXUP_FLAG_FIX_SCHEME_TYPOS ###
