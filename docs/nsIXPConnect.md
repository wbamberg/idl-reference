---
layout: default
---

# nsIXPConnect #
***********************************************************************/  

## Methods ##

### initClassesWithNewWrappedGlobal(aJSContext, aCOMObj, aPrincipal, aFlags, aOptions) ###
  
Creates a new global object using the given aCOMObj as the global  
object. The object will be set up according to the flags (defined  
below). If you do not pass INIT_JS_STANDARD_CLASSES, then aCOMObj  
must implement nsIXPCScriptable so it can resolve the standard  
classes when asked by the JS engine.  
  
@param aJSContext the context to use while creating the global object.  
@param aCOMObj the native object that represents the global object.  
@param aPrincipal the principal of the code that will run in this  
                  compartment. Can be null if not on the main thread.  
@param aFlags one of the flags below specifying what options this  
              global object wants.  
@param aOptions JSAPI-specific options for the new compartment.  
  

#### Parameters ####

<table>

<tr>
<td>aJSContext</td>
<td>the context to use while creating the global object.  
</td>
</tr>

<tr>
<td>aCOMObj</td>
<td>the native object that represents the global object.  
</td>
</tr>

<tr>
<td>aPrincipal</td>
<td>the principal of the code that will run in this  
                  compartment. Can be null if not on the main thread.  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>one of the flags below specifying what options this  
              global object wants.  
</td>
</tr>

<tr>
<td>aOptions</td>
<td>JSAPI-specific options for the new compartment.  
</td>
</tr>

</table>

### wrapNative(aJSContext, aScope, aCOMObj, aIID) ###
  
wrapNative will create a new JSObject or return an existing one.  
  
The JSObject is returned inside a refcounted nsIXPConnectJSObjectHolder.  
As long as this holder is held the JSObject will be protected from  
collection by JavaScript's garbage collector. It is a good idea to  
transfer the JSObject to some equally protected place before releasing  
the holder (i.e. use JS_SetProperty to make this object a property of  
some other JSObject).  
  
This method now correctly deals with cases where the passed in xpcom  
object already has an associated JSObject for the cases:  
 1) The xpcom object has already been wrapped for use in the same scope  
    as an nsIXPConnectWrappedNative.  
 2) The xpcom object is in fact a nsIXPConnectWrappedJS and thus already  
    has an underlying JSObject.  
  
It *might* be possible to QueryInterface the nsIXPConnectJSObjectHolder  
returned by the method into a nsIXPConnectWrappedNative or a  
nsIXPConnectWrappedJS.  
  
This method will never wrap the JSObject involved in an  
XPCNativeWrapper before returning.  
  
Returns:  
   success:  
      NS_OK  
   failure:  
      NS_ERROR_XPC_BAD_CONVERT_NATIVE  
      NS_ERROR_XPC_CANT_GET_JSOBJECT_OF_DOM_OBJECT  
      NS_ERROR_FAILURE  
  

### wrapNativeToJSVal(aJSContext, aScope, aCOMObj, aCache, aIID, aAllowWrapper, aVal) ###
  
Same as wrapNative, but it returns the JSObject in aVal. C++ callers  
must ensure that aVal is rooted.  
aIID may be null, it means the same as passing in  
&NS_GET_IID(nsISupports) but when passing in null certain shortcuts  
can be taken because we know without comparing IIDs that the caller is  
asking for an nsISupports wrapper.  
If aAllowWrapper, then the returned value will be wrapped in the proper  
type of security wrapper on top of the XPCWrappedNative (if needed).  
This method doesn't push aJSContext on the context stack, so the caller  
is required to push it if the top of the context stack is not equal to  
aJSContext.  
  

### wrapJS(aJSContext, aJSObj, aIID, result) ###
  
wrapJS will yield a new or previously existing xpcom interface pointer  
to represent the JSObject passed in.  
  
This method now correctly deals with cases where the passed in JSObject  
already has an associated xpcom interface for the cases:  
 1) The JSObject has already been wrapped as a nsIXPConnectWrappedJS.  
 2) The JSObject is in fact a nsIXPConnectWrappedNative and thus already  
    has an underlying xpcom object.  
 3) The JSObject is of a jsclass which supports getting the nsISupports  
    from the JSObject directly. This is used for idlc style objects  
    (e.g. DOM objects).  
  
It *might* be possible to QueryInterface the resulting interface pointer  
to nsIXPConnectWrappedJS.  
  
Returns:  
  success:  
    NS_OK  
   failure:  
      NS_ERROR_XPC_BAD_CONVERT_JS  
      NS_ERROR_FAILURE  
  

### jSValToVariant(cx, aJSVal) ###
  
Wraps the given jsval in a nsIVariant and returns the new variant.  
  

### getWrappedNativeOfJSObject(aJSContext, aJSObj) ###
  
