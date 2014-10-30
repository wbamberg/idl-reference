---
layout: default
---

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
  
@param DOMCSSStyleSheet aSheet  
@param DOMString aInput  
       The new source string for the style sheet.  
  

### scrollElementIntoView(aElement) ###
  
Scroll an element completely into view, if possible.  
This is similar to ensureElementIsVisible but for all ancestors.  
  
@param DOMElement aElement  
  

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
