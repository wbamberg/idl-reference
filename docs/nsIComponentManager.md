---
layout: default
---

# nsIComponentManager #

## Methods ##

### getClassObject(aClass, aIID, result) ###
  
getClassObject  
  
Returns the factory object that can be used to create instances of  
CID aClass  
  
@param aClass The classid of the factory that is being requested  
  

#### Parameters ####

<table>

<tr>
<td>aClass</td>
<td>The classid of the factory that is being requested  
</td>
</tr>

</table>

### getClassObjectByContractID(aContractID, aIID, result) ###
  
getClassObjectByContractID  
  
Returns the factory object that can be used to create instances of  
CID aClass  
  
@param aClass The classid of the factory that is being requested  
  

#### Parameters ####

<table>

<tr>
<td>aClass</td>
<td>The classid of the factory that is being requested  
</td>
</tr>

</table>

### createInstance(aClass, aDelegate, aIID, result) ###
  
createInstance  
  
Create an instance of the CID aClass and return the interface aIID.  
  
@param aClass : ClassID of object instance requested  
@param aDelegate : Used for aggregation  
@param aIID : IID of interface requested  
  

#### Parameters ####

<table>

<tr>
<td>aClass</td>
<td>: ClassID of object instance requested  
</td>
</tr>

<tr>
<td>aClass</td>
<td>: ClassID of object instance requested  
</td>
</tr>

<tr>
<td>aClass</td>
<td>: ClassID of object instance requested  
</td>
</tr>

</table>

### createInstanceByContractID(aContractID, aDelegate, aIID, result) ###
  
createInstanceByContractID  
  
Create an instance of the CID that implements aContractID and return the  
interface aIID.   
  
@param aContractID : aContractID of object instance requested  
@param aDelegate : Used for aggregation  
@param aIID : IID of interface requested  
  

#### Parameters ####

<table>

<tr>
<td>aContractID</td>
<td>: aContractID of object instance requested  
</td>
</tr>

<tr>
<td>aContractID</td>
<td>: aContractID of object instance requested  
</td>
</tr>

<tr>
<td>aContractID</td>
<td>: aContractID of object instance requested  
</td>
</tr>

</table>

### addBootstrappedManifestLocation(aLocation) ###
  
addBootstrappedManifestLocation  
  
Adds a bootstrapped manifest location on runtime.  
  
@param aLocation : A directory where chrome.manifest resides,  
                   or an XPI with it on the root.  
  

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
  
removeBootstrappedManifestLocation  
  
Removes a bootstrapped manifest location on runtime.  
  
@param aLocation : A directory where chrome.manifest resides,  
                   or an XPI with it on the root.  
  

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
  
getManifestLocations  
  
Get an array of nsIURIs of all registered and builtin manifest locations.  
  
