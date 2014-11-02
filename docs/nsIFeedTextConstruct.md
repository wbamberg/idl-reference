---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/feeds/nsIFeedTextConstruct.idl">Source file</a>
</div>
# nsIFeedTextConstruct #
  
nsIFeedTextConstructs represent feed text fields that can contain  
one of text, HTML, or XHTML. Some extension elements also have "type"  
parameters, and this interface could be used there as well.  
  

## Methods ##

### plainText() ###
  
Returns the text of the text construct, with all markup stripped   
and all entities decoded. If the type attribute's value is "text",  
this function returns the value of the text attribute unchanged.  
  

### createDocumentFragment(element) ###
  
Return an nsIDocumentFragment containing the text and markup.  
  

## Attributes ##

### base ###
  
If the text construct contains (X)HTML, relative references in  
the content should be resolved against this base URI.  
  

### lang ###
  
The language of the text. For example, "en-US" for US English.  
  

### type ###
  
One of "text", "html", or "xhtml". If the type is (x)html, a '<'  
character represents markup. To display that character, an escape  
such as &lt; must be used. If the type is "text", the '<'  
character represents the character itself, and such text should  
not be embedded in markup without escaping it first.  
  

### text ###
  
The content of the text construct.  
  
