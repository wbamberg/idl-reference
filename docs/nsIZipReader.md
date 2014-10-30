---
layout: default
---

# nsIZipReader #

## Methods ##

### open ###
  
Opens a zip file for reading.  
It is allowed to open with another file,   
but it needs to be closed first with close().  
  

### openInner ###
  
Opens a zip file inside a zip file for reading.  
  

### close ###
  
Closes a zip reader. Subsequent attempts to extract files or read from  
its input stream will result in an error.  
  
Subsequent attempts to access a nsIZipEntry obtained from this zip  
reader will cause unspecified behavior.  
  

### test ###
  
Tests the integrity of the archive by performing a CRC check   
on each item expanded into memory.  If an entry is specified  
the integrity of only that item is tested.  If null (javascript)  
or EmptyCString() (c++) is passed in the integrity of all items   
in the archive are tested.    
  

### extract ###
  
Extracts a zip entry into a local file specified by outFile.  
The entry must be stored in the zip in either uncompressed or  
DEFLATE-compressed format for the extraction to be successful.  
If the entry is a directory, the directory will be extracted  
non-recursively.  
  

### getEntry ###
  
Returns a nsIZipEntry describing a specified zip entry.  
  

### hasEntry ###
  
Checks whether the zipfile contains an entry specified by entryName.  
  

### findEntries ###
  
Returns a string enumerator containing the matching entry names.  
  
@param aPattern  
  A regular expression used to find matching entries in the zip file.  
  Set this parameter to null (javascript) or EmptyCString() (c++) or "*"   
  to get all entries; otherwise, use the  
  following syntax:  
  
  o * matches anything  
  o ? matches one character  
  o $ matches the end of the string  
  o [abc] matches one occurrence of a, b, or c. The only character that  
          must be escaped inside the brackets is ].  ^ and - must never  
          appear in the first and second positions within the brackets,   
          respectively.  (In the former case, the behavior specified for  
          '[^az]' will happen.)  
  o [a-z] matches any character between a and z.  The characters a and z  
          must either both be letters or both be numbers, with the  
          character represented by 'a' having a lower ASCII value than  
          the character represented by 'z'.  
  o [^az] matches any character except a or z.  If ] is to appear inside  
          the brackets as a character to not match, it must be escaped.  
  o pat~pat2 returns matches to the pattern 'pat' which do not also match  
             the pattern 'pat2'.  This may be used to perform filtering  
             upon the results of one pattern to remove all matches which  
             also match another pattern.  For example, because '*'  
             matches any string and '*z*' matches any string containing a  
             'z', '*~*z*' will match all strings except those containing  
             a 'z'.  Note that a pattern may not use '~' multiple times,  
             so a string such as '*~*z*~*y*' is not a valid pattern.  
  o (foo|bar) will match either the pattern foo or the pattern bar.  
              Neither of the patterns foo or bar may use the 'pat~pat2'  
              syntax described immediately above.  
  o \ will escape a special character.  Escaping is required for all  
      special characters unless otherwise specified.  
  o All other characters match case-sensitively.  
  
  An aPattern not conforming to this syntax has undefined behavior.  
  
@throws NS_ERROR_ILLEGAL_VALUE on many but not all invalid aPattern  
                               values.  
  

### getInputStream ###
  
Returns an input stream containing the contents of the specified zip  
entry.  
@param zipEntry the name of the entry to open the stream from  
  

### getInputStreamWithSpec ###
  
Returns an input stream containing the contents of the specified zip  
entry. If the entry refers to a directory (ends with '/'), a directory stream   
is opened, otherwise the contents of the file entry is returned.  
@param aJarSpec the Spec of the URI for the JAR (only used for directory streams)  
@param zipEntry the name of the entry to open the stream from  
  

### getSigningCert ###
  
Returns an object describing the entity which signed   
an entry. parseManifest must be called first. If aEntryName is an  
entry in the jar, getInputStream must be called after parseManifest.  
If aEntryName is an external file which has meta-information   
stored in the jar, verifyExternalFile (not yet implemented) must   
be called before getPrincipal.  
  

## Attributes ##

### file ###
  
The file that represents the zip with which this zip reader was  
initialized.  
  

### manifestEntriesCount ###
