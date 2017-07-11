import os
import xlrd
from xlrd.sheet import empty_cell

path = 'T:/DELTA Center/Travis/Fall 2016 Data/100% Online/Graduate'
for root, dirs, files in os.walk(path):
    xlsfiles=[ _ for _ in files if _.endswith('.xlsx') ]
    for xlsfile in xlsfiles:
        workbook = xlrd.open_workbook(os.path.join(root, xlsfile))
        worksheetName = workbook.sheet_by_index(0)

#worksheetName = raw_input("Enter in the Spreadsheet Name: ")
#print('Worksheet %s has been chosen', worksheetName)
#sheet = workbook.sheet_by_name(worksheetName)



        filename = worksheetName.name + '.html'
        script_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(script_dir, filename) ,'w') as f:
            wrapper = """<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>SHSU Online Enrollment - Fall 2015</title>
        <meta name="viewport" content="width=device-width">

        <link rel="stylesheet" href="http://www.shsu.edu/dl_www/maps/css/normalize.min.css">
        <link rel="stylesheet" href="http://www.shsu.edu/dl_www/maps/css/tabulous.css">
        <link rel="stylesheet" href="http://www.shsu.edu/dl_www/maps/css/main.css">
        <!--[if IE]>
            <link rel="stylesheet" type="text/css" href="http://www.shsu.edu/dl_www/maps/css/ie-only.css" />
        <![endif]-->
        
    </head>
    <body>
        <!--[if lt IE 7]>
            <p class="chromeframe">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">activate Google Chrome Frame</a> to improve your experience.</p>
        <![endif]-->

        <div class="map">
            <img src="img/%s.jpg" alt="SHSU Online State Enrollment Loading..."/>
        </div>
        <div class="enrollmentData">
            <h2>%s</h2>
"""
            part1 = wrapper %(worksheetName.name, worksheetName.name)

            totalEnroll = worksheetName.cell_value(0,1)
            gradEnroll = worksheetName.cell_value(1,1)
            wrapper= """
            <p class="enrollmentText"><strong>Total Enrollment:</strong> %d</p>
            <div id="tabs">
                <ul>
                        <li><a href="#tabs-1" title="">Graduate </a></li>
                    </ul>
                    <div id="tabs_container">
                        <div id="tabs-1">
                        <p class="enrollmentText">Graduate Enrollment: %d</p>
                            <!-- First column of data -->
                            <span class="dataLeft">
                                <ul>
"""
            part2 = wrapper %(totalEnroll, gradEnroll)
            f.write(part1 + part2)
            sheet = worksheetName
            for col in range(1, sheet.nrows):
                names = sheet.cell(col,0)
                nums = sheet.cell_value(col,1)
            
                if names.value != xlrd.empty_cell.value:
                    if nums != xlrd.empty_cell.value:
                        f.write('\t\t\t\t\t\t\t\t\t'+ '<li><strong>' + names.value + '</strong> '+ repr(nums)[:-2]+'</li>' + "\n")
            wrapper= """
                                </ul>
                            </span>
                            <!-- Second column of data (only applicable if more than 25 entries -->
                            <span class="dataRight">
                                <ul>
                                    <li></li>
                                </ul>
                            </span>
                        </div>
                    </div>
                    <!-- NOTE: For the Graduate and Undergraduate Academic Programs, delete line 34 and 52-66. There's no tab interface for these maps. Instead change the label to match what you're wanting to display. -->
              </div>
        </div>
        <script type="text/javascript" src="http://code.jquery.com/jquery-latest.min.js"></script>
        <script type="text/javascript" src="http://www.shsu.edu/dl_www/maps/js/tabulous.min.js"></script>
        <script type="text/javascript">
            $(document).ready(function($) {

                 $('#tabs').tabulous({
                    effect: 'slideLeft'
                });

            });
        </script>
    </body>
</html>"""
            whole = wrapper % ()
            f.write(whole)
            f.close()
