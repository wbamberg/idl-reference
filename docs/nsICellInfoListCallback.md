---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/mobileconnection/interfaces/nsICellInfo.idl">Source file</a>
</div>

# nsICellInfoListCallback #

## Methods ##

### notifyGetCellInfoList(count, result) ###
  
result is an array of nsICellInfo, which could be instances of  
nsIGsmCellInfo, nsIWcdmaCellInfo, nsICdmaCellInfo or nsILteCellInfo.  
  

### notifyGetCellInfoListFailed(error) ###
  
Callback function with error message.  
  
