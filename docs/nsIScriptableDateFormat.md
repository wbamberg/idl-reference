---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/intl/locale/nsIScriptableDateFormat.idl">Source file</a>
</div>

# nsIScriptableDateFormat #
<pre>  
Format date and time in a human readable format.  
  
</pre>
## Methods ##

### FormatDateTime(locale, dateFormatSelector, timeFormatSelector, year, month, day, hour, minute, second) ###
<pre>  
Format the given date and time in a human readable format.  
  
The underlying operating system is used to format the date and time.  
  
Pass an empty string as the locale parameter to use the OS settings with  
the preferred date and time formatting given by the user.  
  
Pass a locale code as described in nsILocale as the locale parameter  
(e.g. en-US) to use a specific locale. If the given locale is not  
available, a fallback will be used.  
  
NOTE: The output of this method depends on the operating system and user  
settings. Even if you pass a locale code as the first parameter, there  
are no guarantees about which locale and exact format the returned value  
uses. Even if you know the locale, the format might be customized by the  
user. Therefore you should not use the returned values in contexts where  
you depend on any specific format or language.  
  
@param locale  
       Locale code of locale used to format the date or an empty string  
       to follow user preference.  
@param dateFormatSelector  
       Indicate which format should preferably be used for the date.  
       Use one of the dateFormat* constants.  
@param timeFormatSelector  
       Indicate which format should preferably be used for the time.  
       Use one of the timeFormat* constants.  
@param year, month, day, hour, minute and second  
       The date and time to be formatted, given in the computer's local  
       time zone.  
@return The date and time formatted as human readable text according to  
        user preferences or the given locale.  
  
</pre>
#### Parameters ####

<table>

<tr>
<td>locale</td>
<td>       Locale code of locale used to format the date or an empty string  
       to follow user preference.  
</td>
</tr>

<tr>
<td>dateFormatSelector</td>
<td>       Indicate which format should preferably be used for the date.  
       Use one of the dateFormat* constants.  
</td>
</tr>

<tr>
<td>timeFormatSelector</td>
<td>       Indicate which format should preferably be used for the time.  
       Use one of the timeFormat* constants.  
</td>
</tr>

<tr>
<td>year,</td>
<td>month, day, hour, minute and second  
       The date and time to be formatted, given in the computer's local  
       time zone.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The date and time formatted as human readable text according to  
        user preferences or the given locale.  
</td>
</tr>

</table>

### FormatDate(locale, dateFormatSelector, year, month, day) ###
<pre>  
Format the given date in a human readable format.  
  
See FormatDateTime for details.  
  
</pre>
### FormatTime(locale, timeFormatSelector, hour, minute, second) ###
<pre>  
Format the given time in a human readable format.  
  
See FormatDateTime for details.  
  
</pre>
## Constants ##

### dateFormatNone ###
<pre>  
Do not include the date in the format string.  
  
</pre>
### dateFormatLong ###
<pre>  
Provide the long date format.  
  
NOTE:  
The original definitions of dateFormatLong and dateFormatShort are from  
the Windows platform.   
In US English dateFormatLong output will be like:  
    Wednesday, January 29, 2003 4:02:14 PM  
In US English dateFormatShort output will be like:  
    1/29/03 4:02:14 PM  
On platforms like Linux, it is rather difficult to achieve exact  
same output, and since we are aiming at human readers, it does not make  
sense to achieve exact same result. We will do just enough as the  
platform allow us to do.   
  
</pre>
### dateFormatShort ###
<pre>  
Provide the short date format. See also dateFormatLong.  
  
</pre>
### dateFormatYearMonth ###
<pre>  
Format using only the year and month.  
  
</pre>
### dateFormatWeekday ###
<pre>  
Provide the Week day (e.g. Mo, Mon, Monday or similar).  
  
</pre>
### timeFormatNone ###
<pre>  
Don't include the time in the format string.  
  
</pre>
### timeFormatSeconds ###
<pre>  
Provide the time format with seconds.  
  
</pre>
### timeFormatNoSeconds ###
<pre>  
Provide the time format without seconds.  
  
</pre>
### timeFormatSecondsForce24Hour ###
<pre>  
Provide the time format with seconds, and force the time format to use  
24-hour clock, regardless of the locale conventions.  
  
</pre>
### timeFormatNoSecondsForce24Hour ###
<pre>  
Provide the time format without seconds, and force the time format to use  
24-hour clock, regardless of the locale conventions.  
  
</pre>