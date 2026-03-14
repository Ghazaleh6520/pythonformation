condition = 23


match condition:
    case 1:
        print ('ok')
    case 2:
        print ('pas ok')
    case 3:
        print ('Au revoir')
    case _: #autre
        print ('Reformulez votre demande')