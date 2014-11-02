---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/base/nsIDOMSerializer.idl">Source file</a>
</div>

# nsIDOMSerializer #
  
The nsIDOMSerializer interface is really a placeholder till the W3C  
DOM Working Group defines a mechanism for serializing DOM nodes.  
An instance of this interface can be used to serialize a DOM document  
or any DOM subtree.  
  

## Methods ##

### serializeToString(root) ###
  
The subtree rooted by the specified element is serialized to  
a string.  
  
@param root The root of the subtree to be serialized. This could  
            be any node, including a Document.  
@returns The serialized subtree in the form of a Unicode string  
  

#### Parameters ####

<table>

<tr>
<td>root</td>
<td>The root of the subtree to be serialized. This could  
            be any node, including a Document.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The serialized subtree in the form of a Unicode string  
</td>
</tr>

</table>

### serializeToStream(root, stream, charset) ###
  
The subtree rooted by the specified element is serialized to  
a byte stream using the character set specified.  
@param root The root of the subtree to be serialized. This could  
            be any node, including a Document.  
@param stream The byte stream to which the subtree is serialized.  
@param charset The name of the character set to use for the encoding  
               to a byte stream.  If this string is empty and root is  
               a document, the document's character set will be used.  
  

#### Parameters ####

<table>

<tr>
<td>root</td>
<td>The root of the subtree to be serialized. This could  
            be any node, including a Document.  
</td>
</tr>

<tr>
<td>stream</td>
<td>The byte stream to which the subtree is serialized.  
</td>
</tr>

<tr>
<td>charset</td>
<td>The name of the character set to use for the encoding  
               to a byte stream.  If this string is empty and root is  
               a document, the document's character set will be used.  
</td>
</tr>

</table>
