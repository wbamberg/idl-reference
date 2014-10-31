---
layout: default
---

# nsIParserUtils #
  
Non-Web HTML parser functionality to Firefox extensions and XULRunner apps.   
Don't use this from within Gecko--use nsContentUtils, nsTreeSanitizer, etc.  
directly instead.  
  

## Methods ##

### sanitize(src, flags) ###
  
Parses a string into an HTML document, sanitizes the document and   
returns the result serialized to a string.  
  
The sanitizer is designed to protect against XSS when sanitized content  
is inserted into a different-origin context without an iframe-equivalent  
sandboxing mechanism.  
  
By default, the sanitizer doesn't try to avoid leaking information that   
the content was viewed to third parties. That is, by default, e.g.   
<img src> pointing to an HTTP server potentially controlled by a third   
party is not removed. To avoid ambient information leakage upon loading  
the sanitized content, use the SanitizerInternalEmbedsOnly flag. In that   
case, <a href> links (and similar) to other content are preserved, so an  
explicit user action (following a link) after the content has been loaded  
can still leak information.  
  
By default, non-dangerous non-CSS presentational HTML elements and   
attributes or forms are not removed. To remove these, use   
SanitizerDropNonCSSPresentation and/or SanitizerDropForms.  
  
By default, comments and CSS is removed. To preserve comments, use  
SanitizerAllowComments. To preserve <style> and style="", use   
SanitizerAllowStyle. -moz-binding is removed from <style> and style="" if  
present. In this case, properties that Gecko doesn't recognize can get   
removed as a side effect. Note! If -moz-binding is not present, <style>  
and style="" and SanitizerAllowStyle is specified, the sanitized content  
may still be XSS dangerous if loaded into a non-Gecko Web engine!  
  
@param src the HTML source to parse (C++ callers are allowed but not  
           required to use the same string for the return value.)  
@param flags sanitization option flags defined above  
  

#### Parameters ####

<table>

<tr>
<td>src</td>
<td>the HTML source to parse (C++ callers are allowed but not  
           required to use the same string for the return value.)  
</td>
</tr>

<tr>
<td>flags</td>
<td>sanitization option flags defined above  
</td>
</tr>

</table>

### convertToPlainText(src, flags, wrapCol) ###
  
Convert HTML to plain text.  
  
@param src the HTML source to parse (C++ callers are allowed but not  
           required to use the same string for the return value.)  
@param flags conversion option flags defined in nsIDocumentEncoder  
@param wrapCol number of characters per line; 0 for no auto-wrapping  
  

#### Parameters ####

<table>

<tr>
<td>src</td>
<td>the HTML source to parse (C++ callers are allowed but not  
           required to use the same string for the return value.)  
</td>
</tr>

<tr>
<td>flags</td>
<td>conversion option flags defined in nsIDocumentEncoder  
</td>
</tr>

<tr>
<td>wrapCol</td>
<td>number of characters per line; 0 for no auto-wrapping  
</td>
</tr>

</table>

### parseFragment(fragment, flags, isXML, baseURI, element) ###
  
Parses markup into a sanitized document fragment.  
  
@param fragment the input markup  
@param flags sanitization option flags defined above  
@param isXML true if |fragment| is XML and false if HTML  
@param baseURI the base URL for this fragment  
@param element the context node for the fragment parsing algorithm  
  

#### Parameters ####

<table>

<tr>
<td>fragment</td>
<td>the input markup  
</td>
</tr>

<tr>
<td>flags</td>
<td>sanitization option flags defined above  
</td>
</tr>

<tr>
<td>isXML</td>
<td>true if |fragment| is XML and false if HTML  
</td>
</tr>

<tr>
<td>baseURI</td>
<td>the base URL for this fragment  
</td>
</tr>

<tr>
<td>element</td>
<td>the context node for the fragment parsing algorithm  
</td>
</tr>

</table>

## Constants ##

### SanitizerAllowComments ###
  
Flag for sanitizer: Allow comment nodes.  
  

### SanitizerAllowStyle ###
  
Flag for sanitizer: Allow <style> and style="" (with contents sanitized  
in case of -moz-binding). Note! If -moz-binding is absent, properties  
that might be XSS risks in other Web engines are preserved!  
  

### SanitizerCidEmbedsOnly ###
  
Flag for sanitizer: Only allow cid: URLs for embedded content.  
  
At present, sanitizing CSS backgrounds, etc., is not supported, so setting   
this together with SanitizerAllowStyle doesn't make sense.  
  
At present, sanitizing CSS syntax in SVG presentational attributes is not  
supported, so this option flattens out SVG.  
  

### SanitizerDropNonCSSPresentation ###
  
Flag for sanitizer: Drop non-CSS presentational HTML elements and   
attributes, such as <font>, <center> and bgcolor="".  
  

### SanitizerDropForms ###
  
Flag for sanitizer: Drop forms and form controls (excluding   
fieldset/legend).  
  

### SanitizerDropMedia ###
  
Flag for sanitizer: Drop <img>, <video>, <audio> and <source> and flatten  
out SVG.  
  
