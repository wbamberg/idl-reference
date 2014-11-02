---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/toolkit/components/passwordmgr/nsILoginManagerPrompter.idl">Source file</a>
</div>

# nsILoginManagerPrompter #

## Methods ##

### init(aWindow) ###
  
Initialize the prompter. Must be called before using other interfaces.  
  
@param aWindow  
       The in which the user is doing some login-related action that's  
       resulting in a need to prompt them for something. The prompt  
       will be associated with this window (or, if a notification bar  
       is being used, topmost opener in some cases).  
  

#### Parameters ####

<table>

<tr>
<td>aWindow</td>
<td>       The in which the user is doing some login-related action that's  
       resulting in a need to prompt them for something. The prompt  
       will be associated with this window (or, if a notification bar  
       is being used, topmost opener in some cases).  
</td>
</tr>

</table>

### setE10sData(aData) ###
  
If the caller knows which browser this prompter is being created for,  
they can call this function to avoid having to calculate it from the  
window passed to init.  
  
@param aBrowser the <browser> to use for this prompter.  
  

#### Parameters ####

<table>

<tr>
<td>aBrowser</td>
<td>the <browser> to use for this prompter.  
</td>
</tr>

</table>

### promptToSavePassword(aLogin) ###
  
Ask the user if they want to save a login (Yes, Never, Not Now)  
  
@param aLogin  
       The login to be saved.  
  

#### Parameters ####

<table>

<tr>
<td>aLogin</td>
<td>       The login to be saved.  
</td>
</tr>

</table>

### promptToChangePassword(aOldLogin, aNewLogin) ###
  
Ask the user if they want to change a login's password. If the  
user consents, modifyLogin() will be called.  
  
@param aOldLogin  
       The existing login (with the old password).  
@param aNewLogin  
       The new login.  
  

#### Parameters ####

<table>

<tr>
<td>aOldLogin</td>
<td>       The existing login (with the old password).  
</td>
</tr>

<tr>
<td>aNewLogin</td>
<td>       The new login.  
</td>
</tr>

</table>

### promptToChangePasswordWithUsernames(logins, count, aNewLogin) ###
  
Ask the user if they want to change the password for one of  
multiple logins, when the caller can't determine exactly which  
login should be changed. If the user consents, modifyLogin() will  
be called.  
  
@param logins  
       An array of existing logins.  
@param count  
       (length of the array)  
@param aNewLogin  
       The new login.  
  
Note: Because the caller does not know the username of the login  
      to be changed, aNewLogin.username and aNewLogin.usernameField  
      will be set (using the user's selection) before modifyLogin()  
      is called.  
  

#### Parameters ####

<table>

<tr>
<td>logins</td>
<td>       An array of existing logins.  
</td>
</tr>

<tr>
<td>count</td>
<td>       (length of the array)  
</td>
</tr>

<tr>
<td>aNewLogin</td>
<td>       The new login.  
</td>
</tr>

</table>
