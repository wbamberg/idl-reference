---
layout: default
---

# nsIClassInfo #
  
Provides information about a specific implementation class.  If you want  
your class to implement nsIClassInfo, see nsIClassInfoImpl.h for  
instructions--you most likely do not want to inherit from nsIClassInfo.  
  

## Methods ##

### getInterfaces(count, array) ###
  
Get an ordered list of the interface ids that instances of the class   
promise to implement. Note that nsISupports is an implicit member   
of any such list and need not be included.   
  
Should set *count = 0 and *array = null and return NS_OK if getting the   
list is not supported.  
  

### getHelperForLanguage(language) ###
  
Get a language mapping specific helper object that may assist in using  
objects of this class in a specific lanaguage. For instance, if asked  
for the helper for nsIProgrammingLanguage::JAVASCRIPT this might return   
an object that can be QI'd into the nsIXPCScriptable interface to assist   
XPConnect in supplying JavaScript specific behavior to callers of the   
instance object.  
  
see: nsIProgrammingLanguage.idl  
  
Should return null if no helper available for given language.  
  

## Attributes ##

### contractID ###
  
A contract ID through which an instance of this class can be created  
(or accessed as a service, if |flags & SINGLETON|), or null.  
  

### classDescription ###
  
A human readable string naming the class, or null.  
  

### classID ###
  
A class ID through which an instance of this class can be created  
(or accessed as a service, if |flags & SINGLETON|), or null.  
  

### implementationLanguage ###
  
Return language type from list in nsIProgrammingLanguage  
  

### flags ###

### classIDNoAlloc ###
  
Also a class ID through which an instance of this class can be created  
(or accessed as a service, if |flags & SINGLETON|).  If the class does  
not have a CID, it should return NS_ERROR_NOT_AVAILABLE.  This attribute  
exists so C++ callers can avoid allocating and freeing a CID, as would  
happen if they used classID.  
  

## Constants ##

### SINGLETON ###
  
Bitflags for 'flags' attribute.  
  

### THREADSAFE ###

### MAIN_THREAD_ONLY ###

### DOM_OBJECT ###

### PLUGIN_OBJECT ###

### SINGLETON_CLASSINFO ###

### CONTENT_NODE ###
  
'flags' attribute bitflag: whether objects of this type implement  
nsIContent.  
  

### RESERVED ###
