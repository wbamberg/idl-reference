---
layout: default
---

# nsIDocumentEncoder #

## Methods ##

### init(aDocument, aMimeType, aFlags) ###
  
Initialize with a pointer to the document and the mime type.  
@param aDocument Document to encode.  
@param aMimeType MimeType to use. May also be set by SetMimeType.  
@param aFlags Flags to use while encoding. May also be set by SetFlags.  
  

#### Parameters ####

<table>

<tr>
<td>aDocument</td>
<td>Document to encode.  
</td>
</tr>

<tr>
<td>aMimeType</td>
<td>MimeType to use. May also be set by SetMimeType.  
</td>
</tr>

<tr>
<td>aFlags</td>
<td>Flags to use while encoding. May also be set by SetFlags.  
</td>
</tr>

</table>

### nativeInit(aDocument, aMimeType, aFlags) ###

### setSelection(aSelection) ###
  
 If the selection is set to a non-null value, then the  
 selection is used for encoding, otherwise the entire  
 document is encoded.  
@param aSelection The selection to encode.  
  

#### Parameters ####

<table>

<tr>
<td>aSelection</td>
<td>The selection to encode.  
</td>
</tr>

</table>

### setRange(aRange) ###
  
 If the range is set to a non-null value, then the  
 range is used for encoding, otherwise the entire  
 document or selection is encoded.  
@param aRange The range to encode.  
  

#### Parameters ####

<table>

<tr>
<td>aRange</td>
<td>The range to encode.  
</td>
</tr>

</table>

### setNode(aNode) ###
  
 If the node is set to a non-null value, then the  
 node is used for encoding, otherwise the entire  
 document or range or selection is encoded.  
@param aNode The node to encode.  
  

#### Parameters ####

<table>

<tr>
<td>aNode</td>
<td>The node to encode.  
</td>
</tr>

</table>

### setNativeNode(aNode) ###

### setContainerNode(aContainer) ###
  
 If the container is set to a non-null value, then its  
 child nodes are used for encoding, otherwise the entire  
 document or range or selection or node is encoded.  
 @param aContainer The node which child nodes will be encoded.  
  

### setNativeContainerNode(aContainer) ###

### setCharset(aCharset) ###
  
 Documents typically have an intrinsic character set,  
 but if no intrinsic value is found, the platform character set  
 is used. This function overrides both the intrinisc and platform  
 charset.  
 @param aCharset Overrides the both the intrinsic or platform  
 character set when encoding the document.  
  
 Possible result codes: NS_ERROR_NO_CHARSET_CONVERTER  
  

### setWrapColumn(aWrapColumn) ###
  
 Set a wrap column.  This may have no effect in some types of encoders.  
@param aWrapColumn Column to which to wrap.  
  

#### Parameters ####

<table>

<tr>
<td>aWrapColumn</td>
<td>Column to which to wrap.  
</td>
</tr>

</table>

### encodeToStream(aStream) ###
  
 Encode the document and send the result to the nsIOutputStream.  
  
 Possible result codes are the stream errors which might have  
 been encountered.  
@param aStream Stream into which to encode.  
  

#### Parameters ####

<table>

<tr>
<td>aStream</td>
<td>Stream into which to encode.  
</td>
</tr>

</table>

### encodeToString() ###
  
Encode the document into a string.  
  
@return The document encoded into a string.  
  

### encodeToStringWithContext(aContextString, aInfoString) ###
  
Encode the document into a string. Stores the extra context information  
into the two arguments.  
@param [OUT] aContextString The string where the parent hierarchy  
             information will be stored.  
@param [OUT] aInfoString The string where extra context info will  
             be stored.  
@return The document encoded as a string.  
  
  

#### Parameters ####

<table>

<tr>
<td>[OUT]</td>
<td>aContextString The string where the parent hierarchy  
             information will be stored.  
</td>
</tr>

<tr>
<td>[OUT]</td>
<td>aInfoString The string where extra context info will  
             be stored.  
</td>
</tr>

</table>

### encodeToStringWithMaxLength(aMaxLength) ###
  
Encode the document into a string of limited size.  
@param aMaxLength After aMaxLength characters, the encoder will stop  
                  encoding new data.  
                  Only values > 0 will be considered.  
                  The returned string may be slightly larger than  
                  aMaxLength because some serializers (eg. HTML)  
                  may need to close some tags after they stop  
                  encoding new data, or finish a line (72 columns  
                  by default for the plain text serializer).  
  
@return The document encoded into a string.  
  

#### Parameters ####

<table>

<tr>
<td>aMaxLength</td>
<td>After aMaxLength characters, the encoder will stop  
                  encoding new data.  
                  Only values > 0 will be considered.  
                  The returned string may be slightly larger than  
                  aMaxLength because some serializers (eg. HTML)  
                  may need to close some tags after they stop  
                  encoding new data, or finish a line (72 columns  
                  by default for the plain text serializer).  
</td>
</tr>

</table>

### setNodeFixup(aFixup) ###
  
Set the fixup object associated with node persistence.  
@param aFixup The fixup object.  
  

#### Parameters ####

<table>

<tr>
<td>aFixup</td>
<td>The fixup object.  
</td>
</tr>

</table>

## Attributes ##

### mimeType ###
  
 The mime type preferred by the encoder.  This piece of api was  
 added because the copy encoder may need to switch mime types on you  
 if you ask it to copy html that really represents plaintext content.  
 Call this AFTER Init() and SetSelection() have both been called.  
  

## Constants ##

### OutputSelectionOnly ###
   
