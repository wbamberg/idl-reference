---
layout: default
---

# nsIScriptLoaderObserver #

## scriptAvailable ##

The script is available for evaluation. For inline scripts, this
method will be called synchronously. For externally loaded scripts,
this method will be called when the load completes.

@param aResult A result code representing the result of loading
       a script. If this is a failure code, script evaluation
       will not occur.
@param aElement The element being processed.
@param aIsInline Is this an inline script or externally loaded?
@param aURI What is the URI of the script (the document URI if
       it is inline).
@param aLineNo At what line does the script appear (generally 1
       if it is a loaded script).


## scriptEvaluated ##

The script has been evaluated.

@param aResult A result code representing the success or failure of
       the script evaluation.
@param aElement The element being processed.
@param aIsInline Is this an inline script or externally loaded?

