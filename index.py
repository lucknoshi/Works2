import  random

def randpasswd(length, chars=None):
    if chars is None:
        chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*()_+/*\\|<>;:"

        passwd = ""
        for i in range(length):
            password += random.choice(chars)

        return password
    
    # omit this if you just want the funcion
    print(randpasswd(12))