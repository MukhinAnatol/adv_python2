import csv
from reg_expr import format_csv
from remove_doubles import remove_doubles

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

formatted_list = format_csv(contacts_list)
output_data = remove_doubles(formatted_list)

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(output_data)