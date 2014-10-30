---
layout: default
---

# nsISerializationHelper #

## Methods ##

### serializeToString(serializable) ###
  
Serialize the object to a base64 string. This string can be later passed  
as an input to deserializeObject method.  
  

### deserializeObject(input) ###
  
Takes base64 encoded string that cointains serialization of a single  
object. Most commonly, input is result of previous call to  
serializeToString.  
  
