---
layout: default
---

# nsISAXAttributes #

Interface for a list of XML attributes.

This interface allows access to a list of attributes in
three different ways:

1.) by attribute index;
2.) by Namespace-qualified name; or
3.) by XML qualified name.

The list will not contain attributes that were declared #IMPLIED
but not specified in the start tag.  It will also not contain
attributes used as Namespace declarations (xmlns*) unless the
http://xml.org/sax/features/namespace-prefixes feature
is set to true (it is false by default).

The order of attributes in the list is unspecified.


## Methods ##

### getIndexFromName ###

Look up the index of an attribute by Namespace name.
@param uri The Namespace URI, or the empty string
           if the name has no Namespace URI.
@param localName The attribute's local name.
@return The index of the attribute, or -1
        if it does not appear in the list.


### getIndexFromQName ###

Look up the index of an attribute by XML qualified name.
@param qName The qualified name.
@return The index of the attribute, or -1
        if it does not appear in the list.


### getLocalName ###

Look up an attribute's local name by index.
@param index The attribute index (zero-based).
@return The local name, or null if the index is out of range.


### getQName ###

Look up an attribute's XML qualified name by index.
@param index The attribute index (zero-based).
@return The XML qualified name, or the empty string if none is
        available, or null if the index is out of range.


### getType ###

Look up an attribute's type by index. The attribute type is one
of the strings "CDATA", "ID", "IDREF", "IDREFS", "NMTOKEN",
"NMTOKENS", "ENTITY", "ENTITIES", or "NOTATION" (always in upper
case). If the parser has not read a declaration for the
attribute, or if the parser does not report attribute types, then
it must return the value "CDATA" as stated in the XML 1.0
Recommendation (clause 3.3.3, "Attribute-Value
Normalization"). For an enumerated attribute that is not a
notation, the parser will report the type as "NMTOKEN".

@param index The attribute index (zero-based).
@return The attribute's type as a string, or null if the index is
        out of range.


### getTypeFromName ###

Look up an attribute's type by Namespace name.
@param uri The Namespace URI, or the empty string
            if the name has no Namespace URI.
@param localName The attribute's local name.
@return The attribute type as a string, or null if the attribute
        is not in the list.


### getTypeFromQName ###

Look up an attribute's type by XML qualified name.
@param qName The qualified name.
@return The attribute type as a string, or null if the attribute
        is not in the list.


### getURI ###

Look up an attribute's Namespace URI by index.
@param index The attribute index (zero-based).
@return The Namespace URI, or the empty string if none is available,
        or null if the index is out of range.


### getValue ###

Look up an attribute's value by index.  If the attribute value is
a list of tokens (IDREFS, ENTITIES, or NMTOKENS), the tokens will
be concatenated into a single string with each token separated by
a single space.

@param index The attribute index (zero-based).
@return The attribute's value as a string, or null if the index is
        out of range.


### getValueFromName ###

Look up an attribute's value by Namespace name.  If the attribute
value is a list of tokens (IDREFS, ENTITIES, or NMTOKENS), the
tokens will be concatenated into a single string with each token
separated by a single space.

@param uri The Namespace URI, or the empty string
            if the name has no Namespace URI.
@param localName The attribute's local name.
@return The attribute's value as a string, or null if the attribute is
        not in the list.


### getValueFromQName ###

Look up an attribute's value by XML qualified (prefixed) name.
If the attribute value is a list of tokens (IDREFS, ENTITIES, or
NMTOKENS), the tokens will be concatenated into a single string
with each token separated by a single space.

@param qName The qualified (prefixed) name.
@return The attribute's value as a string, or null if the attribute is
        not in the list.


## Attributes ##

### length ###

Return the number of attributes in the list. Once you know the
number of attributes, you can iterate through the list.

@return The number of attributes in the list.

