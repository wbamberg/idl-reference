---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/streamconv/public/nsITXTToHTMLConv.idl">Source file</a>
</div>

# nsITXTToHTMLConv #

## Methods ##

### setTitle(text) ###
  
@param text: Title to set for the HTML document.  Only applicable if  
             preFormatHTML(true) is called.  
@result      The given title will be used to form an HTML document  
             from the plain text document.  
  

#### Parameters ####

<table>

<tr>
<td>text:</td>
<td>Title to set for the HTML document.  Only applicable if  
             preFormatHTML(true) is called.  
@result      The given title will be used to form an HTML document  
             from the plain text document.  
</td>
</tr>

</table>

### preFormatHTML(value) ###
  
@param value: true to use an HTML header and footer on the document,  
              false to omit it.  
@result       The document will use a header and footer if value is  
              true.  
  

#### Parameters ####

<table>

<tr>
<td>value:</td>
<td>true to use an HTML header and footer on the document,  
              false to omit it.  
@result       The document will use a header and footer if value is  
              true.  
</td>
</tr>

</table>
