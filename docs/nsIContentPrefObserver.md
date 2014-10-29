---
layout: default
---

# nsIContentPrefObserver #

## Methods ##

### onContentPrefSet ###

Called when a content pref is set to a different value.

@param    aGroup      the group to which the pref belongs, or null
                      if it's a global pref (applies to all sites)
@param    aName       the name of the pref that was set
@param    aValue      the new value of the pref


### onContentPrefRemoved ###

Called when a content pref is removed.

@param    aGroup      the group to which the pref belongs, or null
                      if it's a global pref (applies to all sites)
@param    aName       the name of the pref that was removed

