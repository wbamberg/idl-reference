---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/browser/components/feeds/nsIWebContentConverterRegistrar.idl">Source file</a>
</div>

# nsIWebContentHandlerInfo #

## Methods ##

### getHandlerURI(uri) ###
   
Gets the service URL Spec, with the loading document URI encoded in it.  
  

#### Parameters ####

<table>

<tr>
<td>uri</td>
<td>         The URI of the document being loaded  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The URI of the service with the loading document URI encoded in   
         it.  
</td>
</tr>

</table>

## Attributes ##

### contentType ###
  
The content type handled by the handler  
  

### uri ###
  
The uri of the handler, with an embedded %s where the URI of the loaded  
document will be encoded.  
  
