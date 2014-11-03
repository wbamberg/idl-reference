---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/parser/xml/nsISAXXMLFilter.idl">Source file</a>
</div>

# nsISAXXMLFilter #
<pre>  
Interface for an XML filter.  
  
An XML filter is like an XML reader, except that it obtains its  
events from another XML reader rather than a primary source like an  
XML document or database.  Filters can modify a stream of events as  
they pass on to the final application.  
  
</pre>
## Attributes ##

### parent ###
<pre>  
The parent reader.  
  
Allows the application to query the parent reader (which may be  
another filter).  It is generally a bad idea to perform any  
operations on the parent reader directly: they should all pass  
through this filter.  
  
</pre>