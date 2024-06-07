import csv



file = open ("Books.csv", "w")
newrecord = "le seigneur des anneaux, jrr tolkien, 1973\n"
file.write(str(newrecord))
newrecord = "babel, john stiegmann, 1999\n"
file.write(str(newrecord))
newrecord = "tropiques, pal goodwill, 1997\n"
file.write(str(newrecord)) 
newrecord = "le goût des choses, mc arthur, 2021\n"
file.write(str(newrecord))
newrecord = "1984, georges orwell, 1972\n"
file.write(str(newrecord))
file.close()