---
layout: default
---

# mozITXTToHTMLConv #

## Methods ##

### scanTXT(text, whattodo) ###
  
@param text: plain text to scan. May be a line, paragraph (recommended)  
or just a substring.<p>  
Must be non-escaped, pure unicode.<p>  
<em>Note:</em> ScanTXT(a, o) + ScanTXT(b, o) may be !=  
Scan(a + b, o)  
@param whattodo: Bitfield describing the modes of operation  
@result      "<", ">" and "&" are escaped and HTML tags are inserted where  
appropriate.  
  

#### Parameters ####

<table>

<tr>
<td>text:</td>
<td>plain text to scan. May be a line, paragraph (recommended)  
or just a substring.<p>  
Must be non-escaped, pure unicode.<p>  
<em>Note:</em> ScanTXT(a, o) + ScanTXT(b, o) may be !=  
Scan(a + b, o)  
</td>
</tr>

<tr>
<td>whattodo:</td>
<td>Bitfield describing the modes of operation  
@result      "<", ">" and "&" are escaped and HTML tags are inserted where  
appropriate.  
</td>
</tr>

</table>

### scanHTML(text, whattodo) ###
  
Adds additional formatting to user edited text, that the user was too lazy  
or "unknowledged" (DELETEME: is that a word?) to make.  
<p>  
<em>Note:</em> Don't use kGlyphSubstitution with this function. This option  
generates tags, that are unuseable for UAs other than Mozilla. This would  
be a data loss bug.  
  
@param text: HTML source to scan. May be a line, paragraph (recommended)  
or just a substring.<p>  
Must be correct HTML. "<", ">" and "&" must be escaped,  
other chars must be pure unicode.<p>  
<em>Note:</em> ScanTXT(a, o) + ScanTXT(b, o) may be !=  
Scan(a + b, o)  
@param whattodo: Bitfield describing the modes of operation  
@result      Additional HTML tags are inserted where appropriate.  
  

#### Parameters ####

<table>

<tr>
<td>text:</td>
<td>HTML source to scan. May be a line, paragraph (recommended)  
or just a substring.<p>  
Must be correct HTML. "<", ">" and "&" must be escaped,  
other chars must be pure unicode.<p>  
<em>Note:</em> ScanTXT(a, o) + ScanTXT(b, o) may be !=  
Scan(a + b, o)  
</td>
</tr>

<tr>
<td>whattodo:</td>
<td>Bitfield describing the modes of operation  
@result      Additional HTML tags are inserted where appropriate.  
</td>
</tr>

</table>

### citeLevelTXT(line, logLineStart) ###
  
@param line: line in original msg, possibly starting starting with  
txt quote tags like ">"  
@param logLineStart: pos in line, where the real content (logical line)  
begins, i.e. pos after all txt quote tags.  
E.g. position of "t" in "> > text".  
Initial value must be 0, unless line is not real line.  
@return      Cite Level, i.e. number of txt quote tags found, i.e. number of  
nested quotes.  
  

#### Parameters ####

<table>

<tr>
<td>line:</td>
<td>line in original msg, possibly starting starting with  
txt quote tags like ">"  
</td>
</tr>

<tr>
<td>logLineStart:</td>
<td>pos in line, where the real content (logical line)  
begins, i.e. pos after all txt quote tags.  
E.g. position of "t" in "> > text".  
Initial value must be 0, unless line is not real line.  
</td>
</tr>

</table>

### findURLInPlaintext(text, aLength, aPos, aStartPos, aEndPos) ###
   
@param a wide string to scan for the presence of a URL.  
@param aLength --> the length of the buffer to be scanned  
@param aPos --> the position in the buffer to start scanning for a url  
  
aStartPos --> index into the start of a url (-1 if no url found)  
aEndPos --> index of the last character in the url (-1 if no url found)  
  

#### Parameters ####

<table>

<tr>
<td>a</td>
<td>wide string to scan for the presence of a URL.  
</td>
</tr>

<tr>
<td>aLength</td>
<td>--> the length of the buffer to be scanned  
</td>
</tr>

<tr>
<td>aPos</td>
<td>--> the position in the buffer to start scanning for a url  
</td>
</tr>

</table>

## Constants ##

### kEntities ###

### kURLs ###

### kGlyphSubstitution ###

### kStructPhrase ###
