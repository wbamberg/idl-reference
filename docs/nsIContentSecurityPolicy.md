---
layout: default
---

# nsIContentSecurityPolicy #
  
nsIContentSecurityPolicy  
Describes an XPCOM component used to model and enforce CSPs.  Instances of  
this class may have multiple policies within them, but there should only be  
one of these per document/principal.  
  

## Methods ##

### getPolicy(index) ###
  
Accessor method for a read-only string version of the policy at a given  
index.  
  

### removePolicy(index) ###
  
Remove a policy associated with this CSP context.  
@throws NS_ERROR_FAILURE if the index is out of bounds or invalid.  
  

### appendPolicy(policyString, reportOnly) ###
  
Parse and install a CSP policy.  
@param aPolicy  
       String representation of the policy (e.g., header value)  
@param reportOnly  
       Should this policy affect content, script and style processing or  
       just send reports if it is violated?  
  

#### Parameters ####

<table>

<tr>
<td>aPolicy</td>
<td>       String representation of the policy (e.g., header value)  
</td>
</tr>

<tr>
<td>reportOnly</td>
<td>       Should this policy affect content, script and style processing or  
       just send reports if it is violated?  
</td>
</tr>

</table>

### getAllowsInlineScript(shouldReportViolations) ###
  
Whether this policy allows in-page script.  
@param shouldReportViolations  
    Whether or not the use of inline script should be reported.  
    This function always returns "true" for report-only policies, but when  
    any policy (report-only or otherwise) is violated,  
    shouldReportViolations is true as well.  
@return  
    Whether or not the effects of the inline script should be allowed  
    (block the compilation if false).  
  

#### Parameters ####

<table>

<tr>
<td>shouldReportViolations</td>
<td>    Whether or not the use of inline script should be reported.  
    This function always returns "true" for report-only policies, but when  
    any policy (report-only or otherwise) is violated,  
    shouldReportViolations is true as well.  
</td>
</tr>

</table>

### getAllowsEval(shouldReportViolations) ###
  
whether this policy allows eval and eval-like functions  
such as setTimeout("code string", time).  
@param shouldReportViolations  
    Whether or not the use of eval should be reported.  
    This function returns "true" when violating report-only policies, but  
    when any policy (report-only or otherwise) is violated,  
    shouldReportViolations is true as well.  
@return  
    Whether or not the effects of the eval call should be allowed  
    (block the call if false).  
  

#### Parameters ####

<table>

<tr>
<td>shouldReportViolations</td>
<td>    Whether or not the use of eval should be reported.  
    This function returns "true" when violating report-only policies, but  
    when any policy (report-only or otherwise) is violated,  
    shouldReportViolations is true as well.  
</td>
</tr>

</table>

### getAllowsInlineStyle(shouldReportViolations) ###
  
