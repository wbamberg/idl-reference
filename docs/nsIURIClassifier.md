---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIURIClassifier.idl">Source file</a>
</div>

# nsIURIClassifier #
<code>  
The URI classifier service checks a URI against lists of phishing  
and malware sites.  
  
</code>
## Methods ##

### classify(aPrincipal, aTrackingProtectionEnabled, aCallback) ###
<code>  
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
  
</code>
#### Parameters ####

<table>

<tr>
<td>aPrincipal</td>
<td>       The principal that should be checked by the URI classifier.  
</td>
</tr>

<tr>
<td>aTrackingProtectionEnabled</td>
<td>       Whether or not to classify the given URI against tracking  
       protection lists  
</td>
</tr>

<tr>
<td>aCallback</td>
<td>       The URI classifier will call this callback when the URI has been  
       classified.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td><code>false</code> if classification is not necessary.  The  
        callback will not be called.  
        <code>true</code> if classification will be performed.  The  
        callback will be called.  
</td>
</tr>

</table>
