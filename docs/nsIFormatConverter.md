---
layout: default
---

# nsIFormatConverter #

## Methods ##

### getInputDataFlavors ###

Get the list of the "input" data flavors (mime types as nsISupportsCString),
in otherwords, the flavors that this converter can convert "from" (the 
incoming data to the converter).


### getOutputDataFlavors ###

Get the list of the "output" data flavors (mime types as nsISupportsCString),
in otherwords, the flavors that this converter can convert "to" (the 
outgoing data to the converter).

@param  aDataFlavorList fills list with supported flavors


### canConvert ###

Determines whether a conversion from one flavor to another is supported

@param  aFromFormatConverter flavor to convert from
@param  aFromFormatConverter flavor to convert to


### convert ###

Converts from one flavor to another.

@param  aFromFormatConverter flavor to convert from
@param  aFromFormatConverter flavor to convert to (destination own the memory)
@returns returns NS_OK if it was converted

