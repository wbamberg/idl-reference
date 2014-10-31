---
layout: default
---

# nsINetworkInterfaceListService #

## Methods ##

### getDataInterfaceList(condition) ###
  
Obtain a list of network interfaces that satisfy the specified condition.  
@param condition flags that specify the interfaces to be returned. This  
       can be OR combination of LIST_* flags, or zero to make all available  
       interfaces returned.  
  

#### Parameters ####

<table>

<tr>
<td>condition</td>
<td>flags that specify the interfaces to be returned. This  
       can be OR combination of LIST_* flags, or zero to make all available  
       interfaces returned.  
</td>
</tr>

</table>

## Constants ##

### LIST_NOT_INCLUDE_MMS_INTERFACES ###

### LIST_NOT_INCLUDE_SUPL_INTERFACES ###

### LIST_NOT_INCLUDE_IMS_INTERFACES ###

### LIST_NOT_INCLUDE_DUN_INTERFACES ###
