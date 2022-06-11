import string
def rot13():
    rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    archivo = open('testing.txt', 'r')
    archivo2 = open('ricardo.txt', 'a')


    for line in archivo:
        pala = line.split()
        for caracteres in pala:
            rot = caracteres.translate(rot13)
            archivo2.writelines(rot)
        
rot13()