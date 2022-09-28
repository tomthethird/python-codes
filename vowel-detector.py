string = input()

a = string.count("a")
A = string.count("A")
e = string.count("e")
E = string.count("E")
i = string.count("i")
I = string.count("I")
o = string.count("o")
O = string.count("O")
u = string.count("u")
U = string.count("U")

if a > 0 or A > 0:
    a = 1

if e > 0 or E > 0:
    e = 1

if i > 0 or I > 0:
    i = 1

if o > 0 or O > 0:
    o = 1

if u > 0 or U > 0:
    u = 1

vowel = a + e + i + o + u

if vowel == 1:
    print("There is only one different vowel in the string.")
else:
    print(f"There are {vowel} different vowels in the string.")