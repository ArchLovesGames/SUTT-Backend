import json
import openpyxl

wb_obj = openpyxl.load_workbook("Mess Menu Sample.xlsx")
sheet_obj = wb_obj.active

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
headers = ["BREAKFAST", "LUNCH", "DINNER"]
rows = sheet_obj.max_row
cols = sheet_obj.max_column
menu_list = []

class Menu:
    def __init__(self, date, bitems, litems, ditems):
        self.DATE = date
        self.BREAKFAST = bitems
        self.LUNCH = litems
        self.DINNER = ditems

i = 1
while i < cols:
    blist, llist, dlist = [], [], []
    r = 2
    d = sheet_obj.cell(r, i).value
    r += 1

    while r < rows + 1:
        while r < rows and sheet_obj.cell(r, i).value not in days:
            cell_value = sheet_obj.cell(r, i).value
            if cell_value in headers or cell_value == None or cell_value == "**************" or cell_value == "***************":
                r += 1
                continue
            blist.append(cell_value)
            r += 1

        r += 1
        while r < rows and sheet_obj.cell(r, i).value not in days:
            cell_value = sheet_obj.cell(r, i).value
            if cell_value in headers or cell_value == None or cell_value == "**************" or cell_value == "***************":
                r += 1
                continue
            llist.append(cell_value)
            r += 1

        r += 1
        while r < rows:
            cell_value = sheet_obj.cell(r, i).value
            if cell_value in headers or cell_value == None or cell_value == "**************" or cell_value == "***************":
                r += 1
                continue
            dlist.append(cell_value)
            r += 1

        menu_list.append(Menu(d, blist, llist, dlist))
        r += 1

    i += 1
  
menu_json = []
for menu in menu_list:
    menu_json.append({
        menu.DATE.strftime("%d-%m-%Y"): {
            "Breakfast": menu.BREAKFAST,
            "Lunch": menu.LUNCH,
            "Dinner": menu.DINNER
        }
    })
  
  
with open("menu.json", "w") as file:
    json.dump(menu_json, file)





    


    
  
  
  
  
