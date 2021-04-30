import array
# mengonversi sting ke dalam array.array
B = array.array('c')
B.fromstring("Python")
for kararter in B:
    print("%c " % karakter, end='')