---
layout: default
---

# nsIFeedEntry #

An nsIFeedEntry represents an Atom or RSS entry/item. Summary
and/or full-text content may be available, but callers will have to
check both.


## Attributes ##

### summary ###

Uses description, subtitle, summary, content and extensions
to generate a summary. 



### published ###

The date the entry was published, in RFC822 form. Parsable by JS
and mail code.


### content ###

Uses atom:content and content:encoded to provide
a 'full text' view of an entry.



### enclosures ###

Enclosures are podcasts, photocasts, etc.


### mediaContent ###

Enclosures, etc. that might be displayed inline.

