def digit_sum(number):
    number = str(number) # Zuerst in einen String umwandeln, damit durch diesen Interiert werden kann
    sum = 0
    for digit in number:
        sum += int(digit) # Das digit in ein int umwandeln zum addieren
    return sum


def main():
    number = input('Bitte eine Ganzzahl eingeben für Quersummenberechnung> ')
    print(f"Die Quersumme ist: {digit_sum(number)}")


if __name__ == '__main__':
    main()
