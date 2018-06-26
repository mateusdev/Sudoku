#!/usr/bin/python3
# -*- coding: utf8 -*-

# Mateus Gualberto de Sousa Santos - 416766
# Raynara dos Santos Silva - 418097
# Lucas Souza Marques - 408863


matriz = [
            ['0', '0', '0','0', '0', '0','0', '0', '0'],
            ['0', '0', '0','0', '0', '0','0', '0', '0'],
            ['0', '0', '0','0', '0', '0','0', '0', '0'],
            ['0', '0', '0','0', '0', '0','0', '0', '0'],
            ['0', '0', '0','0', '0', '0','0', '0', '0'],
            ['0', '0', '0','0', '0', '0','0', '0', '0'],
            ['0', '0', '0','0', '0', '0','0', '0', '0'],
            ['0', '0', '0','0', '0', '0','0', '0', '0'],
            ['0', '0', '0','0', '0', '0','0', '0', '0']
        ]
letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}
n_dados = []

def mostra_matriz():
    global matriz

    print('    A   B   C    D   E   F    G   H   I')
    print(' ++---+---+---++---+---+---++---+---+---++')

    for i in range(0, 9):
        print("{}||".format(i + 1), end='')
        for j in range(0, 9):                
            if matriz[i][j] == '0':
                print('   ', end='')
            else:
                print(' {} '.format(matriz[i][j][0]), end='')
            if j == 2 or j == 5:
                print("||", end='')
            else:
                print("|", end = '')
        print("|{}".format(i+1))
        if i != 2 and i != 5:
            print(" ++---+---+---++---+---+---++---+---+---++")
        else:
            print(" ++===+===+===++===+===+===++===+===+===++")
    print('    A   B   C    D   E   F    G   H   I')


def checa_linha(n_linha):
    global matriz
    contados = []
    zeros = False

    for i in range(0, 9):
        if matriz[n_linha][i][0] not in contados or matriz[n_linha][i][0] == '0':
            contados.append(matriz[n_linha][i][0])
            if matriz[n_linha][i][0] == '0' and zeros == False:
                zeros = True
        else:
            return 2
    if zeros:
        return 1
    return 0


def checa_coluna(n_coluna):
    global matriz
    contados = []
    zeros = False
    for i in range(0, 9):
        if matriz[i][n_coluna][0] not in contados or matriz[i][n_coluna][0] == '0':
                contados.append(matriz[i][n_coluna][0])
                if matriz[i][n_coluna][0] == '0' and zeros == False:
                    zeros = True
        else:
                return 2
    if zeros:
        return 1
    return 0


def checa_quadra(n_linha, n_coluna):
    global matriz
    contados = []
    range_linha = []
    range_coluna = []
    zeros = False

    if n_linha in range(0, 3):
        range_linha = range(0, 3)

        if n_coluna in range(0, 3):
            range_coluna = range(0, 3)
        elif n_coluna in range(3, 6):
            range_coluna = range(3, 6)
        else:
            range_coluna = range(6, 9)
            
    elif n_linha in range(3, 6):
        range_linha = range(3, 6)
        
        if n_coluna in range(0, 3):
            range_coluna = range(0, 3)
        elif n_coluna in range(3, 6):
            range_coluna = range(3, 6)
        else:
            range_coluna = range(6, 9)
            
    else: # range(6, 9)
        range_linha = range(6, 9)
        
        if n_coluna in range(0, 3):
            range_coluna = range(0, 3)
        elif n_coluna in range(3, 6):
            range_coluna = range(3, 6)
        else:
            range_coluna = range(6, 9)
    
    for i in range_linha:
        for j in range_coluna:
            if matriz[i][j][0] not in contados or matriz[i][j][0] == '0':
                if matriz[i][j][0] == '0' and zeros == False:
                    zeros = True
                contados.append(matriz[i][j][0])
            else:
                return 2
    if zeros:
        return 1
    return 0


