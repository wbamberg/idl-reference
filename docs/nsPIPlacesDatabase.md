---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/places/nsPIPlacesDatabase.idl">Source file</a>
</div>

# nsPIPlacesDatabase #
<pre>  
This is a private interface used by Places components to get access to the  
database.  If outside consumers wish to use this, they should only read from  
the database so they do not break any internal invariants.  
  
</pre>
## Methods ##

### asyncExecuteLegacyQueries(aQueries, aQueryCount, aOptions, aCallback) ###
<pre>  
Asynchronously executes the statement created from queries.  
  
@see nsINavHistoryService::executeQueries  
@note THIS IS A TEMPORARY API.  Don't rely on it, since it will be replaced  
      in future versions by a real async querying API.  
@note Results obtained from this method differ from results obtained from  
      executeQueries, because there is additional filtering and sorting  
      done by the latter.  Thus you should use executeQueries, unless you  
      are absolutely sure that the returned results are fine for  
      your use-case.  
  
</pre>
## Attributes ##

### DBConnection ###
<pre>  
The database connection used by Places.  
  
</pre>