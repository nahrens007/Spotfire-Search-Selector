#This script takes myDataTable Visualization as a script parameter
#It adds columns to a Data Table based on a property. The property has a comma separated list of columns for the data table to show.
from Spotfire.Dxp.Application.Visuals import TablePlot,HtmlTextArea
from Spotfire.Dxp.Data import DataPropertyClass

def main():
    #get underlying data table
    txtArea=textArea.As[HtmlTextArea]()
    txtArea.HtmlContent = ''
    table=tableVis.As[TablePlot]()
    selected=[]
    for col in table.TableColumns:
        selected.append(col.Name)

    all_columns=Document.Data.Properties.GetProperty(DataPropertyClass.Document, "AvailableColumns").Value.split(',')
    Document.Data.Properties.GetProperty(DataPropertyClass.Document, "SelectedColumns").Value=",".join(selected)
    for x in range(0,len(all_columns)):
        all_columns[x] = all_columns[x].strip()
    
    # Search box
    html = '<div id="myContainer"><input type="text" id="myInput" onkeyup="inputSearch()" placeholder="Search for columns...">'
    
    # Buttons to select all / deselect all
    html += '<input type="button" value="Select All" class="myCheckboxAll" onclick="selectAllCheckbox(true)">'
    html += '<input type="button" value="De-Select All" class="myCheckboxAll" onclick="selectAllCheckbox(false)">'
    
    # start of column list 
    html += '<ul id="myUL">'
    for col in all_columns:
        html += '<li>'
        html += '<span class="myColumnOrderIndex">{}</span>'.format(str(selected.index(col)+1) if col in selected else '')
        html += '<input type="checkbox" class="myCheckBoxes" {checked}onclick="checkboxChange(\'{name}\');" id="{name}" value="{name}">'.format(name=col,checked="checked " if col in selected else "")
        html += '<label for="{name}">{name}</label><br>'.format(name=col)
        html += '</li>'

    html+='</ul></div>'
    html+=getCss()
    html+=getJs()
    txtArea.HtmlContent = html

def getCss():
    return '''<style>
#myInput {
  background-image: url('/css/searchicon.png'); /* Add a search icon to input */
  background-position: 10px 12px; /* Position the search icon */
  background-repeat: no-repeat; /* Do not repeat the icon image */
  width: 200px;
  padding: 12px 20px 12px 40px; /* Add some padding */
  border: 1px solid #ddd; /* Add a grey border */
  margin-bottom: 12px; /* Add some space below the input */
}

#myUL {
  /* Remove default list styling */
  list-style-type: none;
  padding: 0;
  margin: 0;
}

#myUL li a {
  text-decoration: none; /* Remove default text underline */
  color: black; /* Add a black text color */
  display: block; /* Make it into a block element to fill the whole list */
}

#myUL li a:hover:not(.header) {
  background-color: #eee; /* Add a hover effect to all links, except for headers */
}

.myCheckboxAll {
    width: 100px;
    height: 21px;
}
.myColumnOrderIndex {
    display: inline-block;
    margin-right: 5px;
    width: 20px;
    overflow: none;
    text-align:right;
}
#myContainer{
    width:275px;
}
</style>'''

def getJs():
    return '''<script>
function inputSearch() {
    // Declare variables
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName('li');

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < li.length; i++) {
        element = li[i].getElementsByTagName("input")[0];
        //txtValue = element.textContent || element.innerText;
        txtValue = element.value
        if (txtValue.toUpperCase().search(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

function checkboxChange() {
    // Document property input field that has currently selected columns.
    var elem = document.getElementById("myInputField").childNodes[1];
    var columns = [];
    
    if (arguments.length > 0) {
        // If column name was sent in, i.e., if an individual column was selected (not select all button)
        
        // split columns into array
        var checkedColumns=elem.value.split(",");
        
        // If column is already in document property (elem.value list), then deselect, otherwise, select
        var remove = false;
        for (i = 0; i<checkedColumns.length; i++) {
            if (checkedColumns[i]===arguments[0]) {
                remove=true;
            }
            else if (checkedColumns[i] != "") {
                columns.push(checkedColumns[i]);
            }
        }
        if (!remove) {
            columns.push(arguments[0]);
        }
        
    } else {
    
        // All checkboxes
        var checkboxes = document.getElementsByClassName("myCheckBoxes");
        
        // If the checkboxes are checked, then add the column.
        for (i = 0; i< checkboxes.length; i++) {
            if (checkboxes[i].checked) {
                columns.push(checkboxes[i].value);
            }
        }
    }
    
    elem.value=columns;
    elem.focus();
    elem.blur();
    
    var allColEl = document.getElementById("myUL").childNodes;
    
    for (i = 0; i < allColEl.length; i++) {
        // allColEl[i].childNodes[0] is order index
        // allColEl[i].childNodes[1] is checkbox
        // allColEl[i].childNodes[2] is label
        var index = columns.indexOf(allColEl[i].childNodes[1].value);
        if (index > -1) {
            allColEl[i].childNodes[0].textContent=index+1;
        } else {
            allColEl[i].childNodes[0].textContent="";
        }
    }
}

function selectAllCheckbox(check) {
    var checkboxes = document.getElementsByClassName("myCheckBoxes");
    for (i = 0; i< checkboxes.length; i++) {
        checkboxes[i].checked=check;
    }
    checkboxChange(); // make sure checkboxes register as changed.
}
</script>'''

main()