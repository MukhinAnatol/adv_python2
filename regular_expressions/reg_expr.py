import re
def format_csv(list):

  phone_pattern_ext = re.compile(r"(\+7|8)+\s?\(?(\d{3})\)?\s?-?(\d{3})-?(\d{2})-?(\d+)\s\(?[а-я]+\.\s([0-9]+)\)?")
  phone_pattern = re.compile(r"(\+7|8)+\s?\(?(\d{3})\)?\s?-?(\d{3})-?(\d{2})-?(\d+)")
  name_pattern_1 = re.compile(r"([А-Я][а-я]+)\s?\,?([А-Я][а-я]+).([А-Я][а-я]+)\,+")
  name_pattern_2 = re.compile(r"^([А-Я][а-я]+)\s([А-Я][а-я]+),")

  for index, line in enumerate(list):
    line = ','.join(line)
    line = re.sub(phone_pattern, r'+7(\2)\3-\4-\5', line)
    line = re.sub(phone_pattern_ext, r'+7(\2)\3-\4-\5 доб.\6', line)
    line = re.sub(name_pattern_1, r'\1,\2,\3,', line)
    line = re.sub(name_pattern_2, r'\1,\2', line)
    list[index] = line.split(',')
  return list
