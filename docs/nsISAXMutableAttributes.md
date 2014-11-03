---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/parser/xml/nsISAXMutableAttributes.idl">Source file</a>
</div>

# nsISAXMutableAttributes #
<pre>  
This interface extends the nsISAXAttributes interface with  
manipulators so that the list can be modified or reused.  
  
</pre>
## Methods ##

### addAttribute(uri, localName, qName, type, value) ###
<pre>  
Add an attribute to the end of the list.  
  
For the sake of speed, this method does no checking  
to see if the attribute is already in the list: that is  
the responsibility of the application.  
  
@param uri The Namespace URI, or the empty string if  
       none is available or Namespace processing is not  
       being performed.  
@param localName The local name, or the empty string if  
       Namespace processing is not being performed.  
@param qName The qualified (prefixed) name, or the empty string  
       if qualified names are not available.  
@param type The attribute type as a string.  
@param value The attribute value.  
  
</pre>
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
<pre>  
Clear the attribute list for reuse.  
  
</pre>
### removeAttribute(index) ###
<pre>  
Remove an attribute from the list.  
  
@param index The index of the attribute (zero-based).  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>index</td>
<td>The index of the attribute (zero-based).  
</td>
</tr>

</table>

### setAttributes(attributes) ###
<pre>  
Set the attributes list. This method will clear any attributes in  
the list before adding the attributes from the argument.  
  
@param attributes The attributes object to replace populate the  
                  list with.  
  
</pre>
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
<pre>  
Set an attribute in the list.  
  
For the sake of speed, this method does no checking for name  
conflicts or well-formedness: such checks are the responsibility  
of the application.  
  
@param index The index of the attribute (zero-based).  
@param uri The Namespace URI, or the empty string if  
       none is available or Namespace processing is not  
       being performed.  
@param localName The local name, or the empty string if  
       Namespace processing is not being performed.  
@param qName The qualified name, or the empty string  
       if qualified names are not available.  
@param type The attribute type as a string.  
@param value The attribute value.  
  
</pre>
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
<pre>  
Set the local name of a specific attribute.  
  
@param index The index of the attribute (zero-based).  
@param localName The attribute's local name, or the empty  
       string for none.  
  
</pre>
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
<pre>  
Set the qualified name of a specific attribute.  
  
@param index The index of the attribute (zero-based).  
@param qName The attribute's qualified name, or the empty  
       string for none.  
  
</pre>
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
<pre>  
Set the type of a specific attribute.  
  
@param index The index of the attribute (zero-based).  
@param type The attribute's type.  
  
</pre>
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
<pre>  
Set the Namespace URI of a specific attribute.  
  
@param index The index of the attribute (zero-based).  
@param uri The attribute's Namespace URI, or the empty  
       string for none.  
  
</pre>
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
<pre>  
Set the value of a specific attribute.  
  
@param index The index of the attribute (zero-based).  
@param value The attribute's value.  
  
</pre>
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
