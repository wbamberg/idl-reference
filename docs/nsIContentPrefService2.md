---
layout: default
---

# nsIContentPrefService2 #
  
Content Preferences  
  
Content preferences allow the application to associate arbitrary data, or  
"preferences", with specific domains, or web "content".  Specifically, a  
content preference is a structure with three values: a domain with which the  
preference is associated, a name that identifies the preference within its  
domain, and a value.  (See nsIContentPref below.)  
  
For example, if you want to remember the user's preference for a certain zoom  
level on www.mozilla.org pages, you might store a preference whose domain is  
"www.mozilla.org", whose name is "zoomLevel", and whose value is the numeric  
zoom level.  
  
A preference need not have a domain, and in that case the preference is  
called a "global" preference.  This interface doesn't impart any special  
significance to global preferences; they're simply name-value pairs that  
aren't associated with any particular domain.  As a consumer of this  
interface, you might choose to let a global preference override all non-  
global preferences of the same name, for example, for whatever definition of  
"override" is appropriate for your use case.  
  
  
Domain Parameters  
  
Many methods of this interface accept a "domain" parameter.  Domains may be  
specified either exactly, like "example.com", or as full URLs, like  
"http://example.com/foo/bar".  In the latter case the API extracts the full  
domain from the URL, so if you specify "http://foo.bar.example.com/baz", the  
domain is taken to be "foo.bar.example.com", not "example.com".  
  
  
Private-Browsing Context Parameters  
  
Many methods also accept a "context" parameter.  This parameter relates to  
private browsing and determines the kind of storage that a method uses,  
either the usual permanent storage or temporary storage set aside for private  
browsing sessions.  
  
Pass null to unconditionally use permanent storage.  Pass an nsILoadContext  
to use storage appropriate to the context's usePrivateBrowsing attribute: if  
usePrivateBrowsing is true, temporary private-browsing storage is used, and  
otherwise permanent storage is used.  A context can be obtained from the  
window or channel whose content pertains to the preferences being modified or  
retrieved.  
  
  
Callbacks  
  
The methods of callback objects are always called asynchronously.  
  
Observers are called after callbacks are called, but they are called in the  
same turn of the event loop as callbacks.  
  
See nsIContentPrefCallback2 below for more information about callbacks.  
  

## Methods ##

### getByName(name, context, callback) ###
  
Gets all the preferences with the given name.  
  
@param name      The preferences' name.  
@param context   The private-browsing context, if any.  
@param callback  handleResult is called once for each preference unless  
                 no such preferences exist, in which case handleResult  
                 is not called at all.  
  

#### Parameters ####

<table>

<tr>
<td>name</td>
<td>The preferences' name.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>callback</td>
<td>handleResult is called once for each preference unless  
                 no such preferences exist, in which case handleResult  
                 is not called at all.  
</td>
</tr>

</table>

### getByDomainAndName(domain, name, context, callback) ###
  
Gets the preference with the given domain and name.  
  
@param domain    The preference's domain.  
@param name      The preference's name.  
@param context   The private-browsing context, if any.  
@param callback  handleResult is called once unless no such preference  
                 exists, in which case handleResult is not called at all.  
  

#### Parameters ####

<table>

<tr>
<td>domain</td>
<td>The preference's domain.  
</td>
</tr>

<tr>
<td>name</td>
<td>The preference's name.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>callback</td>
<td>handleResult is called once unless no such preference  
                 exists, in which case handleResult is not called at all.  
</td>
</tr>

</table>

### getBySubdomainAndName(domain, name, context, callback) ###
  
Gets all preferences with the given name whose domains are either the same  
as or subdomains of the given domain.  
  
@param domain    The preferences' domain.  
@param name      The preferences' name.  
@param context   The private-browsing context, if any.  
@param callback  handleResult is called once for each preference.  If no  
                 such preferences exist, handleResult is not called at all.  
  

#### Parameters ####

<table>

<tr>
<td>domain</td>
<td>The preferences' domain.  
</td>
</tr>

<tr>
<td>name</td>
<td>The preferences' name.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>callback</td>
<td>handleResult is called once for each preference.  If no  
                 such preferences exist, handleResult is not called at all.  
</td>
</tr>

</table>

### getGlobal(name, context, callback) ###
  
Gets the preference with no domain and the given name.  
  
@param name      The preference's name.  
@param context   The private-browsing context, if any.  
@param callback  handleResult is called once unless no such preference  
                 exists, in which case handleResult is not called at all.  
  

#### Parameters ####

<table>

<tr>
<td>name</td>
<td>The preference's name.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>callback</td>
<td>handleResult is called once unless no such preference  
                 exists, in which case handleResult is not called at all.  
</td>
</tr>

</table>

### getCachedByDomainAndName(domain, name, context) ###
  
Synchronously retrieves from the in-memory cache the preference with the  
given domain and name.  
  
