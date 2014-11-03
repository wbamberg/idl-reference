---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/threads/nsISupportsPriority.idl">Source file</a>
</div>

# nsISupportsPriority #
<code>  
This interface exposes the general notion of a scheduled object with a  
integral priority value.  Following UNIX conventions, smaller (and possibly  
negative) values have higher priority.  
  
This interface does not strictly define what happens when the priority of an  
object is changed.  An implementation of this interface is free to define  
the side-effects of changing the priority of an object.  In some cases,  
changing the priority of an object may be disallowed (resulting in an  
exception being thrown) or may simply be ignored.  
  
</code>
## Methods ##

### adjustPriority(delta) ###
<code>  
This method adjusts the priority attribute by a given delta.  It helps  
reduce the amount of coding required to increment or decrement the value  
of the priority attribute.  
  
</code>
## Attributes ##

### priority ###
  
This attribute may be modified to change the priority of this object.  The  
implementation of this interface is free to truncate a given priority  
value to whatever limits are appropriate.  Typically, this attribute is  
initialized to PRIORITY_NORMAL, but implementations may choose to assign a  
different initial value.  
  

## Constants ##

### PRIORITY_HIGHEST ###
  
Typical priority values.  
  

### PRIORITY_HIGH ###

### PRIORITY_NORMAL ###

### PRIORITY_LOW ###

### PRIORITY_LOWEST ###
