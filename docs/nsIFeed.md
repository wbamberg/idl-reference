---
layout: default
---

# nsIFeed #

An nsIFeed represents a single Atom or RSS feed.


## subtitle ##
 
Uses description, subtitle, and extensions
to generate a summary. 


## TYPE_FEED ##

## TYPE_AUDIO ##

## TYPE_IMAGE ##

## TYPE_VIDEO ##

## type ##

The type of feed. For example, a podcast would be TYPE_AUDIO.


## enclosureCount ##

The total number of enclosures found in the feed.


## items ##

The items or entries in feed.


## cloud ##

No one really knows what cloud is for.

It supposedly enables some sort of interaction with an XML-RPC or
SOAP service.


## generator ##

Information about the software that produced the feed.


## image ##

An image url and some metadata (as defined by RSS2).



## textInput ##

No one really knows what textInput is for.

See
<http://www.cadenhead.org/workbench/news/2894/rss-joy-textinput>
for more details.


## skipDays ##

Days to skip fetching. This field was supposed to designate
intervals for feed fetching. It's not generally implemented. For
example, if this array contained "Monday", aggregators should not
fetch the feed on Mondays.


## skipHours ##

Hours to skip fetching. This field was supposed to designate
intervals for feed fetching. It's not generally implemented. See
<http://blogs.law.harvard.edu/tech/rss> for more information.