In addition to caching preference values, the cache also keeps track of  
preferences that are known not to exist.  If the preference is known not to  
exist, the value attribute of the returned object will be undefined  
(nsIDataType::VTYPE_VOID).  
  
If the preference is neither cached nor known not to exist, then null is  
returned, and get() must be called to determine whether the preference  
exists.  
  
@param domain   The preference's domain.  
@param name     The preference's name.  
@param context  The private-browsing context, if any.  
@return         The preference, or null if no such preference is known to  
                exist.  
  

#### Parameters ####

<table>

<tr>
<td>domain</td>
<td>The preference's domain.  
</td>
</tr>

<tr>
<td>name</td>
<td>The preference's name.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

</table>

### getCachedBySubdomainAndName(domain, name, context, len, prefs) ###
  
Synchronously retrieves from the in-memory cache all preferences with the  
given name whose domains are either the same as or subdomains of the given  
domain.  
  
The preferences are returned in an array through the out-parameter.  If a  
preference for a particular subdomain is known not to exist, then an object  
corresponding to that preference will be present in the array, and, as with  
getCachedByDomainAndName, its value attribute will be undefined.  
  
@param domain   The preferences' domain.  
@param name     The preferences' name.  
@param context  The private-browsing context, if any.  
@param len      The length of the returned array.  
@param prefs    The array of preferences.  
  

#### Parameters ####

<table>

<tr>
<td>domain</td>
<td>The preferences' domain.  
</td>
</tr>

<tr>
<td>name</td>
<td>The preferences' name.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>len</td>
<td>The length of the returned array.  
</td>
</tr>

<tr>
<td>prefs</td>
<td>The array of preferences.  
</td>
</tr>

</table>

### getCachedGlobal(name, context) ###
  
Synchronously retrieves from the in-memory cache the preference with no  
domain and the given name.  
  
As with getCachedByDomainAndName, if the preference is cached then it is  
returned; if the preference is known not to exist, then the value attribute  
of the returned object will be undefined; if the preference is neither  
cached nor known not to exist, then null is returned.  
  
@param name     The preference's name.  
@param context  The private-browsing context, if any.  
@return         The preference, or null if no such preference is known to  
                exist.  
  

#### Parameters ####

<table>

<tr>
<td>name</td>
<td>The preference's name.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

</table>

### set(domain, name, value, context, callback) ###
  
Sets a preference.  
  
@param domain    The preference's domain.  
@param name      The preference's name.  
@param value     The preference's value.  
@param context   The private-browsing context, if any.  
@param callback  handleCompletion is called when the preference has been  
                 stored.  
  

#### Parameters ####

<table>

<tr>
<td>domain</td>
<td>The preference's domain.  
</td>
</tr>

<tr>
<td>name</td>
<td>The preference's name.  
</td>
</tr>

<tr>
<td>value</td>
<td>The preference's value.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>callback</td>
<td>handleCompletion is called when the preference has been  
                 stored.  
</td>
</tr>

</table>

### setGlobal(name, value, context, callback) ###
  
Sets a preference with no domain.  
  
@param name      The preference's name.  
@param value     The preference's value.  
@param context   The private-browsing context, if any.  
@param callback  handleCompletion is called when the preference has been  
                 stored.  
  

#### Parameters ####

<table>

<tr>
<td>name</td>
<td>The preference's name.  
</td>
</tr>

<tr>
<td>value</td>
<td>The preference's value.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>callback</td>
<td>handleCompletion is called when the preference has been  
                 stored.  
</td>
</tr>

</table>

### removeByDomainAndName(domain, name, context, callback) ###
  
Removes the preference with the given domain and name.  
  
@param domain    The preference's domain.  
@param name      The preference's name.  
@param context   The private-browsing context, if any.  
@param callback  handleCompletion is called when the operation completes.  
  

#### Parameters ####

<table>

<tr>
<td>domain</td>
<td>The preference's domain.  
</td>
</tr>

<tr>
<td>name</td>
<td>The preference's name.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>callback</td>
<td>handleCompletion is called when the operation completes.  
</td>
</tr>

</table>

### removeBySubdomainAndName(domain, name, context, callback) ###
  
Removes all the preferences with the given name whose domains are either  
the same as or subdomains of the given domain.  
  
@param domain    The preferences' domain.  
@param name      The preferences' name.  
@param context   The private-browsing context, if any.  
@param callback  handleCompletion is called when the operation completes.  
  

#### Parameters ####

<table>

<tr>
<td>domain</td>
<td>The preferences' domain.  
</td>
</tr>

<tr>
<td>name</td>
<td>The preferences' name.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>callback</td>
<td>handleCompletion is called when the operation completes.  
</td>
</tr>

</table>

### removeGlobal(name, context, callback) ###
  
Removes the preference with no domain and the given name.  
  
