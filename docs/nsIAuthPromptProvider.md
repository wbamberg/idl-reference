---
layout: default
---

# nsIAuthPromptProvider #

## Methods ##

### getAuthPrompt ###

Request a prompt interface for the given prompt reason;
@throws NS_ERROR_NOT_AVAILABLE if no prompt is allowed or
available for the given reason.

@param aPromptReason   The reason for the auth prompt;
                       one of #PROMPT_NORMAL or #PROMPT_PROXY
@param iid             The desired interface, e.g.
                       NS_GET_IID(nsIAuthPrompt2).
@returns an nsIAuthPrompt2 interface, or throws NS_ERROR_NOT_AVAILABLE


## Constants ##

### PROMPT_NORMAL ###

Normal (non-proxy) prompt request.


### PROMPT_PROXY ###

Proxy auth request.

