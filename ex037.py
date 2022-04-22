#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('\033[0;0;36m-=\033[m'*20)
num = int(input('\033[0;0;31mDigite um número inteiro: \033[m'))
print('''Escolha uma das bases para fazer a conversão: 
\033[0;0;33m
[ 1 ] converter em BINÁRIO
[ 2 ] converter em OCTAL
[ 3 ] converter em HEXADECIMAL
\033[m''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para \033[0;0;35mBINÁRIO\033[m é igual a \033[0;0;35m{}\033[m'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para \033[0;0;34mOCTAL\033[m é igual a \033[0;0;34m{}\033[m'. format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para \033[0;0;32mHEXADECIMAL\033[m é igual a \033[0;0;32m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('Onde você viu o \033[7;30;47m  {}  \033[m ? Tenta novamente e faz direito!'.format(opcao))
