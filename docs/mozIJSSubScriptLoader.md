---
layout: default
---

# mozIJSSubScriptLoader #

## Methods ##

### loadSubScript ###

This method should only be called from JS!
In JS, the signature looks like:
rv loadSubScript (url [, obj] [, charset]);
@param url the url of the sub-script, it MUST be either a file:,
           resource:, or chrome: url, and MUST be local.
@param obj an optional object to evaluate the script onto, it
           defaults to the global object of the caller.
@param charset optionally specifies the character encoding of
               the file. If absent, the file is interpreted
               as ASCII.
@retval rv the value returned by the sub-script


### loadSubScriptWithOptions ###

This method should only be called from JS!
In JS, the signature looks like:
rv = loadSubScript (url, optionsObject)
@param url the url of the sub-script, it MUST be either a file:,
           resource:, or chrome: url, and MUST be local.
@param optionsObject an object with parameters. Valid parameters are:
                     - charset: specifying the character encoding of the file (default: ASCII)
                     - target:  an object to evaluate onto (default: global object of the caller)
                     - ignoreCache: if set to true, will bypass the cache for reading the file.
@retval rv the value returned by the sub-script


### precompileScript ###
