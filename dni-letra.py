def dnil(dni):
    # convert DNI to integer before '%'
    #How can I do it with a list or aDictionary?
    let = ((int(dni)) % 23)
    if let == 0:
        return 'T'
    elif let == 1:
        return 'R'
    elif let == 2:
        return 'W'
    elif let == 3:
        return 'A'
    elif let == 4:
        return 'G'
    elif let == 5:
        return 'M'
    elif let == 6:
        return 'Y'
    elif let == 7:
        return 'F'
    elif let == 8:
        return 'P'
    elif let == 9:
        return 'D'
    elif let == 10:
        return 'X'
    elif let == 11:
        return 'B'
    elif let == 12:
        return 'N'
    elif let == 13:
        return 'J'
    elif let == 14:
        return 'Z'
    elif let == 15:
        return 'S'
    elif let == 16:
        return 'Q'
    elif let == 17:
        return 'V'
    elif let == 18:
        return 'H'
    elif let == 19:
        return 'L'
    elif let == 20:
        return 'C'
    elif let == 21:
        return 'K'
    elif let == 22:
        return 'E'
    else:
        return 'no se'

# Ask for DNI + adding text
print('La letra de tu DNI es: ' + (dnil(input('Escribe tu DNI sin letra: '))))

