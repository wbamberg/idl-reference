---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/embedding/components/webbrowserpersist/nsIWebBrowserPersist.idl">Source file</a>
</div>

# nsIWebBrowserPersist #
<pre>  
Interface for persisting DOM documents and URIs to local or remote storage.  
  
</pre>
## Methods ##

### saveURI(aURI, aCacheKey, aReferrer, aPostData, aExtraHeaders, aFile, aPrivacyContext) ###
<pre>  
Save the specified URI to file.  
  
@param aURI       URI to save to file. Some implementations of this interface  
                  may also support <CODE>nullptr</CODE> to imply the currently  
                  loaded URI.  
@param aCacheKey  An object representing the URI in the cache or  
                  <CODE>nullptr</CODE>.  This can be a necko cache key,  
                  an nsIWebPageDescriptor, or the currentDescriptor of an  
                  nsIWebPageDescriptor.  
@param aReferrer  The referrer URI to pass with an HTTP request or  
                  <CODE>nullptr</CODE>.  
@param aPostData  Post data to pass with an HTTP request or  
                  <CODE>nullptr</CODE>.  
@param aExtraHeaders Additional headers to supply with an HTTP request  
                  or <CODE>nullptr</CODE>.  
@param aFile      Target file. This may be a nsIFile object or an  
                  nsIURI object with a file scheme or a scheme that  
                  supports uploading (e.g. ftp).  
@param aPrivacyContext A context from which the privacy status of this  
                  save operation can be determined. Must only be null  
                  in situations in which no such context is available  
                  (eg. the operation has no logical association with any  
                  window or document)  
  
@see nsIFile  
@see nsIURI  
@see nsIInputStream  
  
@throws NS_ERROR_INVALID_ARG One or more arguments was invalid.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aURI</td>
<td>URI to save to file. Some implementations of this interface  
                  may also support <CODE>nullptr</CODE> to imply the currently  
                  loaded URI.  
</td>
</tr>

<tr>
<td>aCacheKey</td>
<td>An object representing the URI in the cache or  
                  <CODE>nullptr</CODE>.  This can be a necko cache key,  
                  an nsIWebPageDescriptor, or the currentDescriptor of an  
                  nsIWebPageDescriptor.  
</td>
</tr>

<tr>
<td>aReferrer</td>
<td>The referrer URI to pass with an HTTP request or  
                  <CODE>nullptr</CODE>.  
</td>
</tr>

<tr>
<td>aPostData</td>
<td>Post data to pass with an HTTP request or  
                  <CODE>nullptr</CODE>.  
</td>
</tr>

<tr>
<td>aExtraHeaders</td>
<td>Additional headers to supply with an HTTP request  
                  or <CODE>nullptr</CODE>.  
</td>
</tr>

<tr>
<td>aFile</td>
<td>Target file. This may be a nsIFile object or an  
                  nsIURI object with a file scheme or a scheme that  
                  supports uploading (e.g. ftp).  
</td>
</tr>

<tr>
<td>aPrivacyContext</td>
<td>A context from which the privacy status of this  
                  save operation can be determined. Must only be null  
                  in situations in which no such context is available  
                  (eg. the operation has no logical association with any  
                  window or document)  
</td>
</tr>

</table>

### savePrivacyAwareURI(aURI, aCacheKey, aReferrer, aPostData, aExtraHeaders, aFile, aIsPrivate) ###
<pre>  
@param aIsPrivate Treat the save operation as private (ie. with  
                  regards to networking operations and persistence  
                  of intermediate data, etc.)  
@see saveURI for all other parameter descriptions  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aIsPrivate</td>
<td>Treat the save operation as private (ie. with  
                  regards to networking operations and persistence  
                  of intermediate data, etc.)  
@see saveURI for all other parameter descriptions  
</td>
</tr>

</table>

### saveChannel(aChannel, aFile) ###
<pre>  
Save a channel to a file. It must not be opened yet.  
@see saveURI  
  
</pre>
### saveDocument(aDocument, aFile, aDataPath, aOutputContentType, aEncodingFlags, aWrapColumn) ###
<pre>  
Save the specified DOM document to file and optionally all linked files  
(e.g. images, CSS, JS & subframes). Do not call this method until the  
document has finished loading!  
  
@param aDocument          Document to save to file. Some implementations of  
                          this interface may also support <CODE>nullptr</CODE>  
                          to imply the currently loaded document.  
@param aFile              Target local file. This may be a nsIFile object or an  
                          nsIURI object with a file scheme or a scheme that  
                          supports uploading (e.g. ftp).  
@param aDataPath          Path to directory where URIs linked to the document  
                          are saved or nullptr if no linked URIs should be saved.  
                          This may be a nsIFile object or an nsIURI object  
                          with a file scheme.  
