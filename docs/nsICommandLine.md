---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/commandlines/nsICommandLine.idl">Source file</a>
</div>

# nsICommandLine #
  
Represents the command line used to invoke a XUL application. This may be the  
original command-line of this instance, or a command line remoted from another  
instance of the application.  
  
DEFINITIONS:  
"arguments" are any values found on the command line.  
"flags" are switches. In normalized form they are preceded by a single dash.  
Some flags may take "parameters", e.g. "--url <param>".  
  

## Methods ##

### getArgument(aIndex) ###
  
Get an argument from the array of command-line arguments.  
  
On windows, flags of the form /flag are normalized to -flag. /flag:param  
are normalized to -flag param.  
  
On *nix and mac flags of the form --flag are normalized to -flag. --flag=param  
are normalized to the form -flag param.  
  
@param aIndex The argument to retrieve. This index is 0-based, and does  
              not include the application name.  
@return       The indexth argument.  
@throws       NS_ERROR_INVALID_ARG if aIndex is out of bounds.  
  

#### Parameters ####

<table>

<tr>
<td>aIndex</td>
<td>The argument to retrieve. This index is 0-based, and does  
              not include the application name.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The indexth argument.  
@throws       NS_ERROR_INVALID_ARG if aIndex is out of bounds.  
</td>
</tr>

</table>

### findFlag(aFlag, aCaseSensitive) ###
  
Find a command-line flag.  
  
@param aFlag          The flag name to locate. Do not include the initial  
                      hyphen.  
@param aCaseSensitive Whether to do case-sensitive comparisons.  
@return               The position of the flag in the command line.  
  

#### Parameters ####

<table>

<tr>
<td>aFlag</td>
<td>The flag name to locate. Do not include the initial  
                      hyphen.  
</td>
</tr>

<tr>
<td>aCaseSensitive</td>
<td>Whether to do case-sensitive comparisons.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The position of the flag in the command line.  
</td>
</tr>

</table>

### removeArguments(aStart, aEnd) ###
  
Remove arguments from the command line. This normally occurs after  
a handler has processed the arguments.  
  
@param aStart  Index to begin removing.  
@param aEnd    Index to end removing, inclusive.  
  

#### Parameters ####

<table>

<tr>
<td>aStart</td>
<td>Index to begin removing.  
</td>
</tr>

<tr>
<td>aEnd</td>
<td>Index to end removing, inclusive.  
</td>
</tr>

</table>

### handleFlag(aFlag, aCaseSensitive) ###
  
A helper method which will find a flag and remove it in one step.  
  
@param aFlag  The flag name to find and remove.  
@param aCaseSensitive Whether to do case-sensitive comparisons.  
@return       Whether the flag was found.  
  

#### Parameters ####

<table>

<tr>
<td>aFlag</td>
<td>The flag name to find and remove.  
</td>
</tr>

<tr>
<td>aCaseSensitive</td>
<td>Whether to do case-sensitive comparisons.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Whether the flag was found.  
</td>
</tr>

</table>

### handleFlagWithParam(aFlag, aCaseSensitive) ###
  
Find a flag with a parameter and remove both. This is a helper  
method that combines "findFlag" and "removeArguments" in one step.  
  
@return   null (a void astring) if the flag is not found. The parameter value  
          if found. Note that null and the empty string are not the same.  
@throws   NS_ERROR_INVALID_ARG if the flag exists without a parameter  
  
@param aFlag The flag name to find and remove.  
@param aCaseSensitive Whether to do case-sensitive flag search.  
  

#### Parameters ####

<table>

<tr>
<td>aFlag</td>
<td>The flag name to find and remove.  
</td>
</tr>

<tr>
<td>aCaseSensitive</td>
<td>Whether to do case-sensitive flag search.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>null (a void astring) if the flag is not found. The parameter value  
          if found. Note that null and the empty string are not the same.  
@throws   NS_ERROR_INVALID_ARG if the flag exists without a parameter  
</td>
</tr>

</table>

### resolveFile(aArgument) ###
  
Resolve a file-path argument into an nsIFile. This method gracefully  
handles relative or absolute file paths, according to the working  
directory of this command line.  
  
@param aArgument  The command-line argument to resolve.  
  

#### Parameters ####

<table>

<tr>
<td>aArgument</td>
<td>The command-line argument to resolve.  
</td>
</tr>

</table>

### resolveURI(aArgument) ###
  
Resolves a URI argument into a URI. This method has platform-specific  
logic for converting an absolute URI or a relative file-path into the  
appropriate URI object; it gracefully handles win32 C:\ paths which would  
confuse the ioservice if passed directly.  
  
@param aArgument  The command-line argument to resolve.  
  

#### Parameters ####

<table>

<tr>
<td>aArgument</td>
<td>The command-line argument to resolve.  
</td>
</tr>

</table>

## Attributes ##

### length ###
  
Number of arguments in the command line. The application name is not  
part of the command line.  
  

### state ###
  
The type of command line being processed.  
  
STATE_INITIAL_LAUNCH  is the first launch of the application instance.  
STATE_REMOTE_AUTO     is a remote command line automatically redirected to  
                      this instance.  
STATE_REMOTE_EXPLICIT is a remote command line explicitly redirected to  
                      this instance using xremote/windde/appleevents.  
  

### preventDefault ###
  
There may be a command-line handler which performs a default action if  
there was no explicit action on the command line (open a default browser  
window, for example). This flag allows the default action to be prevented.  
  

### workingDirectory ###
  
The working directory for this command line. Use this property instead  
of the working directory for the current process, since a redirected  
command line may have had a different working directory.  
  

### windowContext ###
  
A window to be targeted by this command line. In most cases, this will  
be null (xremote will sometimes set this attribute).  
  

## Constants ##

### STATE_INITIAL_LAUNCH ###

### STATE_REMOTE_AUTO ###

### STATE_REMOTE_EXPLICIT ###
