---
layout: default
---

# nsIStructuredCloneContainer #
  
This interface acts as a container for an object serialized using the  
structured clone algorithm.  
  
You can copy an object into an nsIStructuredCloneContainer using  
initFromVariant or initFromBase64.  It's an error to initialize an  
nsIStructuredCloneContainer more than once.  
  
Once you've initialized the container, you can get a copy of the object it  
stores by calling deserializeToVariant.  You can also get a base-64-encoded  
string containing a copy of the container's serialized data, using  
getDataAsBase64.  
  

## Methods ##

### initFromJSVal(aData) ###
  
Initialize this structured clone container so it contains a clone of the  
given jsval.  
  

### initFromBase64(aData, aFormatVersion) ###
  
Initialize this structured clone container from a base-64-encoded byte  
stream, stored in aData.  aFormatVersion should be the version of the  
structured clone algorithm which was used to generate aData.  
  

### deserializeToVariant() ###
  
Deserialize the object this container holds, returning it wrapped as  
an nsIVariant.  
  

### getDataAsBase64() ###
  
Get this structured clone container's data as a base-64-encoded string.  
  

## Attributes ##

### serializedNBytes ###
  
Get the size in bytes of this container's serialized data.  
  

### formatVersion ###
  
Get the version of the structured clone algorithm which was used to  
generate this container's serialized buffer.  
  
