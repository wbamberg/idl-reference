---
layout: default
---

# nsIObjectLoadingContent #

This interface represents a content node that loads objects.

Please make sure to update the MozObjectLoadingContent WebIDL
interface to mirror this interface when changing it.


## Methods ##

### getContentTypeForMIMEType ###

Gets the content type that corresponds to the give MIME type.  See the
constants above for the list of possible values.  If nothing else fits,
TYPE_NULL will be returned.


### hasNewFrame ###

Tells the content about an associated object frame.
This can be called multiple times for different frames.

This is noscript because this is an internal method that will go away, and
because nsIObjectFrame is unscriptable.


### getPrintFrame ###

If this object is in going to be printed, this method
returns the nsIObjectFrame object which should be used when
printing the plugin. The returned nsIFrame is in the original document,
not in the static clone.


### pluginDestroyed ###

### pluginCrashed ###

### playPlugin ###

This method will play a plugin that has been stopped by the
click-to-play plugins or play-preview features.


### reload ###

Forces a re-evaluation and reload of the tag, optionally invalidating its
click-to-play state.  This can be used when the MIME type that provides a
type has changed, for instance, to force the tag to re-evalulate the
handler to use.


### stopPluginInstance ###

### syncStartPluginInstance ###

### asyncStartPluginInstance ###

### initializeFromChannel ###

Puts the tag in the "waiting on a channel" state and adopts this
channel. This does not override the normal logic of examining attributes
and the channel type, so the load may cancel this channel if it decides not
to use one.

This assumes:
 - This tag has not begun loading yet
 - This channel has not yet hit OnStartRequest
 - The caller will continue to pass channel events to us as a listener


### cancelPlayPreview ###

This method will disable the play-preview plugin state.


## Attributes ##

### actualType ###

The actual mime type (the one we got back from the network
request) for the element.


### displayedType ###

Gets the type of the content that's currently loaded. See
the constants above for the list of possible values.


### baseURI ###

Returns the base URI of the object as seen by plugins. This differs from
the normal codebase in that it takes <param> tags and plugin-specific
quirks into account.


### pluginInstance ###

Returns the plugin instance if it has already been instantiated. This
will never instantiate the plugin and so is safe to call even when
content script must not execute.


### activated ###

This attribute will return true if the current content type has been
activated, either explicitly or by passing checks that would have it be
click-to-play or play-preview.


### srcURI ###

The URL of the data/src loaded in the object. This may be null (i.e.
an <embed> with no src).


### pluginFallbackType ###

The plugin's current state of fallback content. This property
only makes sense if the plugin is not activated.


### hasRunningPlugin ###

If this object currently owns a running plugin, regardless of whether or
not one is pending spawn/despawn.


## Constants ##

### TYPE_LOADING ###

See notes in nsObjectLoadingContent.h


### TYPE_IMAGE ###

### TYPE_PLUGIN ###

### TYPE_DOCUMENT ###

### TYPE_NULL ###

### PLUGIN_ACTIVE ###

### PLUGIN_UNSUPPORTED ###

### PLUGIN_ALTERNATE ###

### PLUGIN_DISABLED ###

### PLUGIN_BLOCKLISTED ###

### PLUGIN_OUTDATED ###

### PLUGIN_CRASHED ###

### PLUGIN_SUPPRESSED ###

### PLUGIN_USER_DISABLED ###

### PLUGIN_CLICK_TO_PLAY ###

### PLUGIN_VULNERABLE_UPDATABLE ###

### PLUGIN_VULNERABLE_NO_UPDATE ###

### PLUGIN_PLAY_PREVIEW ###
