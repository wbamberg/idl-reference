---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/system/nsIXULRuntime.idl">Source file</a>
</div>

# nsIXULRuntime #
  
Provides information about the XUL runtime.  
@status UNSTABLE - This interface is not frozen and will probably change in  
                   future releases. If you need this functionality to be  
                   stable/frozen, please contact Benjamin Smedberg.  
  

## Methods ##

### invalidateCachesOnRestart() ###
  
Signal the apprunner to invalidate caches on the next restart.  
This will cause components to be autoregistered and all  
fastload data to be re-created.  
  

### ensureContentProcess() ###
  
Starts a child process. This method is intented to pre-start a  
content child process so that when it is actually needed, it is  
ready to go.  
  
@throw NS_ERROR_NOT_AVAILABLE if not available.  
  

## Attributes ##

### inSafeMode ###
  
Whether the application was launched in safe mode.  
  

### logConsoleErrors ###
  
Whether to write console errors to a log file. If a component  
encounters startup errors that might prevent the app from showing  
proper UI, it should set this flag to "true".  
  

### OS ###
  
A string tag identifying the current operating system. This is taken  
from the OS_TARGET configure variable. It will always be available.  
  

### XPCOMABI ###
  
A string tag identifying the binary ABI of the current processor and  
compiler vtable. This is taken from the TARGET_XPCOM_ABI configure  
variable. It may not be available on all platforms, especially  
unusual processor or compiler combinations.  
  
The result takes the form <processor>-<compilerABI>, for example:  
  x86-msvc  
  ppc-gcc3  
  
This value should almost always be used in combination with "OS".  
  
@throw NS_ERROR_NOT_AVAILABLE if not available.  
  

### widgetToolkit ###
  
A string tag identifying the target widget toolkit in use.  
This is taken from the MOZ_WIDGET_TOOLKIT configure variable.  
  

### processType ###
  
The type of the caller's process.  Returns one of the values above.  
  

### processID ###
  
The system process ID of the caller's process.  
  

### browserTabsRemoteAutostart ###
  
If true, browser tabs may be opened by default in a different process  
from the main browser UI.  
  

### accessibilityEnabled ###
  
If true, the accessibility service is running.  
  

### keyboardMayHaveIME ###
  
This returns a very rough approximation of whether IME is likely  
to be used for the browser session. DO NOT USE! This is temporary  
and will be removed.  
  

### replacedLockTime ###
  
Modification time of the profile lock before the profile was locked on  
this startup. Used to know the last time the profile was used and not  
closed cleanly. This is set to 0 if there was no existing profile lock.  
  

### lastRunCrashID ###
  
Local ID of the minidump generated when the process crashed  
on the previous run. Can be passed directly to CrashSubmit.submit.  
  

### isReleaseBuild ###
  
True if this is a RELEASE_BUILD.  
  

### isOfficialBranding ###
  
True if this build uses official branding (MOZ_OFFICIAL_BRANDING).  
  

### defaultUpdateChannel ###
  
The default update channel (MOZ_UPDATE_CHANNEL).  
  

### distributionID ###
  
The distribution ID for this build (MOZ_DISTRIBUTION_ID).  
  

### isOfficial ###
  
True if this is an official build (MOZILLA_OFFICIAL).  
  

## Constants ##

### PROCESS_TYPE_DEFAULT ###
  
The legal values of processType.  
  

### PROCESS_TYPE_PLUGIN ###

### PROCESS_TYPE_CONTENT ###

### PROCESS_TYPE_IPDLUNITTEST ###

### PROCESS_TYPE_GMPLUGIN ###
