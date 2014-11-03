---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/editor/nsIHTMLEditor.idl">Source file</a>
</div>

# nsIHTMLEditor #

## Methods ##

### addDefaultProperty(aProperty, aAttribute, aValue) ###
  
AddDefaultProperty() registers a default style property with the editor  
  
@param aProperty   the property to set by default  
@param aAttribute  the attribute of the property, if applicable.  
                   May be null.  
                   Example: aProperty="font", aAttribute="color"  
@param aValue      if aAttribute is not null, the value of the attribute.  
                   Example: aProperty="font", aAttribute="color",  
                            aValue="0x00FFFF"  
  

#### Parameters ####

<table>

<tr>
<td>aProperty</td>
<td>the property to set by default  
</td>
</tr>

<tr>
<td>aAttribute</td>
<td>the attribute of the property, if applicable.  
                   May be null.  
                   Example: aProperty="font", aAttribute="color"  
</td>
</tr>

<tr>
<td>aValue</td>
<td>if aAttribute is not null, the value of the attribute.  
                   Example: aProperty="font", aAttribute="color",  
                            aValue="0x00FFFF"  
</td>
</tr>

</table>

### removeDefaultProperty(aProperty, aAttribute, aValue) ###
  
RemoveDefaultProperty() unregisters a default style property with the editor  
  
@param aProperty   the property to remove from defaults  
@param aAttribute  the attribute of the property, if applicable.  
                   May be null.  
                   Example: aProperty="font", aAttribute="color"  
@param aValue      if aAttribute is not null, the value of the attribute.  
                   Example: aProperty="font", aAttribute="color",  
                            aValue="0x00FFFF"  
  

#### Parameters ####

<table>

<tr>
<td>aProperty</td>
<td>the property to remove from defaults  
</td>
</tr>

<tr>
<td>aAttribute</td>
<td>the attribute of the property, if applicable.  
                   May be null.  
                   Example: aProperty="font", aAttribute="color"  
</td>
</tr>

<tr>
<td>aValue</td>
<td>if aAttribute is not null, the value of the attribute.  
                   Example: aProperty="font", aAttribute="color",  
                            aValue="0x00FFFF"  
</td>
</tr>

</table>

### removeAllDefaultProperties() ###
  
RemoveAllDefaultProperties() unregisters all default style properties with the editor  
  
  

### setInlineProperty(aProperty, aAttribute, aValue) ###
  
SetInlineProperty() sets the aggregate properties on the current selection  
  
@param aProperty   the property to set on the selection   
@param aAttribute  the attribute of the property, if applicable.  
                   May be null.  
                   Example: aProperty="font", aAttribute="color"  
@param aValue      if aAttribute is not null, the value of the attribute.  
                   May be null.  
                   Example: aProperty="font", aAttribute="color",  
                            aValue="0x00FFFF"  
  

#### Parameters ####

<table>

<tr>
<td>aProperty</td>
<td>the property to set on the selection   
</td>
</tr>

<tr>
<td>aAttribute</td>
<td>the attribute of the property, if applicable.  
                   May be null.  
                   Example: aProperty="font", aAttribute="color"  
</td>
</tr>

<tr>
<td>aValue</td>
<td>if aAttribute is not null, the value of the attribute.  
                   May be null.  
                   Example: aProperty="font", aAttribute="color",  
                            aValue="0x00FFFF"  
</td>
</tr>

</table>

### getInlineProperty(aProperty, aAttribute, aValue, aFirst, aAny, aAll) ###
  
getInlineProperty() gets aggregate properties of the current selection.  
All object in the current selection are scanned and their attributes are  
represented in a list of Property object.  
  
@param aProperty   the property to get on the selection   
@param aAttribute  the attribute of the property, if applicable.  
                   May be null.  
                   Example: aProperty="font", aAttribute="color"  
@param aValue      if aAttribute is not null, the value of the attribute.  
                   May be null.  
                   Example: aProperty="font", aAttribute="color",  
                            aValue="0x00FFFF"  
@param aFirst      [OUT] PR_TRUE if the first text node in the  
                         selection has the property  
@param aAny        [OUT] PR_TRUE if any of the text nodes in the  
                         selection have the property  
@param aAll        [OUT] PR_TRUE if all of the text nodes in the  
                         selection have the property  
  

#### Parameters ####

<table>

<tr>
<td>aProperty</td>
<td>the property to get on the selection   
</td>
</tr>

