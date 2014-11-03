---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/base/nsIDocumentLoaderFactory.idl">Source file</a>
</div>

# nsIDocumentLoaderFactory #
<pre>  
To get a component that implements nsIDocumentLoaderFactory  
for a given mimetype, use nsICategoryManager to find an entry  
with the mimetype as its name in the category "Gecko-Content-Viewers".  
The value of the entry is the contractid of the component.  
The component is a service, so use GetService, not CreateInstance to get it.  
  
</pre>
## Methods ##

### createInstance(aCommand, aChannel, aLoadGroup, aContentType, aContainer, aExtraInfo, aDocListenerResult) ###

### createInstanceForDocument(aContainer, aDocument, aCommand) ###

### createBlankDocument(aLoadGroup, aPrincipal) ###
<pre>  
Create a blank document using the given loadgroup and given  
principal.  aPrincipal is allowed to be null, in which case the  
new document will get the about:blank codebase principal.  
  
</pre>