---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/js/xpconnect/idl/nsIXPCScriptable.idl">Source file</a>
</div>

# nsIXPCScriptable #
<pre>  
Note: This is not really an XPCOM interface.  For example, callers must  
guarantee that they set the *_retval of the various methods that return a  
boolean to PR_TRUE before making the call.  Implementations may skip writing  
to *_retval unless they want to return PR_FALSE.  
  
</pre>
## Methods ##

### getScriptableFlags() ###

### preCreate(nativeObj, cx, globalObj, parentObj) ###

### create(wrapper, cx, obj) ###

### postCreate(wrapper, cx, obj) ###

### postTransplant(wrapper, cx, obj) ###

### addProperty(wrapper, cx, obj, id, vp) ###

### delProperty(wrapper, cx, obj, id) ###

### getProperty(wrapper, cx, obj, id, vp) ###

### setProperty(wrapper, cx, obj, id, vp) ###

### enumerate(wrapper, cx, obj) ###

### newEnumerate(wrapper, cx, obj, enum_op, statep, idp) ###

### newResolve(wrapper, cx, obj, id, objp) ###

### convert(wrapper, cx, obj, type, vp) ###

### finalize(wrapper, fop, obj) ###

### call(wrapper, cx, obj, args) ###

### construct(wrapper, cx, obj, args) ###

### hasInstance(wrapper, cx, obj, val, bp) ###

### postCreatePrototype(cx, proto) ###

## Attributes ##

### className ###

## Constants ##

### WANT_PRECREATE ###

### WANT_CREATE ###

### WANT_POSTCREATE ###

### WANT_ADDPROPERTY ###

### WANT_DELPROPERTY ###

### WANT_GETPROPERTY ###

### WANT_SETPROPERTY ###

### WANT_ENUMERATE ###

### WANT_NEWENUMERATE ###

### WANT_NEWRESOLVE ###

### WANT_CONVERT ###

### WANT_FINALIZE ###

### WANT_CALL ###

### WANT_CONSTRUCT ###

### WANT_HASINSTANCE ###

### USE_JSSTUB_FOR_ADDPROPERTY ###

### USE_JSSTUB_FOR_DELPROPERTY ###

### USE_JSSTUB_FOR_SETPROPERTY ###

### DONT_ENUM_STATIC_PROPS ###

### DONT_ENUM_QUERY_INTERFACE ###

### DONT_ASK_INSTANCE_FOR_SCRIPTABLE ###

### CLASSINFO_INTERFACES_ONLY ###

### ALLOW_PROP_MODS_DURING_RESOLVE ###

### ALLOW_PROP_MODS_TO_PROTOTYPE ###

### IS_GLOBAL_OBJECT ###

### DONT_REFLECT_INTERFACE_NAMES ###

### RESERVED ###
