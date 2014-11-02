---
layout: default
---
<div class='links' style='float:right'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/dom/interfaces/events/nsIDOMEventTarget.idl">Source file</a>
</div>
# nsIDOMEventTarget #

## Methods ##

### addEventListener(type, listener, useCapture, wantsUntrusted) ###
  
This method allows the registration of event listeners on the event target.  
If an EventListener is added to an EventTarget while it is processing an  
event, it will not be triggered by the current actions but may be   
triggered during a later stage of event flow, such as the bubbling phase.  
  
If multiple identical EventListeners are registered on the same   
EventTarget with the same parameters the duplicate instances are   
discarded. They do not cause the EventListener to be called twice   
and since they are discarded they do not need to be removed with the   
removeEventListener method.  
  
@param   type The event type for which the user is registering  
@param   listener The listener parameter takes an interface   
                  implemented by the user which contains the methods   
                  to be called when the event occurs.  
@param   useCapture If true, useCapture indicates that the user   
                    wishes to initiate capture. After initiating   
                    capture, all events of the specified type will be   
                    dispatched to the registered EventListener before   
                    being dispatched to any EventTargets beneath them   
                    in the tree. Events which are bubbling upward   
                    through the tree will not trigger an   
                    EventListener designated to use capture.  
@param   wantsUntrusted If false, the listener will not receive any  
                        untrusted events (see above), if true, the  
                        listener will receive events whether or not  
                        they're trusted  
  

#### Parameters ####

<table>

<tr>
<td>type</td>
<td>The event type for which the user is registering  
</td>
</tr>

<tr>
<td>listener</td>
<td>The listener parameter takes an interface   
                  implemented by the user which contains the methods   
                  to be called when the event occurs.  
</td>
</tr>

<tr>
<td>useCapture</td>
<td>If true, useCapture indicates that the user   
                    wishes to initiate capture. After initiating   
                    capture, all events of the specified type will be   
                    dispatched to the registered EventListener before   
                    being dispatched to any EventTargets beneath them   
                    in the tree. Events which are bubbling upward   
                    through the tree will not trigger an   
                    EventListener designated to use capture.  
</td>
</tr>

<tr>
<td>wantsUntrusted</td>
<td>If false, the listener will not receive any  
                        untrusted events (see above), if true, the  
                        listener will receive events whether or not  
                        they're trusted  
</td>
</tr>

</table>

### addSystemEventListener(type, listener, aUseCapture, aWantsUntrusted) ###
  
addSystemEventListener() adds an event listener of aType to the system  
group.  Typically, core code should use system group for listening to  
content (i.e., non-chrome) element's events.  If core code uses  
nsIDOMEventTarget::AddEventListener for a content node, it means  
that the listener cannot listen the event when web content calls  
stopPropagation() of the event.  
  
@param aType            An event name you're going to handle.  
@param aListener        An event listener.  
@param aUseCapture      TRUE if you want to listen the event in capturing  
                        phase.  Otherwise, FALSE.  
@param aWantsUntrusted  TRUE if you want to handle untrusted events.  
                        Otherwise, FALSE.  
@return                 NS_OK if succeed.  Otherwise, NS_ERROR_*.  
  

#### Parameters ####

<table>

<tr>
<td>aType</td>
<td>An event name you're going to handle.  
</td>
</tr>

<tr>
<td>aListener</td>
<td>An event listener.  
</td>
</tr>

<tr>
<td>aUseCapture</td>
<td>TRUE if you want to listen the event in capturing  
                        phase.  Otherwise, FALSE.  
</td>
</tr>

<tr>
<td>aWantsUntrusted</td>
<td>TRUE if you want to handle untrusted events.  
                        Otherwise, FALSE.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>NS_OK if succeed.  Otherwise, NS_ERROR_*.  
</td>
</tr>

</table>

### removeEventListener(type, listener, useCapture) ###
  
This method allows the removal of event listeners from the event   
target. If an EventListener is removed from an EventTarget while it   
is processing an event, it will not be triggered by the current actions.   
EventListeners can never be invoked after being removed.  
Calling removeEventListener with arguments which do not identify any   
currently registered EventListener on the EventTarget has no effect.  
  
@param   type Specifies the event type of the EventListener being   
              removed.  
@param   listener The EventListener parameter indicates the   
                  EventListener to be removed.  
@param   useCapture Specifies whether the EventListener being   
                    removed was registered as a capturing listener or   
                    not. If a listener was registered twice, one with   
                    capture and one without, each must be removed   
                    separately. Removal of a capturing listener does   
                    not affect a non-capturing version of the same   
                    listener, and vice versa.  
  

#### Parameters ####

<table>

<tr>
<td>type</td>
<td>Specifies the event type of the EventListener being   
              removed.  
</td>
</tr>

<tr>
<td>listener</td>
<td>The EventListener parameter indicates the   
                  EventListener to be removed.  
</td>
</tr>

<tr>
<td>useCapture</td>
<td>Specifies whether the EventListener being   
                    removed was registered as a capturing listener or   
                    not. If a listener was registered twice, one with   
                    capture and one without, each must be removed   
                    separately. Removal of a capturing listener does   
                    not affect a non-capturing version of the same   
                    listener, and vice versa.  
