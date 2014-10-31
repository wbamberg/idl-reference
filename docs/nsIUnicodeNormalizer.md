---
layout: default
---

# nsIUnicodeNormalizer #

## Methods ##

### NormalizeUnicodeNFD(aSrc, aDest) ###
  
Normalize Unicode (NFD, NFC, NFKD, NFKC).  
  
NFD: Canonical Decomposition  
NFC: Canonical Decomposition, followed by Canonical Composition  
NFKD: Compatibility Decomposition  
NFKC: Compatibility Decomposition, followed by Canonical Composition  
Reference: Unicode Standard, TR15, Unicode Normalization Forms  
  
@param aSrc         [IN]  nsAString which contains an input UTF-16 string.  
@param aDest        [OUT] A pointer to an output buffer provided by a callee.  
@return             NS_OK for success,   
  

#### Parameters ####

<table>

<tr>
<td>aSrc</td>
<td>[IN]  nsAString which contains an input UTF-16 string.  
</td>
</tr>

<tr>
<td>aSrc</td>
<td>[IN]  nsAString which contains an input UTF-16 string.  
</td>
</tr>

</table>

### NormalizeUnicodeNFC(aSrc, aDest) ###

### NormalizeUnicodeNFKD(aSrc, aDest) ###

### NormalizeUnicodeNFKC(aSrc, aDest) ###
