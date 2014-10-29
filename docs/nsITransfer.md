---
layout: default
---

# nsITransfer #

## Methods ##

### init ###

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


### setSha256Hash ###

### setSignatureInfo ###

### setRedirects ###
