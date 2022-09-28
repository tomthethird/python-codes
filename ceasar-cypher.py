phrase = input()
shift = int(input())

for char in phrase:
    letter = ord(char)
    if (letter > 64 and letter < 91) or (letter > 96 and letter < 123):
        letter += shift
        if (letter > 90 and letter < 97) or (letter > 122 and letter < 128):
            letter -= 26
        letter = chr(letter)
        print(letter, end="")
    else:
        letter = chr(letter)
        print(letter, end="")