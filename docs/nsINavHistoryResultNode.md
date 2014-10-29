---
layout: default
---

# nsINavHistoryResultNode #

## parent ##

Indentifies the parent result node in the result set. This is null for
top level nodes.


## parentResult ##

The history-result to which this node belongs.


## uri ##

URI of the resource in question. For visits and URLs, this is the URL of
the page. For folders and queries, this is the place: URI of the
corresponding folder or query. This may be empty for other types of
objects like host containers.


## RESULT_TYPE_URI ##

Identifies the type of this node. This node can then be QI-ed to the
corresponding specialized result node interface.


## RESULT_TYPE_QUERY ##

## RESULT_TYPE_FOLDER ##

## RESULT_TYPE_SEPARATOR ##

## RESULT_TYPE_FOLDER_SHORTCUT ##

## type ##

## title ##

Title of the web page, or of the node's query (day, host, folder, etc)


## accessCount ##

Total number of times the URI has ever been accessed. For hosts, this
is the total of the children under it, NOT the total times the host has
been accessed (this would require an additional query, so is not given
by default when most of the time it is never needed).


## time ##

This is the time the user accessed the page.

If this is a visit, it is the exact time that the page visit occurred.

If this is a URI, it is the most recent time that the URI was visited.
Even if you ask for all URIs for a given date range long ago, this might
contain today's date if the URI was visited today.

For hosts, or other node types with children, this is the most recent
access time for any of the children.

For days queries this is the respective endTime - a maximum possible
visit time to fit in the day range.


## icon ##

This URI can be used as an image source URI and will give you the favicon
for the page. It is *not* the URI of the favicon, but rather something
that will resolve to the actual image.

In most cases, this is an annotation URI that will query the favicon
service. If the entry has no favicon, this is the chrome URI of the
default favicon. If the favicon originally lived in chrome, this will
be the original chrome URI of the icon.


## indentLevel ##

This is the number of levels between this node and the top of the
hierarchy. The members of result.children have indentLevel = 0, their
children have indentLevel = 1, etc. The indent level of the root node is
set to -1.


## bookmarkIndex ##

When this item is in a bookmark folder (parent is of type folder), this is
the index into that folder of this node. These indices start at 0 and
increase in the order that they appear in the bookmark folder. For items
that are not in a bookmark folder, this value is -1.


## itemId ##

If the node is an item (bookmark, folder or a separator) this value is the
row ID of that bookmark in the database. For other nodes, this value is
set to -1.


## dateAdded ##

If the node is an item (bookmark, folder or a separator) this value is the 
time that the item was created. For other nodes, this value is 0.


## lastModified ##

If the node is an item (bookmark, folder or a separator) this value is the 
time that the item was last modified. For other nodes, this value is 0.

 @note When an item is added lastModified is set to the same value as
       dateAdded.


## tags ##

For uri nodes, this is a sorted list of the tags, delimited with commans,
for the uri represented by this node. Otherwise this is an empty string.


## pageGuid ##

The unique ID associated with the page. It my return an empty string
if the result node is a non-URI node.


## bookmarkGuid ##

The unique ID associated with the bookmark. It returns an empty string
if the result node is not associated with a bookmark, a folder or a
separator.

