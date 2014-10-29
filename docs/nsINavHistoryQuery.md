---
layout: default
---

# nsINavHistoryQuery #

This object encapsulates all the query parameters you're likely to need
when building up history UI. All parameters are ANDed together.

This is not intended to be a super-general query mechanism. This was designed
so that most queries can be done in only one SQL query. This is important
because, if the user has their profile on a networked drive, query latency
can be non-negligible.


## TIME_RELATIVE_EPOCH ##

Time range for results (INCLUSIVE). The *TimeReference is one of the
constants TIME_RELATIVE_* which indicates how to interpret the
corresponding time value.
  TIME_RELATIVE_EPOCH (default):
    The time is relative to Jan 1 1970 GMT, (this is a normal PRTime)
  TIME_RELATIVE_TODAY:
    The time is relative to this morning at midnight. Normally used for
    queries relative to today. For example, a "past week" query would be
    today-6 days -> today+1 day
  TIME_RELATIVE_NOW:
    The time is relative to right now.

Note: PRTime is in MICROseconds since 1 Jan 1970. Javascript date objects
are expressed in MILLIseconds since 1 Jan 1970.

As a special case, a 0 time relative to TIME_RELATIVE_EPOCH indicates that
the time is not part of the query. This is the default, so an empty query
will match any time. The has* functions return whether the corresponding
time is considered.

You can read absolute*Time to get the time value that the currently loaded
reference points + offset resolve to.


## TIME_RELATIVE_TODAY ##

## TIME_RELATIVE_NOW ##

## beginTime ##

## beginTimeReference ##

## hasBeginTime ##

## absoluteBeginTime ##

## endTime ##

## endTimeReference ##

## hasEndTime ##

## absoluteEndTime ##

## searchTerms ##

Text search terms.


## hasSearchTerms ##

## minVisits ##

Set lower or upper limits for how many times an item has been
visited.  The default is -1, and in that case all items are
matched regardless of their visit count.


## maxVisits ##

## setTransitions ##

When the set of transitions is nonempty, results are limited to pages which
have at least one visit for each of the transition types.
@note: For searching on more than one transition this can be very slow.

Limit results to the specified list of transition types.


## getTransitions ##

Get the transitions set for this query.


## transitionCount ##

Get the count of the set query transitions.


## onlyBookmarked ##

When set, returns only bookmarked items, when unset, returns anything. Setting this
is equivalent to listing all bookmark folders in the 'folders' parameter.


## domainIsHost ##

This controls the meaning of 'domain', and whether it is an exact match
'domainIsHost' = true, or hierarchical (= false).


## domain ##

This is the host or domain name (controlled by domainIsHost). When
domainIsHost, domain only does exact matching on host names. Otherwise,
it will return anything whose host name ends in 'domain'.

This one is a little different than most. Setting it to an empty string
is a real query and will match any URI that has no host name (local files
and such). Set this to NULL (in C++ use SetIsVoid) if you don't want
domain matching.


## hasDomain ##

## uriIsPrefix ##

Controls the interpretation of 'uri'. When unset (default), the URI will
request an exact match of the specified URI. When set, any history entry
beginning in 'uri' will match. For example "http://bar.com/foo" will match
"http://bar.com/foo" as well as "http://bar.com/foo/baz.gif".


## uri ##

This is a URI to match, to, for example, find out every time you visited
a given URI. Use uriIsPrefix to control whether this is an exact match.


## hasUri ##

## annotationIsNot ##

Test for existence or non-existence of a given annotation. We don't
currently support >1 annotation name per query. If 'annotationIsNot' is
true, we test for the non-existence of the specified annotation.

Testing for not annotation will do the same thing as a normal query and
remove everything that doesn't have that annotation. Asking for things
that DO have a given annotation is a little different. It also includes
things that have never been visited. This allows place queries to be
returned as well as anything else that may have been tagged with an
annotation. This will only work for RESULTS_AS_URI since there will be
no visits for these items.


## annotation ##

## hasAnnotation ##

## tags ##

Limit results to items that are tagged with all of the given tags.  This
attribute must be set to an array of strings.  When called as a getter it
will return an array of strings sorted ascending in lexicographical order.
The array may be empty in either case.  Duplicate tags may be specified
when setting the attribute, but the getter returns only unique tags.

To search for items that are tagged with any given tags rather than all,
multiple queries may be passed to nsINavHistoryService.executeQueries().


## tagsAreNot ##

If 'tagsAreNot' is true, the results are instead limited to items that
are not tagged with any of the given tags.  This attribute is used in
conjunction with the 'tags' attribute.


## getFolders ##

Limit results to items that are in all of the given folders.


## folderCount ##

## setFolders ##

For the special result type RESULTS_AS_TAG_CONTENTS we can define only
one folder that must be a tag folder. This is not recursive so results
will be returned from the first level of that folder.


## clone ##

Creates a new query item with the same parameters of this one.