<tr>
<td>aAttribute</td>
<td>the attribute of the property, if applicable.  
                   May be null.  
                   Example: aProperty="font", aAttribute="color"  
</td>
</tr>

<tr>
<td>aValue</td>
<td>if aAttribute is not null, the value of the attribute.  
                   May be null.  
                   Example: aProperty="font", aAttribute="color",  
                            aValue="0x00FFFF"  
</td>
</tr>

<tr>
<td>aFirst</td>
<td>[OUT] PR_TRUE if the first text node in the  
                         selection has the property  
</td>
</tr>

<tr>
<td>aAny</td>
<td>[OUT] PR_TRUE if any of the text nodes in the  
                         selection have the property  
</td>
</tr>

<tr>
<td>aAll</td>
<td>[OUT] PR_TRUE if all of the text nodes in the  
                         selection have the property  
</td>
</tr>

</table>

### getInlinePropertyWithAttrValue(aProperty, aAttribute, aValue, aFirst, aAny, aAll) ###

### removeAllInlineProperties() ###
  
removeAllInlineProperties() deletes all the inline properties from all   
text in the current selection.  
  

### removeInlineProperty(aProperty, aAttribute) ###
  
removeInlineProperty() deletes the properties from all text in the current  
selection.  If aProperty is not set on the selection, nothing is done.  
  
@param aProperty   the property to remove from the selection   
                   All atoms are for normal HTML tags (e.g.:  
                   nsIEditorProperty::font) except when you want to  
                   remove just links and not named anchors.  
                   For that, use nsIEditorProperty::href  
@param aAttribute  the attribute of the property, if applicable.  
                   May be null.  
                   Example: aProperty=nsIEditorProptery::font,  
                   aAttribute="color"  
                   nsIEditProperty::allAttributes is special.  
                   It indicates that all content-based text properties  
                   are to be removed from the selection.  
  

#### Parameters ####

<table>

<tr>
<td>aProperty</td>
<td>the property to remove from the selection   
                   All atoms are for normal HTML tags (e.g.:  
                   nsIEditorProperty::font) except when you want to  
                   remove just links and not named anchors.  
                   For that, use nsIEditorProperty::href  
</td>
</tr>

<tr>
<td>aAttribute</td>
<td>the attribute of the property, if applicable.  
                   May be null.  
                   Example: aProperty=nsIEditorProptery::font,  
                   aAttribute="color"  
                   nsIEditProperty::allAttributes is special.  
                   It indicates that all content-based text properties  
                   are to be removed from the selection.  
</td>
</tr>

</table>

### increaseFontSize() ###
  
 Increase font size for text in selection by 1 HTML unit  
 All existing text is scanned for existing <FONT SIZE> attributes  
 so they will be incremented instead of inserting new <FONT> tag  
  

### decreaseFontSize() ###
  
 Decrease font size for text in selection by 1 HTML unit  
 All existing text is scanned for existing <FONT SIZE> attributes  
 so they will be decreased instead of inserting new <FONT> tag  
  

### nodeIsBlock(node) ###
  
Tests if a node is a BLOCK element according the the HTML 4.0 DTD.  
  This does NOT consider CSS effect on display type  
  
@param aNode      the node to test  
  

#### Parameters ####

<table>

<tr>
<td>aNode</td>
<td>the node to test  
</td>
</tr>

</table>

### insertHTML(aInputString) ###
  
Insert some HTML source at the current location  
  
@param aInputString   the string to be inserted  
  

#### Parameters ####

<table>

<tr>
<td>aInputString</td>
<td>the string to be inserted  
</td>
</tr>

</table>

### pasteNoFormatting(aSelectionType) ###
   
Paste the text in the OS clipboard at the cursor position, replacing  
the selected text (if any), but strip out any HTML styles and formatting  
  

### rebuildDocumentFromSource(aSourceString) ###
   
 Rebuild the entire document from source HTML  
 Needed to be able to edit HEAD and other outside-of-BODY content  
  
 @param aSourceString   HTML source string of the entire new document  
  

#### Parameters ####

<table>

<tr>
<td>m</td>
<td>aSourceString   HTML source string of the entire new document  
</td>
</tr>

</table>

### insertHTMLWithContext(aInputString, aContextStr, aInfoStr, aFlavor, aSourceDoc, aDestinationNode, aDestinationOffset, aDeleteSelection) ###
  
Insert some HTML source, interpreting  
the string argument according to the given context.  
  
