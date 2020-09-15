var1 = 2
var2 = 1.5
var3 = 1.3


# finds the largest word in the text
# and returns its length
def get_max(text: str):
    text = text.lower() + '.'
    count = 0
    max_ = 0
    for letter in text:
        if 96 < ord(letter) < 123:
            count += 1
        else:
            if count > max_:
                max_ = count
            count = 0
    return max_


def encrypt(text: str):
    max_ = get_max(text)
    shift = (max_*var1)/var2  # shift calculation
    result = ''
    for letter in text:

        if shift >= 26:
            shift -= 26  # shift can't be bigger than the count of letters in Eng alphabet

        letter_ord = ord(letter)
        changed_letter_ord = letter_ord + int(shift)  # calculates new letter

        new_letter_ord = letter_ord  # if the letter if symbol, it won't change it

        # checks the new letter to be correct
        if ((64 < letter_ord < 91) and (changed_letter_ord > 90)) or ((96 < letter_ord < 123) and (changed_letter_ord > 122)):
            new_letter_ord = changed_letter_ord - 26  # changes if not correct
        elif (64 < letter_ord < changed_letter_ord < 91) or (96 < letter_ord < changed_letter_ord < 123):
            new_letter_ord = changed_letter_ord

        result += chr(new_letter_ord)
        shift += var3  # changes the shift
    return result


# decrypt is reversed encrypt
def decrypt(text: str):
    max_ = get_max(text)
    shift = (max_ * var1) / var2  # shift calculation
    result = ''
    for letter in text:
        if shift >= 26:
            shift -= 26  # shift can't be bigger than the count of letters in Eng alphabet

        letter_ord = ord(letter)
        changed_letter_ord = letter_ord - int(shift)  # calculates new letter

        new_letter_ord = letter_ord  # if the letter if symbol, it won't change it

        # checks the new letter to be correct
        if ((64 < letter_ord < 91) and (changed_letter_ord < 65)) or ((96 < letter_ord < 123) and (changed_letter_ord < 97)):
            new_letter_ord = changed_letter_ord + 26  # changes if not correct
        elif (64 < changed_letter_ord < letter_ord < 91) or (96 < changed_letter_ord < letter_ord < 123):
            new_letter_ord = changed_letter_ord

        result += chr(new_letter_ord)
        shift += var3  # changes the shift
    return result


if __name__ == "__main__":
    while True:
        mode = int(input("decrypt, encrypt(1/0): "))
        text = input("Your text: ")
        if mode:
            print(decrypt(text))
        else:
            print(encrypt(text))
