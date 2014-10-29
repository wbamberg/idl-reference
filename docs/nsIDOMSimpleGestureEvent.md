---
layout: default
---

# nsIDOMSimpleGestureEvent #

The nsIDOMSimpleGestureEvent interface is the datatype for all
Mozilla-specific simple gesture events in the Document Object Model.

The following events are generated:

MozSwipeGestureStart - Generated when the user starts a horizontal
swipe across the input device.  This event not only acts as a signal,
but also asks two questions:  Should a swipe really be started, and
in which directions should the user be able to swipe?  The first
question is answered by event listeners by calling or not calling
preventDefault() on the event.  Since a swipe swallows all scroll
events, the default action of the swipe start event is *not* to
start a swipe. Call preventDefault() if you want a swipe to be
started.
The second question (swipe-able directions) is answered in the
allowedDirections field.
If this event has preventDefault() called on it (and thus starts
a swipe), it guarantees a future MozSwipeGestureEnd event that
will signal the end of a swipe animation.

MozSwipeGestureUpdate - Generated periodically while the user is
continuing a horizontal swipe gesture.  The "delta" value represents
the current absolute gesture amount.  This event may even be sent
after a MozSwipeGesture event fired in order to allow for fluid
completion of a swipe animation.  The direction value is meaningless
on swipe update events.

MozSwipeGestureEnd - Generated when the swipe animation is completed.

MozSwipeGesture - Generated when the user releases a swipe across
across the input device.  This event signals that the actual swipe
operation is complete, even though the animation might not be finished
yet.  This event can be sent without accompanying start / update / end
events, and it can also be handled on its own if the consumer doesn't
want to handle swipe animation events.
Only the direction value has any significance, the delta value is
meaningless.

MozMagnifyGestureStart - Generated when the user begins the magnify
("pinch") gesture.  The "delta" value represents the initial
movement.

MozMagnifyGestureUpdate - Generated periodically while the user is
continuing the magnify ("pinch") gesture.  The "delta" value
represents the movement since the last MozMagnifyGestureStart or
MozMagnifyGestureUpdate event.

MozMagnifyGesture - Generated when the user has completed the
magnify ("pinch") gesture.  If you only want to receive a single
event when the magnify gesture is complete, you only need to hook
this event and can safely ignore the MozMagnifyGestureStart and the
MozMagnifyGestureUpdate events. The "delta" value is the cumulative
amount represented by the user's gesture.

MozRotateGestureStart - Generated when the user begins the rotation
gesture.  The "delta" value represents the initial rotation.

MozRotateGestureUpdate - Generated periodically while the user is
continuing the rotation gesture.  The "delta" value represents the
rotation since the last MozRotateGestureStart or
MozRotateGestureUpdate event.

MozRotateGesture - Generated when the user has completed the
rotation gesture.  If you only want to receive a single event when
the rotation gesture is complete, you only need to hook this event
and can safely ignore the MozRotateGestureStart and the
MozRotateGestureUpdate events.  The "delta" value is the cumulative
amount of rotation represented by the user's gesture.

MozTapGesture - Generated when the user executes a two finger
tap gesture on the input device. Client coordinates contain the
center point of the tap.
(XXX On OS X, only Lion (10.7) and up)

MozPressTapGesture - Generated when the user executes a press
and tap two finger gesture (first finger down, second finger down,
second finger up, first finger up) on the input device.
Client coordinates contain the center pivot point of the action.
(XXX Not implemented on Mac)

MozEdgeUIGesture - Generated when the user swipes the display to
invoke edge ui.
(XXX Win8 only)

Default behavior:

Some operating systems support default behaviors for gesture events
when they are not handled by the application. Consumers should
use event.preventDefault() to prevent default behavior when
consuming events.


## DIRECTION_UP ##

## DIRECTION_DOWN ##

## DIRECTION_LEFT ##

## DIRECTION_RIGHT ##

## ROTATION_COUNTERCLOCKWISE ##

## ROTATION_CLOCKWISE ##

## allowedDirections ##

## direction ##

## delta ##

## clickCount ##

## initSimpleGestureEvent ##
