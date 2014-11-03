---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/components/nsIComponentRegistrar.idl">Source file</a>
</div>

# nsIComponentRegistrar #

## Methods ##

### autoRegister(aSpec) ###
<code>  
autoRegister  
  
Register a .manifest file, or an entire directory containing  
these files. Registration lasts for this run only, and is not cached.  
  
@note Formerly this method would register component files directly. This  
      is no longer supported.  
  
</code>
### autoUnregister(aSpec) ###
<code>  
autoUnregister  
@status OBSOLETE: This method is no longer implemented, but preserved  
                  in this interface for binary compatibility with  
                  Mozilla 1.9.2.  
  
</code>
### registerFactory(aClass, aClassName, aContractID, aFactory) ###
<code>  
registerFactory  
  
Register a factory with a given ContractID, CID and Class Name.  
  
@param aClass      : CID of object  
@param aClassName  : Class Name of CID (unused)  
@param aContractID : ContractID associated with CID aClass. May be null  
                     if no contract ID is needed.  
@param aFactory    : Factory that will be registered for CID aClass.  
                     If aFactory is null, the contract will be associated  
                     with a previously registered CID.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aClass</td>
<td>: CID of object  
</td>
</tr>

<tr>
<td>aClassName</td>
<td>: Class Name of CID (unused)  
</td>
</tr>

<tr>
<td>aContractID</td>
<td>: ContractID associated with CID aClass. May be null  
                     if no contract ID is needed.  
</td>
</tr>

<tr>
<td>aFactory</td>
<td>: Factory that will be registered for CID aClass.  
                     If aFactory is null, the contract will be associated  
                     with a previously registered CID.  
</td>
</tr>

</table>

### unregisterFactory(aClass, aFactory) ###
<code>  
unregisterFactory  
  
Unregister a factory associated with CID aClass.  
  
@param aClass   : CID being unregistered  
@param aFactory : Factory previously registered to create instances of  
                  CID aClass.  
  
@throws NS_ERROR* Method failure.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aClass</td>
<td>: CID being unregistered  
</td>
</tr>

<tr>
<td>aFactory</td>
<td>: Factory previously registered to create instances of  
                  CID aClass.  
</td>
</tr>

</table>

### registerFactoryLocation(aClass, aClassName, aContractID, aFile, aLoaderStr, aType) ###
<code>  
registerFactoryLocation  
@status OBSOLETE: This method is no longer implemented, but preserved  
                  in this interface for binary compatibility with  
                  Mozilla 1.9.2.  
  
</code>
### unregisterFactoryLocation(aClass, aFile) ###
<code>  
unregisterFactoryLocation  
@status OBSOLETE: This method is no longer implemented, but preserved  
                  in this interface for binary compatibility with  
                  Mozilla 1.9.2.  
  
</code>
### isCIDRegistered(aClass) ###
<code>  
isCIDRegistered  
  
Returns true if a factory is registered for the CID.  
  
@param aClass : CID queried for registeration  
@return       : true if a factory is registered for CID   
                false otherwise.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aClass</td>
<td>: CID queried for registeration  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>: true if a factory is registered for CID   
                false otherwise.  
</td>
</tr>

</table>

### isContractIDRegistered(aContractID) ###
<code>  
isContractIDRegistered  
  
Returns true if a factory is registered for the contract id.  
  
@param aClass : contract id queried for registeration  
@return       : true if a factory is registered for contract id   
                false otherwise.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aClass</td>
<td>: contract id queried for registeration  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>: true if a factory is registered for contract id   
                false otherwise.  
</td>
</tr>

</table>

### enumerateCIDs() ###
<code>  
enumerateCIDs  
  
Enumerate the list of all registered CIDs.  
  
@return : enumerator for CIDs.  Elements of the enumeration can be QI'ed  
          for the nsISupportsID interface.  From the nsISupportsID, you   
          can obtain the actual CID.  
  
</code>
#### Returns ####

<table>

<tr>
<td>: enumerator for CIDs.  Elements of the enumeration can be QI'ed  
          for the nsISupportsID interface.  From the nsISupportsID, you   
          can obtain the actual CID.  
</td>
</tr>

</table>

### enumerateContractIDs() ###
<code>  
enumerateContractIDs  
  
Enumerate the list of all registered ContractIDs.  
  
@return : enumerator for ContractIDs. Elements of the enumeration can be   
          QI'ed for the nsISupportsCString interface.  From  the  
          nsISupportsCString interface, you can obtain the actual   
          Contract ID string.  
  
</code>
#### Returns ####

<table>

<tr>
<td>: enumerator for ContractIDs. Elements of the enumeration can be   
          QI'ed for the nsISupportsCString interface.  From  the  
          nsISupportsCString interface, you can obtain the actual   
          Contract ID string.  
</td>
</tr>

</table>

### CIDToContractID(aClass) ###
<code>  
CIDToContractID  
@status OBSOLETE: This method is no longer implemented, but preserved  
                  in this interface for binary compatibility with  
                  Mozilla 1.9.2.  
  
</code>
### contractIDToCID(aContractID) ###
<code>  
contractIDToCID  
  
Returns the CID for a given Contract ID, if one exists and is registered.  
  
@return : Contract ID.  
  
</code>
#### Returns ####

<table>

<tr>
<td>: Contract ID.  
</td>
</tr>

</table>
