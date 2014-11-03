---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/tools/profiler/nsIProfiler.idl">Source file</a>
</div>

# nsIProfiler #

## Methods ##

### StartProfiler(aEntries, aInterval, aFeatures, aFeatureCount, aThreadNameFilters, aFilterCount) ###

### StopProfiler() ###

### IsPaused() ###

### PauseSampling() ###

### ResumeSampling() ###

### AddMarker(aMarker) ###

### GetProfile() ###

### getProfileData() ###

### IsActive() ###

### GetFeatures(aCount, aFeatures) ###

### getSharedLibraryInformation() ###
<code>  
Returns a JSON string of an array of shared library objects.  
Every object has three properties: start, end, and name.  
start and end are integers describing the address range that the library  
occupies in memory. name is the path of the library as a string.  
  
On Windows profiling builds, the shared library objects will have  
additional pdbSignature and pdbAge properties for uniquely identifying  
shared library versions for stack symbolication.  
  
</code>