---
layout: default
---

# nsIWebVTTListener #

Listener for a JS WebVTT parser (vtt.js).


## Methods ##

### onCue ###

Is called when the WebVTTParser successfully parses a WebVTT cue.

@param cue An object representing the data of a parsed WebVTT cue.


### onRegion ###

Is called when the WebVTT parser successfully parses a WebVTT region.

@param region An object representing the data of a parsed
              WebVTT region.


### onParsingError ###

Is called when the WebVTT parser encounters a parsing error.

@param error The error code of the ParserError the occured.

