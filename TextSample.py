#1 - justificação de textos


def limpa_texto(string):
    """ Recebe uma cadeira de caracteres qualquer e devolve a cadeia de caracteres limpa (ou seja, sem os caracteres brancos ASCII)
    Qualquer string ---> string 'limpa'
    """
    #Utilizar a funcionalidade 'replace' para substituir todos os caracteres brancos ASCII da nossa string por espaços
    for c in ('\n','\t','\v','\f','\r'):
        string_final = string.replace(c,' ')
    #dividir a string com o 'split'
    string_final = string_final.split()
    #junta-la com o 'join' (separada por espaços)
    string_final = ' '.join(string_final)
    return string_final

def corta_texto(string,num):
    """ Recebe uma cadeia de caracteres(correspondente a um texto limpo) e um inteiro positivo(largura de coluna) e devolve duas sub-cadeias
    de caracteres limpas constituidas apenas por palavras completas e , no caso da primeira, com a largura máxima possivel mais perto ou igual à da coluna. 
    Sendo que a segunda é constituida pela restante parte da string
    string,int ---> string,string
    """
    #separar a string por palavras(lista de palavras)
    c = string.split()
    string_final = ''
    #para os casos que não tÊm a primeira parte do tuplo vazia, teremos de ver quantas palavras cabem sabendo que temos limite de caracteres
    #percorremos um for desde o priemiro elemento da lista de palavras até ,no maximo, ao final, adicionando as palavras e os respetivos espaços
    #caso o numero de caracteres por coluna já esteja adequado e ainda nao tenhamos chegado ao fim da lista de palavras 'quebramos' o ciclo
    for e in range(0,len(c)):
        if len(string_final)+len(c[e]) < num and e!= 0:
            string_final += ' '+ c[e]
        elif e == 0 and len(c[e])<=num: #se o comprimento da primeira palavra for menor ou igual à largura da coluna a primeira parte do tuplo será logo ocupada pela primeira palavra da string
            string_final += c[e]
        else:
            break
    #devolvemos a nossa string final.strip() de forma a eliminar espaços indesejados e a segunda parte do tuplo que nada mais é que a string inicial desde a proxima palavra da lista até ao fim (igualmente com strip)
    return string_final.strip(),string[len(string_final):].strip()

def insere_espacos(string,num):
    """Esta funçao recebe uma cadeia de carateres e um inteiro positivo correspondentes a um
    texto limpo e uma largura de coluna respetivamente e devolve uma cadeia de caracteres 
    com os espaços devidos de forma a perfazer a largura da coluna.
    string,int ---> string
    """
    #num = numero de espaços a adicionar
    num = num - len(string)
    #a = lista de palavras
    a = string.split()
    # verificar a condição do enunciado - se tiver mais de duas palavras na lista adiciona no meio caso contrario no final
    if len(a)>=2:
        i = 0
        contador = 0
        for e in string:
            if e == ' ':
                contador += 1 
        #conta o numero de espaços que tem
        #enquanto houver espaços para colocar até fazer a dimensão da string vamos adicionando espaços um a cada indice da lista de palavras (espaços que ja existiam mais os novos)
        while i<(num+contador):
            for c in range(1,len(a)):
                a[c] = ' ' + a[c]
                i+=1
                # se acontecer de o numero de espaços se esgotar antes de percorrer toda a string o ciclo for acaba e consequentemente o while tbm
                if i>=(num+contador):
                    break
        #tendo a nossa lista com os espaços desejados e só juntar tudo
        string_final = ''
        for f in a:
            string_final += f
        return string_final
    else:
        for c in range(num):
            string += ' '
        return string

