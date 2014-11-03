---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIMacDockSupport.idl">Source file</a>
</div>

# nsIMacDockSupport #
<pre>  
Allow applications to interface with the Mac OS X Dock.  
  
Applications may indicate progress on their Dock icon. Only one such  
progress indicator is available to the entire application.  
  
</pre>
## Methods ##

### activateApplication(aIgnoreOtherApplications) ###
<pre>  
Activate the application. This should be used by an application to  
activate itself when a dock menu is selected as selection of a dock menu  
item does not automatically activate the application.  
  
@param aIgnoreOtherApplications If false, the application is activated  
       only if no other application is currently active. If true, the  
       application activates regardless.   
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aIgnoreOtherApplications</td>
<td>If false, the application is activated  
       only if no other application is currently active. If true, the  
       application activates regardless.   
</td>
</tr>

</table>

## Attributes ##

### dockMenu ###
<pre>  
Menu to use for application-specific dock menu items.  
  
</pre>
### badgeText ###
<pre>  
Text used to badge the dock tile.  
  
</pre>