---
layout: default
---

# nsIWebBrowserPersist #
  
Interface for persisting DOM documents and URIs to local or remote storage.  
  

## Methods ##

### saveURI(aURI, aCacheKey, aReferrer, aPostData, aExtraHeaders, aFile, aPrivacyContext) ###
  
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
<td>aURI</td>
<td>URI to save to file. Some implementations of this interface  
                  may also support <CODE>nullptr</CODE> to imply the currently  
                  loaded URI.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>URI to save to file. Some implementations of this interface  
                  may also support <CODE>nullptr</CODE> to imply the currently  
                  loaded URI.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>URI to save to file. Some implementations of this interface  
                  may also support <CODE>nullptr</CODE> to imply the currently  
                  loaded URI.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>URI to save to file. Some implementations of this interface  
                  may also support <CODE>nullptr</CODE> to imply the currently  
                  loaded URI.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>URI to save to file. Some implementations of this interface  
                  may also support <CODE>nullptr</CODE> to imply the currently  
                  loaded URI.  
</td>
</tr>

<tr>
<td>aURI</td>
<td>URI to save to file. Some implementations of this interface  
                  may also support <CODE>nullptr</CODE> to imply the currently  
                  loaded URI.  
</td>
</tr>

</table>

### savePrivacyAwareURI(aURI, aCacheKey, aReferrer, aPostData, aExtraHeaders, aFile, aIsPrivate) ###
  
@param aIsPrivate Treat the save operation as private (ie. with  
                  regards to networking operations and persistence  
                  of intermediate data, etc.)  
@see saveURI for all other parameter descriptions  
  

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
  
Save a channel to a file. It must not be opened yet.  
@see saveURI  
  

### saveDocument(aDocument, aFile, aDataPath, aOutputContentType, aEncodingFlags, aWrapColumn) ###
  
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
<td>aDocument</td>
<td>Document to save to file. Some implementations of  
                          this interface may also support <CODE>nullptr</CODE>  
                          to imply the currently loaded document.  
</td>
</tr>

<tr>
<td>aDocument</td>
<td>Document to save to file. Some implementations of  
                          this interface may also support <CODE>nullptr</CODE>  
                          to imply the currently loaded document.  
</td>
</tr>

<tr>
<td>aDocument</td>
<td>Document to save to file. Some implementations of  
                          this interface may also support <CODE>nullptr</CODE>  
                          to imply the currently loaded document.  
</td>
</tr>

<tr>
<td>aDocument</td>
<td>Document to save to file. Some implementations of  
                          this interface may also support <CODE>nullptr</CODE>  
                          to imply the currently loaded document.  
</td>
</tr>

<tr>
<td>aDocument</td>
<td>Document to save to file. Some implementations of  
                          this interface may also support <CODE>nullptr</CODE>  
                          to imply the currently loaded document.  
</td>
</tr>

</table>

### cancelSave() ###
  
Cancels the current operation. The caller is responsible for cleaning up  
partially written files or directories. This has the same effect as calling  
cancel with an argument of NS_BINDING_ABORTED.  
  

## Attributes ##

### persistFlags ###
  
Flags governing how data is fetched and saved from the network.   
It is best to set this value explicitly unless you are prepared  
to accept the default values.  
  

### currentState ###
  
Current state of the persister object.  
  

### result ###
  
Value indicating the success or failure of the persist  
operation.  
  
@throws NS_BINDING_ABORTED Operation cancelled.  
@throws NS_ERROR_FAILURE Non-specific failure.  
  

### progressListener ###
  
Callback listener for progress notifications. The object that the  
embbedder supplies may also implement nsIInterfaceRequestor and be  
prepared to return nsIAuthPrompt or other interfaces that may be required  
to download data.  
  
@see nsIAuthPrompt  
@see nsIInterfaceRequestor  
  

## Constants ##

### PERSIST_FLAGS_NONE ###
 No special persistence behaviour. */  

### PERSIST_FLAGS_FROM_CACHE ###
 Use cached data if present (skipping validation), else load from network */  

### PERSIST_FLAGS_BYPASS_CACHE ###
 Bypass the cached data. */  

### PERSIST_FLAGS_IGNORE_REDIRECTED_DATA ###
 Ignore any redirected data (usually adverts). */  

### PERSIST_FLAGS_IGNORE_IFRAMES ###
 Ignore IFRAME content (usually adverts). */  

### PERSIST_FLAGS_NO_CONVERSION ###
 Do not run the incoming data through a content converter e.g. to decompress it */  

### PERSIST_FLAGS_REPLACE_EXISTING_FILES ###
 Replace existing files on the disk (use with due diligence!) */  

### PERSIST_FLAGS_NO_BASE_TAG_MODIFICATIONS ###
 Don't modify or add base tags */  

