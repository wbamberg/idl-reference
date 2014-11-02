---
layout: default
---

# nsIBrowserSearchService #

## Methods ##

### init(aObserver) ###
  
Start asynchronous initialization.  
  
The callback is triggered once initialization is complete, which may be  
immediately, if initialization has already been completed by some previous  
call to this method. The callback is always invoked asynchronously.  
  
@param aObserver An optional object observing the end of initialization.  
  

#### Parameters ####

<table>

<tr>
<td>aObserver</td>
<td>An optional object observing the end of initialization.  
</td>
</tr>

</table>

### addEngine(engineURL, dataType, iconURL, confirm, callback) ###
  
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
  

#### Parameters ####

<table>

<tr>
<td>engineURL</td>
<td>       The URL to the search engine's description file.  
</td>
</tr>

<tr>
<td>dataType</td>
<td>       An integer representing the plugin file format. Must be one  
       of the supported search engine data types defined above.  
</td>
</tr>

<tr>
<td>iconURL</td>
<td>       A URL string to an icon file to be used as the search engine's  
       icon. This value may be overridden by an icon specified in the  
       engine description file.  
</td>
</tr>

<tr>
<td>confirm</td>
<td>       A boolean value indicating whether the user should be asked for  
       confirmation before this engine is added to the list.  If this  
       value is false, the engine will be added to the list upon successful  
       load, but it will not be selected as the current engine.  
</td>
</tr>

<tr>
<td>callback</td>
<td>       A nsISearchInstallCallback that will be notified when the  
       addition is complete, or if the addition fails. It will not be  
       called if addEngine throws an exception.  
</td>
</tr>

</table>

### addEngineWithDetails(name, iconURL, alias, description, method, url, extensionID) ###
  
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
  

#### Parameters ####

<table>

<tr>
<td>name</td>
<td>       The search engine's name. Must be unique. Must not be null.  
</td>
</tr>

<tr>
<td>iconURL</td>
<td>       Optional: A URL string pointing to the icon to be used to represent  
       the engine.  
</td>
</tr>

<tr>
<td>alias</td>
<td>       Optional: A unique shortcut that can be used to retrieve the  
       search engine.  
</td>
</tr>

<tr>
<td>description</td>
<td>       Optional: a description of the search engine.  
</td>
</tr>

<tr>
<td>method</td>
<td>       The HTTP request method used when submitting a search query.  
       Must be a case insensitive value of either "get" or "post".  
</td>
</tr>

<tr>
<td>url</td>
<td>       The URL to which search queries should be sent.  
       Must not be null.  
</td>
</tr>

<tr>
<td>extensionID</td>
<td>[optional]  
       Optional: The correct extensionID if called by an add-on.  
</td>
</tr>

</table>

### restoreDefaultEngines() ###
  
Un-hides all engines installed in the directory corresponding to  
the directory service's NS_APP_SEARCH_DIR key. (i.e. the set of  
engines returned by getDefaultEngines)  
  

### getEngineByAlias(alias) ###
  
Returns an engine with the specified alias.  
  
@param   alias  
         The search engine's alias.  
@returns The corresponding nsISearchEngine object, or null if it doesn't  
         exist.  
  

#### Parameters ####

<table>

<tr>
<td>alias</td>
<td>         The search engine's alias.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The corresponding nsISearchEngine object, or null if it doesn't  
         exist.  
</td>
</tr>

</table>

### getEngineByName(aEngineName) ###
  
Returns an engine with the specified name.  
  
@param   aEngineName  
         The name of the engine.  
@returns The corresponding nsISearchEngine object, or null if it doesn't  
         exist.  
  

#### Parameters ####

<table>

<tr>
<td>aEngineName</td>
<td>         The name of the engine.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The corresponding nsISearchEngine object, or null if it doesn't  
         exist.  
</td>
</tr>

</table>

### getEngines(engineCount, engines) ###
  
Returns an array of all installed search engines.  
  
@returns an array of nsISearchEngine objects.  
  

#### Returns ####

<table>

<tr>
<td>an array of nsISearchEngine objects.  
</td>
</tr>

</table>

### getVisibleEngines(engineCount, engines) ###
  
Returns an array of all installed search engines whose hidden attribute is  
false.  
  
@returns an array of nsISearchEngine objects.  
  

#### Returns ####

<table>

<tr>
<td>an array of nsISearchEngine objects.  
</td>
</tr>

</table>

### getDefaultEngines(engineCount, engines) ###
  
Returns an array of all default search engines. This includes all loaded  
engines that aren't in the user's profile directory  
(NS_APP_USER_SEARCH_DIR).  
  
@returns an array of nsISearchEngine objects.  
  

#### Returns ####

<table>

<tr>
<td>an array of nsISearchEngine objects.  
</td>
</tr>

</table>

### moveEngine(engine, newIndex) ###
  
Moves a visible search engine.  
  
@param  engine  
        The engine to move.  
@param  newIndex  
        The engine's new index in the set of visible engines.  
  
@throws NS_ERROR_FAILURE if newIndex is out of bounds, or if engine is  
        hidden.  
  

#### Parameters ####

<table>

<tr>
<td>engine</td>
<td>        The engine to move.  
</td>
</tr>

<tr>
<td>newIndex</td>
<td>        The engine's new index in the set of visible engines.  
</td>
</tr>

</table>

### removeEngine(engine) ###
  
Removes the search engine. If the search engine is installed in a global  
location, this will just hide the engine. If the engine is in the user's  
profile directory, it will be removed from disk.  
  
@param  engine  
        The engine to remove.  
  

#### Parameters ####

<table>

<tr>
<td>engine</td>
<td>        The engine to remove.  
</td>
</tr>

</table>

### parseSubmissionURL(url) ###
  
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
  

#### Parameters ####

<table>

<tr>
<td>url</td>
<td>       String containing the URL to parse, for example  
       "https://www.google.com/search?q=terms".  
</td>
</tr>

</table>

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
  