Output only the selection (as opposed to the whole document).  
  

### OutputFormatted ###
 Plaintext output: Convert html to plaintext that looks like the html.  
Implies wrap (except inside <pre>), since html wraps.  
HTML, XHTML and XML output: do prettyprinting, ignoring existing formatting.  
XML output : it doesn't implicitly wrap  
  

### OutputRaw ###
 Don't do prettyprinting. Don't do any wrapping that's not in the existing  
HTML/XML source. This option overrides OutputFormatted if both are set.  
HTML/XHTML output: If neither are set, there won't be prettyprinting too, but  
long lines will be wrapped.  
Supported also in XML and Plaintext output.  
@note This option does not affect entity conversion.  
  

### OutputBodyOnly ###
   
Do not print html head tags.  
XHTML/HTML output only.  
  

### OutputPreformatted ###
  
Output as though the content is preformatted  
(e.g. maybe it's wrapped in a PRE or PRE_WRAP style tag)  
Plaintext output only.  
XXXbz How does this interact with  
OutputFormatted/OutputRaw/OutputPreformatted/OutputFormatFlowed?  
  

### OutputWrap ###
  
Wrap even if we're not doing formatted output (e.g. for text fields).  
Supported in XML, XHTML, HTML and Plaintext output.  
Set implicitly in HTML/XHTML output when no OutputRaw.  
Ignored when OutputRaw.  
XXXLJ: set implicitly in HTML/XHTML output, to keep compatible behaviors  
       for old callers of this interface  
XXXbz How does this interact with OutputFormatFlowed?  
  

### OutputFormatFlowed ###
  
Output for format flowed (RFC 2646). This is used when converting  
to text for mail sending. This differs just slightly  
but in an important way from normal formatted, and that is that  
lines are space stuffed. This can't (correctly) be done later.  
PlainText output only.  
XXXbz How does this interact with  
OutputFormatted/OutputRaw/OutputPreformatted/OutputWrap?  
  

### OutputAbsoluteLinks ###
  
Convert links, image src, and script src to absolute URLs when possible.  
XHTML/HTML output only.  
  

### OutputEncodeW3CEntities ###
  
Attempt to encode entities standardized at W3C (HTML, MathML, etc).  
This is a catch-all flag for documents with mixed contents. Beware of  
interoperability issues. See below for other flags which might likely  
do what you want.  
HTML output only.  
  

### OutputCRLineBreak ###
   
LineBreak processing: if this flag is set than CR line breaks will  
be written. If neither this nor OutputLFLineBreak is set, then we  
will use platform line breaks. The combination of the two flags will  
cause CRLF line breaks to be written.  
  

### OutputLFLineBreak ###
   
LineBreak processing: if this flag is set than LF line breaks will  
be written. If neither this nor OutputCRLineBreak is set, then we  
will use platform line breaks. The combination of the two flags will  
cause CRLF line breaks to be written.  
  

### OutputNoScriptContent ###
  
Output the content of noscript elements (only for serializing  
to plaintext).  
  

### OutputNoFramesContent ###
  
Output the content of noframes elements (only for serializing  
to plaintext). (Used only internally in the plain text serializer;  
ignored if passed by the caller.)  
  

### OutputNoFormattingInPre ###
  
Don't allow any formatting nodes (e.g. <br>, <b>) inside a <pre>.  
This is used primarily by mail. XHTML/HTML output only.  
  

### OutputEncodeBasicEntities ###
  
Encode entities when outputting to a string.  
E.g. If set, we'll output &nbsp; if clear, we'll output 0xa0.  
The basic set is just &nbsp; &amp; &lt; &gt; &quot; for interoperability  
with older products that don't support &alpha; and friends.  
HTML output only.  
  

### OutputEncodeLatin1Entities ###
  
Encode entities when outputting to a string.  
The Latin1 entity set additionally includes 8bit accented letters  
between 128 and 255.  
HTML output only.  
  

### OutputEncodeHTMLEntities ###
  
Encode entities when outputting to a string.  
The HTML entity set additionally includes accented letters, greek  
letters, and other special markup symbols as defined in HTML4.  
HTML output only.  
  

### OutputPersistNBSP ###
  
Normally &nbsp; is replaced with a space character when  
encoding data as plain text, set this flag if that's  
not desired.  
Plaintext output only.  
  

### OutputDontRewriteEncodingDeclaration ###
  
Normally when serializing the whole document using the HTML or   
XHTML serializer, the encoding declaration is rewritten to match.  
This flag suppresses that behavior.  
  

### SkipInvisibleContent ###
  
When using the HTML or XHTML serializer, skip elements that are not  
visible when this flag is set.  Elements are not visible when they  
have CSS style display:none or visibility:collapse, for example.  
  

### OutputFormatDelSp ###
  
Output for delsp=yes (RFC 3676). This is used with OutputFormatFlowed  
when converting to text for mail sending.  
PlainText output only.  
  

### OutputDropInvisibleBreak ###
  
Drop <br> elements considered "invisible" by the editor. OutputPreformatted  
implies this flag.  
  

### OutputIgnoreMozDirty ###
  
Don't check for _moz_dirty attributes when deciding whether to  
pretty-print if this flag is set (bug 599983).  
  

### OutputNonTextContentAsPlaceholder ###
  
Output the content of non-text elements as the placehodler character  
U+FFFC (OBJECT REPLACEMENT CHARACTER, only for serializing to plaintext).  
  

### OutputDontRemoveLineEndingSpaces ###
  
Don't Strip ending spaces from a line (only for serializing to plaintext).  
  
