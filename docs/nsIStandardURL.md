---
layout: default
---

# nsIStandardURL #
  
nsIStandardURL defines the interface to an URL with the standard  
file path format common to protocols like http, ftp, and file.  
It supports initialization from a relative path and provides  
some customization on how URLs are normalized.  
  

## Methods ##

### init(aUrlType, aDefaultPort, aSpec, aOriginCharset, aBaseURI) ###
  
Initialize a standard URL.  
  
@param aUrlType       - one of the URLTYPE_ flags listed above.  
@param aDefaultPort   - if the port parsed from the URL string matches  
                        this port, then the port will be removed from the  
                        canonical form of the URL.  
@param aSpec          - URL string.  
@param aOriginCharset - the charset from which this URI string  
                        originated.  this corresponds to the charset  
                        that should be used when communicating this  
                        URI to an origin server, for example.  if  
                        null, then provide aBaseURI implements this  
                        interface, the origin charset of aBaseURI will  
                        be assumed, otherwise defaulting to UTF-8 (i.e.,  
                        no charset transformation from aSpec).  
@param aBaseURI       - if null, aSpec must specify an absolute URI.  
                        otherwise, aSpec will be resolved relative  
                        to aBaseURI.  
  

#### Parameters ####

<table>

<tr>
<td>aUrlType</td>
<td>- one of the URLTYPE_ flags listed above.  
</td>
</tr>

<tr>
<td>aUrlType</td>
<td>- one of the URLTYPE_ flags listed above.  
</td>
</tr>

<tr>
<td>aUrlType</td>
<td>- one of the URLTYPE_ flags listed above.  
</td>
</tr>

<tr>
<td>aUrlType</td>
<td>- one of the URLTYPE_ flags listed above.  
</td>
</tr>

<tr>
<td>aUrlType</td>
<td>- one of the URLTYPE_ flags listed above.  
</td>
</tr>

</table>

## Constants ##

### URLTYPE_STANDARD ###
  
blah:foo/bar    => blah://foo/bar  
blah:/foo/bar   => blah:///foo/bar  
blah://foo/bar  => blah://foo/bar  
blah:///foo/bar => blah:///foo/bar  
  

### URLTYPE_AUTHORITY ###
  
blah:foo/bar    => blah://foo/bar  
blah:/foo/bar   => blah://foo/bar  
blah://foo/bar  => blah://foo/bar  
blah:///foo/bar => blah://foo/bar  
  

### URLTYPE_NO_AUTHORITY ###
  
blah:foo/bar    => blah:///foo/bar  
blah:/foo/bar   => blah:///foo/bar  
blah://foo/bar  => blah://foo/bar  
blah:///foo/bar => blah:///foo/bar  
  
