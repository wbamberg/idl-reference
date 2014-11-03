---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/xpcom/base/nsIVersionComparator.idl">Source file</a>
</div>

# nsIVersionComparator #
  
Version strings are dot-separated sequences of version-parts.  
  
A version-part consists of up to four parts, all of which are optional:  
  
<number-a><string-b><number-c><string-d (everything else)>  
  
A version-part may also consist of a single asterisk "*" which indicates  
"infinity".  
  
Numbers are base-10, and are zero if left out.  
Strings are compared bytewise.  
  
For additional backwards compatibility, if "string-b" is "+" then  
"number-a" is incremented by 1 and "string-b" becomes "pre".  
  
1.0pre1  
< 1.0pre2    
  < 1.0 == 1.0.0 == 1.0.0.0  
    < 1.1pre == 1.1pre0 == 1.0+  
      < 1.1pre1a  
        < 1.1pre1  
          < 1.1pre10a  
            < 1.1pre10  
  
Although not required by this interface, it is recommended that  
numbers remain within the limits of a signed char, i.e. -127 to 128.  
  

## Methods ##

### compare(A, B) ###
  
Compare two version strings  
  

#### Parameters ####

<table>

<tr>
<td>A</td>
<td>The first version  
</td>
</tr>

<tr>
<td>B</td>
<td>The second version  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>< 0 if A < B  
         = 0 if A == B  
         > 0 if A > B  
</td>
</tr>

</table>
