---
layout: default
---

# nsINativeFileWatcherService #
  
A service providing native implementations of path changes notification.  
  

## Methods ##

### addPath(pathToWatch, onChange, onError, onSuccess) ###
  
Watches the passed path for changes. If it's a directory, every file  
it contains is watched. Recursively watches subdirectories. If the  
resource is already being watched, does nothing. If the passed path  
is a file, the behaviour is not specified.  
  
@param pathToWatch The path to watch for changes.  
@param onChange  
       The callback invoked whenever a change on a watched  
       resource is detected.  
@param onError  
       The optional callback invoked whenever an error occurs.  
@param onSuccess  
       The optional callback invoked when the file watcher starts  
       watching the resource for changes.  
  

### removePath(pathToUnwatch, onChange, onError, onSuccess) ###
  
Removes the provided path from the watched resources. If the path  
was not being watched or the callbacks were not registered, silently  
ignores the request.  
Please note that the file watcher only considers the onChange callbacks  
when deciding to close a watch on a resource. If there are no more onChange  
callbacks associated to the watch, it gets closed (even though it still has  
some error callbacks associated).  
  
@param pathToUnwatch The path to un-watch.  
@param onChange  
       The registered callback invoked whenever a change on a watched  
       resource is detected.  
@param onError  
       The optionally registered callback invoked whenever an error  
       occurs.  
@param onSuccess  
       The optional callback invoked when the file watcher stops  
       watching the resource for changes.  
  
