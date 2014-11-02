---
layout: default
---

# nsIAddonInterposition #
  
This interface allows Firefox to expose different implementations of its own  
classes to add-ons. Once an interposition is created, it must be assigned to  
an add-on using Cu.setAddonInterposition (JS) or xpc::SetAddonInterposition  
(C++). In both cases, the arguments should be the add-on ID and the  
interposition object (which must be an nsIAddonInterposition). This must  
happen before any compartments are created for the given add-on.  
  
Every time the add-on accesses a property on any object outside its own set  
of compartments, XPConnect will call the interposition's  
interpose method. If the interposition wants to replace the given  
property, it should return a replacement property descriptor for it. If not,  
it should return null.  
  

## Methods ##

### interpose(addonId, target, iface, prop) ###
  
Returns a replacement property descriptor for a browser object.  
  
@param addonId The ID of the add-on accessing the property.  
@param target The browser object being accessed.  
@param iface The IID of the interface the property is associated with. This  
             parameter is only available for XPCWrappedNative targets. As  
             such, it's only useful as an optimization to avoid  
             instanceof checks on the target.  
@param prop The name of the property being accessed.  
@return A property descriptor or null.  
  

#### Parameters ####

<table>

<tr>
<td>addonId</td>
<td>The ID of the add-on accessing the property.  
</td>
</tr>

<tr>
<td>target</td>
<td>The browser object being accessed.  
</td>
</tr>

<tr>
<td>iface</td>
<td>The IID of the interface the property is associated with. This  
             parameter is only available for XPCWrappedNative targets. As  
             such, it's only useful as an optimization to avoid  
             instanceof checks on the target.  
</td>
</tr>

<tr>
<td>prop</td>
<td>The name of the property being accessed.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>A property descriptor or null.  
</td>
</tr>

</table>
