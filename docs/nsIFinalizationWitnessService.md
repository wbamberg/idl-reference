---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/finalizationwitness/nsIFinalizationWitnessService.idl">Source file</a>
</div>

# nsIFinalizationWitnessService #

## Methods ##

### make(aTopic, aString) ###
  
Create a new Finalization Witness.  
  
A finalization witness is an object whose sole role is to  
broadcast when it is garbage-collected. Once the witness is  
created, call method its method |forget()| to prevent the  
broadcast.  
  
  

#### Parameters ####

<table>

<tr>
<td>aTopic</td>
<td>The topic that the witness will broadcast using  
              Services.obs.  
</td>
</tr>

<tr>
<td>aString</td>
<td>The string that the witness will broadcast.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>An object with a single method |forget()|.  
</td>
</tr>

</table>