@param aOutputContentType The desired MIME type format to save the   
                          document and all subdocuments into or nullptr to use  
                          the default behaviour.  
@param aEncodingFlags     Flags to pass to the encoder.  
@param aWrapColumn        For text documents, indicates the desired width to  
                          wrap text at. Parameter is ignored if wrapping is not  
                          specified by the encoding flags.  
  
@see nsIFile  
@see nsIURI  
  
@throws NS_ERROR_INVALID_ARG One or more arguments was invalid.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aDocument</td>
<td>Document to save to file. Some implementations of  
                          this interface may also support <CODE>nullptr</CODE>  
                          to imply the currently loaded document.  
</td>
</tr>

<tr>
<td>aFile</td>
<td>Target local file. This may be a nsIFile object or an  
                          nsIURI object with a file scheme or a scheme that  
                          supports uploading (e.g. ftp).  
</td>
</tr>

<tr>
<td>aDataPath</td>
<td>Path to directory where URIs linked to the document  
                          are saved or nullptr if no linked URIs should be saved.  
                          This may be a nsIFile object or an nsIURI object  
                          with a file scheme.  
</td>
</tr>

<tr>
<td>aOutputContentType</td>
<td>The desired MIME type format to save the   
                          document and all subdocuments into or nullptr to use  
                          the default behaviour.  
</td>
</tr>

<tr>
<td>aEncodingFlags</td>
<td>Flags to pass to the encoder.  
</td>
</tr>

<tr>
<td>aWrapColumn</td>
<td>For text documents, indicates the desired width to  
                          wrap text at. Parameter is ignored if wrapping is not  
                          specified by the encoding flags.  
</td>
</tr>

</table>

### cancelSave() ###
<pre>  
Cancels the current operation. The caller is responsible for cleaning up  
partially written files or directories. This has the same effect as calling  
cancel with an argument of NS_BINDING_ABORTED.  
  
</pre>
## Attributes ##

### persistFlags ###
<pre>  
Flags governing how data is fetched and saved from the network.   
It is best to set this value explicitly unless you are prepared  
to accept the default values.  
  
</pre>
### currentState ###
<pre>  
Current state of the persister object.  
  
</pre>
### result ###
<pre>  
Value indicating the success or failure of the persist  
operation.  
  
@throws NS_BINDING_ABORTED Operation cancelled.  
@throws NS_ERROR_FAILURE Non-specific failure.  
  
</pre>
### progressListener ###
<pre>  
Callback listener for progress notifications. The object that the  
embbedder supplies may also implement nsIInterfaceRequestor and be  
prepared to return nsIAuthPrompt or other interfaces that may be required  
to download data.  
  
@see nsIAuthPrompt  
@see nsIInterfaceRequestor  
  
</pre>
## Constants ##

### PERSIST_FLAGS_NONE ###
<pre> No special persistence behaviour. */  
</pre>
### PERSIST_FLAGS_FROM_CACHE ###
<pre> Use cached data if present (skipping validation), else load from network */  
</pre>
### PERSIST_FLAGS_BYPASS_CACHE ###
<pre> Bypass the cached data. */  
</pre>
### PERSIST_FLAGS_IGNORE_REDIRECTED_DATA ###
<pre> Ignore any redirected data (usually adverts). */  
</pre>
### PERSIST_FLAGS_IGNORE_IFRAMES ###
<pre> Ignore IFRAME content (usually adverts). */  
</pre>
### PERSIST_FLAGS_NO_CONVERSION ###
<pre> Do not run the incoming data through a content converter e.g. to decompress it */  
</pre>
### PERSIST_FLAGS_REPLACE_EXISTING_FILES ###
<pre> Replace existing files on the disk (use with due diligence!) */  
</pre>
### PERSIST_FLAGS_NO_BASE_TAG_MODIFICATIONS ###
<pre> Don't modify or add base tags */  
</pre>
### PERSIST_FLAGS_FIXUP_ORIGINAL_DOM ###
<pre> Make changes to original dom rather than cloning nodes */  
</pre>
### PERSIST_FLAGS_FIXUP_LINKS_TO_DESTINATION ###
<pre> Fix links relative to destination location (not origin) */  
</pre>
### PERSIST_FLAGS_DONT_FIXUP_LINKS ###
<pre> Don't make any adjustments to links */  
</pre>
### PERSIST_FLAGS_SERIALIZE_OUTPUT ###
<pre> Force serialization of output (one file at a time; not concurrent) */  
</pre>
### PERSIST_FLAGS_DONT_CHANGE_FILENAMES ###
<pre> Don't make any adjustments to filenames */  
</pre>
### PERSIST_FLAGS_FAIL_ON_BROKEN_LINKS ###
<pre> Fail on broken inline links */  
</pre>
### PERSIST_FLAGS_CLEANUP_ON_FAILURE ###
<pre>  
Automatically cleanup after a failed or cancelled operation, deleting all  
created files and directories. This flag does nothing for failed upload  
operations to remote servers.  
  
