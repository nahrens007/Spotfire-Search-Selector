#This script takes myDataTable Visualization as a script parameter
#It adds columns to a Data Table based on a property. The property has a comma separated list of columns for the data table to show.
from Spotfire.Dxp.Application.Visuals import TablePlot
from Spotfire.Dxp.Data import DataPropertyClass

#get underlying data table
dt=tableVis.As[TablePlot]()
cols = dt.Data.DataTableReference.Columns

#get document property
selection = Document.Data.Properties.GetProperty(DataPropertyClass.Document, "SelectedColumns").Value.split(",")

#parse columns from selection

for col in selection:
   #remove columns from document property
   try:
      dt.TableColumns.Remove(cols[str(col)])
   except:
      print col + " is not in table"