### PERSIST_FLAGS_FIXUP_ORIGINAL_DOM ###
 Make changes to original dom rather than cloning nodes */  

### PERSIST_FLAGS_FIXUP_LINKS_TO_DESTINATION ###
 Fix links relative to destination location (not origin) */  

### PERSIST_FLAGS_DONT_FIXUP_LINKS ###
 Don't make any adjustments to links */  

### PERSIST_FLAGS_SERIALIZE_OUTPUT ###
 Force serialization of output (one file at a time; not concurrent) */  

### PERSIST_FLAGS_DONT_CHANGE_FILENAMES ###
 Don't make any adjustments to filenames */  

### PERSIST_FLAGS_FAIL_ON_BROKEN_LINKS ###
 Fail on broken inline links */  

### PERSIST_FLAGS_CLEANUP_ON_FAILURE ###
  
Automatically cleanup after a failed or cancelled operation, deleting all  
created files and directories. This flag does nothing for failed upload  
operations to remote servers.  
  

### PERSIST_FLAGS_AUTODETECT_APPLY_CONVERSION ###
  
Let the WebBrowserPersist decide whether the incoming data is encoded  
and whether it needs to go through a content converter e.g. to  
decompress it.  
  

### PERSIST_FLAGS_APPEND_TO_FILE ###
  
Append the downloaded data to the target file.  
This can only be used when persisting to a local file.  
  

### PERSIST_FLAGS_FORCE_ALLOW_COOKIES ###
  
Force relevant cookies to be sent with this load even if normally they  
wouldn't be.  
  

### PERSIST_STATE_READY ###
 Persister is ready to save data */  

### PERSIST_STATE_SAVING ###
 Persister is saving data */  

### PERSIST_STATE_FINISHED ###
 Persister has finished saving data */  

### ENCODE_FLAGS_SELECTION_ONLY ###
 Output only the current selection as opposed to the whole document. */  

### ENCODE_FLAGS_FORMATTED ###
  
For plaintext output. Convert html to plaintext that looks like the html.  
Implies wrap (except inside &lt;pre&gt;), since html wraps.  
HTML output: always do prettyprinting, ignoring existing formatting.  
  

### ENCODE_FLAGS_RAW ###
  
Output without formatting or wrapping the content. This flag  
may be used to preserve the original formatting as much as possible.  
  

### ENCODE_FLAGS_BODY_ONLY ###
 Output only the body section, no HTML tags. */  

### ENCODE_FLAGS_PREFORMATTED ###
 Wrap even if when not doing formatted output (e.g. for text fields). */  

### ENCODE_FLAGS_WRAP ###
 Wrap documents at the specified column. */  

### ENCODE_FLAGS_FORMAT_FLOWED ###
  
For plaintext output. Output for format flowed (RFC 2646). This is used  
when converting to text for mail sending. This differs just slightly  
but in an important way from normal formatted, and that is that  
lines are space stuffed. This can't (correctly) be done later.  
  

### ENCODE_FLAGS_ABSOLUTE_LINKS ###
 Convert links to absolute links where possible. */  

### ENCODE_FLAGS_ENCODE_W3C_ENTITIES ###
   
Attempt to encode entities standardized at W3C (HTML, MathML, etc).  
This is a catch-all flag for documents with mixed contents. Beware of  
interoperability issues. See below for other flags which might likely  
do what you want.  
  

### ENCODE_FLAGS_CR_LINEBREAKS ###
  
Output with carriage return line breaks. May also be combined with  
ENCODE_FLAGS_LF_LINEBREAKS and if neither is specified, the platform  
default format is used.  
  

### ENCODE_FLAGS_LF_LINEBREAKS ###
  
Output with linefeed line breaks. May also be combined with  
ENCODE_FLAGS_CR_LINEBREAKS and if neither is specified, the platform  
default format is used.  
  

### ENCODE_FLAGS_NOSCRIPT_CONTENT ###
 For plaintext output. Output the content of noscript elements. */  

### ENCODE_FLAGS_NOFRAMES_CONTENT ###
 For plaintext output. Output the content of noframes elements. */  

### ENCODE_FLAGS_ENCODE_BASIC_ENTITIES ###
  
Encode basic entities, e.g. output &nbsp; instead of character code 0xa0.   
The basic set is just &nbsp; &amp; &lt; &gt; &quot; for interoperability  
with older products that don't support &alpha; and friends.  
  

### ENCODE_FLAGS_ENCODE_LATIN1_ENTITIES ###
  
Encode Latin1 entities. This includes the basic set and  
accented letters between 128 and 255.  
  

### ENCODE_FLAGS_ENCODE_HTML_ENTITIES ###
  
Encode HTML4 entities. This includes the basic set, accented  
letters, greek letters and certain special markup symbols.  
  
