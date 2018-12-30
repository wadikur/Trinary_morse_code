char_to_trinary = {
    " ": "000000",
    "a": "000012",
    "b": "002111",
    "c": "002121",
    "d": "000211",
    "e": "000001",
    "f": "001121",
    "g": "000221",
    "h": "001111",
    "i": "000011",
    "j": "001222",
    "k": "000212",
    "l": "001211",
    "m": "000022",
    "n": "000021",
    "o": "000222",
    "p": "001221",
    "q": "002212",
    "r": "000121",
    "s": "000111",
    "t": "000002",
    "u": "000112",
    "v": "001112",
    "w": "000122",
    "x": "002112",
    "y": "002122",
    "z": "002211",
    "": "",
    "0": "022222",
    "1": "012222",
    "2": "011222",
    "3": "011122",
    "4": "011112",
    "5": "011111",
    "6": "021111",
    "7": "022111",
    "8": "022211",
    "9": "022221",
    "&": "012111",
    "'": "122221",
    "@": "122121",
    ")": "212212",
    "(": "021221",
    ":": "222111",
    ",": "221122",
    "=": "021112",
    "!": "212122",
    ".": "121212",
    "-": "211112",
    "+": "012121",
    '"': "121121",
    "?": "112211",
    "/": "021121",
}

trinary_to_char = dict((v, k) for k, v in char_to_trinary.items())

# print(trinary_to_char)


def trinary_encoder(inputs):
    return "".join([char_to_trinary[i] for i in list(str(inputs).lower())])


# print(trinary_encoder("BooomBOOOOM"))


def trinary_decoder(inp):
    chars = [str(inp)[i : i + 6] for i in range(0, len(inp), 6)]
    return "".join([trinary_to_char[i] for i in chars])


# print(trinary_decoder("002111000222000222000222000022002111000222000222000222000222000022"))

separator = "/"

trinary_to_morse = {"1": ".", "2": "-", "0": separator}
morse_to_trinary = dict((v, k) for k, v in trinary_to_morse.items())


def trinary2morse(inp):

    chars = [
        int(str(inp)[i : i + 6]) for i in range(0, len(inp), 6)
    ]  # strip down all zeros in the beginning
    morse = ["".join([trinary_to_morse[i] for i in str(char)]) for char in chars]

    return " ".join(morse)  # joining with ' ' provides the space between two chars


# print(trinary2morse(trinary_encoder('SOS Notice Me Senpai.')))


def morse2trinary(inp):

    chars = inp.split()  # splits stuff with space
    trinary = ["".join([morse_to_trinary[i] for i in str(char)]) for char in chars]
    trinary = [
        "{0:06d}".format(int(n)) for n in trinary
    ]  # add the leading zeroes back again.

    return "".join(trinary)


# print(trinary_decoder(morse2trinary('... --- ... / -. --- - .. -.-. . / -- . / ... . -. .--. .- .. .-.-.-')))

text_to_morse = lambda x: trinary2morse(trinary_encoder(x))
morse_to_text = lambda x: trinary_decoder(morse_to_trinary(x))

choices = {
    1: trinary_encoder,
    2: trinary_decoder,
    3: trinary2morse,
    4: morse2trinary,
    5: text_to_morse,
    6: morse_to_text,
}


def prompter():
    print(
        """Welcome to the Trinary-Text-Morse Encoder-Decoder.
            Make sure to enter everything in string format.
            Chose an option first.
            1. Text to trinary
            2. Trinary to text
            3. Trinary to morse
            4. Morse to trinary
            5. Text to morse
            6. Morse to text
        """
    )
    choice = int(input("Enter the number for your chosen option: "))
    assert choice in range(1, 7)

    inp = str(input("Enter the text: "))
    return choices[choice](inp)


while True:
    output = prompter()
    print(output)
    if output:
        confirmation = str(input("Do you want another round? y/n: "))
        if confirmation in ["N", "n", "no", "No", "NO"]:
            break
        elif confirmation in ["y", "Y", "yes", "Yes"]:
            pass
        else:
            print("Choose a valid option")
            break
    else:
        print("Something wrong, try again.")
        break
