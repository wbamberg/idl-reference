---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/docshell/shistory/public/nsISHTransaction.idl">Source file</a>
</div>

# nsISHTransaction #
  
The nsISHTransaction.  
  

## Methods ##

### create(aSHEntry, aPrev) ###
  
Create a transaction with parent and History Entry   
  

## Attributes ##

### sHEntry ###
  
The nsISHEntry for the current transaction  
  

### prev ###
  
The parent of this transaction  
  

### next ###
  
The legitimate child of this transaction   
  

### persist ###
  
Specifies if this transaction should persist.  If not it will be replaced  
by new additions to the list.  
  
