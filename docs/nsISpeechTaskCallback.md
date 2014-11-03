---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/media/webspeech/synth/nsISpeechService.idl">Source file</a>
</div>

# nsISpeechTaskCallback #
<code>  
A callback is implemented by the service. For direct audio services, it is  
required to implement these, although it could be helpful to use the  
cancel method for shutting down the speech resources.  
  
</code>
## Methods ##

### onPause() ###
<code>  
The user or application has paused the speech.  
  
</code>
### onResume() ###
<code>  
The user or application has resumed the speech.  
  
</code>
### onCancel() ###
<code>  
The user or application has canceled the speech.  
  
</code>