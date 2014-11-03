---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/netwerk/base/public/nsIAuthPrompt.idl">Source file</a>
</div>

# nsIAuthPrompt #

## Methods ##

### prompt(dialogTitle, text, passwordRealm, savePassword, defaultText, result) ###
<code>  
Puts up a text input dialog with OK and Cancel buttons.  
Note: prompt uses separate args for the "in" and "out" values of the  
      input field, whereas the other functions use a single inout arg.  
@param  dialogText    The title for the dialog.  
@param  text          The text to display in the dialog.  
@param  passwordRealm The "realm" the password belongs to: e.g.  
                      ldap://localhost/dc=test  
@param  savePassword  One of the SAVE_PASSWORD_* options above.  
@param  defaultText   The default text to display in the text input box.  
@param  result        The value entered by the user if OK was  
                      selected.  
@return true for OK, false for Cancel  
  
</code>
#### Parameters ####

<table>

<tr>
<td>dialogText</td>
<td>The title for the dialog.  
</td>
</tr>

<tr>
<td>text</td>
<td>The text to display in the dialog.  
</td>
</tr>

<tr>
<td>passwordRealm</td>
<td>The "realm" the password belongs to: e.g.  
                      ldap://localhost/dc=test  
</td>
</tr>

<tr>
<td>savePassword</td>
<td>One of the SAVE_PASSWORD_* options above.  
</td>
</tr>

<tr>
<td>defaultText</td>
<td>The default text to display in the text input box.  
</td>
</tr>

<tr>
<td>result</td>
<td>The value entered by the user if OK was  
                      selected.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true for OK, false for Cancel  
</td>
</tr>

</table>

### promptUsernameAndPassword(dialogTitle, text, passwordRealm, savePassword, user, pwd) ###
<code>  
Puts up a username/password dialog with OK and Cancel buttons.  
Puts up a password dialog with OK and Cancel buttons.  
@param  dialogText    The title for the dialog.  
@param  text          The text to display in the dialog.  
@param  passwordRealm The "realm" the password belongs to: e.g.  
                      ldap://localhost/dc=test  
@param  savePassword  One of the SAVE_PASSWORD_* options above.  
@param  user          The username entered in the dialog.  
@param  pwd           The password entered by the user if OK was  
                      selected.  
@return true for OK, false for Cancel  
  
</code>
#### Parameters ####

<table>

<tr>
<td>dialogText</td>
<td>The title for the dialog.  
</td>
</tr>

<tr>
<td>text</td>
<td>The text to display in the dialog.  
</td>
</tr>

<tr>
<td>passwordRealm</td>
<td>The "realm" the password belongs to: e.g.  
                      ldap://localhost/dc=test  
</td>
</tr>

<tr>
<td>savePassword</td>
<td>One of the SAVE_PASSWORD_* options above.  
</td>
</tr>

<tr>
<td>user</td>
<td>The username entered in the dialog.  
</td>
</tr>

<tr>
<td>pwd</td>
<td>The password entered by the user if OK was  
                      selected.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true for OK, false for Cancel  
</td>
</tr>

</table>

### promptPassword(dialogTitle, text, passwordRealm, savePassword, pwd) ###
<code>  
Puts up a password dialog with OK and Cancel buttons.  
@param  dialogText    The title for the dialog.  
@param  text          The text to display in the dialog.  
@param  passwordRealm The "realm" the password belongs to: e.g.  
                      ldap://localhost/dc=test. If a username is  
                      specified (http://user@site.com) it will be used  
                      when matching existing logins or saving new ones.  
                      If no username is specified, only password-only  
                      logins will be matched or saved.  
                      Note: if a username is specified, the username  
                      should be escaped.  
@param  savePassword  One of the SAVE_PASSWORD_* options above.  
@param  pwd           The password entered by the user if OK was  
                      selected.  
@return true for OK, false for Cancel  
  
</code>
#### Parameters ####

<table>

<tr>
<td>dialogText</td>
<td>The title for the dialog.  
</td>
</tr>

<tr>
<td>text</td>
<td>The text to display in the dialog.  
</td>
</tr>

<tr>
<td>passwordRealm</td>
<td>The "realm" the password belongs to: e.g.  
                      ldap://localhost/dc=test. If a username is  
                      specified (http://user@site.com) it will be used  
                      when matching existing logins or saving new ones.  
                      If no username is specified, only password-only  
                      logins will be matched or saved.  
                      Note: if a username is specified, the username  
                      should be escaped.  
</td>
</tr>

<tr>
<td>savePassword</td>
<td>One of the SAVE_PASSWORD_* options above.  
</td>
</tr>

<tr>
<td>pwd</td>
<td>The password entered by the user if OK was  
                      selected.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>true for OK, false for Cancel  
</td>
</tr>

</table>

## Constants ##

### SAVE_PASSWORD_NEVER ###

### SAVE_PASSWORD_FOR_SESSION ###

### SAVE_PASSWORD_PERMANENTLY ###
