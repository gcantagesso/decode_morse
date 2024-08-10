'''

O Código Morse é um sistema de representação de letras, algarismos e sinais de pontuação através
de um sinal codificado enviado de modo intermitente. Foi desenvolvido por Samuel Morse em 1837, 
criador do telégrafo elétrico, dispositivo que utiliza correntes elétricas para controlar eletroímãs 
que atuam na emissão e na recepção de sinais. 
O script tem a finalidade de decifrar uma mensagem em código morse e salvá-la em texto.

'''

import os
import sys
import datetime
import pandas as pd
from config import file_path, dict_morse

def decode_morse(dict_morse_msg):
    '''
    input : mensagem em código morse com as letras separadas por espaços
    output : palavra escrito em letras e algarismos
    
    '''
    # Divide o código morse por espaços duplos para obter as palavras
    words = dict_morse_msg.split('  ')
    decoded_message = ''
    
    # Decodifica cada palavra
    for word in words:
        # Divide a palavra por espaços simples para obter as letras
        letters = word.split(' ')
        for letter in letters:
            decoded_message += dict_morse.get(letter, '')
        decoded_message += ' '
    
    return decoded_message.strip()

def save_clear_msg_csv_hdr(decoded_message):
    '''
    input : mensagem em texto claro
    output : palavra escrito em letras e algarismos, salva em arquivo csv
    '''
    now = datetime.datetime.now()
    df = pd.DataFrame([[decoded_message, now]], columns=["mensagem", "datetime"])
    hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode ="a", index = False, header=hdr)

if __name__ == "__main__":
    msg_entrada = decode_morse(sys.argv[1])
    save_clear_msg_csv_hdr(msg_entrada)