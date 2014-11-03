---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIBrowserSearchService.idl">Source file</a>
</div>

# nsISearchEngine #

## Methods ##

### getSubmission(data, responseType, purpose) ###
<pre>  
Gets a nsISearchSubmission object that contains information about what to  
send to the search engine, including the URI and postData, if applicable.  
  
@param  data  
        Data to add to the submission object.  
        i.e. the search terms.  
  
@param  responseType [optional]  
        The MIME type that we'd like to receive in response  
        to this submission.  If null, will default to "text/html".  
  
@param purpose [optional]  
       A string meant to indicate the context of the search request. This  
       allows the search service to provide a different nsISearchSubmission  
       depending on e.g. where the search is triggered in the UI.  
  
@returns A nsISearchSubmission object that contains information about what  
         to send to the search engine.  If no submission can be  
         obtained for the given responseType, returns null.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>data</td>
<td>        Data to add to the submission object.  
        i.e. the search terms.  
</td>
</tr>

<tr>
<td>responseType</td>
<td>[optional]  
        The MIME type that we'd like to receive in response  
        to this submission.  If null, will default to "text/html".  
</td>
</tr>

<tr>
<td>purpose</td>
<td>[optional]  
       A string meant to indicate the context of the search request. This  
       allows the search service to provide a different nsISearchSubmission  
       depending on e.g. where the search is triggered in the UI.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>A nsISearchSubmission object that contains information about what  
         to send to the search engine.  If no submission can be  
         obtained for the given responseType, returns null.  
</td>
</tr>

</table>

### addParam(name, value, responseType) ###
<pre>  
Adds a parameter to the search engine's submission data. This should only  
be called on engines created via addEngineWithDetails.  
  
@param name  
       The parameter's name. Must not be null.  
  
@param value  
       The value to pass. If value is "{searchTerms}", it will be  
       substituted with the user-entered data when retrieving the  
       submission. Must not be null.  
  
@param responseType  
       Since an engine can have several different request URLs,  
       differentiated by response types, this parameter selects  
       a request to add parameters to.  If null, will default  
       to "text/html"  
  
@throws NS_ERROR_FAILURE if the search engine is read-only.  
@throws NS_ERROR_INVALID_ARG if name or value are null.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       The parameter's name. Must not be null.  
</td>
</tr>

<tr>
<td>value</td>
<td>       The value to pass. If value is "{searchTerms}", it will be  
       substituted with the user-entered data when retrieving the  
       submission. Must not be null.  
</td>
</tr>

<tr>
<td>responseType</td>
<td>       Since an engine can have several different request URLs,  
       differentiated by response types, this parameter selects  
       a request to add parameters to.  If null, will default  
       to "text/html"  
</td>
</tr>

</table>

### supportsResponseType(responseType) ###
<pre>  
Determines whether the engine can return responses in the given  
MIME type.  Returns true if the engine spec has a URL with the  
given responseType, false otherwise.  
  
@param responseType  
       The MIME type to check for  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>responseType</td>
<td>       The MIME type to check for  
</td>
</tr>

</table>

### getIconURLBySize(width, height) ###
<pre>  
Returns a string with the URL to an engine's icon matching both width and  
height. Returns null if icon with specified dimensions is not found.  
  
@param width  
       Width of the requested icon.  
@param height  
       Height of the requested icon.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>width</td>
<td>       Width of the requested icon.  
</td>
</tr>

<tr>
<td>height</td>
<td>       Height of the requested icon.  
</td>
</tr>

</table>

### getIcons() ###
<pre>  
Gets an array of all available icons. Each entry is an object with  
width, height and url properties. width and height are numeric and  
represent the icon's dimensions. url is a string with the URL for  
the icon.  
  
</pre>
### speculativeConnect(options) ###
<pre>  
Opens a speculative connection to the engine's search URI  
(and suggest URI, if different) to reduce request latency  
  
@param  options  
        An object that must contain the following fields:  
        {window} the content window for the window performing the search  
  
@throws NS_ERROR_INVALID_ARG if options is omitted or lacks required  
        elemeents  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>options</td>
<td>        An object that must contain the following fields:  
        {window} the content window for the window performing the search  
</td>
</tr>

</table>

### getResultDomain(responseType) ###
<pre>  
Gets a string representing the hostname from which search results for a  
given responseType are returned, minus the leading "www." (if present).  
This can be specified as an url attribute in the engine description file,  
but will default to host from the <Url>'s template otherwise.  
  
@param  responseType [optional]  
        The MIME type to get resultDomain for.  Defaults to "text/html".  
  
@return the resultDomain for the given responseType.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>responseType</td>
<td>[optional]  
        The MIME type to get resultDomain for.  Defaults to "text/html".  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>the resultDomain for the given responseType.  
</td>
</tr>

</table>

## Attributes ##

### alias ###
<pre>  
An optional shortcut alias for the engine.  
When non-null, this is a unique identifier.  
  
</pre>
### description ###
<pre>  
A text description describing the engine.  
  
</pre>
### hidden ###
<pre>  
Whether the engine should be hidden from the user.  
  
</pre>
### iconURI ###
<pre>  
A nsIURI corresponding to the engine's icon, stored locally. May be null.  
  
</pre>
### name ###
<pre>  
The display name of the search engine. This is a unique identifier.  
  
</pre>
### searchForm ###
<pre>  
A URL string pointing to the engine's search form.  
  
</pre>
### type ###
<pre>  
The search engine type.  
  
</pre>
### identifier ###
<pre>  
An optional unique identifier for this search engine within the context of  
the distribution, as provided by the distributing entity.  
  
</pre>
## Constants ##

### TYPE_MOZSEARCH ###
<pre>  
Supported search engine types.  
  
</pre>
### TYPE_SHERLOCK ###

### TYPE_OPENSEARCH ###

### DATA_XML ###
<pre>  
Supported search engine data types.  
  
</pre>
### DATA_TEXT ###
