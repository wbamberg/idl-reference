---
layout: default
---
<div id='links'><a href="../index.html">Index</a>
<a href="http://dxr.mozilla.org/mozilla-central/source/layout/inspector/inIDOMUtils.idl">Source file</a>
</div>

# inIDOMUtils #

## Methods ##

### getAllStyleSheets(aDoc, aLength, aSheets) ###

### getCSSStyleRules(aElement, aPseudo) ###

### getRuleLine(aRule) ###

### getRuleColumn(aRule) ###

### getSelectorCount(aRule) ###

### getSelectorText(aRule, aSelectorIndex) ###

### getSpecificity(aRule, aSelectorIndex) ###

### selectorMatchesElement(aElement, aRule, aSelectorIndex, aPseudo) ###

### isInheritedProperty(aPropertyName) ###

### getCSSPropertyNames(aFlags, aCount, aProps) ###

### getCSSValuesForProperty(aProperty, aLength, aValues) ###

### colorNameToRGB(aColorName) ###

### rgbToColorName(aR, aG, aB) ###

### colorToRGBA(aColorString) ###

### isValidCSSColor(aColorString) ###

### cssPropertyIsValid(aPropertyName, aPropertyValue) ###

### getSubpropertiesForCSSProperty(aProperty, aLength, aValues) ###

### cssPropertyIsShorthand(aProperty) ###

### cssPropertySupportsType(aProperty, type) ###

### isIgnorableWhitespace(aDataNode) ###

### getParentForNode(aNode, aShowingAnonymousContent) ###

### getChildrenForNode(aNode, aShowingAnonymousContent) ###

### getBindingURLs(aElement) ###

### getContentState(aElement) ###

### setContentState(aElement, aState) ###

### getUsedFontFaces(aRange) ###

### addPseudoClassLock(aElement, aPseudoClass) ###

### removePseudoClassLock(aElement, aPseudoClass) ###

### hasPseudoClassLock(aElement, aPseudoClass) ###

### clearPseudoClassLocks(aElement) ###

### parseStyleSheet(aSheet, aInput) ###
  
Parse CSS and update the style sheet in place.  
  
  

#### Parameters ####

<table>

<tr>
<td>DOMCSSStyleSheet</td>
<td>aSheet  
</td>
</tr>

<tr>
<td>DOMString</td>
<td>aInput  
       The new source string for the style sheet.  
</td>
</tr>

</table>

### scrollElementIntoView(aElement) ###
  
Scroll an element completely into view, if possible.  
This is similar to ensureElementIsVisible but for all ancestors.  
  
  

#### Parameters ####

<table>

<tr>
<td>DOMElement</td>
<td>aElement  
</td>
</tr>

</table>

## Constants ##

### EXCLUDE_SHORTHANDS ###

### INCLUDE_ALIASES ###

### TYPE_LENGTH ###

### TYPE_PERCENTAGE ###

### TYPE_COLOR ###

### TYPE_URL ###

### TYPE_ANGLE ###

### TYPE_FREQUENCY ###

### TYPE_TIME ###

### TYPE_GRADIENT ###

### TYPE_TIMING_FUNCTION ###

### TYPE_IMAGE_RECT ###

### TYPE_NUMBER ###
