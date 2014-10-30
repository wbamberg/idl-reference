---
layout: default
---

# mozIRepresentativeColorCallback #

## Methods ##

### onComplete ###
  
Will be called when color analysis finishes.  
  
@param success  
       True if analysis was successful, false otherwise.  
       Analysis can fail if the image is transparent, imageURI doesn't  
       resolve to a valid image, or the image is too big.  
  
@param color  
       The representative color as an integer in RGB form.  
       e.g. 0xFF0102 == rgb(255,1,2)  
       If success is false, color is not provided.  
  
