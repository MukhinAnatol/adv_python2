from pprint import pprint
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

import re
def format_csv(list):

  phone_pattern_ext = re.compile(r"(\+7|8)+\s?\(?(\d{3})\)?\s?-?(\d{3})-?(\d{2})-?(\d+)\s\(?[а-я]+\.\s([0-9]+)\)?")
  phone_pattern = re.compile(r"(\+7|8)+\s?\(?(\d{3})\)?\s?-?(\d{3})-?(\d{2})-?(\d+)")
  name_pattern = re.compile(r"([А-Я]{1}[а-я]+)\s?\,?([А-Я]{1}[а-я]+)\s?\,*([А-Я]{1}[а-я]+)?\,*")

  for index, line in enumerate(list):
    line = ','.join(line)
    #print(line)
    line = re.sub(phone_pattern, r'+7(\2)\3-\4-\5', line)
    line = re.sub(phone_pattern_ext, r'+7(\2)\3-\4-\5 доб.\6', line)
    line = re.sub(name_pattern, r'\1,\2,\3,', line)
    list[index] = line.split(',')
    #print(line)
  return(list)

formatted_list = format_csv(contacts_list)
#pprint(formatted_list)

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(formatted_list)