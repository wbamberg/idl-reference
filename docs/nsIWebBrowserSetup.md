---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/browser/nsIWebBrowserSetup.idl">Source file</a>
</div>

# nsIWebBrowserSetup #
<pre>  
The nsIWebBrowserSetup interface lets you set properties on a browser  
object; you can do so at any time during the life cycle of the browser.  
  
@note Unless stated otherwise, settings are presumed to be enabled by  
      default.  
  
</pre>
## Methods ##

### setProperty(aId, aValue) ###
<pre>  
Sets an integer or boolean property on the new web browser object.  
Only PR_TRUE and PR_FALSE are legal boolean values.  
  
@param aId The identifier of the property to be set.  
@param aValue The value of the property.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aId</td>
<td>The identifier of the property to be set.  
</td>
</tr>

<tr>
<td>aValue</td>
<td>The value of the property.  
</td>
</tr>

</table>

## Constants ##

### SETUP_ALLOW_PLUGINS ###
<pre>  
Boolean. Enables/disables plugin support for this browser.  
  
@see setProperty  
  
</pre>
### SETUP_ALLOW_JAVASCRIPT ###
<pre>  
Boolean. Enables/disables Javascript support for this browser.  
  
@see setProperty  
  
</pre>
### SETUP_ALLOW_META_REDIRECTS ###
<pre>  
Boolean. Enables/disables meta redirect support for this browser.  
Meta redirect timers will be ignored if this option is disabled.  
  
@see setProperty  
  
</pre>
### SETUP_ALLOW_SUBFRAMES ###
<pre>  
Boolean. Enables/disables subframes within the browser  
  
@see setProperty  
  
</pre>
### SETUP_ALLOW_IMAGES ###
<pre>  
Boolean. Enables/disables image loading for this browser  
window. If you disable the images, load a page, then enable the images,  
the page will *not* automatically load the images for the previously  
loaded page. This flag controls the state of a webBrowser at load time   
and does not automatically re-load a page when the state is toggled.   
Reloading must be done by hand, or by walking through the DOM tree and   
re-setting the src attributes.  
  
@see setProperty  
  
</pre>
### SETUP_FOCUS_DOC_BEFORE_CONTENT ###
<pre>  
Boolean. Enables/disables whether the document as a whole gets focus before  
traversing the document's content, or after traversing its content.  
  
NOTE: this property is obsolete and now has no effect  
  
@see setProperty  
  
</pre>
### SETUP_USE_GLOBAL_HISTORY ###
<pre>  
Boolean. Enables/disables the use of global history in the browser. Visited  
URLs will not be recorded in the global history when it is disabled.  
  
@see setProperty  
  
</pre>
### SETUP_IS_CHROME_WRAPPER ###
<pre>  
Boolean. A value of PR_TRUE makes the browser a chrome wrapper.  
Default is PR_FALSE.  
  
@since mozilla1.0  
  
@see setProperty  
  
</pre>
### SETUP_ALLOW_DNS_PREFETCH ###
<pre>  
Boolean. Enables/disables DNS prefetch for HTML anchors in this browser.  
This takes effect starting with the next pageload after the property is  
set.  The default is to not allow DNS prefetch, for backwards  
compatibility.  
  
@see setProperty  
  
</pre>