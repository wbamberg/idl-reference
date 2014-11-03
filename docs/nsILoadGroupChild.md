---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsILoadGroupChild.idl">Source file</a>
</div>

# nsILoadGroupChild #
  
nsILoadGroupChild provides a hierarchy of load groups so that the  
root load group can be used to conceptually tie a series of loading  
operations into a logical whole while still leaving them separate  
for the purposes of cancellation and status events.  
  

## Attributes ##

### parentLoadGroup ###
  
The parent of this load group. It is stored with  
a nsIWeakReference/nsWeakPtr so there is no requirement for the  
parentLoadGroup to out live the child, nor will the child keep a  
reference count on the parent.  
  

### childLoadGroup ###
  
The nsILoadGroup associated with this nsILoadGroupChild  
  

### rootLoadGroup ###
  
The rootLoadGroup is the recursive parent of this  
load group where parent is defined as parentlLoadGroup if set  
or childLoadGroup.loadGroup as a backup. (i.e. parentLoadGroup takes  
precedence.) The nsILoadGroup child is the root if neither parent  
nor loadgroup attribute is specified.  
  
