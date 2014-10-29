---
layout: default
---

# nsIMIMEService #

The MIME service is responsible for mapping file extensions to MIME-types
(see RFC 2045). It also provides access to nsIMIMEInfo interfaces and
acts as a general convenience wrapper of nsIMIMEInfo interfaces.

The MIME service maintains a database with a <b>one</b> MIME type <b>to many</b>
file extensions rule. Adding the same file extension to multiple MIME types
is illegal and behavior is undefined.

@see nsIMIMEInfo


## getFromTypeAndExtension ##

Retrieves an nsIMIMEInfo using both the extension
and the type of a file. The type is given preference
during the lookup. One of aMIMEType and aFileExt
can be an empty string. At least one of aMIMEType and aFileExt
must be nonempty.


## getTypeFromExtension ##

Retrieves a ACString representation of the MIME type
associated with this file extension.

@param  A file extension (excluding the dot ('.')).
@return The MIME type, if any.


## getTypeFromURI ##

Retrieves a ACString representation of the MIME type
associated with this URI. The association is purely
file extension to MIME type based. No attempt to determine
the type via server headers or byte scanning is made.

@param  The URI the user wants MIME info on.
@return The MIME type, if any.


## getTypeFromFile ##

## getPrimaryExtension ##

Given a Type/Extension combination, returns the default extension
for this type. This may be identical to the passed-in extension.

@param aMIMEType The Type to get information on. Must not be empty.
@param aFileExt  File Extension. Can be empty.

