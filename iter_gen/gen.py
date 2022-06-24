
def Flat_Generator(data):
    for element in data:
        if not isinstance (element, list):
            yield element
        else:
            for item in Flat_Generator(element):
                yield item
