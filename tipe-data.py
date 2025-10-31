#tipe data tuple

tuple_1 = (2,3,4)
tuple_2 = ("doni","fitri")
tuple_3 = (24,False,"hallo")
print(tuple_1,tuple_2,tuple_3)


#fungsi tuple

#stiring ke tuple
alphabets = tuple("abcdefgh")
print(alphabets)

#list ke tuple

number = tuple([1,2,3,4,5,6,7])
print(number)

#range ke tuple

r = range(0,10)
rtuple = tuple(r)
print(rtuple)

#tipe data dictionary
biodaya_1 = {
    "nama" : "dafi",
    "hobi" : "masak",
    "umur" : "16",
}
print("nama: %s" %(biodaya_1["nama"]),
    "nama: %s" %(biodaya_1["hobi"]),
    "nama: %s" %(biodaya_1["umur"]))
