from Spotfire.Dxp.Application.Visuals import TablePlot

v = tableVis.As[TablePlot]()

# increase all column widths by 10 pixels
for col in v.Columns:
	if col.Width <= 50:
		col.Width=50
	else:
		col.Width = col.Width - 10