---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/js/xpconnect/idl/mozIJSSubScriptLoader.idl">Source file</a>
</div>

# mozIJSSubScriptLoader #

## Methods ##

### loadSubScript(url, obj, charset) ###
  
This method should only be called from JS!  
In JS, the signature looks like:  
rv loadSubScript (url [, obj] [, charset]);  
  

#### Parameters ####

<table>

<tr>
<td>url</td>
<td>the url of the sub-script, it MUST be either a file:,  
           resource:, or chrome: url, and MUST be local.  
</td>
</tr>

<tr>
<td>obj</td>
<td>an optional object to evaluate the script onto, it  
           defaults to the global object of the caller.  
</td>
</tr>

<tr>
<td>charset</td>
<td>optionally specifies the character encoding of  
               the file. If absent, the file is interpreted  
               as ASCII.  
@retval rv the value returned by the sub-script  
</td>
</tr>

</table>

### loadSubScriptWithOptions(url, options) ###
  
This method should only be called from JS!  
In JS, the signature looks like:  
rv = loadSubScript (url, optionsObject)  
  

#### Parameters ####

<table>

<tr>
<td>url</td>
<td>the url of the sub-script, it MUST be either a file:,  
           resource:, or chrome: url, and MUST be local.  
</td>
</tr>

<tr>
<td>optionsObject</td>
<td>an object with parameters. Valid parameters are:  
                     - charset: specifying the character encoding of the file (default: ASCII)  
                     - target:  an object to evaluate onto (default: global object of the caller)  
                     - ignoreCache: if set to true, will bypass the cache for reading the file.  
@retval rv the value returned by the sub-script  
</td>
</tr>

</table>

### precompileScript(uri, principal, observer) ###
