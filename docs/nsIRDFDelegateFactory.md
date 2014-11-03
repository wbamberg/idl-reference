---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/rdf/base/nsIRDFDelegateFactory.idl">Source file</a>
</div>

# nsIRDFDelegateFactory #
<pre>  
This interface should be implemented by an XPCOM factory that  
is registered to handle "@mozilla.org/rdf/delegate-factory/[key]/[scheme];1"  
ContractIDs.  
  
The factory will be invoked to create delegate objects from  
nsIRDFResource::GetDelegate().  
  
</pre>
## Methods ##

### CreateDelegate(aOuter, aKey, aIID, aResult) ###
<pre>  
Create a delegate for the specified RDF resource.  
  
The created delegate should forward AddRef() and Release()  
calls to the aOuter object.  
  
</pre>