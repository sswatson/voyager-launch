// let the grid know which columns and what data to use
var gridOptions = {
  defaultColDef: {
    enableValue: true,
    sortable: true,
    resizable: true,
    filter: true,
    editable: true,
  },
  columnDefs: columnDefs,
  rowData: rowData,
  onFirstDataRendered: autoSizeAll,
  rowDragManaged: true,
  animateRows: true
};

function autoSizeAll() {
  // resize columns
  var allColumnIds = [];
  gridOptions.columnApi.getAllColumns().forEach(function(column) {
        allColumnIds.push(column.colId);
  });
  gridOptions.columnApi.autoSizeColumns(allColumnIds);
}

function onBtExport() {
  var params = {fileName: "data.csv"}
  gridOptions.api.exportDataAsCsv(params)
}

// wait for the document to be loaded, otherwise
// ag-Grid will not find the div in the document.
document.addEventListener("DOMContentLoaded", function() {

  // lookup the container we want the Grid to use
  var eGridDiv = document.querySelector('#myGrid');

  // create the grid passing in the div to use together with the columns & data we want to use
  new agGrid.Grid(eGridDiv, gridOptions);
  
});

function onFilterTextBoxChanged() {
    gridOptions.api.setQuickFilter(document.getElementById('filter-text-box').value);
}