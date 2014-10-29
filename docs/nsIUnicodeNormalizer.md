---
layout: default
---

# nsIUnicodeNormalizer #

## NormalizeUnicodeNFD ##

Normalize Unicode (NFD, NFC, NFKD, NFKC).

NFD: Canonical Decomposition
NFC: Canonical Decomposition, followed by Canonical Composition
NFKD: Compatibility Decomposition
NFKC: Compatibility Decomposition, followed by Canonical Composition
Reference: Unicode Standard, TR15, Unicode Normalization Forms

@param aSrc         [IN]  nsAString which contains an input UTF-16 string.
@param aDest        [OUT] A pointer to an output buffer provided by a callee.
@return             NS_OK for success, 


## NormalizeUnicodeNFC ##

## NormalizeUnicodeNFKD ##

## NormalizeUnicodeNFKC ##
