---
layout: default
---

# nsIFeedContainer #

A shared base for feeds and items, which are pretty similar,
but they have some divergent attributes and require
different convenience methods.


## Methods ##

### normalize ###

Syncs a container's fields with its convenience attributes.


## Attributes ##

### id ###

Many feeds contain an ID distinct from their URI, and
entries have standard fields for this in all major formats.


### fields ###

The fields found in the document. Common Atom
and RSS fields are normalized. This includes some namespaced
extensions such as dc:subject and content:encoded. 
Consumers can avoid normalization by checking the feed type
and accessing specific fields.

Common namespaces are accessed using prefixes, like get("dc:subject");.
See nsIFeedResult::registerExtensionPrefix.


### title ###

Sometimes there's no title, or the title contains markup, so take
care in decoding the attribute.


### link ###

Returns the primary link for the feed or entry.


### links ###

Returns all links for a feed or entry.


### categories ###

Returns the categories found in a feed or entry.


### rights ###

The rights or license associated with a feed or entry.


### authors ###

A list of nsIFeedPersons that authored the feed.


### contributors ###

A list of nsIFeedPersons that contributed to the feed.


### updated ###

The date the feed was updated, in RFC822 form. Parsable by JS
and mail code.

