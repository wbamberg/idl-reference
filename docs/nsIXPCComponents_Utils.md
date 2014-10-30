---
layout: default
---

# nsIXPCComponents_Utils #
  
interface of Components.utils  
  

## Methods ##

### reportError ###

### evalInSandbox ###

### getSandboxAddonId ###

### getSandboxMetadata ###

### setSandboxMetadata ###

### import ###

### isModuleLoaded ###
  
Returns true if the js file located at 'registryLocation' location has  
been loaded previously via the import method above. Returns false  
otherwise.  
  
@param resourceURI A resource:// URI string representing the location of  
       the js file to be checked if it is already loaded or not.  
@returns boolean, true if the js file has been loaded via import. false  
         otherwise  
  

### unload ###

### importGlobalProperties ###

### getWeakReference ###

### forceGC ###

### forceCC ###

### finishCC ###

### ccSlice ###

### getMaxCCSliceTimeSinceClear ###

### clearMaxCCTime ###

### forceShrinkingGC ###

### schedulePreciseGC ###

### schedulePreciseShrinkingGC ###

### unlinkGhostWindows ###

### nondeterministicGetWeakMapKeys ###
  
Return the keys in a weak map.  This operation is  
non-deterministic because it is affected by the scheduling of the  
garbage collector and the cycle collector.  
  
This should only be used to write tests of the interaction of  
the GC and CC with weak maps.  
  
@param aMap weak map or other JavaScript value  
@returns If aMap is a weak map object, return the keys of the weak  
map as an array.  Otherwise, return undefined.  
  

### getJSTestingFunctions ###

### getGlobalForObject ###

### isProxy ###

### exportFunction ###

### createObjectIn ###

### makeObjectPropsNormal ###

### isDeadWrapper ###
  
Determines whether this object is backed by a DeadObjectProxy.  
  
Dead-wrapper objects hold no other objects alive (they have no outgoing  
reference edges) and will throw if you touch them (e.g. by  
reading/writing a property).  
  

### isCrossProcessWrapper ###
  
Determines whether this object is a cross-process wrapper.  
  

### recomputeWrappers ###

### setWantXrays ###

### forcePermissiveCOWs ###

### skipCOWCallableChecks ###

### forcePrivilegedComponentsForScope ###

### getComponentsForScope ###

### dispatch ###

### setGCZeal ###

### nukeSandbox ###

### blockScriptForGlobal ###

### unblockScriptForGlobal ###

### isXrayWrapper ###
  
Check whether the given object is an XrayWrapper.  
  

### waiveXrays ###
  
Waive Xray on a given value. Identity op for primitives.  
  

### unwaiveXrays ###
  
Strip off Xray waivers on a given value. Identity op for primitives.  
  

### getClassName ###
  
Gets the name of the JSClass of the object.  
  
if |aUnwrap| is true, all wrappers are unwrapped first. Unless you're  
specifically trying to detect whether the object is a proxy, this is  
probably what you want.  
  

### getDOMClassInfo ###
  
Get a DOM classinfo for the given classname.  Only some class  
names are supported.  
  

### getIncumbentGlobal ###
  
Gets the incument global for the execution of this function. For internal  
and testing use only.  
  
If |callback| is passed, it is invoked with the incumbent global as its  
sole argument. This allows the incumbent global to be measured in callback  
environments with no scripted frames on the stack.  
  

### generateXPCWrappedJS ###
  
Forces the generation of an XPCWrappedJS for a given object. For internal  
and testing use only. This is only useful to set up wrapper map conditions  
for a testcase. The return value is not an XPCWrappedJS itself, but an  
opaque nsISupports holder that keeps the underlying XPCWrappedJS alive.  
  
if |scope| is passed, the XPCWrappedJS is generated in the scope of that object.  
  

### getWatchdogTimestamp ###
  
Retrieve the last time, in microseconds since epoch, that a given  
watchdog-related event occured.  
  
Valid categories:  
  "RuntimeStateChange"      - Runtime switching between active and inactive states  
  "WatchdogWakeup"          - Watchdog waking up from sleeping  
  "WatchdogHibernateStart"  - Watchdog begins hibernating  
  "WatchdogHibernateStop"   - Watchdog stops hibernating  
  

### getJSEngineTelemetryValue ###

### cloneInto ###

### getWebIDLCallerPrincipal ###

### getObjectPrincipal ###

### getCompartmentLocation ###

### setAddonInterposition ###

### now ###

## Attributes ##

### Sandbox ###

### strict ###

### werror ###

### strict_mode ###

### ion ###
