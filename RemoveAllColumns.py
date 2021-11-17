#This script takes myDataTable Visualization as a script parameter
#It adds columns to a Data Table based on a property. The property has a comma separated list of columns for the data table to show.
from Spotfire.Dxp.Application.Visuals import TablePlot
from Spotfire.Dxp.Data import DataPropertyClass

#get underlying data table
dt=tableVis.As[TablePlot]()

#remove all columns
dt.TableColumns.Clear()