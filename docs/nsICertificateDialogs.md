---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/security/manager/ssl/public/nsICertificateDialogs.idl">Source file</a>
</div>

# nsICertificateDialogs #
  
Functions that implement user interface dialogs to manage certificates.  
  

## Methods ##

### confirmDownloadCACert(ctx, cert, trust) ###
  
 UI shown when a user is asked to download a new CA cert.  
 Provides user with ability to choose trust settings for the cert.  
 Asks the user to grant permission to import the certificate.  
  
 @param ctx A user interface context.  
 @param cert The certificate that is about to get installed.  
 @param trust a bit mask of trust flags,   
              see nsIX509CertDB for possible values.  
  
 @return true if the user allows to import the certificate.  
  

#### Parameters ####

<table>

<tr>
<td>m</td>
<td>ctx A user interface context.  
 @param cert The certificate that is about to get installed.  
 @param trust a bit mask of trust flags,   
              see nsIX509CertDB for possible values.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true if the user allows to import the certificate.  
</td>
</tr>

</table>

### notifyCACertExists(ctx) ###
  
 UI shown when a web site has delivered a CA certificate to  
 be imported, but the certificate is already contained in the  
 user's storage.  
  
 @param ctx A user interface context.  
  

#### Parameters ####

<table>

<tr>
<td>m</td>
<td>ctx A user interface context.  
</td>
</tr>

</table>

### setPKCS12FilePassword(ctx, password) ###
  
 UI shown when a user's personal certificate is going to be  
 exported to a backup file.  
 The implementation of this dialog should make sure   
 to prompt the user to type the password twice in order to  
 confirm correct input.  
 The wording in the dialog should also motivate the user   
 to enter a strong password.  
  
 @param ctx A user interface context.  
 @param password The password provided by the user.  
  
 @return false if the user requests to cancel.  
  

#### Parameters ####

<table>

<tr>
<td>m</td>
<td>ctx A user interface context.  
 @param password The password provided by the user.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>false if the user requests to cancel.  
</td>
</tr>

</table>

### getPKCS12FilePassword(ctx, password) ###
  
 UI shown when a user is about to restore a personal  
 certificate from a backup file.  
 The user is requested to enter the password  
 that was used in the past to protect that backup file.  
  
 @param ctx A user interface context.  
 @param password The password provided by the user.  
  
 @return false if the user requests to cancel.  
  

#### Parameters ####

<table>

<tr>
<td>m</td>
<td>ctx A user interface context.  
 @param password The password provided by the user.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>false if the user requests to cancel.  
</td>
</tr>

</table>

### viewCert(ctx, cert) ###
  
 UI shown when a certificate needs to be shown to the user.  
 The implementation should try to display as many attributes  
 as possible.  
  
 @param ctx A user interface context.  
 @param cert The certificate to be shown to the user.  
  

#### Parameters ####

<table>

<tr>
<td>m</td>
<td>ctx A user interface context.  
 @param cert The certificate to be shown to the user.  
</td>
</tr>

</table>