@param name      The preference's name.  
@param context   The private-browsing context, if any.  
@param callback  handleCompletion is called when the operation completes.  
  

#### Parameters ####

<table>

<tr>
<td>name</td>
<td>The preference's name.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>callback</td>
<td>handleCompletion is called when the operation completes.  
</td>
</tr>

</table>

### removeByDomain(domain, context, callback) ###
  
Removes all preferences with the given domain.  
  
@param domain    The preferences' domain.  
@param context   The private-browsing context, if any.  
@param callback  handleCompletion is called when the operation completes.  
  

#### Parameters ####

<table>

<tr>
<td>domain</td>
<td>The preferences' domain.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>callback</td>
<td>handleCompletion is called when the operation completes.  
</td>
</tr>

</table>

### removeBySubdomain(domain, context, callback) ###
  
Removes all preferences whose domains are either the same as or subdomains  
of the given domain.  
  
@param domain    The preferences' domain.  
@param context   The private-browsing context, if any.  
@param callback  handleCompletion is called when the operation completes.  
  

#### Parameters ####

<table>

<tr>
<td>domain</td>
<td>The preferences' domain.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>callback</td>
<td>handleCompletion is called when the operation completes.  
</td>
</tr>

</table>

### removeByName(name, context, callback) ###
  
Removes all preferences with the given name regardless of domain, including  
global preferences with the given name.  
  
@param name      The preferences' name.  
@param context   The private-browsing context, if any.  
@param callback  handleCompletion is called when the operation completes.  
  

#### Parameters ####

<table>

<tr>
<td>name</td>
<td>The preferences' name.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>callback</td>
<td>handleCompletion is called when the operation completes.  
</td>
</tr>

</table>

### removeAllDomains(context, callback) ###
  
Removes all non-global preferences -- in other words, all preferences that  
have a domain.  
  
@param context   The private-browsing context, if any.  
@param callback  handleCompletion is called when the operation completes.  
  

#### Parameters ####

<table>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>callback</td>
<td>handleCompletion is called when the operation completes.  
</td>
</tr>

</table>

### removeAllDomainsSince(since, context, callback) ###
  
Removes all non-global preferences created after and including |since|.  
  
@param since     Timestamp in milliseconds.  
@param context   The private-browsing context, if any.  
@param callback  handleCompletion is called when the operation completes.  
  

#### Parameters ####

<table>

<tr>
<td>since</td>
<td>Timestamp in milliseconds.  
</td>
</tr>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>callback</td>
<td>handleCompletion is called when the operation completes.  
</td>
</tr>

</table>

### removeAllGlobals(context, callback) ###
  
Removes all global preferences -- in other words, all preferences that have  
no domain.  
  
@param context   The private-browsing context, if any.  
@param callback  handleCompletion is called when the operation completes.  
  

#### Parameters ####

<table>

<tr>
<td>context</td>
<td>The private-browsing context, if any.  
</td>
</tr>

<tr>
<td>callback</td>
<td>handleCompletion is called when the operation completes.  
</td>
</tr>

</table>

### addObserverForName(name, observer) ###
  
Registers an observer that will be notified whenever a preference with the  
given name is set or removed.  
  
When a set or remove method is called, observers are called after the set  
or removal completes and after the method's callback is called, and they  
are called in the same turn of the event loop as the callback.  
  
The service holds a strong reference to the observer, so the observer must  
be removed later to avoid leaking it.  
  
@param name      The name of the preferences to observe.  Pass null to  
                 observe all preference changes regardless of name.  
@param observer  The observer.  
  

#### Parameters ####

<table>

<tr>
<td>name</td>
<td>The name of the preferences to observe.  Pass null to  
                 observe all preference changes regardless of name.  
</td>
</tr>

<tr>
<td>observer</td>
<td>The observer.  
</td>
</tr>

</table>

### removeObserverForName(name, observer) ###
  
Unregisters an observer for the given name.  
  
@param name      The name for which the observer was registered.  Pass null  
                 if the observer was added with a null name.  
@param observer  The observer.  
  

#### Parameters ####

<table>

<tr>
<td>name</td>
<td>The name for which the observer was registered.  Pass null  
                 if the observer was added with a null name.  
</td>
</tr>

<tr>
<td>observer</td>
<td>The observer.  
</td>
</tr>

</table>

### extractDomain(str) ###
  
Extracts and returns the domain from the given string representation of a  
URI.  This is how the API extracts domains from URIs passed to it.  
  
@param str  The string representation of a URI, like  
            "http://example.com/foo/bar".  
@return     If the given string is a valid URI, the domain of that URI is  
            returned.  Otherwise, the string itself is returned.  
  

#### Parameters ####

<table>

<tr>
<td>str</td>
<td>The string representation of a URI, like  
            "http://example.com/foo/bar".  
</td>
</tr>

</table>
