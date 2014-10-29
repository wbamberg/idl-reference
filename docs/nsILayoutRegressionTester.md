---
layout: default
---

# nsILayoutRegressionTester #

## Methods ##

### dumpFrameModel ###

### compareFrameModels ###

## Constants ##

### DUMP_FLAGS_MASK_DEFAULT ###

Dumps the content of a window
@param aWindowToDump       the window to dump (may be an iframe etc)
@param aFile               the file to dump to. It will be created if necessary, otherwise
truncated. If nil, write to stdout.
@param aFlagsMask          some flags that determine what to dump
@param aFlagsMask          some flags that determine what to dump
@param aResult             a status value indicating whether the dump happened, 
whether the page was still loading, or whether some other error happened.


### DUMP_FLAGS_MASK_PRINT_MODE ###

### DUMP_RESULT_COMPLETED ###

### DUMP_RESULT_LOADING ###

### DUMP_RESULT_ERROR ###

### COMPARE_FLAGS_VERBOSE ###

Compares the contents of frame model files
@param aBaseFile           the baseline file, opened with read permissions
@param aVerFile            file containing the results to verify, opened with read permissions
@param aFlags              flags specifying output verbosity
@param aResult             result of the comparison: zero if the files are same, non-zero if different


### COMPARE_FLAGS_BRIEF ###
