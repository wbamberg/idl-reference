---
layout: default
---

# nsIMemoryReporterManager #

## Methods ##

### init() ###

### registerStrongReporter(reporter) ###

### registerWeakReporter(reporter) ###

### unregisterStrongReporter(reporter) ###

### unregisterWeakReporter(reporter) ###

### blockRegistrationAndHideExistingReporters() ###

### unblockRegistrationAndRestoreOriginalReporters() ###

### registerStrongReporterEvenIfBlocked(aReporter) ###

### getReports(handleReport, handleReportData, finishReporting, finishReportingData, anonymize) ###

### getReportsExtended(handleReport, handleReportData, finishReporting, finishReportingData, anonymize, minimizeMemoryUsage, DMDDumpIdent) ###

### getReportsForThisProcess(handleReport, handleReportData, anonymize) ###

### getReportsForThisProcessExtended(handleReport, handleReportData, anonymize, DMDFile) ###

### minimizeMemoryUsage(callback) ###

### sizeOfTab(window, jsObjectsSize, jsStringsSize, jsOtherSize, domSize, styleSize, otherSize, totalSize, jsMilliseconds, nonJSMilliseconds) ###

## Attributes ##

### explicit ###

### vsize ###

### vsizeMaxContiguous ###

### resident ###

### residentFast ###

### residentUnique ###

### heapAllocated ###

### heapOverheadRatio ###

### JSMainRuntimeGCHeap ###

### JSMainRuntimeTemporaryPeak ###

### JSMainRuntimeCompartmentsSystem ###

### JSMainRuntimeCompartmentsUser ###

### imagesContentUsedUncompressed ###

### storageSQLite ###

### lowMemoryEventsVirtual ###

### lowMemoryEventsPhysical ###

### ghostWindows ###

### pageFaultsHard ###

### hasMozMallocUsableSize ###

### isDMDEnabled ###

### isDMDRunning ###
