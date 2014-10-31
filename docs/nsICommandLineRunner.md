---
layout: default
---

# nsICommandLineRunner #
  
Extension of nsICommandLine that allows for initialization of new command lines  
and running the command line actions by processing the command line handlers.  
  
@status INTERNAL - This interface is not meant for use by embedders, and is  
                   not intended to be frozen. If you are an embedder and need  
                   functionality provided by this interface, talk to Benjamin  
                   Smedberg <benjamin@smedbergs.us>.  
  

## Methods ##

### init(argc, argv, workingDir, state) ###
  
This method assumes a native character set, and is meant to be called  
with the argc/argv passed to main(). Talk to bsmedberg if you need to  
create a command line using other data. argv will not be altered in any  
way.  
  
On Windows, the "native" character set is UTF-8, not the native codepage.  
  
@param workingDir The working directory for resolving file and URI paths.  
@param state      The nsICommandLine.state flag.  
  

#### Parameters ####

<table>

<tr>
<td>workingDir</td>
<td>The working directory for resolving file and URI paths.  
</td>
</tr>

<tr>
<td>state</td>
<td>The nsICommandLine.state flag.  
</td>
</tr>

</table>

### setWindowContext(aWindow) ###
  
Set the windowContext parameter.  
  

### run() ###
  
Process the command-line handlers in the proper order, calling "handle()" on  
each.  
  
@throws NS_ERROR_ABORT if any handler throws NS_ERROR_ABORT. All other errors  
        thrown by handlers will be silently ignored.  
  

## Attributes ##

### helpText ###
  
Process and combine the help text provided by each command-line handler.  
  
