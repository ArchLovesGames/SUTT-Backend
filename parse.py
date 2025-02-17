import json
import openpyxl

sheet = "Mess Menu Sample.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

days = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
headers = ["BREAKFAST","LUNCH","DINNER"]  
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
  blist = []
  llist = []
  dlist = []
  r = 2
  d = sheet_obj.cell(r,i).value
  r+=1
  while (r<rows+1):
    while (sheet_obj.cell(r,i).value not in days):
      if (sheet_obj.cell(r,i).value in headers):
        continue
      elif (sheet_obj.cell(r,i).value = None):
        continue
      elif (sheet_obj.cell(r,i).value = "***************"):
        continue
      else
          blist.append(sheet_obj.cell(r, i).value)
      r+=1
    r+=1
    while (sheet_obj.cell(r,i).value not in days):
      if (sheet_obj.cell(r,i).value in headers):
        continue
      elif (sheet_obj.cell(r,i).value = None):
        continue
      elif (sheet_obj.cell(r,i).value = "***************"):
        continue
      else
          llist.append(sheet_obj.cell(r, i).value)    
      r+=1
    r+=1
    while (r != rows)
      if (sheet_obj.cell(r,i).value in headers):
          continue
        elif (sheet_obj.cell(r,i).value = None):
          continue
        elif (sheet_obj.cell(r,i).value = "***************"):
          continue
        else
          dlist.append(sheet_obj.cell(r, i).value)        
      r+=1

    menu_list.append(Menu(d, blist, llist, dlist))
    r+=1
  i+=1


menu_json = []
i = 1
while i<len(menu_list)
    menu_json.append({
        menu.DATE: {
            "Breakfast": menu.BREAKFAST,
            "Lunch": menu.LUNCH,
            "Dinner": menu.DINNER
        }
    })

with open('menu.json', 'w') as file:
  json.dump(menu_json, file)




    


    
  
  
  
  
