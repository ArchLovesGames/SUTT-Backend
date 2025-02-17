# SUTT-Backend
The Backend task for SUTT

SUTT Backend Task 1: Mess Menu Parsing

Task Description:

You are tasked with creating a Python program to parse a provided Excel spreadsheet
containing the mess menu and converting its contents into Python objects. The resulting
Python objects must then be serialized into a JSON file.

Excel Sheet parsing: You are provided with an Excel spreadsheet that contains the mess
menu with different days in different columns. You have to read and parse that data using
either Pandas or Openpyxl (both are python libraries used extensively for excel and other
data manipulation). Ensure that you handle any potential issues, such as missing data or
data format inconsistencies, the mess menu has many such problems. Note: Make sure you
exclude the “ ******** ” in some rows. PS: YOU ARE NOT ALLOWED TO MODIFY THE EXCEL,
UNLESS THERE IS SOME EXTREME ISSUE.

JSON Serialization: After successfully creating Python objects representing the
menu items, you should serialize these objects into a JSON file. The format of this JSON file
should be as follows:

[
"Date1" : {
"Breakfast" : [ ...Breakfast Items... ],
"Lunch" : [ ...Lunch Items... ],
"Dinner" : [ ...Dinner Items...]
},
"Date2" : {
"Breakfast" : [ ...Breakfast Items... ],
"Lunch" : [ ...Lunch Items... ],
"Dinner" : [ ...Dinner Items...]
},
.......
]

