---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/parser/xml/nsISAXMutableAttributes.idl">Source file</a>
</div>

# nsISAXMutableAttributes #
  
This interface extends the nsISAXAttributes interface with  
manipulators so that the list can be modified or reused.  
  

## Methods ##

### addAttribute(uri, localName, qName, type, value) ###
  
Add an attribute to the end of the list.  
  
For the sake of speed, this method does no checking  
to see if the attribute is already in the list: that is  
the responsibility of the application.  
  
  

#### Parameters ####

<table>

<tr>
<td>uri</td>
<td>The Namespace URI, or the empty string if  
       none is available or Namespace processing is not  
       being performed.  
</td>
</tr>

<tr>
<td>localName</td>
<td>The local name, or the empty string if  
       Namespace processing is not being performed.  
</td>
</tr>

<tr>
<td>qName</td>
<td>The qualified (prefixed) name, or the empty string  
       if qualified names are not available.  
</td>
</tr>

<tr>
<td>type</td>
<td>The attribute type as a string.  
</td>
</tr>

<tr>
<td>value</td>
<td>The attribute value.  
</td>
</tr>

</table>

### clear() ###
  
Clear the attribute list for reuse.  
  

### removeAttribute(index) ###
  
Remove an attribute from the list.  
  
  

#### Parameters ####

<table>

<tr>
<td>index</td>
<td>The index of the attribute (zero-based).  
</td>
</tr>

</table>

### setAttributes(attributes) ###
  
Set the attributes list. This method will clear any attributes in  
the list before adding the attributes from the argument.  
  
  

#### Parameters ####

<table>

<tr>
<td>attributes</td>
<td>The attributes object to replace populate the  
                  list with.  
</td>
</tr>

</table>

### setAttribute(index, uri, localName, qName, type, value) ###
  
Set an attribute in the list.  
  
For the sake of speed, this method does no checking for name  
conflicts or well-formedness: such checks are the responsibility  
of the application.  
  
  

#### Parameters ####

<table>

<tr>
<td>index</td>
<td>The index of the attribute (zero-based).  
</td>
</tr>

<tr>
<td>uri</td>
<td>The Namespace URI, or the empty string if  
       none is available or Namespace processing is not  
       being performed.  
</td>
</tr>

<tr>
<td>localName</td>
<td>The local name, or the empty string if  
       Namespace processing is not being performed.  
</td>
</tr>

<tr>
<td>qName</td>
<td>The qualified name, or the empty string  
       if qualified names are not available.  
</td>
</tr>

<tr>
<td>type</td>
<td>The attribute type as a string.  
</td>
</tr>

<tr>
<td>value</td>
<td>The attribute value.  
</td>
</tr>

</table>

### setLocalName(index, localName) ###
  
Set the local name of a specific attribute.  
  
  

#### Parameters ####

<table>

<tr>
<td>index</td>
<td>The index of the attribute (zero-based).  
</td>
</tr>

<tr>
<td>localName</td>
<td>The attribute's local name, or the empty  
       string for none.  
</td>
</tr>

</table>

### setQName(index, qName) ###
  
Set the qualified name of a specific attribute.  
  
  

#### Parameters ####

<table>

<tr>
<td>index</td>
<td>The index of the attribute (zero-based).  
</td>
</tr>

<tr>
<td>qName</td>
<td>The attribute's qualified name, or the empty  
       string for none.  
</td>
</tr>

</table>

### setType(index, type) ###
  
Set the type of a specific attribute.  
  
  

#### Parameters ####

<table>

<tr>
<td>index</td>
<td>The index of the attribute (zero-based).  
</td>
</tr>

<tr>
<td>type</td>
<td>The attribute's type.  
</td>
</tr>

</table>

### setURI(index, uri) ###
  
Set the Namespace URI of a specific attribute.  
  
  

#### Parameters ####

<table>

<tr>
<td>index</td>
<td>The index of the attribute (zero-based).  
</td>
</tr>

<tr>
<td>uri</td>
<td>The attribute's Namespace URI, or the empty  
       string for none.  
</td>
</tr>

</table>

### setValue(index, value) ###
  
Set the value of a specific attribute.  
  
  

#### Parameters ####

<table>

<tr>
<td>index</td>
<td>The index of the attribute (zero-based).  
</td>
</tr>

<tr>
<td>value</td>
<td>The attribute's value.  
</td>
</tr>

</table>
