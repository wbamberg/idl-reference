---
layout: default
---

# nsIHTMLInlineTableEditor #

## inlineTableEditingEnabled ##

boolean indicating if inline table editing is enabled in the editor.
When inline table editing is enabled, and when the selection is
contained in a table cell, special buttons allowing to add/remove
a line/column are available on the cell's border.


## showInlineTableEditingUI ##

Shows inline table editing UI around a table cell
@param aCell [IN] a DOM Element being a table cell, td or th


## hideInlineTableEditingUI ##

Hide all inline table editing UI


## doInlineTableEditingAction ##

Modifies the table containing the selection according to the
activation of an inline table editing UI element
@param aUIAnonymousElement [IN] the inline table editing UI element


## refreshInlineTableEditingUI ##

Refresh already visible inline table editing UI

