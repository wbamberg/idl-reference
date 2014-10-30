---
layout: default
---

# nsIAccessibleTable #

## Methods ##

### getCellAt(rowIndex, columnIndex) ###
  
Return the accessible object at the specified row and column in the table.  
If both row and column index are valid then the corresponding accessible  
object is returned that represents the requested cell regardless of whether  
the cell is currently visible (on the screen).  
  
@param  rowIndex     [in] the row index to retrieve the cell at  
@param  columnIndex  [in] the column index to retrieve the cell at  
  

### getCellIndexAt(rowIndex, columnIndex) ###
  
Translate the given row and column indices into the corresponding cell  
index.  
  
@param  rowIndex    [in] the row index to return cell index at  
@param  columnIndex [in] the column index to return cell index at  
  

### getColumnIndexAt(cellIndex) ###
  
Translate the given cell index into the corresponding column index.  
  
@param  cellIndex  [in] index of the table cell to return column index for  
  

### getRowIndexAt(cellIndex) ###
  
Translate the given cell index into the corresponding row index.  
  
@param cellIndex  [in] index of the table cell to return row index for  
  

### getRowAndColumnIndicesAt(cellIndex, rowIndex, columnIndex) ###
  
Translate the given cell index into the corresponding row and column  
indices.  
  
@param cellIndex    [in] cell index to return row and column indices for  
@param rowIndex     [out] row index at the given cell index  
@param columnIndex  [out] column index at the given cell index  
  

### getColumnExtentAt(row, column) ###
  
Return the number of columns occupied by the accessible cell at  
the specified row and column in the table. The result differs from 1 if  
the specified cell spans multiple columns.  
  
@param  row     [in] row index of the cell to return the column extent for  
@param  column  [in] column index of the cell to return the column extent  
                 for  
  

### getRowExtentAt(row, column) ###
  
Return the number of rows occupied by the accessible cell at the specified  
row and column in the table. The result differs from 1 if the specified  
cell spans multiple rows.  
  
@param  row     [in] row index of the cell to return the column extent for  
@param  column  [in] column index of the cell to return the column extent  
                 for  
  

### getColumnDescription(columnIndex) ###
  
Return the description text of the specified column in the table.  
  
@param  columnIndex  [in] the column index to retrieve description for  
  

### getRowDescription(rowIndex) ###
  
Return the description text of the specified row in the table.  
  
@param  rowIndex  [in] the row index to retrieve description for  
  

### isColumnSelected(columnIndex) ###
  
Return a boolean value indicating whether the specified column is  
selected, i.e. all cells within the column are selected.  
  
@param  columnIndex  [in] the column index to determine if it's selected  
  

### isRowSelected(rowIndex) ###
  
Return a boolean value indicating whether the specified row is selected,  
i.e. all cells within the row are selected.  
  
@param  rowIndex  [in] the row index to determine whether it's selected  
  

### isCellSelected(rowIndex, columnIndex) ###
  
Return a boolean value indicating whether the specified cell is selected.  
  
@param  rowIndex     [in] the row index of the cell  
@param  columnIndex  [in] the column index of the cell  
  

### getSelectedCellIndices(cellsArraySize, cellsArray) ###
  
Return an array of cell indices currently selected.  
  
@param  cellsArraySize  [in] length of array  
@param  cellsArray      [in] array of indexes of selected cells  
  

### getSelectedColumnIndices(columnsArraySize, columnsArray) ###
  
Return an array of column indices currently selected.  
  
@param  columnsArraySize  [in] length of array  
@param  columnsArray      [in] array of indices of selected columns  
  

### getSelectedRowIndices(rowsArraySize, rowsArray) ###
  
Return an array of row indices currently selected.  
  
@param  rowsArraySize  [in] Length of array  
@param  rowsArray      [in] array of indices of selected rows  
  

### selectRow(rowIndex) ###
  
Select a row and unselects all previously selected rows.  
  
@param  rowIndex  [in] the row index to select  
  

### selectColumn(columnIndex) ###
  
Select a column and unselects all previously selected columns.  
  
@param  columnIndex  [in] the column index to select  
  

### unselectRow(rowIndex) ###
  
Unselect the given row, leaving other selected rows selected (if any).  
  
@param  rowIndex  [in] the row index to select  
  

### unselectColumn(columnIndex) ###
  
Unselect the given column, leaving other selected columns selected (if any).  
  
@param  columnIndex  [in] the column index to select  
  

### isProbablyForLayout() ###
  
Use heuristics to determine if table is most likely used for layout.  
  

## Attributes ##

### caption ###
  
Return the caption accessible for the table. For example, html:caption  
element of html:table element.  
  

### summary ###
  
Return summary description for the table. For example, @summary attribute  
on html:table element.  
  

### columnCount ###
  
Return columns count in the table.  
  

### rowCount ###
  
Return rows count in the table.  
  

### selectedCellCount ###
  
Return the total number of selected cells.  
  

### selectedColumnCount ###
  
Return the total number of selected columns.  
  

### selectedRowCount ###
  
Return the total number of selected rows.  
  

### selectedCells ###
  
Return an array of selected cells.  
  
