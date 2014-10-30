---
layout: default
---

# nsIFormAutofillContentService #
  
Defines a service used by DOM content to request Form Autofill, in particular  
when the requestAutocomplete method of Form objects is invoked.  
  
This service lives in the process that hosts the requesting DOM content.  
This means that, in a multi-process (e10s) environment, there can be an  
instance of the service for each content process, in addition to an instance  
for the chrome process.  
  
@remarks The service implementation uses a child-side message manager to  
         communicate with a parent-side message manager living in the chrome  
         process, where most of the processing is located.  
  

## Methods ##

### requestAutocomplete ###
  
Invoked by the requestAutocomplete method of the DOM Form object.  
  
The application is expected to display a user interface asking for the  
details that are relevant to the form being filled in.  The application  
should use the "autocomplete" attributes on the input elements as hints  
about which type of information is being requested.  
  
The processing will result in either an "autocomplete" simple DOM Event or  
an AutocompleteErrorEvent being fired on the form.  
  
@param aForm  
       The form on which the requestAutocomplete method was invoked.  
@param aWindow  
       The window where the form is located.  This must be specified even  
       for elements that are not in a document, and is used to generate the  
       DOM events resulting from the operation.  
  
