---
layout: default
---

# nsIXSLTProcessorPrivate #

## Attributes ##

### flags ###

Flags for this processor. Defaults to 0. See individual flags above
for documentation for effect of reset()


## Constants ##

### DISABLE_ALL_LOADS ###

Disables all loading of external documents, such as from
<xsl:import> and document()
Defaults to off and is *not* reset by calls to reset()

