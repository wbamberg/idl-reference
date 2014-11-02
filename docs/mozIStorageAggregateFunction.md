---
layout: default
---

# mozIStorageAggregateFunction #
  
mozIStorageAggregateFunction represents aggregate SQL function.  
Common examples of aggregate functions are SUM() and COUNT().  
  
An aggregate function calculates one result for a given set of data, where  
a set of data is a group of tuples. There can be one group  
per request or many of them, if GROUP BY clause is used or not.  
  

## Methods ##

### onStep(aFunctionArguments) ###
  
onStep is called when next value should be passed to  
a custom function.  
  
@param aFunctionArguments    The arguments passed in to the function  
  

#### Parameters ####

<table>

<tr>
<td>aFunctionArguments</td>
<td>The arguments passed in to the function  
</td>
</tr>

</table>

### onFinal() ###
  
Called when all tuples in a group have been processed and the engine  
needs the aggregate function's value.  
  
@returns aggregate result as Variant.  
  

#### Returns ####

<table>

<tr>
<td>aggregate result as Variant.  
</td>
</tr>

</table>