def justifica_texto(string,num):
    """ Esta função recebe uma cadeia de carateres não vazia e um inteiro positivo correspondentes a um texto qualquer e uma largura de coluna 
        respetivamente, e devolve um tuplo de cadeias de carateres justificadas, isto é, de comprimento igual à largura da coluna.
        Qualquer string, int ---> tuplo(strings justificadas)
    """
    if string != '' and type(string)==str and type(num)==int:
        str1 = string.split() #lista de elementos
        maior = 0
        for c in str1:
            comp = len(c)
            if comp > maior:
                maior = comp #vê qual elemento é maior na lista
        if maior <= num: #compara os argumentos e verifica a validade, caso nao sejam lança um erro
            tuplo = ()
            string_res = ''
            i = 0 
            # enquanto a segunda string do tuplo produzido pelo corta_texto for diferente de vazio , 'justificamos' o texto e adicionamos ao nosso tuplo final
            while True:
                string = limpa_texto(string)
                string = corta_texto(string,num)
                string_res = insere_espacos(string[0],num)
                tuplo += (string_res,)
                string = string[-1]
                if string == '':
                    break
                i+=1
            #como a ultima cadeia do tuplo terá de ser justificada atraves de junção de espaços teremos de repetir um processo usado em insere_espaços
            #otimização --> utilizar um argumento neutro em 'insere_espaços', tornaria desnecessária este acrescimo de linhas
            string2 = limpa_texto(tuplo[-1]) #limpamos o texto da ultima cadeia de caracteres
            for w in range(abs(num-len(string2))): #vemos os espaços a adicionar e adicionamos
                string2 += ' '
            tuplo_final = tuplo[:-1]+(string2,) #resultado será a junção dos dois tuplos (o que contem as primeiras linhas e o que contem a ultima)
            return tuplo_final
        else:
            raise ValueError ('justifica_texto: argumentos invalidos')
    else:
        raise ValueError ('justifica_texto: argumentos invalidos')

#2 - Método de hondt

def calcula_quocientes(dic,num):
    ''' Recebe um dicionário com os votos apurados num círculo (com pelo menos
    um partido) e um inteiro positivo representando o número de deputados; e devolve o
    dicionário com as mesmas chaves do dicionário argumento (correspondente a partidos)
    contendo a lista (de comprimento igual ao número de deputados) com os quocientes
    calculados com o método de Hondt ordenados em ordem decrescente. 
    circulo eleitorial(dicionário), nº deputados(inteiro) ----> dicionário c/ quocientes
    '''
    novo_dic = dic.copy()
    lista_valores = []
    for c in novo_dic: #percorre o dicionário pelas chaves
        valor = novo_dic[c] #assume o primeiro valor associado à primeira chave(partido)
        for d in range(1,num+1):  #loop de divisões sucesssivas para calcular todos os quocientes daquele partido
            res = valor/d
            lista_valores.append(res)
        novo_dic[c] = lista_valores #alteração do valor no dicionário final para a lista dos quocientes
        lista_valores=[]
    return novo_dic

def min_partido(valor,dic,novo_dic):  
    #função auxuliar com o objetivo de ver qual dos partidos com o mesmo valor de quociente tem
    # o menor numero de votos daquele circulo eleitoral
    lista_partido=[]
    for c in novo_dic:
        if valor in novo_dic[c]: # ver quais partidos têm o mesmo valor e adicionar a uma lista de 'repetidos'
            partido = c
            lista_partido.append((partido,dic[partido]))
    menor = lista_partido[0][1] #pegar no primeiro valor
    partido = lista_partido[0][0] #pegar na primeira chave(partido)
    for k in lista_partido:
        if k[1]<menor: #verificar qual será o que tem menos votos totais daquele circulo
            menor = k[1]
            partido = k[0]
    return partido #retornar o partido com o mesmo numero de quociente mas menos votos totais no circulo

def atribui_mandatos(dic,num):
    ''' recebe um dicionário com os votos apurados num círculo e um inteiro representando o número de deputados, 
    e devolve a lista ordenada de tamanho igual ao número de deputados contendo as cadeias de carateres dos partidos 
    que obtiveram cada mandato.
    dicionário(circulo eleitoral),inteiro(numero de deputados) ----> lista ordenada de partidos
    '''
    novo_dic = calcula_quocientes(dic,num) #calcula os quocientes
    maior = 0
    lista = []
    for c  in range(num):
        for c in novo_dic:
            linha = novo_dic[c]
            maximo = max(linha)
            if maximo >= maior: #analisa sempre o valor maximo daquele circulo e associa a um partido
                maior = maximo
                partido = c
        partido = min_partido(maior,dic,novo_dic) #verifica se o partido em questão nao entra em conflito com nenhum outro ao nivel dos votos
        # e se sim vai procurar atraves da função auxiliar 'min_partido' qual é o partido adeqaudo aquele mandato
        novo_dic[partido].remove(maior) # remove o valor para que nao hajam repetições 
        lista.append(partido) # adiciona à nossa lista ordenada de partidos
        maior = 0
    return lista
        
