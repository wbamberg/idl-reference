---
layout: default
---

# nsIProfiler #

## Methods ##

### StartProfiler ###

### StopProfiler ###

### IsPaused ###

### PauseSampling ###

### ResumeSampling ###

### AddMarker ###

### GetProfile ###

### getProfileData ###

### IsActive ###

### GetFeatures ###

### getSharedLibraryInformation ###
  
Returns a JSON string of an array of shared library objects.  
Every object has three properties: start, end, and name.  
start and end are integers describing the address range that the library  
occupies in memory. name is the path of the library as a string.  
  
On Windows profiling builds, the shared library objects will have  
additional pdbSignature and pdbAge properties for uniquely identifying  
shared library versions for stack symbolication.  
  
