---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIPrintSettingsWin.idl">Source file</a>
</div>

# nsIPrintSettingsWin #
  
Simplified PrintSettings for Windows interface   
  

## Attributes ##

### deviceName ###
  
Data Members  
  
Each of these data members make a copy   
of the contents. If you get the value,   
you own the memory.  
  
The following three pieces of data are needed  
to create a DC for printing. These are typcially   
gotten via the PrintDLG call ro can be obtained  
via the "m_pd" data member of the CPrintDialog  
in MFC.  
  

### driverName ###

### devMode ###