@param aInputString   the string to be inserted  
@param aContextStr    Context of insertion  
@param aInfoStr       Related info to aInputString   
@param aFlavor        Transferable flavor, can be ""  
@param aSourceDoc          document where input was dragged from (may be null)  
@param aDestinationNode    location for insertion (such as when dropped)  
@param aDestinationOffset  used with aDestNode to determine insert location  
@param aDeleteSelection    used with aDestNode during drag&drop   
@param aCollapseSelection  used with aDestNode during drag&drop  
  

#### Parameters ####

<table>

<tr>
<td>aInputString</td>
<td>the string to be inserted  
</td>
</tr>

<tr>
<td>aContextStr</td>
<td>Context of insertion  
</td>
</tr>

<tr>
<td>aInfoStr</td>
<td>Related info to aInputString   
</td>
</tr>

<tr>
<td>aFlavor</td>
<td>Transferable flavor, can be ""  
</td>
</tr>

<tr>
<td>aSourceDoc</td>
<td>document where input was dragged from (may be null)  
</td>
</tr>

<tr>
<td>aDestinationNode</td>
<td>location for insertion (such as when dropped)  
</td>
</tr>

<tr>
<td>aDestinationOffset</td>
<td>used with aDestNode to determine insert location  
</td>
</tr>

<tr>
<td>aDeleteSelection</td>
<td>used with aDestNode during drag&drop   
</td>
</tr>

<tr>
<td>aCollapseSelection</td>
<td>used with aDestNode during drag&drop  
</td>
</tr>

</table>

### insertElementAtSelection(aElement, aDeleteSelection) ###
   
Insert an element, which may have child nodes, at the selection  
Used primarily to insert a new element for various insert element dialogs,  
  but it enforces the HTML 4.0 DTD "CanContain" rules, so it should  
  be useful for other elements.  
  
@param aElement           The element to insert  
@param aDeleteSelection   Delete the selection before inserting  
    If aDeleteSelection is PR_FALSE, then the element is inserted   
    after the end of the selection for all element except  
    Named Anchors, which insert before the selection  
  

#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>The element to insert  
</td>
</tr>

<tr>
<td>aDeleteSelection</td>
<td>Delete the selection before inserting  
    If aDeleteSelection is PR_FALSE, then the element is inserted   
    after the end of the selection for all element except  
    Named Anchors, which insert before the selection  
</td>
</tr>

</table>

### setDocumentTitle(aTitle) ###
   
  Set the documents title.  
  

### updateBaseURL() ###
   
  Set the BaseURL for the document to the current URL  
    but only if the page doesn't have a <base> tag  
  This should be done after the document URL has changed,  
    such as after saving a file  
  This is used as base for relativizing link and image urls  
  

### selectElement(aElement) ###
   
Set the selection at the suppled element  
  
@param aElement   An element in the document  
  

#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>An element in the document  
</td>
</tr>

</table>

### setCaretAfterElement(aElement) ###
   
Create a collapsed selection just after aElement  
  
