---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/widget/nsIFilePicker.idl">Source file</a>
</div>

# nsIFilePicker #

## Methods ##

### init(parent, title, mode) ###
  
Initialize the file picker widget.  The file picker is not valid until this  
method is called.  
  
@param      parent   nsIDOMWindow parent.  This dialog will be dependent  
                     on this parent. parent must be non-null.  
@param      title    The title for the file widget  
@param      mode     load, save, or get folder  
  
  

#### Parameters ####

<table>

<tr>
<td>parent</td>
<td>nsIDOMWindow parent.  This dialog will be dependent  
                     on this parent. parent must be non-null.  
</td>
</tr>

<tr>
<td>title</td>
<td>The title for the file widget  
</td>
</tr>

<tr>
<td>mode</td>
<td>load, save, or get folder  
</td>
</tr>

</table>

### appendFilters(filterMask) ###
  
Append to the  filter list with things from the predefined list  
  
@param      filters  mask of filters i.e. (filterAll | filterHTML)  
  
  

#### Parameters ####

<table>

<tr>
<td>filters</td>
<td>mask of filters i.e. (filterAll | filterHTML)  
</td>
</tr>

</table>

### appendFilter(title, filter) ###
  
Add a filter  
  
@param      title    name of the filter  
@param      filter   extensions to filter -- semicolon and space separated  
  
  

#### Parameters ####

<table>

<tr>
<td>title</td>
<td>name of the filter  
</td>
</tr>

<tr>
<td>filter</td>
<td>extensions to filter -- semicolon and space separated  
</td>
</tr>

</table>

### show() ###
  
Show File Dialog. The dialog is displayed modally.  
  
@return returnOK if the user selects OK, returnCancel if the user selects cancel  
  
  

#### Returns ####

<table>

<tr>
<td>returnOK if the user selects OK, returnCancel if the user selects cancel  
</td>
</tr>

</table>

### open(aFilePickerShownCallback) ###
  
Opens the file dialog asynchrounously.  
The passed in object's done method will be called upon completion.  
  

## Attributes ##

### defaultString ###
  
The filename that should be suggested to the user as a default. This should  
include the extension.  
  
@throws NS_ERROR_FAILURE on attempts to get  
  

### defaultExtension ###
  
The extension that should be associated with files of the type we  
want to work with.  On some platforms, this extension will be  
automatically appended to filenames the user enters, if needed.    
  

### filterIndex ###
  
The filter which is currently selected in the File Picker dialog  
  
@return Returns the index (0 based) of the selected filter in the filter list.   
  

### displayDirectory ###
  
Set the directory that the file open/save dialog initially displays  
  
@param      displayDirectory  the name of the directory  
  
  

### file ###
  
Get the nsIFile for the file or directory.  
  
@return Returns the file currently selected  
  

### fileURL ###
  
Get the nsIURI for the file or directory.  
  
@return Returns the file currently selected  
  

### files ###
  
Get the enumerator for the selected files  
only works in the modeOpenMultiple mode  
  
@return Returns the files currently selected  
  

### domfile ###
  
Get the nsIDOMFile for the file.  
  
@return Returns the file currently selected as File  
  

### domfiles ###
  
Get the enumerator for the selected files  
only works in the modeOpenMultiple mode  
  
@return Returns the files currently selected as Files  
  

### addToRecentDocs ###
  
Controls whether the chosen file(s) should be added to the system's recent  
documents list. This attribute will be ignored if the system has no "Recent  
Docs" concept, or if the application is in private browsing mode (in which  
case the file will not be added). Defaults to true.  
  

### mode ###
  
The picker's mode, as set by the 'mode' argument passed to init()  
(one of the modeOpen et. al. constants specified above).  
  

## Constants ##

### modeOpen ###

### modeSave ###

### modeGetFolder ###

### modeOpenMultiple ###

### returnOK ###

### returnCancel ###

### returnReplace ###

### filterAll ###

### filterHTML ###

### filterText ###

### filterImages ###

### filterXML ###

### filterXUL ###

### filterApps ###

### filterAllowURLs ###

### filterAudio ###

### filterVideo ###
