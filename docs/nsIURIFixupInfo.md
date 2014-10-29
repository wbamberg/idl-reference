---
layout: default
---

# nsIURIFixupInfo #

Interface indicating what we found/corrected when fixing up a URI


## Attributes ##

### consumer ###

Consumer that asked for fixed up URI.


### preferredURI ###

Our best guess as to what URI the consumer will want. Might
be null if we couldn't salvage anything (for instance, because
the input was invalid as a URI and FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP
was not passed)


### fixedURI ###

The fixed-up original input, *never* using a keyword search.
(might be null if the original input was not recoverable as
a URL, e.g. "foo bar"!)


### keywordProviderName ###

The name of the keyword search provider used to provide a keyword search;
empty string if no keyword search was done.


### keywordAsSent ###

The keyword as used for the search (post trimming etc.)
empty string if no keyword search was done.


### fixupChangedProtocol ###

Whether we changed the protocol instead of using one from the input as-is.


### fixupCreatedAlternateURI ###

Whether we created an alternative URI. We might have added a prefix and/or
suffix, the contents of which are controlled by the
browser.fixup.alternate.prefix and .suffix prefs, with the defaults being
"www." and ".com", respectively.


### originalInput ###

The original input

