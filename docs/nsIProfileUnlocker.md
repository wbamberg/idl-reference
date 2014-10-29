---
layout: default
---

# nsIProfileUnlocker #

## ATTEMPT_QUIT ##

## FORCE_QUIT ##

## unlock ##

Try to unlock the specified profile by attempting or forcing the
process that currently holds the lock to quit.

@param aSeverity either ATTEMPT_QUIT or FORCE_QUIT
@throws NS_ERROR_FAILURE if unlocking failed.

