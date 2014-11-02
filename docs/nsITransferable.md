---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsITransferable.idl">Source file</a>
</div>

# nsITransferable #

## Methods ##

### init(aContext) ###
  
Initializes a transferable object.  This should be called on all  
transferable objects.  Failure to do so will result in fatal assertions in  
debug builds.  
  
The load context is used to track whether the transferable is storing privacy-  
sensitive information.  For example, we try to delete data that you copy  
to the clipboard when you close a Private Browsing window.  
  
To get the appropriate load context in Javascript callers, one needs to get  
to the document that the transferable corresponds to, and then get the load  
context from the document like this:  
  
var loadContext = doc.defaultView.QueryInterface(Ci.nsIInterfaceRequestor)  
                                 .getInterface(Ci.nsIWebNavigation)  
                                 .QueryInterface(Ci.nsILoadContext);  
  
In C++ callers, if you have the corresponding document, you can just call  
nsIDocument::GetLoadContext to get to the load context object.  
  
@param aContext the load context associated with the transferable object.  
       This can be set to null if a load context is not available.  
  

#### Parameters ####

<table>

<tr>
<td>aContext</td>
<td>the load context associated with the transferable object.  
       This can be set to null if a load context is not available.  
</td>
</tr>

</table>

### flavorsTransferableCanExport() ###
  
Computes a list of flavors (mime types as nsISupportsCString) that the transferable   
can export, either through intrinsic knowledge or output data converters.  
  
@param  aDataFlavorList fills list with supported flavors. This is a copy of  
         the internal list, so it may be edited w/out affecting the transferable.  
  

#### Parameters ####

<table>

<tr>
<td>aDataFlavorList</td>
<td>fills list with supported flavors. This is a copy of  
         the internal list, so it may be edited w/out affecting the transferable.  
</td>
</tr>

</table>

### getTransferData(aFlavor, aData, aDataLen) ###
  
Given a flavor retrieve the data.   
  
@param  aFlavor (in parameter) the flavor of data to retrieve  
@param  aData the data. Some variant of class in nsISupportsPrimitives.idl  
@param  aDataLen the length of the data  
  

#### Parameters ####

<table>

<tr>
<td>aFlavor</td>
<td>(in parameter) the flavor of data to retrieve  
</td>
</tr>

<tr>
<td>aData</td>
<td>the data. Some variant of class in nsISupportsPrimitives.idl  
</td>
</tr>

<tr>
<td>aDataLen</td>
<td>the length of the data  
</td>
</tr>

</table>

### getAnyTransferData(aFlavor, aData, aDataLen) ###
  
Returns the best flavor in the transferable, given those that have  
been added to it with |AddFlavor()|  
  
@param  aFlavor (out parameter) the flavor of data that was retrieved  
@param  aData the data. Some variant of class in nsISupportsPrimitives.idl  
@param  aDataLen the length of the data  
  

#### Parameters ####

<table>

<tr>
<td>aFlavor</td>
<td>(out parameter) the flavor of data that was retrieved  
</td>
</tr>

<tr>
<td>aData</td>
<td>the data. Some variant of class in nsISupportsPrimitives.idl  
</td>
</tr>

<tr>
<td>aDataLen</td>
<td>the length of the data  
</td>
</tr>

</table>

### isLargeDataSet() ###
  
Returns true if the data is large.  
  

### flavorsTransferableCanImport() ###
  
Computes a list of flavors (mime types as nsISupportsCString) that the transferable can  
accept into it, either through intrinsic knowledge or input data converters.  
  
@param  outFlavorList fills list with supported flavors. This is a copy of  
         the internal list, so it may be edited w/out affecting the transferable.  
  

#### Parameters ####

<table>

<tr>
<td>outFlavorList</td>
<td>fills list with supported flavors. This is a copy of  
         the internal list, so it may be edited w/out affecting the transferable.  
</td>
</tr>

</table>

### setTransferData(aFlavor, aData, aDataLen) ###
  
Sets the data in the transferable with the specified flavor. The transferable  
will maintain its own copy the data, so it is not necessary to do that beforehand.  
  
@param  aFlavor the flavor of data that is being set  
@param  aData the data, either some variant of class in nsISupportsPrimitives.idl,  
        an nsIFile, or an nsIFlavorDataProvider (see above)  
@param  aDataLen the length of the data, or 0 if passing a nsIFlavorDataProvider  
  

#### Parameters ####

<table>

<tr>
<td>aFlavor</td>
<td>the flavor of data that is being set  
</td>
</tr>

<tr>
<td>aData</td>
<td>the data, either some variant of class in nsISupportsPrimitives.idl,  
        an nsIFile, or an nsIFlavorDataProvider (see above)  
</td>
</tr>

<tr>
<td>aDataLen</td>
<td>the length of the data, or 0 if passing a nsIFlavorDataProvider  
</td>
</tr>

</table>

### addDataFlavor(aDataFlavor) ###
  
Add the data flavor, indicating that this transferable   
can receive this type of flavor  
  
@param  aDataFlavor a new data flavor to handle  
  

#### Parameters ####

<table>

<tr>
<td>aDataFlavor</td>
<td>a new data flavor to handle  
</td>
</tr>

</table>

### removeDataFlavor(aDataFlavor) ###
  
Removes the data flavor matching the given one (string compare) and the data  
that goes along with it.  
  
@param  aDataFlavor a data flavor to remove  
  

#### Parameters ####

<table>

<tr>
<td>aDataFlavor</td>
<td>a data flavor to remove  
</td>
</tr>

</table>

## Attributes ##

### converter ###

### isPrivateData ###
  
Use of the SetIsPrivateData() method generated by isPrivateData attribute should   
be avoided as much as possible because the value set may not reflect the status   
of the context in which the transferable was created.  
  

### requestingNode ###
  
The source dom node this transferable was created from.  
Note, currently only in use on Windows for network principal  
information in drag operations.  
  

## Constants ##

### kFlavorHasDataProvider ###
