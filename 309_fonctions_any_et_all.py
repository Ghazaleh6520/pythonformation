print(any([False,False,True,False]))#va donner True
print(all([False,False,True,False]))#va donner False

#exemple1
notes=[12,14,20,10,8]
print(any([x>18 for x in notes]))

#exemple2
files=["chat.jpg","chien.png"]
print(all([f.endswith(".jpg")for f in files]))
