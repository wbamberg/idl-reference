---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/reflect/xptinfo/nsIInterfaceInfo.idl">Source file</a>
</div>

# nsIInterfaceInfo #

## Methods ##

### isScriptable() ###

### isBuiltinClass() ###

### getMethodInfo(index, info) ###
<pre>  
These include methods and constants for parent (and all ancestors).  
  
These do *not* make copies ***explicit bending of XPCOM rules***.  
  
</pre>
### getMethodInfoForName(methodName, index, info) ###

### getConstant(index, constant, name) ###

### getInfoForParam(methodIndex, param) ###
<pre>  
Get the interface information or iid associated with a param of some  
method in this interface.  
  
</pre>
### getIIDForParam(methodIndex, param) ###

### getTypeForParam(methodIndex, param, dimension) ###
<pre>  
These do *not* make copies ***explicit bending of XPCOM rules***.  
  
</pre>
### getSizeIsArgNumberForParam(methodIndex, param, dimension) ###

### getInterfaceIsArgNumberForParam(methodIndex, param) ###

### isIID(IID) ###

### getNameShared(name) ###

### getIIDShared(iid) ###

### isFunction() ###

### hasAncestor(iid) ###

### getIIDForParamNoAlloc(methodIndex, param, iid) ###

## Attributes ##

### name ###

### InterfaceIID ###

### parent ###

### methodCount ###
<pre>  
These include counts for parent (and all ancestors).  
  
</pre>
### constantCount ###
