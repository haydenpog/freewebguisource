import base64
import string
import random
'''

I refuse to explain this.
I wouldn't recommend using this as its just a base64 with extra steps and crackable to anybody with this code.
Actually hash+salt ur accounts please. Your db wont get leaked through sql injection so it shouldn't be a big deal
but please, just change this.


AND BTW, 2 DIFFERENT LOOKING STRINGS CAN BE THE SAME DUE TO THE RANDOMIZED LETTERS
YWRtaW5DWg== IS THE SAME AS YWRtaW5ZUQ==
admin                       admin

'''



def test(text):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))
    ran = [*ran]
    if ran[0] in text:
        text.replace(ran[0], ran[1])
        text = text + ran[0] + ran[1]
    else:
        text = text + ran[0] + ran[1]
    text = base64.b64encode(text.encode("ASCII")).decode("ASCII")
    text = base64.a85encode(text.encode("ASCII")).decode("ASCII")
    print(text)
    return (text)


def testdecode(text):
    text = base64.a85decode(text.encode("ASCII")).decode("ASCII")
    text = base64.b64decode(text.encode("ASCII")).decode("ASCII")
    text = text.replace(text[-1], text[-2])
    text = text.replace(text[-2] + text[-1], "")
    return (text)

'''

BROKEN -- DONT USE

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
        text.replace(text[-1], text[-2])
    except:
        pass
    finally:
        text.replace(text[-2] + text[-1], "")

    text = base64.b64decode(text.encode("ASCII")).decode("ASCII")
    return text
'''

if __name__ == "__main__":
    print(test("admin") + " == '" + test("admin") + " == " + testdecode("@ms.<AQV8Q<,684"))
    pass