from Spotfire.Dxp.Application.Visuals import TablePlot

v = tableVis.As[TablePlot]()

# increase all column widths by 10 pixels
for col in v.Columns:
    col.Width = col.Width + 10