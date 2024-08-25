def findByName(array,name):
    for i,product in enumerate(array):
        if product['name']==name:
            return i 
    return -1

def findById(array,id):
    for i,product in enumerate(array):
        if product['id']==id:
            return i 
    return -1