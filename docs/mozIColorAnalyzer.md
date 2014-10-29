---
layout: default
---

# mozIColorAnalyzer #

## Methods ##

### findRepresentativeColor ###

Given an image URI, find the most representative color for that image
based on the frequency of each color.  Preference is given to colors that
are more interesting.  Avoids the background color if it can be
discerned.  Ignores sufficiently transparent colors.

This is intended to be used on favicon images.  Larger images take longer
to process, especially those with a larger number of unique colors.  If
imageURI points to an image that has more than 128^2 pixels, this method
will fail before analyzing it for performance reasons.

@param imageURI
       A URI pointing to the image - ideally a data: URI, but any scheme
       that will load when setting the src attribute of a DOM img element
       should work.
@param callback
       Function to call when the representative color is found or an
       error occurs.

