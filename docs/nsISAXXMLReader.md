---
layout: default
---

# nsISAXXMLReader #

Interface for reading an XML document using callbacks.

nsISAXXMLReader is the interface that an XML parser's SAX2
driver must implement.  This interface allows an application to set
and query features and properties in the parser, to register event
handlers for document processing, and to initiate a document
parse.


## baseURI ##

The base URI.


## contentHandler ##

If the application does not register a content handler, all
content events reported by the SAX parser will be silently
ignored.

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.


## dtdHandler ##

If the application does not register a DTD handler, all DTD
events reported by the SAX parser will be silently ignored.

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.


## errorHandler ##

If the application does not register an error handler, all
error events reported by the SAX parser will be silently ignored;
however, normal processing may not continue.  It is highly
recommended that all SAX applications implement an error handler
to avoid unexpected bugs.

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.


## declarationHandler ##

A handler for the (optional) XML declaration of a document.
<?xml version='1.0'?>

@note This is not part of the SAX standard.


## lexicalHandler ##

If the application does not register a lexical handler, all
lexical events (e.g. startDTD) reported by the SAX parser will be
silently ignored.

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.


## setFeature ##

Set the value of a feature flag.

The feature name is any fully-qualified URI.  It is possible
for an XMLReader to expose a feature value but to be unable to
change the current value.  Some feature values may be immutable
or mutable only in specific contexts, such as before, during, or
after a parse.

All XMLReaders are required to support setting
http://xml.org/sax/features/namespaces to true and
http://xml.org/sax/features/namespace-prefixes to false.

@param name String flag for a parser feature.
@param value Turn the feature on/off.

@note This is currently supported only for
http://xml.org/sax/features/namespace-prefixes .  All other
features will result in a NOT_IMPLEMENTED exception.


## getFeature ##

Look up the value of a feature flag.

The feature name is any fully-qualified URI.  It is
possible for an XMLReader to recognize a feature name but
temporarily be unable to return its value.
Some feature values may be available only in specific
contexts, such as before, during, or after a parse.

All XMLReaders are required to recognize the
http://xml.org/sax/features/namespaces and the
http://xml.org/sax/features/namespace-prefixes feature names.

@param name String flag for a parser feature.

@note This is currently supported only for
http://xml.org/sax/features/namespace-prefixes .  All other
features will result in a NOT_IMPLEMENTED exception.


## setProperty ##

Set the value of a property. NOT CURRENTLY IMPLEMENTED.

The property name is any fully-qualified URI.  It is possible
for an XMLReader to recognize a property name but to be unable to
change the current value.  Some property values may be immutable
or mutable only in specific contexts, such as before, during, or
after a parse.

XMLReaders are not required to recognize setting any specific
property names, though a core set is defined by SAX2.

This method is also the standard mechanism for setting
extended handlers.

@param name String flag for a parser feature
@param value Turn the feature on/off.


## getProperty ##

Look up the value of a property. NOT CURRENTLY IMPLEMENTED.

The property name is any fully-qualified URI.  It is
possible for an XMLReader to recognize a property name but
temporarily be unable to return its value.
Some property values may be available only in specific
contexts, such as before, during, or after a parse.

XMLReaders are not required to recognize any specific
property names, though an initial core set is documented for
SAX2.

Implementors are free (and encouraged) to invent their own properties,
using names built on their own URIs.

@param name The property name, which is a fully-qualified URI.
@return The current value of the property.


## parseFromString ##


@param str The UTF16 string to be parsed
@param contentType The content type of the string (see parseFromStream)



## parseFromStream ##


@param stream The byte stream whose contents are parsed
@param charset The character set that was used to encode the byte
               stream. NULL if not specified.
@param contentType The content type of the string - either text/xml,
                   application/xml, or application/xhtml+xml.
                   Must not be NULL.



## parseAsync ##

Begin an asynchronous parse. This method initializes the parser,
and must be called before any nsIStreamListener methods. It is
then the caller's duty to call nsIStreamListener methods to drive
the parser. Once this method is called, the caller must not call
one of the other parse methods.

@param observer The nsIRequestObserver to notify upon start or stop.
                Can be NULL.

