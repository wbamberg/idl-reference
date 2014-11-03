---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/shistory/public/nsISHTransaction.idl">Source file</a>
</div>

# nsISHTransaction #
<pre>  
The nsISHTransaction.  
  
</pre>
## Methods ##

### create(aSHEntry, aPrev) ###
<pre>  
Create a transaction with parent and History Entry   
  
</pre>
## Attributes ##

### sHEntry ###
<pre>  
The nsISHEntry for the current transaction  
  
</pre>
### prev ###
<pre>  
The parent of this transaction  
  
</pre>
### next ###
<pre>  
The legitimate child of this transaction   
  
</pre>
### persist ###
<pre>  
Specifies if this transaction should persist.  If not it will be replaced  
by new additions to the list.  
  
</pre>