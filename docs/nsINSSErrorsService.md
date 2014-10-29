---
layout: default
---

# nsINSSErrorsService #

## isNSSErrorCode ##

 @param aNSPRCode An error code obtained using PR_GetError()
 @return True if it is error code defined by the NSS library


## getXPCOMFromNSSError ##

 Function will fail if aNSPRCode is not an NSS error code.
 @param aNSPRCode An error code obtained using PR_GetError()
 @return The result of the conversion, an XPCOM error code


## getErrorMessage ##

 Function will fail if aXPCOMErrorCode is not an NSS error code.
 @param aXPCOMErrorCode An error code obtain using getXPCOMFromNSSError
 return A localized human readable error explanation.


## getErrorClass ##

 Function will fail if aXPCOMErrorCode is not an NSS error code.
 @param aXPCOMErrorCode An error code obtain using getXPCOMFromNSSError
 return the 


## ERROR_CLASS_SSL_PROTOCOL ##

## ERROR_CLASS_BAD_CERT ##

## NSS_SEC_ERROR_BASE ##

 The following values define the range of NSPR error codes used by NSS.
 NSS remains the authorative source for these numbers, as a result,
 the values might change in the future.
 The security module will perform a runtime check and assertion
 to ensure the values are in synch with NSS.


## NSS_SEC_ERROR_LIMIT ##

## NSS_SSL_ERROR_BASE ##

## NSS_SSL_ERROR_LIMIT ##

## MOZILLA_PKIX_ERROR_BASE ##

The error codes within each module must fit in 16 bits. We want these
errors to fit in the same module as the NSS errors but not overlap with
any of them. Converting an NSS SEC, NSS SSL, or mozilla::pkix error to
an NS error involves negating the value of the error and then
synthesizing an error in the NS_ERROR_MODULE_SECURITY module. Hence,
mozilla::pkix errors will start at a negative value that both doesn't
overlap with the current value ranges for NSS errors and that will fit
in 16 bits when negated.

Keep these in sync with pkixnss.h.


## MOZILLA_PKIX_ERROR_LIMIT ##
