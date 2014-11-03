---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsIASN1Object.idl">Source file</a>
</div>

# nsIASN1Object #
<pre>  
This represents an ASN.1 object,  
where ASN.1 is "Abstract Syntax Notation number One".  
  
The additional state information carried in this interface  
makes it fit for being used as the data structure  
when working with visual reprenstation of ASN.1 objects  
in a human user interface, like in a tree widget  
where open/close state of nodes must be remembered.  
  
</pre>
## Attributes ##

### type ###
<pre>  
 "type" will be equal to one of the defined object identifiers.  
  
</pre>
### tag ###
<pre>  
 This contains a tag as explained in ASN.1 standards documents.  
  
</pre>
### displayName ###
<pre>  
 "displayName" contains a human readable explanatory label.  
  
</pre>
### displayValue ###
<pre>  
 "displayValue" contains the human readable value.  
  
</pre>
## Constants ##

### ASN1_END_CONTENTS ###
<pre>  
 Identifiers for the possible types of object.  
  
</pre>
### ASN1_BOOLEAN ###

### ASN1_INTEGER ###

### ASN1_BIT_STRING ###

### ASN1_OCTET_STRING ###

### ASN1_NULL ###

### ASN1_OBJECT_ID ###

### ASN1_ENUMERATED ###

### ASN1_UTF8_STRING ###

### ASN1_SEQUENCE ###

### ASN1_SET ###

### ASN1_PRINTABLE_STRING ###

### ASN1_T61_STRING ###

### ASN1_IA5_STRING ###

### ASN1_UTC_TIME ###

### ASN1_GEN_TIME ###

### ASN1_VISIBLE_STRING ###

### ASN1_UNIVERSAL_STRING ###

### ASN1_BMP_STRING ###

### ASN1_HIGH_TAG_NUMBER ###

### ASN1_CONTEXT_SPECIFIC ###

### ASN1_APPLICATION ###

### ASN1_PRIVATE ###
