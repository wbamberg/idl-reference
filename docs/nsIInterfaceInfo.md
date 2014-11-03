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
<code>  
These include methods and constants for parent (and all ancestors).  
  
These do *not* make copies ***explicit bending of XPCOM rules***.  
  
</code>
### getMethodInfoForName(methodName, index, info) ###

### getConstant(index, constant, name) ###

### getInfoForParam(methodIndex, param) ###
<code>  
Get the interface information or iid associated with a param of some  
method in this interface.  
  
</code>
### getIIDForParam(methodIndex, param) ###

### getTypeForParam(methodIndex, param, dimension) ###
<code>  
These do *not* make copies ***explicit bending of XPCOM rules***.  
  
</code>
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
  
These include counts for parent (and all ancestors).  
  

### constantCount ###
