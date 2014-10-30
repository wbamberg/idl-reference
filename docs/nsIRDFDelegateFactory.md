---
layout: default
---

# nsIRDFDelegateFactory #
  
This interface should be implemented by an XPCOM factory that  
is registered to handle "@mozilla.org/rdf/delegate-factory/[key]/[scheme];1"  
ContractIDs.  
  
The factory will be invoked to create delegate objects from  
nsIRDFResource::GetDelegate().  
  

## Methods ##

### CreateDelegate(aOuter, aKey, aIID, aResult) ###
  
Create a delegate for the specified RDF resource.  
  
The created delegate should forward AddRef() and Release()  
calls to the aOuter object.  
  
