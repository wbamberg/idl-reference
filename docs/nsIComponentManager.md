---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/components/nsIComponentManager.idl">Source file</a>
</div>

# nsIComponentManager #

## Methods ##

### getClassObject(aClass, aIID, result) ###
<code>  
getClassObject  
  
Returns the factory object that can be used to create instances of  
CID aClass  
  
@param aClass The classid of the factory that is being requested  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aClass</td>
<td>The classid of the factory that is being requested  
</td>
</tr>

</table>

### getClassObjectByContractID(aContractID, aIID, result) ###
<code>  
getClassObjectByContractID  
  
Returns the factory object that can be used to create instances of  
CID aClass  
  
@param aClass The classid of the factory that is being requested  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aClass</td>
<td>The classid of the factory that is being requested  
</td>
</tr>

</table>

### createInstance(aClass, aDelegate, aIID, result) ###
<code>  
createInstance  
  
Create an instance of the CID aClass and return the interface aIID.  
  
@param aClass : ClassID of object instance requested  
@param aDelegate : Used for aggregation  
@param aIID : IID of interface requested  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aClass</td>
<td>: ClassID of object instance requested  
</td>
</tr>

<tr>
<td>aDelegate</td>
<td>: Used for aggregation  
</td>
</tr>

<tr>
<td>aIID</td>
<td>: IID of interface requested  
</td>
</tr>

</table>

### createInstanceByContractID(aContractID, aDelegate, aIID, result) ###
<code>  
createInstanceByContractID  
  
Create an instance of the CID that implements aContractID and return the  
interface aIID.   
  
@param aContractID : aContractID of object instance requested  
@param aDelegate : Used for aggregation  
@param aIID : IID of interface requested  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aContractID</td>
<td>: aContractID of object instance requested  
</td>
</tr>

<tr>
<td>aDelegate</td>
<td>: Used for aggregation  
</td>
</tr>

<tr>
<td>aIID</td>
<td>: IID of interface requested  
</td>
</tr>

</table>

### addBootstrappedManifestLocation(aLocation) ###
<code>  
addBootstrappedManifestLocation  
  
Adds a bootstrapped manifest location on runtime.  
  
@param aLocation : A directory where chrome.manifest resides,  
                   or an XPI with it on the root.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aLocation</td>
<td>: A directory where chrome.manifest resides,  
                   or an XPI with it on the root.  
</td>
</tr>

</table>

### removeBootstrappedManifestLocation(aLocation) ###
<code>  
removeBootstrappedManifestLocation  
  
Removes a bootstrapped manifest location on runtime.  
  
@param aLocation : A directory where chrome.manifest resides,  
                   or an XPI with it on the root.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aLocation</td>
<td>: A directory where chrome.manifest resides,  
                   or an XPI with it on the root.  
</td>
</tr>

</table>

### getManifestLocations() ###
<code>  
getManifestLocations  
  
Get an array of nsIURIs of all registered and builtin manifest locations.  
  
</code>