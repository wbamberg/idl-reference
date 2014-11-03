---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/uriloader/base/nsITransfer.idl">Source file</a>
</div>

# nsITransfer #

## Methods ##

### init(aSource, aTarget, aDisplayName, aMIMEInfo, startTime, aTempFile, aCancelable, aIsPrivate) ###
<code>  
Initializes the transfer with certain properties.  This function must  
be called prior to accessing any properties on this interface.  
  
@param aSource The source URI of the transfer. Must not be null.  
  
@param aTarget The target URI of the transfer. Must not be null.  
  
@param aDisplayName The user-readable description of the transfer.  
                    Can be empty.  
  
@param aMIMEInfo The MIME info associated with the target,  
                 including MIME type and helper app when appropriate.  
                 This parameter is optional.  
  
@param startTime Time when the download started (ie, when the first  
                 response from the server was received)  
                 XXX presumably wbp and exthandler do this differently  
  
@param aTempFile The location of a temporary file; i.e. a file in which  
                 the received data will be stored, but which is not  
                 equal to the target file. (will be moved to the real  
                 target by the caller, when the download is finished)  
                 May be null.  
  
@param aCancelable An object that can be used to abort the download.  
                   Must not be null.  
                   Implementations are expected to hold a strong  
                   reference to this object until the download is  
                   finished, at which point they should release the  
                   reference.  
  
@param aIsPrivate Used to determine the privacy status of the new transfer.  
                  If true, indicates that the transfer was initiated from  
                  a source that desires privacy.  
  
</code>
#### Parameters ####

<table>

<tr>
<td>aSource</td>
<td>The source URI of the transfer. Must not be null.  
</td>
</tr>

<tr>
<td>aTarget</td>
<td>The target URI of the transfer. Must not be null.  
</td>
</tr>

<tr>
<td>aDisplayName</td>
<td>The user-readable description of the transfer.  
                    Can be empty.  
</td>
</tr>

<tr>
<td>aMIMEInfo</td>
<td>The MIME info associated with the target,  
                 including MIME type and helper app when appropriate.  
                 This parameter is optional.  
</td>
</tr>

<tr>
<td>startTime</td>
<td>Time when the download started (ie, when the first  
                 response from the server was received)  
                 XXX presumably wbp and exthandler do this differently  
</td>
</tr>

<tr>
<td>aTempFile</td>
<td>The location of a temporary file; i.e. a file in which  
                 the received data will be stored, but which is not  
                 equal to the target file. (will be moved to the real  
                 target by the caller, when the download is finished)  
                 May be null.  
</td>
</tr>

<tr>
<td>aCancelable</td>
<td>An object that can be used to abort the download.  
                   Must not be null.  
                   Implementations are expected to hold a strong  
                   reference to this object until the download is  
                   finished, at which point they should release the  
                   reference.  
</td>
</tr>

<tr>
<td>aIsPrivate</td>
<td>Used to determine the privacy status of the new transfer.  
                  If true, indicates that the transfer was initiated from  
                  a source that desires privacy.  
</td>
</tr>

</table>

### setSha256Hash(aHash) ###

### setSignatureInfo(aSignatureInfo) ###

### setRedirects(aRedirects) ###
