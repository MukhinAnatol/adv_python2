def remove_doubles(data):
  contact_id = {}
  for id, contact in enumerate(data):
    full_name = contact[0] + contact[1]
    if full_name not in contact_id.keys():
      contact_id[full_name] = id
    else:
      for index, original_value in enumerate(data[contact_id[full_name]]):
        if original_value == "":
          data[contact_id[full_name]][index] = contact[index]
      data.pop(id)
  return data