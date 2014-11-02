---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/intl/unicharutil/nsIUnicodeNormalizer.idl">Source file</a>
</div>

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
<td>aDest</td>
<td>[OUT] A pointer to an output buffer provided by a callee.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>NS_OK for success,   
</td>
</tr>

</table>

### NormalizeUnicodeNFC(aSrc, aDest) ###

### NormalizeUnicodeNFKD(aSrc, aDest) ###

### NormalizeUnicodeNFKC(aSrc, aDest) ###
