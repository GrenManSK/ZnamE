PLOCHA = [["a", "b", "c", "d", "e"], ["f", "g", "h", "i", "j"], [
    "k", "l", "m", "n", "o", ], ["p", "q", "r", "s", "t"], [
    "u", "v", "w", "x", "y"], ["A", "B", "C", "D", "E"], [
    "F", "G", "H", "I", "J"], ["K", "L", "M", "N", "O", ], [
    "P", "Q", "R", "S", "T"], ["U", "V", "W", "X", "y"], [
    "z", " ", ",", ".", ":"], ["!", "?", "'", '"', "`"], [
    "1", "2", "3", "4", "5"], ["6", "7", "8", "9", "0"], [
    "\n", "<", ">", ";", "/"], ["\\", "{", "}", "(", ")"],[
    "[","]","|","-","_"],["=","+","@","#","$"],["%","^","&","*","~"]]
def read_file(file):
    obsah = ""
    obsah_list = []
    for i in file:
        obsah = ""
        obsah += i
        for i in obsah:
            i.lower()
            obsah_list.append(i)
    return obsah_list
def encode(obsah):
    sifra = []
    for i in obsah:
        riadok = 0
        stlpec = 0
        while True:
            if riadok == 19 and stlpec == 0:
                break
            if i == PLOCHA[riadok][stlpec]:
                sifra.append(str(riadok) + " " + str(stlpec))
                break
            if stlpec == 4:
                riadok += 1
                stlpec = 0
            else:
                stlpec += 1
    return sifra
def output_file(file, name):
    y = []
    x = open(name + "coded.txt", "w")
    for i in file:
        y.append(i)
    x.write(str(y))
    x.close
    return
def main():
    while True:
        name = input()
        open_file = open(name+'.txt', "r")
        open_file.close
        output_file(encode(read_file(open_file)), name)
        koniec = input("enter to end > ")
        if koniec == "":
            break
main()