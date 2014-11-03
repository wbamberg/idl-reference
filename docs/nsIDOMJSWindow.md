---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/base/nsIDOMJSWindow.idl">Source file</a>
</div>

# nsIDOMJSWindow #

## Methods ##

### dump(str) ###

### setTimeout() ###
<code>  
These methods take typeless arguments and optional arguments, the  
first argument is either a function or a string, the second  
argument must be a number (ms) and the rest of the arguments (2  
... n) are passed to the callback function  
  
</code>
### setInterval() ###

### clearTimeout(handle) ###
<code>  
These methods take one optional argument that's the timer ID to  
clear. Often in existing code these methods are passed undefined,  
which is a nop so we need to support that as well.  
  
</code>
### clearInterval(handle) ###

### setResizable(resizable) ###
<code>  
This method is here for backwards compatibility with 4.x only,  
its implementation is a no-op  
  
</code>
### captureEvents() ###
<code>  
@deprecated These are old Netscape 4 methods. Do not use,  
            the implementation is no-op.  
  
</code>
### releaseEvents() ###

### open(url, name, options) ###
<code>  
This is the scriptable version of nsIDOMWindow::open()  
that takes 3 optional arguments. Its binary name is OpenJS to  
avoid colliding with nsIDOMWindow::open(), which has the  
same signature. The reason we can't have that collision is that  
the implementation needs to know whether it was called from JS or  
not.  
  
IOW, DO NOT CALL THIS FROM C++  
  
</code>
### openDialog(url, name, options) ###
<code>  
This is the scriptable version of  
nsIDOMWindow::openDialog() that takes 3 optional  
arguments, plus any additional arguments are passed on as  
arguments on the dialog's window object (window.arguments).  
  
</code>
## Attributes ##

### frames ###
  
window.frames in Netscape 4.x and IE is just a reference to the  
window itself (i.e. window.frames === window), but this doesn't  
make sense from a generic API point of view so that's why this is  
JS specific.  
  
This property is "replaceable" in JavaScript.  
  

### content ###
