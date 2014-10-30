---
layout: default
---

# nsIComponentRegistrar #

## Methods ##

### autoRegister ###
  
autoRegister  
  
Register a .manifest file, or an entire directory containing  
these files. Registration lasts for this run only, and is not cached.  
  
@note Formerly this method would register component files directly. This  
      is no longer supported.  
  

### autoUnregister ###
  
autoUnregister  
@status OBSOLETE: This method is no longer implemented, but preserved  
                  in this interface for binary compatibility with  
                  Mozilla 1.9.2.  
  

### registerFactory ###
  
registerFactory  
  
Register a factory with a given ContractID, CID and Class Name.  
  
@param aClass      : CID of object  
@param aClassName  : Class Name of CID (unused)  
@param aContractID : ContractID associated with CID aClass. May be null  
                     if no contract ID is needed.  
@param aFactory    : Factory that will be registered for CID aClass.  
                     If aFactory is null, the contract will be associated  
                     with a previously registered CID.  
  

### unregisterFactory ###
  
unregisterFactory  
  
Unregister a factory associated with CID aClass.  
  
@param aClass   : CID being unregistered  
@param aFactory : Factory previously registered to create instances of  
                  CID aClass.  
  
@throws NS_ERROR* Method failure.  
  

### registerFactoryLocation ###
  
registerFactoryLocation  
@status OBSOLETE: This method is no longer implemented, but preserved  
                  in this interface for binary compatibility with  
                  Mozilla 1.9.2.  
  

### unregisterFactoryLocation ###
  
unregisterFactoryLocation  
@status OBSOLETE: This method is no longer implemented, but preserved  
                  in this interface for binary compatibility with  
                  Mozilla 1.9.2.  
  

### isCIDRegistered ###
  
isCIDRegistered  
  
Returns true if a factory is registered for the CID.  
  
@param aClass : CID queried for registeration  
@return       : true if a factory is registered for CID   
                false otherwise.  
  

### isContractIDRegistered ###
  
isContractIDRegistered  
  
Returns true if a factory is registered for the contract id.  
  
@param aClass : contract id queried for registeration  
@return       : true if a factory is registered for contract id   
                false otherwise.  
  

### enumerateCIDs ###
  
enumerateCIDs  
  
Enumerate the list of all registered CIDs.  
  
@return : enumerator for CIDs.  Elements of the enumeration can be QI'ed  
          for the nsISupportsID interface.  From the nsISupportsID, you   
          can obtain the actual CID.  
  

### enumerateContractIDs ###
  
enumerateContractIDs  
  
Enumerate the list of all registered ContractIDs.  
  
@return : enumerator for ContractIDs. Elements of the enumeration can be   
          QI'ed for the nsISupportsCString interface.  From  the  
          nsISupportsCString interface, you can obtain the actual   
          Contract ID string.  
  

### CIDToContractID ###
  
CIDToContractID  
@status OBSOLETE: This method is no longer implemented, but preserved  
                  in this interface for binary compatibility with  
                  Mozilla 1.9.2.  
  

### contractIDToCID ###
  
contractIDToCID  
  
Returns the CID for a given Contract ID, if one exists and is registered.  
  
@return : Contract ID.  
  