Whether this policy allows in-page styles.  
This includes <style> tags with text content and style="" attributes in  
HTML elements.  
@param shouldReportViolations  
    Whether or not the use of inline style should be reported.  
    If there are report-only policies, this function may return true  
    (don't block), but one or more policy may still want to send  
    violation reports so shouldReportViolations will be true even if the  
    inline style should be permitted.  
@return  
    Whether or not the effects of the inline style should be allowed  
    (block the rules if false).  
  

#### Parameters ####

<table>

<tr>
<td>shouldReportViolations</td>
<td>    Whether or not the use of inline style should be reported.  
    If there are report-only policies, this function may return true  
    (don't block), but one or more policy may still want to send  
    violation reports so shouldReportViolations will be true even if the  
    inline style should be permitted.  
</td>
</tr>

</table>

### getAllowsNonce(aNonce, aContentType, shouldReportViolation) ###
  
Whether this policy accepts the given nonce  
@param aNonce  
    The nonce string to check against the policy  
@param aContentType  
    The type of element on which we encountered this nonce  
@param shouldReportViolation  
    Whether or not the use of an incorrect nonce should be reported.  
    This function always returns "true" for report-only policies, but when  
    the report-only policy is violated, shouldReportViolation is true as  
    well.  
@return  
    Whether or not this nonce is valid  
  

#### Parameters ####

<table>

<tr>
<td>aNonce</td>
<td>    The nonce string to check against the policy  
</td>
</tr>

<tr>
<td>aContentType</td>
<td>    The type of element on which we encountered this nonce  
</td>
</tr>

<tr>
<td>shouldReportViolation</td>
<td>    Whether or not the use of an incorrect nonce should be reported.  
    This function always returns "true" for report-only policies, but when  
    the report-only policy is violated, shouldReportViolation is true as  
    well.  
</td>
</tr>

</table>

### getAllowsHash(aContent, aContentType, shouldReportViolation) ###
  
Whether this policy accepts the given inline resource based on the hash  
of its content.  
@param aContent  
    The content of the inline resource to hash (and compare to the  
    hashes listed in the policy)  
@param aContentType  
    The type of inline element (script or style)  
@param shouldReportViolation  
    Whether this inline resource should be reported as a hash-source  
    violation. If there are no hash-sources in the policy, this is  
    always false.  
@return  
    Whether or not this inline resource is whitelisted by a hash-source  
  

#### Parameters ####

<table>

<tr>
<td>aContent</td>
<td>    The content of the inline resource to hash (and compare to the  
    hashes listed in the policy)  
</td>
</tr>

<tr>
<td>aContentType</td>
<td>    The type of inline element (script or style)  
</td>
</tr>

<tr>
<td>shouldReportViolation</td>
<td>    Whether this inline resource should be reported as a hash-source  
    violation. If there are no hash-sources in the policy, this is  
    always false.  
</td>
</tr>

</table>

### logViolationDetails(violationType, sourceFile, scriptSample, lineNum, nonce, content) ###
  
For each violated policy (of type violationType), log policy violation on  
the Error Console and send a report to report-uris present in the violated  
policies.  
  
@param violationType  
    one of the VIOLATION_TYPE_* constants, e.g. inline-script or eval  
@param sourceFile  
    name of the source file containing the violation (if available)  
@param contentSample  
    sample of the violating content (to aid debugging)  
@param lineNum  
    source line number of the violation (if available)  
@param aNonce  
    (optional) If this is a nonce violation, include the nonce so we can  
    recheck to determine which policies were violated and send the  
    appropriate reports.  
@param aContent  
    (optional) If this is a hash violation, include contents of the inline  
    resource in the question so we can recheck the hash in order to  
    determine which policies were violated and send the appropriate  
    reports.  
  

#### Parameters ####

<table>

<tr>
<td>violationType</td>
<td>    one of the VIOLATION_TYPE_* constants, e.g. inline-script or eval  
</td>
</tr>

<tr>
<td>sourceFile</td>
<td>    name of the source file containing the violation (if available)  
</td>
</tr>

<tr>
<td>contentSample</td>
<td>    sample of the violating content (to aid debugging)  
</td>
</tr>

<tr>
<td>lineNum</td>
<td>    source line number of the violation (if available)  
</td>
</tr>

<tr>
<td>aNonce</td>
<td>    (optional) If this is a nonce violation, include the nonce so we can  
    recheck to determine which policies were violated and send the  
    appropriate reports.  
</td>
</tr>

<tr>
<td>aContent</td>
<td>    (optional) If this is a hash violation, include contents of the inline  
    resource in the question so we can recheck the hash in order to  
    determine which policies were violated and send the appropriate  
    reports.  
</td>
</tr>

</table>

### setRequestContext(selfURI, referrer, aChannel) ###
  
Called after the CSP object is created to fill in appropriate request  
context and give it a reference to its owning principal for violation  
report generation.  
This will use whatever data is available, choosing earlier arguments first  
if multiple are available.  Either way, it will attempt to obtain the URI,  
referrer and the principal from whatever is available.  If the channel is  
available, it'll also store that for processing policy-uri directives.  
  

### permitsAncestry(docShell) ###
  
Verifies ancestry as permitted by the policy.  
  
NOTE: Calls to this may trigger violation reports when queried, so this  
value should not be cached.  
  
@param docShell  
   containing the protected resource  
@return  
   true if the frame's ancestors are all allowed by policy (except for  
   report-only policies, which will send reports and then return true  
   here when violated).  
  

#### Parameters ####

<table>

<tr>
<td>docShell</td>
<td>   containing the protected resource  
</td>
</tr>

</table>

### permitsBaseURI(aURI) ###
  
Whether this policy allows setting the document's base URI to  
a given value.  
  
@return  
   Whether or not the provided URI is allowed to be used as the  
   document's base URI. (block the setting if false).  
  

### shouldLoad(aContentType, aContentLocation, aRequestOrigin, aContext, aMimeTypeGuess, aExtra) ###
  
Delegate method called by the service when sub-elements of the protected  
document are being loaded.  Given a bit of information about the request,  
decides whether or not the policy is satisfied.  
  
Calls to this may trigger violation reports when queried, so  
this value should not be cached.  
  

## Attributes ##

### policyCount ###
  
Returns the number of policies attached to this CSP instance.  Useful with  
getPolicy().  
  

## Constants ##

### VIOLATION_TYPE_INLINE_SCRIPT ###

### VIOLATION_TYPE_EVAL ###

### VIOLATION_TYPE_INLINE_STYLE ###

### VIOLATION_TYPE_NONCE_SCRIPT ###

### VIOLATION_TYPE_NONCE_STYLE ###

### VIOLATION_TYPE_HASH_SCRIPT ###

### VIOLATION_TYPE_HASH_STYLE ###