This only succeeds if the JSObject is a nsIXPConnectWrappedNative.  
A new wrapper is *never* constructed.  
  

### getNativeOfWrapper(aJSContext, aJSObj) ###

### createStackFrameLocation(aLanguage, aFilename, aFunctionName, aLineNumber, aCaller) ###

### getCurrentJSContext() ###

### getSafeJSContext() ###

### debugDump(depth) ###

### debugDumpObject(aCOMObj, depth) ###

### debugDumpJSStack(showArgs, showLocals, showThisProps) ###

### wrapJSAggregatedToNative(aOuter, aJSContext, aJSObj, aIID, result) ###
  
wrapJSAggregatedToNative is just like wrapJS except it is used in cases  
where the JSObject is also aggregated to some native xpcom Object.  
At present XBL is the only system that might want to do this.  
  
XXX write more!  
  
Returns:  
  success:  
    NS_OK  
   failure:  
      NS_ERROR_XPC_BAD_CONVERT_JS  
      NS_ERROR_FAILURE  
  

### getWrappedNativeOfNativeObject(aJSContext, aScope, aCOMObj, aIID) ###
  
This only succeeds if the native object is already wrapped by xpconnect.  
A new wrapper is *never* constructed.  
  

### setFunctionThisTranslator(aIID, aTranslator) ###

### reparentWrappedNativeIfFound(aJSContext, aScope, aNewParent, aCOMObj) ###

### rescueOrphansInScope(aJSContext, aScope) ###

### getWrappedNativePrototype(aJSContext, aScope, aClassInfo) ###

### variantToJS(ctx, scope, value) ###

### JSToVariant(ctx, value) ###

### createSandbox(cx, principal) ###
  
Create a sandbox for evaluating code in isolation using  
evalInSandboxObject().  
  
@param cx A context to use when creating the sandbox object.  
@param principal The principal (or NULL to use the null principal)  
                 to use when evaluating code in this sandbox.  
  

#### Parameters ####

<table>

<tr>
<td>cx</td>
<td>A context to use when creating the sandbox object.  
</td>
</tr>

<tr>
<td>principal</td>
<td>The principal (or NULL to use the null principal)  
                 to use when evaluating code in this sandbox.  
</td>
</tr>

</table>

### evalInSandboxObject(source, filename, cx, sandbox) ###
  
Evaluate script in a sandbox, completely isolated from all  
other running scripts.  
  
@param source The source of the script to evaluate.  
@param filename The filename of the script. May be null.  
@param cx The context to use when setting up the evaluation of  
          the script. The actual evaluation will happen on a new  
          temporary context.  
@param sandbox The sandbox object to evaluate the script in.  
@return The result of the evaluation as a jsval. If the caller  
        intends to use the return value from this call the caller  
        is responsible for rooting the jsval before making a call  
        to this method.  
  

#### Parameters ####

<table>

<tr>
<td>source</td>
<td>The source of the script to evaluate.  
</td>
</tr>

<tr>
<td>filename</td>
<td>The filename of the script. May be null.  
</td>
</tr>

<tr>
<td>cx</td>
<td>The context to use when setting up the evaluation of  
          the script. The actual evaluation will happen on a new  
          temporary context.  
</td>
</tr>

<tr>
<td>sandbox</td>
<td>The sandbox object to evaluate the script in.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The result of the evaluation as a jsval. If the caller  
        intends to use the return value from this call the caller  
        is responsible for rooting the jsval before making a call  
        to this method.  
</td>
</tr>

</table>

### setReportAllJSExceptions(reportAllJSExceptions) ###
  
Whether or not XPConnect should report all JS exceptions when returning  
from JS into C++. False by default, although any value set in the  
MOZ_REPORT_ALL_JS_EXCEPTIONS environment variable will override the value  
passed here.  
  

### GarbageCollect(reason) ###
  
Trigger a JS garbage collection.  
Use a js::gcreason::Reason from jsfriendapi.h for the kind.  
  

### NotifyDidPaint() ###
  
Signals a good place to do an incremental GC slice, because the  
browser is drawing a frame.  
  

### holdObject(aJSContext, aObject) ###
  
Creates a JS object holder around aObject that will hold the object  
alive for as long as the holder stays alive.  
  

### writeScript(aStream, aJSContext, aJSScript) ###

### readScript(aStream, aJSContext) ###

### writeFunction(aStream, aJSContext, aJSObject) ###

### readFunction(aStream, aJSContext) ###

## Attributes ##

### CurrentJSStack ###

### CurrentNativeCallContext ###

## Constants ##

### INIT_JS_STANDARD_CLASSES ###

### DONT_FIRE_ONNEWGLOBALHOOK ###

### OMIT_COMPONENTS_OBJECT ###
