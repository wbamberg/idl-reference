---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/xul/templates/nsIXULTemplateRuleFilter.idl">Source file</a>
</div>
# nsIXULTemplateRuleFilter #
  
A rule filter may be used to add additional filtering of results to a rule.  
The filter is used to further reject results from matching the template's  
rules, beyond what the template syntax can do itself, thus allowing for  
more complex result filtering. The rule filter is applied after the rule  
syntax within the template.  
  
Only one filter may apply to each rule within the template and may be  
assigned using the template builder's addRuleFilter method.  
  

## Methods ##

### match(aRef, aRule) ###
  
Evaluate a result and return true if the result is accepted by this  
filter, or false if it is rejected. Accepted results will have output  
generated for them for the rule. Rejected results will not, but they  
may still match another rule.  
  
@param aRef the result to examine  
@param aRule the rule node  
  
@return true if the rule matches  
  

#### Parameters ####

<table>

<tr>
<td>aRef</td>
<td>the result to examine  
</td>
</tr>

<tr>
<td>aRule</td>
<td>the rule node  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if the rule matches  
</td>
</tr>

</table>