def checa_jogo():
    global matriz
    valor = 0
    
    for i in range(0, 3):
        for j in range(0, 3):
            if checa_quadra(i, j * 3) == 2:
                return 2
            elif checa_quadra(i, j * 3) == 1 and valor != 1:
                valor = 1
    
    for i in range(0, 9):
        if checa_linha(i) == 2 or checa_coluna(i) == 2:
            return 2
        elif checa_linha(i) == 1 or checa_coluna(i) == 1 and valor != 1:
            valor = 1
    
    return valor


def valida_jogada(jogada):
    jog_formatada = ''
    for letra in jogada:
        if letra != ' ' and letra != '\n':
            jog_formatada += letra
    
    return jog_formatada.upper()


def ler_pistas():
    global matriz
    global letras
    global n_dados
    pistas = []
    coluna = ''

    arq = open('pistas', 'r')
    for linha in arq:
        if linha != '\n':
            pistas.append(valida_jogada(linha))

    if len(pistas) < 1 or len(pistas) > 80:
        return False
    
    for linha in pistas:
        if len(linha) != 5:
            return False
        else:
            try:
                coluna = letras[linha[0]]
                l = int(linha[2]) - 1
                int(linha[-1])
            except:
                return False
            
            if l == -1 or linha[4] == '0':
                return False
            
            if matriz[l][coluna] == '0':
                n_dados.append(linha[4] + 'd')
                matriz[l][coluna] = linha[4] + 'd'
    
    if checa_jogo() < 2:
        return True
    else:
        return False


def ler_jogada(jogada):
    global matriz
    global letras
    jogada = valida_jogada(jogada)
    
    if len(jogada) == 4:
        if jogada[0] == 'D' and jogada[1] in letras:
            coluna = letras[jogada[1]]
            linha = int(jogada[3]) - 1

            if matriz[linha][coluna] not in n_dados:
                matriz[linha][coluna] = '0'
            else:
                return False
        else:
            return False

    elif len(jogada) == 5:
        if jogada[0] in letras:
            coluna = letras[jogada[0]]

            try:
                linha = int(jogada[2]) - 1
                valor = int(jogada[-1])
            except:
                return False

            if linha == -1:
                return False
                
            valor = jogada[-1]
            valor_anterior = matriz[linha][coluna]
            if matriz[linha][coluna] not in n_dados and valor != '0':
                matriz[linha][coluna] = valor
            else:
                return False

            if checa_coluna(coluna) == 2 \
            or checa_linha(linha) == 2 \
            or checa_quadra(linha, coluna) == 2 \
            or matriz[linha][coluna] in n_dados:
                matriz[linha][coluna] = valor_anterior
                return False
        else:
            return False
    else:
        return False
    
    return True


def modo_interativo():
    jogoacabou = False
    
    while jogoacabou == False:
        jog = input("Digite uma jogada: ")
        resultado = ler_jogada(jog)
        mostra_matriz()
        if resultado == False:
            print("ERRO! Tente outra vez!")
        else:
            if checa_jogo() == 0:
                jogoacabou = True

    print("PARABENS! JOGO COMPLETO!")


def modo_batch():    
    linhas = []
    erros = []
    arq = open('batch', 'r')
    for linha in arq:
        jogada = valida_jogada(linha)
        if len(jogada) != 5 and jogada != '':
            print("Erro de formatacao do arquivo de jogadas batch.")
            return False
        elif linha != '\n':
            linhas.append(valida_jogada(linha))
    
    
    for linha in linhas:
        if ler_jogada(linha) == False:
            erros.append("A jogada ({},{}) = {} eh invalida!".format(linha[0], linha[2], linha[-1]))
    
    if checa_jogo() == 0:
        print("A grade foi preenchida com sucesso!")
        return True
    else:
        for i in erros:
            print(i)
        
        print("A grade foi nao foi preenchida!")
        return False


def main():
    pistas = ler_pistas()
    mostra_matriz()
    
    if pistas == False:
        print("Configuracao de dicas invalida .")
        return False

    print("Escolha o modo de jogo: ")
    print("1 - interativo")
    print("2 - batch")
    print("[QUALQUER] - sair")
    print()
    escolha = input("~~~> ")
    
    if escolha == '1':
        modo_interativo()
    elif escolha == '2':
        modo_batch()
        
    else:
        print("Saindo!")

main()
