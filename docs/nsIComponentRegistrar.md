---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/components/nsIComponentRegistrar.idl">Source file</a>
</div>

# nsIComponentRegistrar #

## Methods ##

### autoRegister(aSpec) ###
  
autoRegister  
  
Register a .manifest file, or an entire directory containing  
these files. Registration lasts for this run only, and is not cached.  
  
@note Formerly this method would register component files directly. This  
      is no longer supported.  
  

### autoUnregister(aSpec) ###
  
autoUnregister  
@status OBSOLETE: This method is no longer implemented, but preserved  
                  in this interface for binary compatibility with  
                  Mozilla 1.9.2.  
  

### registerFactory(aClass, aClassName, aContractID, aFactory) ###
  
registerFactory  
  
Register a factory with a given ContractID, CID and Class Name.  
  
@param aClass      : CID of object  
@param aClassName  : Class Name of CID (unused)  
@param aContractID : ContractID associated with CID aClass. May be null  
                     if no contract ID is needed.  
@param aFactory    : Factory that will be registered for CID aClass.  
                     If aFactory is null, the contract will be associated  
                     with a previously registered CID.  
  

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
  
unregisterFactory  
  
Unregister a factory associated with CID aClass.  
  
@param aClass   : CID being unregistered  
@param aFactory : Factory previously registered to create instances of  
                  CID aClass.  
  
@throws NS_ERROR* Method failure.  
  

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
  
registerFactoryLocation  
@status OBSOLETE: This method is no longer implemented, but preserved  
                  in this interface for binary compatibility with  
                  Mozilla 1.9.2.  
  

### unregisterFactoryLocation(aClass, aFile) ###
  
unregisterFactoryLocation  
@status OBSOLETE: This method is no longer implemented, but preserved  
                  in this interface for binary compatibility with  
                  Mozilla 1.9.2.  
  

### isCIDRegistered(aClass) ###
  
isCIDRegistered  
  
Returns true if a factory is registered for the CID.  
  
@param aClass : CID queried for registeration  
@return       : true if a factory is registered for CID   
                false otherwise.  
  

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
  
isContractIDRegistered  
  
Returns true if a factory is registered for the contract id.  
  
@param aClass : contract id queried for registeration  
@return       : true if a factory is registered for contract id   
                false otherwise.  
  

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
  
enumerateCIDs  
  
Enumerate the list of all registered CIDs.  
  
@return : enumerator for CIDs.  Elements of the enumeration can be QI'ed  
          for the nsISupportsID interface.  From the nsISupportsID, you   
          can obtain the actual CID.  
  

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
  
enumerateContractIDs  
  
Enumerate the list of all registered ContractIDs.  
  
@return : enumerator for ContractIDs. Elements of the enumeration can be   
          QI'ed for the nsISupportsCString interface.  From  the  
          nsISupportsCString interface, you can obtain the actual   
          Contract ID string.  
  

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
  
CIDToContractID  
@status OBSOLETE: This method is no longer implemented, but preserved  
                  in this interface for binary compatibility with  
                  Mozilla 1.9.2.  
  

### contractIDToCID(aContractID) ###
  
contractIDToCID  
  
Returns the CID for a given Contract ID, if one exists and is registered.  
  
@return : Contract ID.  
  

#### Returns ####

<table>

<tr>
<td>: Contract ID.  
</td>
</tr>

</table>
