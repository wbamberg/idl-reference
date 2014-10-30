---
layout: default
---

# nsIMessageListener #
  
Message managers provide a way for chrome-privileged JS code to  
communicate with each other, even across process boundaries.  
  
Message managers are separated into "parent side" and "child side".  
These don't always correspond to process boundaries, but can.  For  
each child-side message manager, there is always exactly one  
corresponding parent-side message manager that it sends messages  
to.  However, for each parent-side message manager, there may be  
either one or many child-side managers it can message.  
  
Message managers that always have exactly one "other side" are of  
type nsIMessageSender.  Parent-side message managers that have many  
"other sides" are of type nsIMessageBroadcaster.  
  
Child-side message managers can send synchronous messages to their  
parent side, but not the other way around.  
  
There are two realms of message manager hierarchies.  One realm  
approximately corresponds to DOM elements, the other corresponds to  
process boundaries.  
  
Message managers corresponding to DOM elements  
==============================================  
  
In this realm of message managers, there are  
 - "frame message managers" which correspond to frame elements  
 - "window message managers" which correspond to top-level chrome  
   windows  
 - "group message managers" which correspond to named message  
   managers with a specific window MM as the parent  
 - the "global message manager", on the parent side.  See below.  
  
The DOM-realm message managers can communicate in the ways shown by  
the following diagram.  The parent side and child side can  
correspond to process boundaries, but don't always.  
  
 Parent side                         Child side  
-------------                       ------------  
 global MMg  
  |  
  +-->window MMw1  
  |    |  
  |    +-->frame MMp1_1<------------>frame MMc1_1  
  |    |  
  |    +-->frame MMp1_2<------------>frame MMc1_2  
  |    |  
  |    +-->group MMgr1  
  |    |    |  
  |    |    +-->frame MMp2_1<------->frame MMc2_1  
  |    |    |  
  |    |    +-->frame MMp2_2<------->frame MMc2_2  
  |    |  
  |    +-->group MMgr2  
  |    |    ...  
  |    |  
  |    ...  
  |  
  +-->window MMw2  
  ...  
  
For example: a message sent from MMc1_1, from the child side, is  
sent only to MMp1_1 on the parent side.  However, note that all  
message managers in the hierarchy above MMp1_1, in this diagram  
MMw1 and MMg, will also notify their message listeners when the  
message arrives.  
  
A message sent from MMc2_1 will be sent to MMp2_1 and also notify  
all message managers in the hierarchy above that, including the  
group message manager MMgr1.  
  
For example: a message broadcast through the global MMg on the  
parent side would be broadcast to MMw1, which would transitively  
broadcast it to MMp1_1, MM1p_2.  The message would next be  
broadcast to MMgr1, which would broadcast it to MMp2_1 and MMp2_2.  
After that it would broadcast to MMgr2 and then to MMw2, and so  
on down the hierarchy.  
  
  ***** PERFORMANCE AND SECURITY WARNING *****  
Messages broadcast through the global MM and window or group MMs  
can result in messages being dispatched across many OS processes,  
and to many processes with different permissions.  Great care  
should be taken when broadcasting.  
  
Interfaces  
----------  
  
The global MMg and window MMw's are message broadcasters implementing  
nsIMessageBroadcaster while the frame MMp's are simple message senders  
(nsIMessageSender). Their counterparts in the content processes are  
message senders implementing nsIContentFrameMessageManager.  
  
                   nsIMessageListenerManager  
                 /                           \  
nsIMessageSender                               nsIMessageBroadcaster  
      |  
nsISyncMessageSender (content process/in-process only)  
      |  
nsIContentFrameMessageManager (content process/in-process only)  
      |  
nsIInProcessContentFrameMessageManager (in-process only)  
  
  
Message managers in the chrome process can also be QI'ed to nsIFrameScriptLoader.  
  
  
Message managers corresponding to process boundaries  
====================================================  
  
The second realm of message managers is the "process message  
managers".  With one exception, these always correspond to process  
boundaries.  The picture looks like  
  
 Parent process                      Child processes  
----------------                    -----------------  
 global (GPPMM)  
  |  
  +-->parent in-process PIPMM<-->child in-process CIPPMM  
  |  
  +-->parent (PPMM1)<------------------>child (CPMM1)  
  |  
  +-->parent (PPMM2)<------------------>child (CPMM2)  
  ...  
  
Note, PIPMM and CIPPMM both run in the parent process.  
  
For example: the parent-process PPMM1 sends messages to the  
child-process CPMM1.  
  
For example: CPMM1 sends messages directly to PPMM1. The global GPPMM  
will also notify their message listeners when the message arrives.  
  
For example: messages sent through the global GPPMM will be  
dispatched to the listeners of the same-process, CIPPMM, CPMM1,  
CPMM2, etc.  
  
  ***** PERFORMANCE AND SECURITY WARNING *****  
Messages broadcast through the GPPMM can result in messages  
being dispatched across many OS processes, and to many processes  
with different permissions.  Great care should be taken when  
broadcasting.  
  
Requests sent to parent-process message listeners should usually  
have replies scoped to the requesting CPMM.  The following pattern  
is common  
  
 const ParentProcessListener = {  
   receiveMessage: function(aMessage) {  
     let childMM = aMessage.target.QueryInterface(Ci.nsIMessageSender);  
     switch (aMessage.name) {  
     case "Foo:Request":  
       // service request  
       childMM.sendAsyncMessage("Foo:Response", { data });  
     }  
   }  
 };  
  

## Methods ##

### receiveMessage() ###
  
This is for JS only.  
receiveMessage is called with one parameter, which has the following  
properties:  
  {  
    target:    %the target of the message. Either an element owning  
                the message manager, or message manager itself if no  
                element owns it%  
    name:      %message name%,  
    sync:      %true or false%.  
    data:      %structured clone of the sent message data%,  
    json:      %same as .data, deprecated%,  
    objects:   %named table of jsvals/objects, or null%  
    principal: %principal for the window app  
  }  
  
Each listener is invoked with its own copy of the message  
parameter.  
  
When the listener is called, 'this' value is the target of the message.  
  
If the message is synchronous, the possible return value is  
returned as JSON (will be changed to use structured clones).  
When there are multiple listeners to sync messages, each  
listener's return value is sent back as an array.  |undefined|  
return values show up as undefined values in the array.  
  