def obtem_partidos(dic):
    '''Esta função recebe um dicionário com a informação sobre as eleições num território
    com vários círculos eleitorais como descrito, e devolve a lista por ordem alfabética com
    o nome de todos os partidos que participaram nas eleições
    dicionário(circulos_eleitorias) ---> lista dos partidos
    '''
    lista_partidos = []
    for c in dic:
        for w in dic[c]['votos']:
            if w not in lista_partidos:
                lista_partidos.append(w)
    return sorted(lista_partidos)

def e_valido(dic):  #fução auxiliar de verificação do dicioário passado como argumento de 'obtem_resultados_eleições
    # decidi fazer uma verificação onde eu vou passo a passo chegando o mais longe possivel no meu dicionário, ou seja, o mais profundo
    # possivel sempre verificando as condições, se nao parar em qualquer lado quer dizer que o dicionário é valido e retorna True
    if type(dic) == dict:
        if len(dic)>= 1:
            for c in dic: #verificar circulo a circulo
                if type(dic[c]) == dict and len(dic[c])>1 and type(c)==str and c!='':
                    for h in dic[c]: #verificar nomes de chaves
                        if h not in ('votos','deputados'):
                            return False
                    if type(dic[c]['votos']) == dict and type(dic[c]['deputados'])==int and dic[c]['deputados']>=1: #verificar tipo e quantidade
                        if len(dic[c]['votos'])>=1:
                            for d in dic[c]['votos']: #verificar o dicionário 'votos', ou seja, chave, valores e quantidades
                                if type(d) != str or type(dic[c]['votos'][d])!= int or d=='' or dic[c]['votos'][d]<1:
                                    return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        else:
            return False
    else:
        return False
    return True

def obtem_resultado_eleicoes(dic):
    '''Esta função recebe um dicionário com a informação sobre as eleições num território com
    vários círculos eleitorais como descrito, e devolve a lista ordenada de comprimento igual
    ao número total de partidos com os resultados das eleições. Cada elemento da lista é
    um tuplo de tamanho 3 contendo o nome de um partido, o número total de deputados
    obtidos e o número total de votos obtidos.
    dicionário(circulos de eleições)--->lista ordenada dos resultados
    '''
    if e_valido(dic): #verificação com auxilio da função 'e_valido'
        lista_partidos = obtem_partidos(dic)
        i=0
        numero_deputados = 0
        numero_votos =  0
        lista_resultados = []
        lista_resultados_final = []
        while i != len(lista_partidos): #avaliar todos os partidos
            for u in dic: 
                num = dic[u]['deputados']
                dicionario = dic[u]['votos']
                lista = atribui_mandatos(dicionario,num) #ver os partidos que adquiriram mandato naquele circulo para aqueles deputados
                for w in lista: #ver numero de votos e deputados total
                    if lista_partidos[i] == w:
                        numero_deputados+=1 
                for o in dicionario:
                    if lista_partidos[i] == o:
                        numero_votos+= dicionario[o]
            #adicionár à lista final
            lista_resultados.append((lista_partidos[i],numero_deputados,numero_votos)) 
            numero_deputados = 0
            numero_votos = 0
            i+=1
        #organizar a lista atraves da função auxiliar
        lista_resultados_final = organiza_lista(lista_resultados)
        return lista_resultados_final
    else:
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')

def organiza_lista(lista):
    # função auxiliar de organização
    return sorted(lista,key = compara,reverse=True)

def compara(x):
    #função auxiliar de comparação
    return (x[1],x[2])

#3 - Sistemas eq.lineares

def produto_interno(t1,t2):
    ''' Esta função recebe dois tuplos de números (inteiros ou reais) com a mesma dimensão
    representando dois vetores e retorna o resultado do produto interno desses dois vetores.
    tuplo1,tuplo2 ---> (tuplo1 X tuplo2)(real)
    '''
    total = 0
    for i in range(len(t2)):
            mult = t1[i]*t2[i]
            total += mult
    return float(total)

def verifica_convergencia(linhas_matriz,const,sol,e):
    '''Recebe um tuplo representando a matriz quadrada A, um tuplo representado as constantes associadas a cada linha da matriz, a solução atual para cada uma das incognitas
    bem como o erro que estará associado a este resultado e verifica se o resultado atual tem um erro inferior ao passado como argumento
    matriz(tuplo),constantes(tuplo),solução(tuplo),erro ----> bool
    '''
    i = 0
    while i != len(linhas_matriz): #como é quadrada nº linhas= nº colunas
        valor = produto_interno(linhas_matriz[i],sol) #produto interno da linha i pelo vetor 'solução' 
        erro = abs(valor-const[i])
        if erro > e: # verificação de todas as linhas
            return False
        i+=1
    return True

