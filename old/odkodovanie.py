import sys
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
        obsah += i
        for i in obsah:
            obsah_list.append(i)
    return obsah_list
def decode(obsah):
    done = ""
    sifra = []
    for i in obsah:
        done += str(i)
        if i == '[' or i == "'" or i == ',' or i == ']':
            done = ""
            continue
        if i == " ":
            sifra.append(i)
        else:
            sifra.append(i)
    return sifra
def real_decode(obsah):
    cislo = 0
    pokracovanie = False
    done = ""
    vysledok = []
    for i in obsah:
        done += str(i)
        cislo = 0
        for i in done:
            cislo += 1
        if i == " ":
            done = ""
            continue
        if pokracovanie and done.isnumeric() and cislo == 1:
            stlpec = int(done)
            vysledok.append(PLOCHA[riadok][stlpec])
            pokracovanie = False
            done = ""
            continue
        if not pokracovanie or cislo == 2:
            pokracovanie = True
            riadok = int(done)
            continue
    return vysledok
def to_text(obsah):
    text = ""
    for i in obsah:
        if i == ".":
            text += i + "\n"
            continue
        text += i
    return text
def create_file(obsah, name):
    x = open(name + "uncoded", "w")
    x.write(obsah)
    x.close
    return
def main():
    while True:
        name = 'data'
        open_file = open(name, "r")
        code = list(decode(read_file(open_file)))
        to_text(real_decode(code))
        create_file(to_text(real_decode(code)), name)
main()