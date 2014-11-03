---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/components/nsIClassInfo.idl">Source file</a>
</div>

# nsIClassInfo #
<pre>  
Provides information about a specific implementation class.  If you want  
your class to implement nsIClassInfo, see nsIClassInfoImpl.h for  
instructions--you most likely do not want to inherit from nsIClassInfo.  
  
</pre>
## Methods ##

### getInterfaces(count, array) ###
<pre>  
Get an ordered list of the interface ids that instances of the class   
promise to implement. Note that nsISupports is an implicit member   
of any such list and need not be included.   
  
Should set *count = 0 and *array = null and return NS_OK if getting the   
list is not supported.  
  
</pre>
### getHelperForLanguage(language) ###
<pre>  
Get a language mapping specific helper object that may assist in using  
objects of this class in a specific lanaguage. For instance, if asked  
for the helper for nsIProgrammingLanguage::JAVASCRIPT this might return   
an object that can be QI'd into the nsIXPCScriptable interface to assist   
XPConnect in supplying JavaScript specific behavior to callers of the   
instance object.  
  
see: nsIProgrammingLanguage.idl  
  
Should return null if no helper available for given language.  
  
</pre>
## Attributes ##

### contractID ###
<pre>  
A contract ID through which an instance of this class can be created  
(or accessed as a service, if |flags & SINGLETON|), or null.  
  
</pre>
### classDescription ###
<pre>  
A human readable string naming the class, or null.  
  
</pre>
### classID ###
<pre>  
A class ID through which an instance of this class can be created  
(or accessed as a service, if |flags & SINGLETON|), or null.  
  
</pre>
### implementationLanguage ###
<pre>  
Return language type from list in nsIProgrammingLanguage  
  
</pre>
### flags ###

### classIDNoAlloc ###
<pre>  
Also a class ID through which an instance of this class can be created  
(or accessed as a service, if |flags & SINGLETON|).  If the class does  
not have a CID, it should return NS_ERROR_NOT_AVAILABLE.  This attribute  
exists so C++ callers can avoid allocating and freeing a CID, as would  
happen if they used classID.  
  
</pre>
## Constants ##

### SINGLETON ###
<pre>  
Bitflags for 'flags' attribute.  
  
</pre>
### THREADSAFE ###

### MAIN_THREAD_ONLY ###

### DOM_OBJECT ###

### PLUGIN_OBJECT ###

### SINGLETON_CLASSINFO ###

### CONTENT_NODE ###
<pre>  
'flags' attribute bitflag: whether objects of this type implement  
nsIContent.  
  
</pre>
### RESERVED ###
