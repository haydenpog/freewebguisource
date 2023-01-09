import base64
import string
import random



def pencode(text):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))
    ran = [*ran]
    text = base64.b64encode(text.encode("ASCII")).decode("ASCII")
    if ran[0] in text:
        text.replace(ran[0], ran[1])
        text = text + ran[0] + ran[1]
    else:
        text = text + ran[0] + ran[1]

    text = base64.b32encode(text.encode("ASCII")).decode("ASCII")
    text = base64.a85encode(text.encode("ASCII")).decode("ASCII")
    return text

def pdecode(text):
    text = base64.a85decode(text.encode("ASCII")).decode("ASCII")
    text = base64.b32decode(text.encode("ASCII")).decode("ASCII")
    try:
        text.replace(text[-1],text[-2])
    except:
        pass
    finally:
        text.replace(text[-2]+text[-1],"")

    text = base64.b64decode(text.encode("ASCII")).decode("ASCII")
    return text

if __name__ == "__main__":
    print(pdecode(r'6Z-^RAQ3V+=]fH&'))
    #print(pdecode(pencode("admin:admin\nhayden:pog")))
    f = open("account.db","w")
    f.write(pencode("admin:admin\nhayden:pog"))
    #print(f.read())
    #print(pdecode(f.read()))
    f.close()