</pre>
### PERSIST_FLAGS_AUTODETECT_APPLY_CONVERSION ###
<pre>  
Let the WebBrowserPersist decide whether the incoming data is encoded  
and whether it needs to go through a content converter e.g. to  
decompress it.  
  
</pre>
### PERSIST_FLAGS_APPEND_TO_FILE ###
<pre>  
Append the downloaded data to the target file.  
This can only be used when persisting to a local file.  
  
</pre>
### PERSIST_FLAGS_FORCE_ALLOW_COOKIES ###
<pre>  
Force relevant cookies to be sent with this load even if normally they  
wouldn't be.  
  
</pre>
### PERSIST_STATE_READY ###
<pre> Persister is ready to save data */  
</pre>
### PERSIST_STATE_SAVING ###
<pre> Persister is saving data */  
</pre>
### PERSIST_STATE_FINISHED ###
<pre> Persister has finished saving data */  
</pre>
### ENCODE_FLAGS_SELECTION_ONLY ###
<pre> Output only the current selection as opposed to the whole document. */  
</pre>
### ENCODE_FLAGS_FORMATTED ###
<pre>  
For plaintext output. Convert html to plaintext that looks like the html.  
Implies wrap (except inside &lt;pre&gt;), since html wraps.  
HTML output: always do prettyprinting, ignoring existing formatting.  
  
</pre>
### ENCODE_FLAGS_RAW ###
<pre>  
Output without formatting or wrapping the content. This flag  
may be used to preserve the original formatting as much as possible.  
  
</pre>
### ENCODE_FLAGS_BODY_ONLY ###
<pre> Output only the body section, no HTML tags. */  
</pre>
### ENCODE_FLAGS_PREFORMATTED ###
<pre> Wrap even if when not doing formatted output (e.g. for text fields). */  
</pre>
### ENCODE_FLAGS_WRAP ###
<pre> Wrap documents at the specified column. */  
</pre>
### ENCODE_FLAGS_FORMAT_FLOWED ###
<pre>  
For plaintext output. Output for format flowed (RFC 2646). This is used  
when converting to text for mail sending. This differs just slightly  
but in an important way from normal formatted, and that is that  
lines are space stuffed. This can't (correctly) be done later.  
  
</pre>
### ENCODE_FLAGS_ABSOLUTE_LINKS ###
<pre> Convert links to absolute links where possible. */  
</pre>
### ENCODE_FLAGS_ENCODE_W3C_ENTITIES ###
<pre>   
Attempt to encode entities standardized at W3C (HTML, MathML, etc).  
This is a catch-all flag for documents with mixed contents. Beware of  
interoperability issues. See below for other flags which might likely  
do what you want.  
  
</pre>
### ENCODE_FLAGS_CR_LINEBREAKS ###
<pre>  
Output with carriage return line breaks. May also be combined with  
ENCODE_FLAGS_LF_LINEBREAKS and if neither is specified, the platform  
default format is used.  
  
</pre>
### ENCODE_FLAGS_LF_LINEBREAKS ###
<pre>  
Output with linefeed line breaks. May also be combined with  
ENCODE_FLAGS_CR_LINEBREAKS and if neither is specified, the platform  
default format is used.  
  
</pre>
### ENCODE_FLAGS_NOSCRIPT_CONTENT ###
<pre> For plaintext output. Output the content of noscript elements. */  
</pre>
### ENCODE_FLAGS_NOFRAMES_CONTENT ###
<pre> For plaintext output. Output the content of noframes elements. */  
</pre>
### ENCODE_FLAGS_ENCODE_BASIC_ENTITIES ###
<pre>  
Encode basic entities, e.g. output &nbsp; instead of character code 0xa0.   
The basic set is just &nbsp; &amp; &lt; &gt; &quot; for interoperability  
with older products that don't support &alpha; and friends.  
  
</pre>
### ENCODE_FLAGS_ENCODE_LATIN1_ENTITIES ###
<pre>  
Encode Latin1 entities. This includes the basic set and  
accented letters between 128 and 255.  
  
</pre>
### ENCODE_FLAGS_ENCODE_HTML_ENTITIES ###
<pre>  
Encode HTML4 entities. This includes the basic set, accented  
letters, greek letters and certain special markup symbols.  
  
</pre>