---
layout: default
---

# nsIModule #
  
The nsIModule interface.  
  

## Methods ##

### getClassObject(aCompMgr, aClass, aIID, aResult) ###
   
Object Instance Creation  
  
Obtains a Class Object from a nsIModule for a given CID and IID pair.    
This class object can either be query to a nsIFactory or a may be   
query to a nsIClassInfo.  
  
@param aCompMgr  : The global component manager  
@param aClass    : ClassID of object instance requested  
@param aIID      : IID of interface requested  
  
  

#### Parameters ####

<table>

<tr>
<td>aCompMgr</td>
<td>: The global component manager  
</td>
</tr>

<tr>
<td>aClass</td>
<td>: ClassID of object instance requested  
</td>
</tr>

<tr>
<td>aIID</td>
<td>: IID of interface requested  
</td>
</tr>

</table>

### registerSelf(aCompMgr, aLocation, aLoaderStr, aType) ###
  
One time registration callback  
  
When the nsIModule is discovered, this method will be  
called so that any setup registration can be preformed.  
  
@param aCompMgr  : The global component manager  
@param aLocation : The location of the nsIModule on disk  
@param aLoaderStr: Opaque loader specific string  
@param aType     : Loader Type being used to load this module   
  

#### Parameters ####

<table>

<tr>
<td>aCompMgr</td>
<td>: The global component manager  
</td>
</tr>

<tr>
<td>aLocation</td>
<td>: The location of the nsIModule on disk  
</td>
</tr>

<tr>
<td>aLoaderStr:</td>
<td>Opaque loader specific string  
</td>
</tr>

<tr>
<td>aType</td>
<td>: Loader Type being used to load this module   
</td>
</tr>

</table>

### unregisterSelf(aCompMgr, aLocation, aLoaderStr) ###
  
One time unregistration callback  
  
When the nsIModule is being unregistered, this method will be  
called so that any unregistration can be preformed  
  
@param aCompMgr   : The global component manager  
@param aLocation  : The location of the nsIModule on disk  
@param aLoaderStr : Opaque loader specific string  
  
  

#### Parameters ####

<table>

<tr>
<td>aCompMgr</td>
<td>: The global component manager  
</td>
</tr>

<tr>
<td>aLocation</td>
<td>: The location of the nsIModule on disk  
</td>
</tr>

<tr>
<td>aLoaderStr</td>
<td>: Opaque loader specific string  
</td>
</tr>

</table>

### canUnload(aCompMgr) ###
   
Module load management  
  
@param aCompMgr  : The global component manager  
  
@return indicates to the caller if the module can be unloaded.  
		Returning PR_TRUE isn't a guarantee that the module will be  
	unloaded. It constitues only willingness of the module to be  
	unloaded.  It is very important to ensure that no outstanding   
      references to the module's code/data exist before returning   
      PR_TRUE.   
	Returning PR_FALSE guaratees that the module won't be unloaded.  
  

#### Parameters ####

<table>

<tr>
<td>aCompMgr</td>
<td>: The global component manager  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>indicates to the caller if the module can be unloaded.  
		Returning PR_TRUE isn't a guarantee that the module will be  
	unloaded. It constitues only willingness of the module to be  
	unloaded.  It is very important to ensure that no outstanding   
      references to the module's code/data exist before returning   
      PR_TRUE.   
	Returning PR_FALSE guaratees that the module won't be unloaded.  
</td>
</tr>

</table>