</td>
</tr>

</table>

### removeSystemEventListener(type, listener, aUseCapture) ###
  
removeSystemEventListener() should be used if you have used  
addSystemEventListener().  
  

### dispatchEvent(evt) ###
  
This method allows the dispatch of events into the implementations   
event model. Events dispatched in this manner will have the same   
capturing and bubbling behavior as events dispatched directly by the   
implementation. The target of the event is the EventTarget on which   
dispatchEvent is called.  
  
@param   evt Specifies the event type, behavior, and contextual   
             information to be used in processing the event.  
@return  Indicates whether any of the listeners which handled the   
         event called preventDefault. If preventDefault was called   
         the value is false, else the value is true.  
@throws  INVALID_STATE_ERR: Raised if the Event's type was   
             not specified by initializing the event before   
             dispatchEvent was called. Specification of the Event's   
             type as null or an empty string will also trigger this   
             exception.  
  

#### Parameters ####

<table>

<tr>
<td>evt</td>
<td>Specifies the event type, behavior, and contextual   
             information to be used in processing the event.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Indicates whether any of the listeners which handled the   
         event called preventDefault. If preventDefault was called   
         the value is false, else the value is true.  
@throws  INVALID_STATE_ERR: Raised if the Event's type was   
             not specified by initializing the event before   
             dispatchEvent was called. Specification of the Event's   
             type as null or an empty string will also trigger this   
             exception.  
</td>
</tr>

</table>

### GetTargetForDOMEvent() ###
  
Returns the nsIDOMEventTarget object which should be used as the target  
of DOMEvents.  
Usually |this| is returned, but for example global object returns  
the outer object.  
  

### GetTargetForEventTargetChain() ###
  
Returns the nsIDOMEventTarget object which should be used as the target  
of the event and when constructing event target chain.  
Usually |this| is returned, but for example global object returns  
the inner object.  
  

### PreHandleEvent(aVisitor) ###
  
Called before the capture phase of the event flow.  
This is used to create the event target chain and implementations  
should set the necessary members of EventChainPreVisitor.  
At least aVisitor.mCanHandle must be set,  
usually also aVisitor.mParentTarget if mCanHandle is PR_TRUE.  
First one tells that this object can handle the aVisitor.mEvent event and  
the latter one is the possible parent object for the event target chain.  
@see EventDispatcher.h for more documentation about aVisitor.  
  
@param aVisitor the visitor object which is used to create the  
                event target chain for event dispatching.  
  
@note Only EventDispatcher should call this method.  
  

#### Parameters ####

<table>

<tr>
<td>aVisitor</td>
<td>the visitor object which is used to create the  
                event target chain for event dispatching.  
</td>
</tr>

</table>

### WillHandleEvent(aVisitor) ###
  
If EventChainPreVisitor.mWantsWillHandleEvent is set PR_TRUE,  
called just before possible event handlers on this object will be called.  
  

### PostHandleEvent(aVisitor) ###
  
Called after the bubble phase of the system event group.  
The default handling of the event should happen here.  
@param aVisitor the visitor object which is used during post handling.  
  
@see EventDispatcher.h for documentation about aVisitor.  
@note Only EventDispatcher should call this method.  
  

#### Parameters ####

<table>

<tr>
<td>aVisitor</td>
<td>the visitor object which is used during post handling.  
</td>
</tr>

</table>

### DispatchDOMEvent(aEvent, aDOMEvent, aPresContext, aEventStatus) ###
  
Dispatch an event.  
@param aEvent the event that is being dispatched.  
@param aDOMEvent the event that is being dispatched, use if you want to  
                 dispatch nsIDOMEvent, not only WidgetEvent.  
@param aPresContext the current presentation context, can be nullptr.  
@param aEventStatus the status returned from the function, can be nullptr.  
  
@note If both aEvent and aDOMEvent are used, aEvent must be the internal  
      event of the aDOMEvent.  
  
If aDOMEvent is not nullptr (in which case aEvent can be nullptr) it is used  
for dispatching, otherwise aEvent is used.  
  
@deprecated This method is here just until all the callers outside Gecko  
            have been converted to use nsIDOMEventTarget::dispatchEvent.  
  

#### Parameters ####

<table>

<tr>
<td>aEvent</td>
<td>the event that is being dispatched.  
</td>
</tr>

<tr>
<td>aDOMEvent</td>
<td>the event that is being dispatched, use if you want to  
                 dispatch nsIDOMEvent, not only WidgetEvent.  
</td>
</tr>

<tr>
<td>aPresContext</td>
<td>the current presentation context, can be nullptr.  
</td>
</tr>

<tr>
<td>aEventStatus</td>
<td>the status returned from the function, can be nullptr.  
</td>
</tr>

</table>

### GetContextForEventHandlers(aRv) ###
  
Get the script context in which the event handlers should be run.  
May return null.  
@note Caller *must* check the value of aRv.  
  

### GetJSContextForEventHandlers() ###
  
If the method above returns null, but a success code, this method  
is called.  
  
