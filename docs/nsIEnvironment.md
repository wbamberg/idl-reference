---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/threads/nsIEnvironment.idl">Source file</a>
</div>

# nsIEnvironment #
<pre>  
Scriptable access to the current process environment.  
  
  
</pre>
## Methods ##

### set(aName, aValue) ###
<pre>  
Set the value of an environment variable.  
  
@param aName   the variable name to set.  
@param aValue  the value to set.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>the variable name to set.  
</td>
</tr>

<tr>
<td>aValue</td>
<td>the value to set.  
</td>
</tr>

</table>

### get(aName) ###
<pre>  
Get the value of an environment variable.  
  
@param aName   the variable name to retrieve.  
@return        returns the value of the env variable. An empty string  
               will be returned when the env variable does not exist or  
               when the value itself is an empty string - please use  
               |exists()| to probe whether the env variable exists  
               or not.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>the variable name to retrieve.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>returns the value of the env variable. An empty string  
               will be returned when the env variable does not exist or  
               when the value itself is an empty string - please use  
               |exists()| to probe whether the env variable exists  
               or not.  
</td>
</tr>

</table>

### exists(aName) ###
<pre>  
Check the existence of an environment variable.  
This method checks whether an environment variable is present in  
the environment or not.  
  
- For Unix/Linux platforms we follow the Unix definition:  
An environment variable exists when |getenv()| returns a non-NULL value.  
An environment variable does not exist when |getenv()| returns NULL.  
- For non-Unix/Linux platforms we have to fall back to a   
"portable" definition (which is incorrect for Unix/Linux!!!!)  
which simply checks whether the string returned by |Get()| is empty  
or not.  
  
@param aName   the variable name to probe.  
@return        if the variable has been set, the value returned is  
               PR_TRUE. If the variable was not defined in the  
               environment PR_FALSE will be returned.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>aName</td>
<td>the variable name to probe.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>if the variable has been set, the value returned is  
               PR_TRUE. If the variable was not defined in the  
               environment PR_FALSE will be returned.  
</td>
</tr>

</table>
