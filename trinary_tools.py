def trinary_encoder(inputs):
    string_lower=str(inputs).lower()
    output_string=''
    dictionary={' ': '0', 'a': '12', 'b': '2111', 'c': '2121', 'd': '211', 'e': '1', 'f': '1121',
            'g': '221', 'h': '1111', 'i': '11', 'j': '1222', 'k': '212', 'l': '1211', 'm': '22',
            'n': '21', 'o': '222', 'p': '1221', 'q': '2212', 'r': '121', 's': '111', 't': '2',
            'u': '112', 'v': '1112', 'w': '122', 'x': '2112', 'y': '2122', 'z': '2211', '': '', 
            '0': '22222', '1': '12222', '2': '11222', '3': '11122', '4': '11112', '5': '11111', 
            '6': '21111', '7': '22111', '8': '22211', '9': '22221', '&': '12111', "'": '122221', 
            '@': '122121', ')': '212212', '(': '21221', ':': '222111', ',': '221122', '=': '21112',
            '!': '212122', '.': '121212', '-': '211112', '+': '12121', '"': '121121', '?': '112211',
            '/': '21121'}
    for s in string_lower:
        output_string=output_string+str(dictionary[s])+'0'
    output_string=output_string[:-1]
    return output_string

def trinary_decoder(inputs):
    string_input=str(inputs)
    string_output=''
    tmp=''
    inv_dictionary={'0': ' ', '12': 'a', '2111': 'b', '2121': 'c', '211': 'd', '1': 'e', '1121': 'f', '221': 'g', '1111': 'h', '11': 'i',         '1222': 'j',          '212': 'k', '1211': 'l', '22': 'm', '21': 'n', '222': 'o', '1221': 'p', '2212': 'q', '121': 'r', '111': 's',           '2': 't', '112': 'u',           '1112': 'v', '122': 'w', '2112': 'x', '2122': 'y', '2211': 'z', '': '', '22222': '0', '12222': '1',        '11222': '2', '11122': '3',              '11112': '4', '11111': '5', '21111': '6', '22111': '7', '22211': '8', '22221': '9',                  '12111': '&', '122221': "'", '122121': '@',              '212212': ')', '21221': '(', '222111': ':', '221122': ',', '21112': '=',          '212122': '!', '121212': '.', '211112': '-', '12121':               '+', '121121': '"', '112211': '?', '21121': '/'}
    for i in range(len(string_input)):
        
        if string_input[i]!='0':
            tmp += string_input[i]
            
        else:
            
            string_output +=inv_dictionary[tmp]
            tmp=''
            if string_input[i+1:i+3]=='00':
                if string_input[i+3]!='0':
                    string_output+=' '
                else:
                    None
            else:
                None
    string_output+=inv_dictionary[tmp]
    return string_output


def trinary2morse(inputs,separator=' / '):
    input_string=str(inputs)
    separator_string=str(separator)
    output_string=''
    for i in range(len(input_string)):
        if input_string[i]=='1':
            output_string+='.'
        elif input_string[i]=='2':
            output_string+='-'
        elif input_string[i]=='0':
            if input_string[i+1:i+3]=='00':
                if input_string[i+3]!='0':
                    output_string+=separator_string
                else:
                    None
            else:
                output_string+=' '
        else:
            None
    return output_string


def morse2trinary(inputs,separator='/'):
    input_string=str(inputs)
    separator_string=str(separator)
    output_string=''
    for i in range(len(input_string)):
        if input_string[i]=='.':
            output_string+='1'
        elif input_string[i]=='-':
            output_string+='2'
        elif input_string[i]==separator:
            output_string+='0'
        elif input_string[i]==' ':
            if input_string[i+1]!=' ':
                output_string+='0'
            else:
                None
        else:
            None
    return output_string