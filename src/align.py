def checa_alinhamento(x, y, i, j):
    if (y[i] != x[j]):
        return 1
    else:
        return 0

def alinhamento_final(matriz, m, n):
    if (m == 0 or n == 0):
        # base da recursão
        return
    print('alo')
    alinhar = matriz[n - 1][m - 1] + checa_alinhamento(x, y, n - 1, m - 1)
    inserir = matriz[n][m - 1] + 1
    deletar = matriz[n - 1][m] + 1

    melhor_escolha = min(alinhar, inserir, deletar)

    if (melhor_escolha == alinhar):
        print("m-1 e n-1 -> alinhar")
        solution.append('Alinhar_' + str(y[n - 1]))
        return alinhamento_final(matriz[:n][:m], m - 1, n - 1)

    elif (melhor_escolha == inserir):
        print("n-1 -> inserir")
        solution.append('Inserir_' + str(y[n - 1]))
        return alinhamento_final(matriz[:n][:m + 1], m, n - 1)

    elif (melhor_escolha == deletar):
        print("m-1 - deletar")
        solution.append('Remover_' + str(x[m - 1]))
        return alinhamento_final(matriz[:n+1][:m], m - 1, n)

    
    

def prepara_matriz(x, y):
    # matriz = [[0 for i in range(len(x) + 1)] for j in range(len(y) + 1)]
    matriz = []
    for i in range(len(y) + 1):
        linha = []
        for j in range(len(x) + 1):
            linha.append(0)
        matriz.append(linha)
    
    for l in range(1, len(y) + 1):
        # primeira linha
        matriz[l][0] = l

    for c in range(1, len(x) + 1):
        # primeira coluna
        matriz[0][c] = c
        
    return matriz

def resolve_matriz(matriz, x, y):
    # Vamos percorrer as colunas 
    for k in range(1, len(x) + 1):
        # Percorrendo termo a termo
        for i in range(1, len(y) + 1):
            for j in range(1, len(x) + 1):
                # A função min() retornará o menor dentre os valores dados como argumentos
                matriz[i][j] = min(matriz[i-1][j-1] + checa_alinhamento(x, y, i-1, j-1), # Alinhar
                                    matriz[i-1][j] + 1, # Deletar
                                    matriz[i][j-1] + 1) # Inserir

    return matriz


if __name__ == "__main__":
    y = "TGCCTAG"
    x = "TCCAGT"
    z = prepara_matriz(x, y)
    z = resolve_matriz(z, x, y)
    solution = []
    alinhamento_final(z, len(x), len(y))
    print(solution[::-1])