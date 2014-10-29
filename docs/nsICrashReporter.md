---
layout: default
---

# nsICrashReporter #

Provides access to crash reporting functionality.

@status UNSTABLE - This interface is not frozen and will probably change in
                   future releases.


## Methods ##

### setEnabled ###

Enable or disable crash reporting at runtime. Not available to script
because the JS engine relies on proper exception handler chaining.


### annotateCrashReport ###

Add some extra data to be submitted with a crash report.

@param key
       Name of the data to be added.
@param data
       Data to be added.

@throw NS_ERROR_NOT_INITIALIZED if crash reporting not initialized
@throw NS_ERROR_INVALID_ARG if key or data contain invalid characters.
                            Invalid characters for key are '=' and
                            '\n'.  Invalid character for data is '\0'.


### appendAppNotesToCrashReport ###

Append some data to the "Notes" field, to be submitted with a crash report.
Unlike annotateCrashReport, this method will append to existing data.

@param data
       Data to be added.

@throw NS_ERROR_NOT_INITIALIZED if crash reporting not initialized
@throw NS_ERROR_INVALID_ARG if data contains invalid characters.
                            The only invalid character is '\0'.


### registerAppMemory ###

Register a given memory range to be included in the crash report.

@param ptr
       The starting address for the bytes.
@param size
       The number of bytes to include.

@throw NS_ERROR_NOT_INITIALIZED if crash reporting not initialized
@throw NS_ERROR_NOT_IMPLEMENTED if unavailable on the current OS


### writeMinidumpForException ###

Write a minidump immediately, with the user-supplied exception
information. This is implemented on Windows only, because
SEH (structured exception handling) exists on Windows only.

@param aExceptionInfo  EXCEPTION_INFO* provided by Window's SEH


### appendObjCExceptionInfoToAppNotes ###

Append note containing an Obj-C exception's info.

@param aException  NSException object to append note for


### UpdateCrashEventsDir ###

Cause the crash reporter to re-evaluate where crash events should go.

This should be called during application startup and whenever profiles
change.


### saveMemoryReport ###

Save an anonymized memory report file for inclusion in a future crash
report in this session.

@throws NS_ERROR_NOT_INITIALIZED if crash reporting is disabled.


## Attributes ##

### enabled ###

Get the enabled status of the crash reporter.


### serverURL ###

Get or set the URL to which crash reports will be submitted.
Only https and http URLs are allowed, as the submission is handled
by OS-native networking libraries.

@throw NS_ERROR_NOT_INITIALIZED if crash reporting is not initialized
@throw NS_ERROR_INVALID_ARG on set if a non-http(s) URL is assigned
@throw NS_ERROR_FAILURE on get if no URL is set


### minidumpPath ###

Get or set the path on the local system to which minidumps will be
written when a crash happens.

@throw NS_ERROR_NOT_INITIALIZED if crash reporting is not initialized


### submitReports ###

User preference for submitting crash reports.

