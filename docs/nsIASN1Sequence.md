---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsIASN1Sequence.idl">Source file</a>
</div>

# nsIASN1Sequence #
  
This represents a sequence of ASN.1 objects,  
where ASN.1 is "Abstract Syntax Notation number One".  
  
Overview of how this ASN1 interface is intended to  
work.  
  
First off, the nsIASN1Sequence is any type in ASN1  
that consists of sub-elements (ie SEQUENCE, SET)  
nsIASN1Printable Items are all the other types that  
can be viewed by themselves without interpreting further.  
Examples would include INTEGER, UTF-8 STRING, OID.  
These are not intended to directly reflect the numberous  
types that exist in ASN1, but merely an interface to ease  
producing a tree display the ASN1 structure of any DER  
object.  
  
The additional state information carried in this interface  
makes it fit for being used as the data structure  
when working with visual reprenstation of ASN.1 objects  
in a human user interface, like in a tree widget  
where open/close state of nodes must be remembered.  
  

## Attributes ##

### ASN1Objects ###
  
 The array of objects stored in the sequence.  
  

### isValidContainer ###
  
 Whether the node at this position in the ASN.1 data structure  
 sequence contains sub elements understood by the  
 application.  
  

### isExpanded ###
  
 Whether the contained objects should be shown or hidden.  
 A UI implementation can use this flag to store the current  
 expansion state when shown in a tree widget.  
  
