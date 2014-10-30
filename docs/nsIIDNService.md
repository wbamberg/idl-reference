---
layout: default
---

# nsIIDNService #
  
nsIIDNService interface.  
  
IDN (Internationalized Domain Name) support. Provides facilities  
for manipulating IDN hostnames according to the specification set  
forth by the IETF.  
  
IDN effort:  
http://www.ietf.org/html.characters/idn-charter.html  
http://www.i-dns.net  
  
IDNA specification:  
http://search.ietf.org/internet-drafts/draft-ietf-idn-idna-06.txt  
  

## Methods ##

### convertUTF8toACE ###
  
Prepares the input hostname according to IDNA ToASCII operation,  
the input hostname is assumed to be UTF8-encoded.  
  

### convertACEtoUTF8 ###
  
This is the ToUnicode operation as specified in the IDNA proposal,  
with an additional step to encode the result in UTF-8.  
It takes an ACE-encoded hostname and performs ToUnicode to it, then  
encodes the resulting string into UTF8.  
  

### isACE ###
  
Checks if the input string is ACE encoded or not.  
  

### normalize ###
  
Performs the unicode normalization needed for hostnames in IDN,  
for callers that want early normalization.  
  

### convertToDisplayIDN ###
  
Normalizes and converts a host to UTF-8 if the host is in the IDN  
whitelist, otherwise converts it to ACE. This is useful for display  
purposes and to ensure an encoding consistent with nsIURI::GetHost().  
If the result is ASCII or ACE encoded, |isASCII| will be true.  
  
