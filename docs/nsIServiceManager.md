---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/components/nsIServiceManager.idl">Source file</a>
</div>

# nsIServiceManager #
<pre>  
The nsIServiceManager manager interface provides a means to obtain  
global services in an application. The service manager depends on the   
repository to find and instantiate factories to obtain services.  
  
Users of the service manager must first obtain a pointer to the global  
service manager by calling NS_GetServiceManager. After that,   
they can request specific services by calling GetService. When they are  
finished they can NS_RELEASE() the service as usual.  
  
A user of a service may keep references to particular services indefinitely  
and only must call Release when it shuts down.  
  
</pre>
## Methods ##

### getService(aClass, aIID, result) ###
<pre>  
getServiceByContractID  
  
Returns the instance that implements aClass or aContractID and the  
interface aIID.  This may result in the instance being created.  
  
@param aClass or aContractID : aClass or aContractID of object   
                               instance requested  
@param aIID : IID of interface requested  
@param result : resulting service   
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aClass</td>
<td>or aContractID : aClass or aContractID of object   
                               instance requested  
</td>
</tr>

<tr>
<td>aIID</td>
<td>: IID of interface requested  
</td>
</tr>

<tr>
<td>result</td>
<td>: resulting service   
</td>
</tr>

</table>

### getServiceByContractID(aContractID, aIID, result) ###

### isServiceInstantiated(aClass, aIID) ###
<pre>  
isServiceInstantiated  
  
isServiceInstantiated will return a true if the service has already  
been created, or throw otherwise  
  
@param aClass or aContractID : aClass or aContractID of object   
                               instance requested  
@param aIID : IID of interface requested  
@throws NS_ERROR_SERVICE_NOT_AVAILABLE if the service hasn't been   
        instantiated  
@throws NS_NOINTERFACE if the IID given isn't supported by the object  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aClass</td>
<td>or aContractID : aClass or aContractID of object   
                               instance requested  
</td>
</tr>

<tr>
<td>aIID</td>
<td>: IID of interface requested  
@throws NS_ERROR_SERVICE_NOT_AVAILABLE if the service hasn't been   
        instantiated  
@throws NS_NOINTERFACE if the IID given isn't supported by the object  
</td>
</tr>

</table>

### isServiceInstantiatedByContractID(aContractID, aIID) ###
