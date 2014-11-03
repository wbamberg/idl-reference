---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/js/xpconnect/idl/xpccomponents.idl">Source file</a>
</div>

# nsIXPCComponents_Utils #
<code>  
interface of Components.utils  
  
</code>
## Methods ##

### reportError(error) ###

### evalInSandbox(source, sandbox, version, filename, lineNo) ###

### getSandboxAddonId(sandbox) ###

### getSandboxMetadata(sandbox) ###

### setSandboxMetadata(sandbox, metadata) ###

### import(aResourceURI, targetObj) ###

### isModuleLoaded(aResourceURI) ###
<code>  
Returns true if the js file located at 'registryLocation' location has  
been loaded previously via the import method above. Returns false  
otherwise.  
  
@param resourceURI A resource:// URI string representing the location of  
       the js file to be checked if it is already loaded or not.  
@returns boolean, true if the js file has been loaded via import. false  
         otherwise  
  
</code>
#### Parameters ####

<table>

<tr>
<td>resourceURI</td>
<td>A resource:// URI string representing the location of  
       the js file to be checked if it is already loaded or not.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>boolean, true if the js file has been loaded via import. false  
         otherwise  
</td>
</tr>

</table>

### unload(registryLocation) ###

### importGlobalProperties(aPropertyList) ###

### getWeakReference(obj) ###

### forceGC() ###

### forceCC() ###

### finishCC() ###

### ccSlice(budget) ###

### getMaxCCSliceTimeSinceClear() ###

### clearMaxCCTime() ###

### forceShrinkingGC() ###

### schedulePreciseGC(callback) ###

### schedulePreciseShrinkingGC(callback) ###

### unlinkGhostWindows() ###

### nondeterministicGetWeakMapKeys(aMap) ###
<code>  
Return the keys in a weak map.  This operation is  
non-deterministic because it is affected by the scheduling of the  
garbage collector and the cycle collector.  
  
This should only be used to write tests of the interaction of  
the GC and CC with weak maps.  
  
@param aMap weak map or other JavaScript value  
@returns If aMap is a weak map object, return the keys of the weak  
map as an array.  Otherwise, return undefined.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aMap</td>
<td>weak map or other JavaScript value  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>If aMap is a weak map object, return the keys of the weak  
map as an array.  Otherwise, return undefined.  
</td>
</tr>

</table>

### getJSTestingFunctions() ###

### getGlobalForObject(obj) ###

### isProxy(vobject) ###

### exportFunction(vfunction, vscope, voptions) ###

### createObjectIn(vobj, voptions) ###

### makeObjectPropsNormal(vobj) ###

### isDeadWrapper(obj) ###
<code>  
Determines whether this object is backed by a DeadObjectProxy.  
  
Dead-wrapper objects hold no other objects alive (they have no outgoing  
reference edges) and will throw if you touch them (e.g. by  
reading/writing a property).  
  
</code>
### isCrossProcessWrapper(obj) ###
<code>  
Determines whether this object is a cross-process wrapper.  
  
</code>
### recomputeWrappers(vobj) ###

### setWantXrays(vscope) ###

### forcePermissiveCOWs() ###

### skipCOWCallableChecks() ###

### forcePrivilegedComponentsForScope(vscope) ###

### getComponentsForScope(vscope) ###

### dispatch(runnable, scope) ###

### setGCZeal(zeal) ###

### nukeSandbox(obj) ###

### blockScriptForGlobal(global) ###

### unblockScriptForGlobal(global) ###

### isXrayWrapper(obj) ###
<code>  
Check whether the given object is an XrayWrapper.  
  
</code>
### waiveXrays(aVal) ###
<code>  
Waive Xray on a given value. Identity op for primitives.  
  
</code>
### unwaiveXrays(aVal) ###
<code>  
Strip off Xray waivers on a given value. Identity op for primitives.  
  
</code>
### getClassName(aObj, aUnwrap) ###
<code>  
Gets the name of the JSClass of the object.  
  
if |aUnwrap| is true, all wrappers are unwrapped first. Unless you're  
specifically trying to detect whether the object is a proxy, this is  
probably what you want.  
  
</code>
### getDOMClassInfo(aClassName) ###
<code>  
Get a DOM classinfo for the given classname.  Only some class  
names are supported.  
  
</code>
### getIncumbentGlobal(callback) ###
<code>  
Gets the incument global for the execution of this function. For internal  
and testing use only.  
  
If |callback| is passed, it is invoked with the incumbent global as its  
sole argument. This allows the incumbent global to be measured in callback  
environments with no scripted frames on the stack.  
  
</code>
### generateXPCWrappedJS(obj, scope) ###
<code>  
Forces the generation of an XPCWrappedJS for a given object. For internal  
and testing use only. This is only useful to set up wrapper map conditions  
for a testcase. The return value is not an XPCWrappedJS itself, but an  
opaque nsISupports holder that keeps the underlying XPCWrappedJS alive.  
  
if |scope| is passed, the XPCWrappedJS is generated in the scope of that object.  
  
</code>
### getWatchdogTimestamp(aCategory) ###
<code>  
Retrieve the last time, in microseconds since epoch, that a given  
watchdog-related event occured.  
  
Valid categories:  
  "RuntimeStateChange"      - Runtime switching between active and inactive states  
  "WatchdogWakeup"          - Watchdog waking up from sleeping  
  "WatchdogHibernateStart"  - Watchdog begins hibernating  
  "WatchdogHibernateStop"   - Watchdog stops hibernating  
  
</code>
### getJSEngineTelemetryValue() ###

### cloneInto(value, scope, options) ###

### getWebIDLCallerPrincipal() ###

### getObjectPrincipal(obj) ###

### getCompartmentLocation(obj) ###

### setAddonInterposition(addonId, interposition) ###

### now() ###

## Attributes ##

### Sandbox ###

### strict ###

### werror ###

### strict_mode ###

### ion ###
