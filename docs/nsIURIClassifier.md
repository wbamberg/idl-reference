---
layout: default
---

# nsIURIClassifier #
  
The URI classifier service checks a URI against lists of phishing  
and malware sites.  
  

## Methods ##

### classify(aPrincipal, aTrackingProtectionEnabled, aCallback) ###
  
Classify a Principal using its URI.  
  
@param aPrincipal  
       The principal that should be checked by the URI classifier.  
@param aTrackingProtectionEnabled  
       Whether or not to classify the given URI against tracking  
       protection lists  
  
@param aCallback  
       The URI classifier will call this callback when the URI has been  
       classified.  
  
@return <code>false</code> if classification is not necessary.  The  
        callback will not be called.  
        <code>true</code> if classification will be performed.  The  
        callback will be called.  
  

#### Parameters ####

<table>

<tr>
<td>aPrincipal</td>
<td>       The principal that should be checked by the URI classifier.  
</td>
</tr>

<tr>
<td>aPrincipal</td>
<td>       The principal that should be checked by the URI classifier.  
</td>
</tr>

<tr>
<td>aPrincipal</td>
<td>       The principal that should be checked by the URI classifier.  
</td>
</tr>

</table>
