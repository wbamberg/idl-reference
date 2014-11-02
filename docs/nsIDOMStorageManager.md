---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/storage/nsIDOMStorageManager.idl">Source file</a>
</div>

# nsIDOMStorageManager #
  
General purpose interface that has two implementations, for localStorage  
resp. sessionStorage with "@mozilla.org/dom/localStorage-manager;1" resp.  
"@mozilla.org/dom/sessionStorage-manager;1" contract IDs.  
  

## Methods ##

### precacheStorage(aPrincipal) ###
  
This starts async preloading of a storage cache for scope  
defined by the principal.  
  

### createStorage(aWindow, aPrincipal, aDocumentURI, aPrivate) ###
  
Returns instance of DOM storage object for given principal.  
A new object is always returned and it is ensured there is  
a storage for the scope created.  
  
@param aWindow  
   The parent window.  
@param aPrincipal  
   Principal to bound storage to.  
@param aDocumentURI  
   URL of the demanding document, used for DOM storage event only.  
@param aPrivate  
   Whether the demanding document is running in Private Browsing mode or not.  
  

#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>   The parent window.  
</td>
</tr>

<tr>
<td>aPrincipal</td>
<td>   Principal to bound storage to.  
</td>
</tr>

<tr>
<td>aDocumentURI</td>
<td>   URL of the demanding document, used for DOM storage event only.  
</td>
</tr>

<tr>
<td>aPrivate</td>
<td>   Whether the demanding document is running in Private Browsing mode or not.  
</td>
</tr>

</table>

### getStorage(aWindow, aPrincipal, aPrivate) ###
  
Returns instance of DOM storage object for given principal.  
If there is no storage managed for the scope, then null is returned and  
no object is created.  Otherwise, an object (new) for the existing storage  
scope is returned.  
  
@param aWindow  
   The parent window.  
@param aPrincipal  
   Principal to bound storage to.  
@param aPrivate  
   Whether the demanding document is running in Private Browsing mode or not.  
  

#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>   The parent window.  
</td>
</tr>

<tr>
<td>aPrincipal</td>
<td>   Principal to bound storage to.  
</td>
</tr>

<tr>
<td>aPrivate</td>
<td>   Whether the demanding document is running in Private Browsing mode or not.  
</td>
</tr>

</table>

### cloneStorage(aStorageToCloneFrom) ###
  
Clones given storage into this storage manager.  
  
@param aStorageToCloneFrom  
   The storage to copy all items from into this manager.  Manager will then  
   return a new and independent object that contains snapshot of data from  
   the moment this method was called.  Modification to this new object will  
   not affect the original storage content we cloned from and vice versa.  
  

#### Parameters ####

<table>

<tr>
<td>aStorageToCloneFrom</td>
<td>   The storage to copy all items from into this manager.  Manager will then  
   return a new and independent object that contains snapshot of data from  
   the moment this method was called.  Modification to this new object will  
   not affect the original storage content we cloned from and vice versa.  
</td>
</tr>

</table>

### checkStorage(aPrincipal, aStorage) ###
  
Returns true if the storage belongs to the given principal and is managed  
(i.e. has been created and is cached) by this storage manager.  
  
@param aPrincipal  
   Principal to check the storage against.  
@param aStorage  
   The storage object to examine.  
  
@result  
   true when the storage object is bound with the principal and is managed  
        by this storage manager.  
   false otherwise  
  

#### Parameters ####

<table>

<tr>
<td>aPrincipal</td>
<td>   Principal to check the storage against.  
</td>
</tr>

<tr>
<td>aStorage</td>
<td>   The storage object to examine.  
</td>
</tr>

</table>

### getLocalStorageForPrincipal(aPrincipal, aDocumentURI, aPrivate) ###
  
@deprecated  
  
Returns instance of localStorage object for aURI's origin.  
This method ensures there is always only a single instance  
for a single origin.  
  
Currently just forwards to the createStorage method of this  
interface.  
  
Extension developers are strongly encouraged to use getStorage  
or createStorage method instead.  
  
