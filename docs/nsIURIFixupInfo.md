---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsIURIFixup.idl">Source file</a>
</div>

# nsIURIFixupInfo #
<pre>  
Interface indicating what we found/corrected when fixing up a URI  
  
</pre>
## Attributes ##

### consumer ###
<pre>  
Consumer that asked for fixed up URI.  
  
</pre>
### preferredURI ###
<pre>  
Our best guess as to what URI the consumer will want. Might  
be null if we couldn't salvage anything (for instance, because  
the input was invalid as a URI and FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP  
was not passed)  
  
</pre>
### fixedURI ###
<pre>  
The fixed-up original input, *never* using a keyword search.  
(might be null if the original input was not recoverable as  
a URL, e.g. "foo bar"!)  
  
</pre>
### keywordProviderName ###
<pre>  
The name of the keyword search provider used to provide a keyword search;  
empty string if no keyword search was done.  
  
</pre>
### keywordAsSent ###
<pre>  
The keyword as used for the search (post trimming etc.)  
empty string if no keyword search was done.  
  
</pre>
### fixupChangedProtocol ###
<pre>  
Whether we changed the protocol instead of using one from the input as-is.  
  
</pre>
### fixupCreatedAlternateURI ###
<pre>  
Whether we created an alternative URI. We might have added a prefix and/or  
suffix, the contents of which are controlled by the  
browser.fixup.alternate.prefix and .suffix prefs, with the defaults being  
"www." and ".com", respectively.  
  
</pre>
### originalInput ###
<pre>  
The original input  
  
</pre>