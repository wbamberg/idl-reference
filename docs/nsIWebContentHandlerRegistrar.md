---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/sidebar/nsIWebContentHandlerRegistrar.idl">Source file</a>
</div>

# nsIWebContentHandlerRegistrar #
<code>  
nsIWebContentHandlerRegistrar  
  
Applications wishing to use web content handlers need to implement this  
interface. Typically they will prompt the user to confirm adding an entry  
to the local list.   
  
The component must have the contract id defined below so that nsNavigator  
can invoke it.   
  
</code>
## Methods ##

### registerContentHandler(mimeType, uri, title, contentWindow) ###
<code>  
See documentation in Navigator.webidl  
The additional contentWindow param for both methods represents the dom  
content window from which the method has been called.  
  
</code>
### registerProtocolHandler(protocol, uri, title, contentWindow) ###
