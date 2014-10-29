---
layout: default
---

# nsIBrowserSearchService #

## Methods ##

### init ###

Start asynchronous initialization.

The callback is triggered once initialization is complete, which may be
immediately, if initialization has already been completed by some previous
call to this method. The callback is always invoked asynchronously.

@param aObserver An optional object observing the end of initialization.


### addEngine ###

Adds a new search engine from the file at the supplied URI, optionally
asking the user for confirmation first.  If a confirmation dialog is
shown, it will offer the option to begin using the newly added engine
right away.

@param engineURL
       The URL to the search engine's description file.

@param dataType
       An integer representing the plugin file format. Must be one
       of the supported search engine data types defined above.

@param iconURL
       A URL string to an icon file to be used as the search engine's
       icon. This value may be overridden by an icon specified in the
       engine description file.

@param confirm
       A boolean value indicating whether the user should be asked for
       confirmation before this engine is added to the list.  If this
       value is false, the engine will be added to the list upon successful
       load, but it will not be selected as the current engine.

@param callback
       A nsISearchInstallCallback that will be notified when the
       addition is complete, or if the addition fails. It will not be
       called if addEngine throws an exception.

@throws NS_ERROR_FAILURE if the type is invalid, or if the description
        file cannot be successfully loaded.


### addEngineWithDetails ###

Adds a new search engine, without asking the user for confirmation and
without starting to use it right away.

@param name
       The search engine's name. Must be unique. Must not be null.

@param iconURL
       Optional: A URL string pointing to the icon to be used to represent
       the engine.

@param alias
       Optional: A unique shortcut that can be used to retrieve the
       search engine.

@param description
       Optional: a description of the search engine.

@param method
       The HTTP request method used when submitting a search query.
       Must be a case insensitive value of either "get" or "post".

@param url
       The URL to which search queries should be sent.
       Must not be null.

@param extensionID [optional]
       Optional: The correct extensionID if called by an add-on.


### restoreDefaultEngines ###

Un-hides all engines installed in the directory corresponding to
the directory service's NS_APP_SEARCH_DIR key. (i.e. the set of
engines returned by getDefaultEngines)


### getEngineByAlias ###

Returns an engine with the specified alias.

@param   alias
         The search engine's alias.
@returns The corresponding nsISearchEngine object, or null if it doesn't
         exist.


### getEngineByName ###

Returns an engine with the specified name.

@param   aEngineName
         The name of the engine.
@returns The corresponding nsISearchEngine object, or null if it doesn't
         exist.


### getEngines ###

Returns an array of all installed search engines.

@returns an array of nsISearchEngine objects.


### getVisibleEngines ###

Returns an array of all installed search engines whose hidden attribute is
false.

@returns an array of nsISearchEngine objects.


### getDefaultEngines ###

Returns an array of all default search engines. This includes all loaded
engines that aren't in the user's profile directory
(NS_APP_USER_SEARCH_DIR).

@returns an array of nsISearchEngine objects.


### moveEngine ###

Moves a visible search engine.

@param  engine
        The engine to move.
@param  newIndex
        The engine's new index in the set of visible engines.

@throws NS_ERROR_FAILURE if newIndex is out of bounds, or if engine is
        hidden.


### removeEngine ###

Removes the search engine. If the search engine is installed in a global
location, this will just hide the engine. If the engine is in the user's
profile directory, it will be removed from disk.

@param  engine
        The engine to remove.


### parseSubmissionURL ###

Determines if the provided URL represents results from a search engine, and
provides details about the match.

The lookup mechanism checks whether the domain name and path of the
provided HTTP or HTTPS URL matches one of the known values for the visible
search engines.  The match does not depend on which of the schemes is used.
The expected URI parameter for the search terms must exist in the query
string, but other parameters are ignored.

@param url
       String containing the URL to parse, for example
       "https://www.google.com/search?q=terms".


## Attributes ##

### isInitialized ###

Determine whether initialization has been completed.

Clients of the service can use this attribute to quickly determine whether
initialization is complete, and decide to trigger some immediate treatment,
to launch asynchronous initialization or to bailout.

Note that this attribute does not indicate that initialization has succeeded.

@return |true| if the search service is now initialized, |false| if
initialization has not been triggered yet.


### defaultEngine ###

The default search engine. Returns the first visible engine if the default
engine is hidden. May be null if there are no visible search engines.


### currentEngine ###

The currently active search engine. May be null if there are no visible
search engines.

