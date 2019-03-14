
static_wheel = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ.?,'
rotor_selection = [' EKMFLGDQVZNTOWYHXUSPAIBRCJ.?,',
                    ' AJDKSIRUXBLHWTMCQGZNPYFVOE.?,',
                    ' BDFHJLCPRTXVZNYEIWGAKMUSQO.?,']
reflector_selection = [' EJMZALYXVBWFCRQUONTSPIKHGD.?,',
                       ' YRUHQSLDPXNGOKMIEBFZCWVJAT.?,',
                       ' FVPJIAOYEDRZXWGCTKUQSBNMHL.?,']

def rotate(rotor):
    rotor[0] = rotor[0][1:] + rotor[0][0]
    rotor[1] = rotor[1][1:] + rotor[1][0]
    return rotor

def index_input(index_in, rotor):
    return rotor[1].find(rotor[0][index_in])

def index_output(index, rotor):
    letter = rotor[1][index]
    return rotor[0].find(letter)

def select_rotors():
    rotor1_select = 2
    rotor2_select = 2
    rotor3_select = 2
    reflector = [reflector_selection[0],static_wheel]
    rotor1 = [rotor_selection[rotor1_select - 1], static_wheel]
    rotor2 = [rotor_selection[rotor2_select - 1], static_wheel]
    rotor3 = [rotor_selection[rotor3_select - 1], static_wheel]
    return rotor1,rotor2,rotor3,reflector

def rotors_section_message (rotor1,rotor2,rotor3,reflector,input):
    i,j = 0,0
    message = input.upper()
    result =[]
    for letter in message:
        index = static_wheel.find(letter)
        index = index_input(index, rotor1)
        index = index_input(index, rotor2)
        index = index_input(index, rotor3)
        index = index_input(index, reflector)
        index = index_output(index, rotor3)
        index = index_output(index, rotor2)
        index = index_output(index, rotor1)
        rotor1 = rotate(rotor1)
        i+=1
        if i == 27:
            i = 0
            rotor2 = rotate(rotor2)
            j += 1
        if j == 27:
            j = 0
            rotor3 = rotate(rotor3)
        result.append(static_wheel[index])
    return ''.join(result)


def rotors_section_letter (rotor1,rotor2,rotor3,reflector,input):
    i,j = 0,0

    while True:
        letter = input.upper()
        index = static_wheel.find(letter)
        print(index)
        index = index_input(index, rotor1)
        index = index_input(index, rotor2)
        index = index_input(index, rotor3)
        index = index_input(index, reflector)
        index = index_output(index, rotor3)
        index = index_output(index, rotor2)
        index = index_output(index, rotor1)
        print(static_wheel[index])
        rotor1 = rotate(rotor1)
        i+=1
        if i == 26:
            i = 0
            rotor2 = rotate(rotor2)
            j += 1
        if j == 26:
            j = 0
            rotor3 = rotate(rotor3)

def main():
    rotor1,rotor2,rotor3,reflector = select_rotors()
    message = input('Enter message: ')
    result = rotors_section_message(rotor1,rotor2,rotor3,reflector,message)
    return result

print(main())