XXX could we parameterize SelectElement(before/select/after>?  
  
The selection is set to parent-of-aElement with an  
  offset 1 greater than aElement's offset  
  but it enforces the HTML 4.0 DTD "CanContain" rules, so it should  
  be useful for other elements.  
  
@param aElement  An element in the document  
  

#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>An element in the document  
</td>
</tr>

</table>

### setParagraphFormat(aParagraphFormat) ###
  
SetParagraphFormat       Insert a block paragraph tag around selection  
@param aParagraphFormat  "p", "h1" to "h6", "address", "pre", or "blockquote"  
  

#### Parameters ####

<table>

<tr>
<td>aParagraphFormat</td>
<td>"p", "h1" to "h6", "address", "pre", or "blockquote"  
</td>
</tr>

</table>

### getParagraphState(aMixed) ###
  
getParagraphState returns what block tag paragraph format is in  
the selection.  
@param aMixed     True if there is more than one format  
@return           Name of block tag. "" is returned for none.  
  

#### Parameters ####

<table>

<tr>
<td>aMixed</td>
<td>True if there is more than one format  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Name of block tag. "" is returned for none.  
</td>
</tr>

</table>

### getFontFaceState(aMixed) ###
   
getFontFaceState returns what font face is in the selection.  
@param aMixed    True if there is more than one font face  
@return          Name of face.  Note: "tt" is returned for  
                 tt tag.  "" is returned for none.  
  

#### Parameters ####

<table>

<tr>
<td>aMixed</td>
<td>True if there is more than one font face  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Name of face.  Note: "tt" is returned for  
                 tt tag.  "" is returned for none.  
</td>
</tr>

</table>

### getFontColorState(aMixed) ###
   
getFontColorState returns what font face is in the selection.  
@param aMixed     True if there is more than one font color  
@return           Color string. "" is returned for none.  
  

#### Parameters ####

<table>

<tr>
<td>aMixed</td>
<td>True if there is more than one font color  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Color string. "" is returned for none.  
</td>
</tr>

</table>

### getBackgroundColorState(aMixed) ###
   
getFontColorState returns what font face is in the selection.  
@param aMixed     True if there is more than one font color  
@return           Color string. "" is returned for none.  
  

#### Parameters ####

<table>

<tr>
<td>aMixed</td>
<td>True if there is more than one font color  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Color string. "" is returned for none.  
</td>
</tr>

</table>

### getHighlightColorState(aMixed) ###
   
getHighlightColorState returns what the highlight color of the selection.  
@param aMixed     True if there is more than one font color  
@return           Color string. "" is returned for none.  
  

#### Parameters ####

<table>

<tr>
<td>aMixed</td>
<td>True if there is more than one font color  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>Color string. "" is returned for none.  
</td>
</tr>

</table>

### getListState(aMixed, aOL, aUL, aDL) ###
   
getListState returns what list type is in the selection.  
@param aMixed    True if there is more than one type of list, or  
                 if there is some list and non-list  
@param aOL       The company that employs me.  No, really, it's   
                 true if an "ol" list is selected.  
@param aUL       true if an "ul" list is selected.  
@param aDL       true if a "dl" list is selected.  
  

#### Parameters ####

<table>

<tr>
<td>aMixed</td>
<td>True if there is more than one type of list, or  
                 if there is some list and non-list  
</td>
</tr>

<tr>
<td>aOL</td>
<td>The company that employs me.  No, really, it's   
                 true if an "ol" list is selected.  
</td>
</tr>

<tr>
<td>aUL</td>
<td>true if an "ul" list is selected.  
</td>
</tr>

<tr>
<td>aDL</td>
<td>true if a "dl" list is selected.  
</td>
</tr>

</table>

### getListItemState(aMixed, aLI, aDT, aDD) ###
   
getListItemState returns what list item type is in the selection.  
@param aMixed    True if there is more than one type of list item, or  
                 if there is some list and non-list  
@param aLI       true if "li" list items are selected.  
@param aDT       true if "dt" list items are selected.  
@param aDD       true if "dd" list items are selected.  
  

#### Parameters ####

<table>

<tr>
<td>aMixed</td>
<td>True if there is more than one type of list item, or  
                 if there is some list and non-list  
</td>
</tr>

<tr>
<td>aLI</td>
<td>true if "li" list items are selected.  
</td>
</tr>

<tr>
<td>aDT</td>
<td>true if "dt" list items are selected.  
</td>
</tr>

<tr>
<td>aDD</td>
<td>true if "dd" list items are selected.  
</td>
</tr>

</table>

### getAlignment(aMixed, aAlign) ###
   
getAlignment     returns what alignment is in the selection.  
@param aMixed    True if there is more than one type of list item, or  
                 if there is some list and non-list  
@param aAlign    enum value for first encountered alignment  
                 (left/center/right)  
  

#### Parameters ####

<table>

<tr>
<td>aMixed</td>
<td>True if there is more than one type of list item, or  
                 if there is some list and non-list  
</td>
</tr>

<tr>
<td>aAlign</td>
<td>enum value for first encountered alignment  
                 (left/center/right)  
</td>
</tr>

</table>

### getIndentState(aCanIndent, aCanOutdent) ###
  
Document me!  
  
  

### makeOrChangeList(aListType, entireList, aBulletType) ###
  
Document me!  
  
  

### removeList(aListType) ###
  
Document me!  
  
  

### indent(aIndent) ###
  
Document me!  
  
  

### align(aAlign) ###
  
Document me!  
  
  

### getElementOrParentByTagName(aTagName, aNode) ###
   
Return the input node or a parent matching the given aTagName,  
  starting the search at the supplied node.  
An example of use is for testing if a node is in a table cell  
  given a selection anchor node.  
  
@param aTagName  The HTML tagname  
 Special input values:  
   Use "href" to get a link node   
     (an "A" tag with the "href" attribute set)  
   Use "anchor" or "namedanchor" to get a named anchor node  
     (an "A" tag with the "name" attribute set)  
   Use "list" to get an OL, UL, or DL list node  
   Use "td" to get either a TD or TH cell node  
  
@param aNode    The node in the document to start the search.  
    If it is null, the anchor node of the current selection is used.  
@return         NS_EDITOR_ELEMENT_NOT_FOUND if an element is not found  
                (passes NS_SUCCEEDED macro)  
  

#### Parameters ####

<table>

<tr>
<td>aTagName</td>
<td>The HTML tagname  
 Special input values:  
   Use "href" to get a link node   
     (an "A" tag with the "href" attribute set)  
   Use "anchor" or "namedanchor" to get a named anchor node  
     (an "A" tag with the "name" attribute set)  
   Use "list" to get an OL, UL, or DL list node  
   Use "td" to get either a TD or TH cell node  
</td>
</tr>

<tr>
<td>aNode</td>
<td>The node in the document to start the search.  
    If it is null, the anchor node of the current selection is used.  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>NS_EDITOR_ELEMENT_NOT_FOUND if an element is not found  
                (passes NS_SUCCEEDED macro)  
</td>
</tr>

</table>

### getSelectedElement(aTagName) ###
   
Return an element only if it is the only node selected,  
   such as an image, horizontal rule, etc.  
The exception is a link, which is more like a text attribute:  
   The Anchor tag is returned if the selection is within the textnode(s)  
   that are children of the "A" node.  
   This could be a collapsed selection, i.e., a caret  
   within the link text.  
  
@param aTagName  The HTML tagname or and empty string   
      to get any element (but only if it is the only element selected)  
   Special input values for Links and Named anchors:  
   Use "href" to get a link node  
     (an "A" tag with the "href" attribute set)  
   Use "anchor" or "namedanchor" to get a named anchor node  
     (an "A" tag with the "name" attribute set)  
@return          NS_EDITOR_ELEMENT_NOT_FOUND if an element is not found  
                 (passes NS_SUCCEEDED macro)  
  

#### Parameters ####

<table>

<tr>
<td>aTagName</td>
<td>The HTML tagname or and empty string   
      to get any element (but only if it is the only element selected)  
   Special input values for Links and Named anchors:  
   Use "href" to get a link node  
     (an "A" tag with the "href" attribute set)  
   Use "anchor" or "namedanchor" to get a named anchor node  
     (an "A" tag with the "name" attribute set)  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>NS_EDITOR_ELEMENT_NOT_FOUND if an element is not found  
                 (passes NS_SUCCEEDED macro)  
</td>
</tr>

</table>

### getHeadContentsAsHTML() ###
   
Output the contents of the <HEAD> section as text/HTML format  
  

### replaceHeadContentsWithHTML(aSourceToInsert) ###
   
Replace all children of <HEAD> with string of HTML source  
  

### createElementWithDefaults(aTagName) ###
   
Return a new element with default attribute values  
  
This does not rely on the selection, and is not sensitive to context.  
  
Used primarily to supply new element for various insert element dialogs  
 (Image, Link, NamedAnchor, Table, and HorizontalRule   
  are the only returned elements as of 7/25/99)  
  
@param aTagName  The HTML tagname  
   Special input values for Links and Named anchors:  
   Use "href" to get a link node  
     (an "A" tag with the "href" attribute set)  
   Use "anchor" or "namedanchor" to get a named anchor node  
     (an "A" tag with the "name" attribute set)  
@return          The new element created.  
  

#### Parameters ####

<table>

<tr>
<td>aTagName</td>
<td>The HTML tagname  
   Special input values for Links and Named anchors:  
   Use "href" to get a link node  
     (an "A" tag with the "href" attribute set)  
   Use "anchor" or "namedanchor" to get a named anchor node  
     (an "A" tag with the "name" attribute set)  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>The new element created.  
</td>
</tr>

</table>

### insertLinkAroundSelection(aAnchorElement) ###
   
Insert an link element as the parent of the current selection  
  
@param aElement   An "A" element with a non-empty "href" attribute  
  

#### Parameters ####

<table>

<tr>
<td>aElement</td>
<td>An "A" element with a non-empty "href" attribute  
</td>
</tr>

</table>

### setBackgroundColor(aColor) ###
   
Set the value of the "bgcolor" attribute on the document's <body> element  
  
@param aColor  The HTML color string, such as "#ffccff" or "yellow"  
  

#### Parameters ####

<table>

<tr>
<td>aColor</td>
<td>The HTML color string, such as "#ffccff" or "yellow"  
</td>
</tr>

</table>

### setBodyAttribute(aAttr, aValue) ###
   
Set an attribute on the document's <body> element  
   such as text, link, background colors  
  
8/31/00 THIS ISN'T BEING USED? SHOULD WE DROP IT?  
  
@param aAttr   The attribute to be set  
@param aValue  The value of the attribute  
  

#### Parameters ####

<table>

<tr>
<td>aAttr</td>
<td>The attribute to be set  
</td>
</tr>

<tr>
<td>aValue</td>
<td>The value of the attribute  
</td>
</tr>

</table>

### getLinkedObjects() ###
  
Find all the nodes in the document which contain references  
to outside URIs (e.g. a href, img src, script src, etc.)  
The objects in the array will be type nsIURIRefObject.  
  
@return aNodeList    the linked nodes found  
  

#### Returns ####

<table>

<tr>
<td>aNodeList    the linked nodes found  
</td>
</tr>

</table>

### addInsertionListener(inFilter) ###
  
Add listener for insertion override  
@param inFilter  function which callers want called during insertion  
  

#### Parameters ####

<table>

<tr>
<td>inFilter</td>
<td>function which callers want called during insertion  
</td>
</tr>

</table>

### removeInsertionListener(inFilter) ###
  
Remove listener for insertion override  
@param inFilter  function which callers do not want called during insertion  
  

#### Parameters ####

<table>

<tr>
<td>inFilter</td>
<td>function which callers do not want called during insertion  
</td>
</tr>

</table>

### createAnonymousElement(aTag, aParentNode, aAnonClass, aIsCreatedHidden) ###
  
Returns an anonymous nsDOMElement of type aTag,  
child of aParentNode. If aIsCreatedHidden is true, the class  
"hidden" is added to the created element. If aAnonClass is not  
the empty string, it becomes the value of the attribute "_moz_anonclass"  
@return a DOM Element  
@param aTag             [IN] a string representing the desired type of  
                             the element to create  
@param aParentNode      [IN] the parent node of the created anonymous  
                             element  
@param aAnonClass       [IN] contents of the _moz_anonclass attribute  
@param aIsCreatedHidden [IN] a boolean specifying if the class "hidden"  
                             is to be added to the created anonymous  
                             element  
  

#### Parameters ####

<table>

<tr>
<td>aTag</td>
<td>[IN] a string representing the desired type of  
                             the element to create  
</td>
</tr>

<tr>
<td>aParentNode</td>
<td>[IN] the parent node of the created anonymous  
                             element  
</td>
</tr>

<tr>
<td>aAnonClass</td>
<td>[IN] contents of the _moz_anonclass attribute  
</td>
</tr>

<tr>
<td>aIsCreatedHidden</td>
<td>[IN] a boolean specifying if the class "hidden"  
                             is to be added to the created anonymous  
                             element  
</td>
</tr>

</table>

#### Returns ####

<table>

<tr>
<td>a DOM Element  
</td>
</tr>

</table>

### getSelectionContainer() ###
  
returns the deepest container of the selection  
@return a DOM Element  
  

#### Returns ####

<table>

<tr>
<td>a DOM Element  
</td>
</tr>

</table>

### checkSelectionStateForAnonymousButtons(aSelection) ###
  
Checks if the anonymous nodes created by the HTML editor have to be  
refreshed or hidden depending on a possible new state of the selection  
@param aSelection [IN] a selection  
  

#### Parameters ####

<table>

<tr>
<td>aSelection</td>
<td>[IN] a selection  
</td>
</tr>

</table>

### isAnonymousElement(aElement) ###

### breakIsVisible(aNode) ###
  
Checks whether a BR node is visible to the user.  
  

### GetActiveEditingHost() ###
  
Get an active editor's editing host in DOM window.  If this editor isn't  
active in the DOM window, this returns NULL.  
  

## Attributes ##

### isCSSEnabled ###
   
A boolean which is true is the HTMLEditor has been instantiated  
with CSS knowledge and if the CSS pref is currently checked  
  
@return    true if CSS handled and enabled  
  

### returnInParagraphCreatesNewParagraph ###
  
A boolean indicating if a return key pressed in a paragraph creates  
another paragraph or just inserts a <br> at the caret  
  
@return    true if CR in a paragraph creates a new paragraph  
  

## Constants ##

### eLeft ###

### eCenter ###

### eRight ###

### eJustify ###