def retira_zeros_diagonal(t1,t2):
    '''Recebe dois tuplos, um representando a matriz quadrada A e outro representado o vetor das constantes asscociadas a cada linha de A e devolve
    dois tuplos da mesma natureza que os passados como argumentos só que com os valores da diagonal principal nunca igual a zero, operando com trocas de linhas
    da matriz para que isto seja possivel
    matriz(tuplo),vetor das constantes(tuplo) ---> matriz sem zeros na diagonal(tuplo),vetor das constantes associado respetivamente(tuplo)
    '''
    i = 0
    t1 = list(t1)
    t2 = list(t2)
    while i != len(t1):
        if t1[i][i] == 0: 
            for j in range(len(t1)):
                if t1[j][i]!= 0 and t1[i][j]!= 0:
                    t1[i],t1[j] = t1[j],t1[i] #troca de linhas
                    t2[i],t2[j] = t2[j],t2[i] #troca de constantes para condizer com as linhas respetivas
                    break  #para evitar que haja mais do que uma troca, porque pode haver mais linhas que satisfação esta condição, no entanto nos so queremos a primeira que satisfaça
        i+=1
    return tuple(t1),tuple(t2)

def eh_diagonal_dominante(m):
    '''Recebe dois tuplos, um representando a matriz quadrada A e outro representado o vetor das constantes asscociadas a cada linha de A e devolve
    um bool(True ou False) se a matriz é diagonal dominante
    matriz quadrada (tuplo) ---> bool
    '''
    soma_total = 0
    for i in range(len(m)): #percorrer todas as linhas
        for j in range(len(m)): #percorrer a linha na sua extensão
            if j!=i:
                soma_total = soma_total + abs(m[i][j]) #soma de todos os valores de uma linha excepto da diagonal
        if abs(m[i][i]) < soma_total: #comparação
            return False
        soma_total = 0
    return True

def eh_matriz_valida(matriz): #função auxiliar de validação de uma matriz quadrada A
    if type(matriz)==tuple:
        comp_linhas = len(matriz) #nº linhas
        for c in matriz:
            if type(c) == tuple:
                comp_colunas = len(c) #nº colunas
                if comp_linhas == comp_colunas:
                    for i in c:
                        if type(i)!= int and type(i)!=float:
                            return False
                else:
                    return False
            else:
                return False
    else:
        return False
    return True

def eh_valido_const(const): #função auxiliar de validação do vetor das constantes
    if type(const)==tuple:
        for c in const:
            if type(c) != float and type(c)!= int:
                return False
    else:
        return False
    return True

def resolve_sistema(t1,t2,e):
    '''Recebe dois tuplos, um representando a matriz quadrada A e outro representado o vetor das constantes asscociadas a cada linha de A, e um valor 
    associado a um erro de aproximação do valor da solução e devolve a solução deste mesmo sistema adequado ao erro passado como argumento.
    matriz quadrada A (tuplo), vetor das constantes (tuplo), erro (real) ---> solução do sistema(tuplo)
    '''
    if eh_matriz_valida(t1) and eh_valido_const(t2) and len(t1)==len(t2) and type(e)==float and e>0: #validade dos argumentos
        sol = [0]*len(t1) #criação de um vetor a zeros de comprimento igual ao numeoro de colunas (que sera a primeira estimativa)
        t1,t2 = retira_zeros_diagonal(t1,t2) #retiramos zeros da diagonal
        if eh_diagonal_dominante(t1): #vemos se é daigonal dominante
            while not verifica_convergencia(t1,t2,sol,e): #enquanto nao verificar convergencia vai fazendo recurso da função auxiliar 'estimativa_seguinte' para obter nova estimativa e comparar
                sol = estimativa_seguinte(t1,t2,sol)
            return sol 
        else:
            raise ValueError('resolve_sistema: matriz nao diagonal dominante')
    else:
        raise ValueError('resolve_sistema: argumentos invalidos')

def estimativa_seguinte(m1,c,atual): #função auxiliar de estimativa seguinte
    resultados = []
    for i in range(len(m1)):
        res = atual[i] + (c[i]- produto_interno(m1[i],atual))/m1[i][i]
        resultados.append(res)
    return tuple(resultados)