def checa_alinhamento(x, y, i, j):
    if (x[i] != y[j]):
        return 1
    else:
        return 0

def alinhamento_final(matriz, m, n):
    if (m == 0 or n == 0):
        # base da recursão
        return

    alinhar = matriz[m - 1][n - 1] + checa_alinhamento(x, y, m - 1, n - 1)
    inserir = matriz[m][n-1] + 1
    deletar = matriz[m-1][n] + 1

    melhor_escolha = min(inserir, alinhar, deletar)
    # print(m, n)
    if (melhor_escolha == inserir):
        # print("n-1 -> inserir")
        solution.append('Inserir_' + str(y[n - 1]))
        return alinhamento_final(matriz[:m+1][:n], m, n - 1)

    elif (melhor_escolha == alinhar):
        # print("m-1 e n-1 -> alinhar")
        solution.append('Alinhar_' + str(y[n - 1]))
        return alinhamento_final(matriz[:m][:n], m - 1, n - 1)

    elif (melhor_escolha == deletar):
        # print("m-1 - deletar")
        solution.append('Remover_' + str(x[m - 1]))
        return alinhamento_final(matriz[:m][:n+1], m - 1, n)

    
    

def prepara_matriz(x, y):
    # matriz = [[0 for i in range(len(x) + 1)] for j in range(len(y) + 1)]
    matriz = []
    for i in range(len(x) + 1):
        linha = []
        for j in range(len(y) + 1):
            linha.append(0)
        matriz.append(linha)
    
    for l in range(1, len(x) + 1):
        # primeira linha
        matriz[l][0] = l

    for c in range(1, len(y) + 1):
        # primeira coluna
        matriz[0][c] = c
        
    return matriz

def resolve_matriz(matriz, x, y):
    # Vamos percorrer as colunas 
    for k in range(1, len(y) + 1):
        # Percorrendo termo a termo
        for i in range(1, len(x) + 1):
            for j in range(1, len(y) + 1):
                # A função min() retornará o menor dentre os valores dados como argumentos
                matriz[i][j] = min(matriz[i-1][j-1] + checa_alinhamento(x, y, i-1, j-1), # Alinhar
                                    matriz[i-1][j] + 1, # Deletar
                                    matriz[i][j-1] + 1) # Inserir

    return matriz

if __name__ == "__main__":
    x = "TCCAGT"
    y = "TGCCTAG"
    z = prepara_matriz(x, y)
    z = resolve_matriz(z, x, y)

    for i in z:
        print(i)

    solution = []
    alinhamento_final(z, len(x), len(y))
    
    # solution = []
    # alinhamento_final(z, len(x), len(y))
    # print(solution[::-1])
    for i in solution[::-1]:
        print(i)