---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/activities/interfaces/nsIActivityUIGlue.idl">Source file</a>
</div>
# nsIActivityUIGlue #
  
To be implemented by @mozilla.org/dom/activities/ui-glue;1  
  

## Methods ##

### chooseActivity(options, activities, callback) ###
  
This method is called even if the size of {@code activities} is 0 so that the callee can  
decide whether or not to defer the request to an alternate activity system.  
  
@param options     The ActivityOptions object in the form of { name: "send", data: { ... } }  
@param activities  A json blob which is an array of { "title":"...", "icon":"..." }.  
@param callback    The callback to send the index of the choosen activity, or the result.  
  

#### Parameters ####

<table>

<tr>
<td>options</td>
<td>The ActivityOptions object in the form of { name: "send", data: { ... } }  
</td>
</tr>

<tr>
<td>activities</td>
<td>A json blob which is an array of { "title":"...", "icon":"..." }.  
</td>
</tr>

<tr>
<td>callback</td>
<td>The callback to send the index of the choosen activity, or the result.  
</td>
</tr>

</table>
