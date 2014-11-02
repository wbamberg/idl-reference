---
layout: default
---

# nsIWebNavigationInfo #
  
The nsIWebNavigationInfo interface exposes a way to get information  
on the capabilities of Gecko webnavigation objects.  
  

## Methods ##

### isTypeSupported(aType, aWebNav) ###
  
Query whether aType is supported.  
@param aType the MIME type in question.  
@param aWebNav the nsIWebNavigation object for which the request  
       is being made.  This is allowed to be null.  If it is non-null,  
       the return value of this method may depend on the exact state of  
       aWebNav and the values set through nsIWebBrowserSetup; otherwise  
       the method will assume that the caller is interested in information  
       about nsIWebNavigation objects in their default state.  
@return an enum value indicating whether and how aType is supported.  
@note This method may rescan plugins to ensure that they're properly  
      registered for the types they support.  
  

#### Parameters ####

<table>

<tr>
<td>aType</td>
<td>the MIME type in question.  
</td>
</tr>

<tr>
<td>aWebNav</td>
<td>the nsIWebNavigation object for which the request  
       is being made.  This is allowed to be null.  If it is non-null,  
       the return value of this method may depend on the exact state of  
       aWebNav and the values set through nsIWebBrowserSetup; otherwise  
       the method will assume that the caller is interested in information  
       about nsIWebNavigation objects in their default state.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>an enum value indicating whether and how aType is supported.  
@note This method may rescan plugins to ensure that they're properly  
      registered for the types they support.  
</td>
</tr>

</table>

## Constants ##

### UNSUPPORTED ###
  
Returned by isTypeSupported to indicate lack of support for a type.  
@note this is guaranteed not to change, so that boolean tests can be done  
on the return value if isTypeSupported to detect whether a type is  
supported at all.  
  

### IMAGE ###
  
Returned by isTypeSupported to indicate that a type is supported as an  
image.  
  

### PLUGIN ###
  
Returned by isTypeSupported to indicate that a type is supported via an  
NPAPI ("Netscape 4 API") plug-in.  This is not the value returned for  
"XPCOM plug-ins".  
  

### OTHER ###
  
@note Other return types may be added here in the future as they become  
relevant.  
  
  
Returned by isTypeSupported to indicate that a type is supported via some  
other means.  
  
