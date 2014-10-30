---
layout: default
---

# nsIBlocklistPrompt #
  
nsIBlocklistPrompt is used, if available, by the default implementation of   
nsIBlocklistService to display a confirmation UI to the user before blocking  
extensions/plugins.  
  

## Methods ##

### prompt(aAddons, aCount) ###
  
Prompt the user about newly blocked addons. The prompt is then resposible  
for soft-blocking any addons that need to be afterwards  
  
@param  aAddons  
        An array of addons and plugins that are blocked. These are javascript  
        objects with properties:  
         name    - the plugin or extension name,  
         version - the version of the extension or plugin,  
         icon    - the plugin or extension icon,  
         disable - can be used by the nsIBlocklistPrompt to allows users to decide  
                   whether a soft-blocked add-on should be disabled,  
         blocked - true if the item is hard-blocked, false otherwise,  
         item    - the nsIPluginTag or Addon object  
@param  aCount  
        The number of addons  
  
