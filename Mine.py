###### MINAS ######

# TAD Gerador - representado por uma lista de dois elementos, em que o primeiro representa o numero
# de bits e o segundo o estado do gerador

# Opreações Básicas:

#   cria_gerador(b,s)
#   cria_copia_gerador(g)
#   obtem_estado(gerador)
#   obtem_bits(gerador)
#   define_estado(gerador,num)
#   def atualiza_estado(gerador)
#   eh_gerador(arg)
#   geradores_iguais(g1,g2)
#   gerador_para_str(g)


def cria_gerador(b,s):
    '''cria_gerador(b, s) --> gerador
    O TAD gerador é usado para gerar números pseudoaleatórios.
    Recebe um inteiro b correspondente ao número de 'bits'
    do gerador e um inteiro positivo s correspondente à 'seed' ou estado inicial,
    e devolve o gerador correspondente.
    '''
    if type(b)==int and type(s)== int and ( b ==32 or b == 64 ) and 0<s<=2**b : #verificações simples e criação do gerador
        return [b,s]
    else:
        raise ValueError('cria_gerador: argumentos invalidos')

def cria_copia_gerador(g): #copia
    '''cria_copia_gerador(g) --> gerador
    Recebe um gerador e devolve uma cópia nova do gerador.
    '''
    b_copy = obtem_bits(g)
    s_copy = obtem_estado(g)
    return cria_gerador(b_copy,s_copy)

def obtem_estado(gerador):
    '''obtem_estado(g) --> int(estado)
    Recebe um gerador e devolve o estado atual do mesmo, sem o alterar.(seed do gerador)
    '''
    return gerador[1]

def obtem_bits(gerador):
    '''obtem_bits(g) --> int(estado)
    Recebe um gerador e devolve os bits do mesmo, sem o alterar.
    '''
     # função auxiliar que decidi criar visto que faz sentido neste TAD
    return gerador[0]

def define_estado(gerador,num):
    '''
    define_estado(g, s) --> int(estado)
    Define o novo valor do estado do gerador g como sendo s,
    e devolve s.
    '''
    gerador[1] = num
    return gerador[1]

def algoritmo_gera(b,s): #função auxiliar para o gerador (xorshift)
    if b == 32:
        s ^= ( s << 13 ) & 0xFFFFFFFF
        s ^= ( s >> 17 ) & 0xFFFFFFFF
        s ^= ( s << 5 ) & 0xFFFFFFFF
    elif b == 64:
        s ^= ( s << 13 ) & 0xFFFFFFFFFFFFFFFF
        s ^= ( s >> 7 ) & 0xFFFFFFFFFFFFFFFF
        s ^= ( s << 17 ) & 0xFFFFFFFFFFFFFFFF
    return s

def atualiza_estado(gerador):
    '''atualiza_estado(g) --> int(estado)
    Atualiza o estado do gerador g de acordo com o algoritmo
    xorshift de geração de números pseudoaleatórios, e devolve-o'''
    s = algoritmo_gera(obtem_bits(gerador),obtem_estado(gerador)) #fazer recurso da função auxiliar 
    if 0<s<=2**(obtem_bits(gerador)): #verificar as condições de um estado deste TAD gerador
        define_estado(gerador,s)
        return s

def eh_gerador(arg):
    '''eh_gerador(arg) --> Bool
    Recebe um argumento e devolve True caso o seu argumento seja um TAD gerador e
    False caso contrário'''
    try: #tenta verificar as condições caso gere um erro,devolve False e em caso de conseguir mas se o argumento nao as satisfizer, devolve False
        return type(arg)==list and type(arg[0])==int and type(arg[1])== int and ( arg[0] ==32 or arg[0] == 64 ) and 0<arg[1]<2**(arg[0])
    except: 
        return False

def geradores_iguais(g1,g2):
    '''geradores_iguais(g1, g2) 
    Devolve True apenas se g1 e g2 forem geradores e se 
    forem iguais.'''
    return g1 == g2 #é uma comparação simples

def gerador_para_str(g):
    '''gerador_para_str(g) --> str
    Devolve a cadeia de carateres que representa o gerador xorshift g.
    '''
    return f'xorshift{obtem_bits(g)}(s={obtem_estado(g)})'

def gera_numero_aleatorio(g,n):
    '''gera_numero_aleatorio(g, n) --> int
    Recebe um gerador (g) e um inteiro(n) , atualiza o estado do gerador g e devolve um número
    aleatório no intervalo [1, n]'''
    atualiza_estado(g)
    seed = obtem_estado(g)
    return 1 + seed%n

def gera_carater_aleatorio(g,c):
    '''gera_caracter_aleatorio(g,c) --> str
    Recebe um gerador (g) e um caracter(c) atualiza o estado do gerador e devolve um carácter
    aleatório no intervalo entre 'A' e o caracter maiusculo c.'''
    atualiza_estado(g)
    l = [chr(a) for a in range(65,ord(c)+1)]
    seed = obtem_estado(g)
    return l[seed%len(l)]


# TAD Coordenada - imutavel - representado por um tuplo de dois elementos, na forma (x,y) em que
#x - corresponde à coluna do campo e y - linha do campo.

# Operações Básicas:

#   cria_coordenada(col,lin)
#   obtem_coluna(coord)
#   obtem_linha(coord)
#   eh_coordenada(coord)
#   coordenadas_iguais(cord1,cord2)
#   coordenada_para_str(cord)
#   str_para_coordenada(str)


def cria_coordenada(col,lin):
    '''cria_coordenada(col, lin) --> Coordenada
    O TAD Coordenada representa a coordenada que será associada cada parcela.
    Recebe os valores correspondentes à coluna col e
    linha lin e devolve a coordenada correspondente.'''
    if type(col)==str and type(lin) == int and 'A'<= col <= 'Z' and len(col)==1 and 1<= lin <= 99: #condições simples e necessárias
        return (col,lin)
    else:
        raise ValueError('cria_coordenada: argumentos invalidos')

def obtem_coluna(coord):
    '''obtem_coluna(coord) --> str(coluna)
    Recebe uma coordenada e devolve a coluna col da coordenada coord.'''
    return coord[0]

def obtem_linha(coord):
    '''obtem_linha(coord)--> int(linha) 
    Recebe uma coordenada e devolve a linha lin da coordenada coord.'''
    return coord[1]

def eh_coordenada(coord):
    '''eh_coordenada(coord) --> bool
    Recebe um argumento(potencialmente uma coordenada) e devolve True caso o seu argumento seja um TAD coordenada
    e False caso contrário.'''
    try: #forma simplificada de verificação que evita erros indesejados em alguns casos especificos
        return type(coord)==tuple and type(coord[0])==str and len(coord[0]) == 1 and type(coord[1])==int and 'A'<= coord[0] <= 'Z' and 1<= coord[1] <= 99
    except:
        return False

def coordenadas_iguais(cord1,cord2):
    '''coordenadas_iguais(cord1, cord2) --> bool
    Recebe duas coordenadas e devolve True apenas se cord1 e cord2 são coordenadas e
    são iguais.'''
    if eh_coordenada(cord1) and eh_coordenada(cord2):
        return cord1 == cord2

def coordenada_para_str(cord):
    '''coordenada_para_str(cord) --> str
    Devolve a cadeia de carateres que representa o TAD Coordenada'''
    if eh_coordenada(cord):
        return '{}{:02}'.format(obtem_coluna(cord),obtem_linha(cord))

def str_para_coordenada(str):
    '''str_para_coordenada(str) --> coordenada
    Devolve a coordenada que é representada pela string introduzida'''
    return cria_coordenada(str[0],int(str[1:]))

def obtem_coordenadas_vizinhas(coordenada):
    '''obtem_coordenadas_vizinhas(c) --> tuplo
    Devolve um tuplo com as coordenadas vizinhas à
    coordenada c, começando pela coordenada na diagonal acima-esquerda de c e seguindo
    no sentido horário.'''
    if eh_coordenada(coordenada):
        tuplo = ()
        col = chr(ord(obtem_coluna(coordenada))-1) #pega na coluna diagonal acima-esquerda
        linha = obtem_linha(coordenada)-1 #pega na linha diagonal acima-esquerda
        for rep in range(4): # vamos descrever as coordenadas vizinhas como 4 linhas distintas de progressão
            for viz in range(2): # em que cada linha é constituida por uma progresão de 2 unidades(col ou lin)(4x2 - Nº Max de coordenadas vizinhas)
                if 'A'<= col <= 'Z' and 1<= linha <= 99: #unicas condições necessárias de verificar
                    cord = cria_coordenada(col,linha)
                    tuplo += (cord,)
                if rep == 0: # 1º linha de progressão - progressão ao nivel das colunas, ou seja, mantemos a linha e avançamos na coluna
                    col = chr(ord(col)+1)
                if rep == 1: # 2º - progressao ao nivel das linhas, ou seja, mantemos a coluna e avancamos na linha
                    linha = linha + 1
                if rep == 2: # 3º - mantemos a linha e regredimos na coluna
                    col = chr(ord(col)-1)
                if rep == 3: # 4º - mantemos a coluna e regredimos nas linhas
                    linha = linha - 1
        return tuplo

def obtem_coordenada_aleatoria(c,g):
    '''obtem_coordenada_aleatoria(c, g) --> coordenada
    Recebe uma coordenada c e um TAD gerador g, e devolve uma coordenada gerada aleatoriamente. Em
    que c define a maior coluna e maior linha possíveis. 
    '''
    if eh_gerador(g): #associa o gera caracter e o gera numero (aleatorios) para criar uma nova coordenada
        nova_cord = cria_coordenada(gera_carater_aleatorio(g,obtem_coluna(c)),gera_numero_aleatorio(g,obtem_linha(c)))
        return nova_cord

# TAD Parcela - representado por um dicionário com onde a chave 'estado' corresponde ao estado da parcela('limpa','marcada','tapada') e a denomiação 'mina'(chave) 
# que está associada a um bool(valor) que nos diz se tem mina ou não.

# Operações Básicas:

#   cria_parcela() 
#   cria_copia_parcela(parcela)
#   limpa_parcela(parcela)
#   marca_parcela(parcela) 
#   desmarca_parcela(parcela)
#   esconde_mina(parcela)
#   eh_parcela(arg)
#   eh_parcela_tapada(parc)
#   eh_parcela_marcada(parc)
#   eh_parcela_limpa(parc)
#   eh_parcela_minada(parc)
#   parcelas_iguais(p1,p2)
#   parcela_para_str(parc)


def cria_parcela():
    '''cria_parcela() --> Parcela
    O TAD Parcela é o objeto que representa cada 'quadradinho' do campo de minas. Tem
    um estado (tapada, limpa ou marcada) e pode esconder uma mina.
    A função cria uma parcela tapada sem mina escondida'''
    return {'estado':'tapada','mina': False}

def cria_copia_parcela(parcela):
    '''cria_copia parcela(p) --> Parcela
    Recebe uma parcela p e devolve uma nova cópia da parcela.'''
    if eh_parcela(parcela): #Criação de um novo dicionário com os valores do anterior
        novo_dic = {'estado':parcela['estado'],'mina':parcela['mina']}
        return novo_dic

def limpa_parcela(parcela):
    '''limpa_parcela(p) --> parcela
    Modifica destrutivamente a parcela p modificando o seu estado
    para limpa, e devolve a própria parcela.'''
    if eh_parcela(parcela):
        parcela['estado'] = 'limpa'
        return parcela

def marca_parcela(parcela):
    '''marca_parcela(p) --> parcela
    Modifica destrutivamente a parcela p modificando o seu estado
    para marcada com uma bandeira, e devolve a própria parcela.'''
    if eh_parcela(parcela):
        parcela['estado'] = 'marcada'
        return parcela

def desmarca_parcela(parcela):
    '''marca_parcela(p) --> parcela
    Modifica destrutivamente a parcela p modificando o seu estado
    para tapada, e devolve a própria parcela.'''
    if eh_parcela(parcela):
        parcela['estado'] = 'tapada'
        return parcela

def esconde_mina(parcela):
    '''esconde_mina(p) --> parcela
    Modifica destrutivamente a parcela p escondendo uma mina
    na parcela, e devolve a própria parcela.'''
    if eh_parcela(parcela):
        parcela['mina'] = True
        return parcela

def eh_parcela(arg):
    '''eh_parcela(arg) --> bool
    Devolve True caso o seu argumento seja um TAD parcela e
    False caso contrário.'''
    try: #verificação padrao para evitar erros e verificações de casos especificos
        return type(arg)==dict and type(arg['mina']) == bool and arg['estado'] in ('limpa','marcada','tapada')   
    except:
        return False

def eh_parcela_tapada(parc):
    '''eh parcela tapada(p) --> bool
    Devolve True caso a parcela p se encontre tapada e False
    caso contrário.'''
    if eh_parcela(parc):
        return parc['estado'] == 'tapada'

def eh_parcela_marcada(parc):
    '''eh_parcela_marcada(p) --> bool
    Devolve True caso a parcela p se encontre marcada
    com uma bandeira e False caso contrário.'''
    if eh_parcela(parc):
        return parc['estado'] == 'marcada'  

def eh_parcela_limpa(parc):
    '''eh_parcela_limpa(p) --> bool
    Devolve True caso a parcela p se encontre limpa e False
    caso contrário.'''
    if eh_parcela(parc):
        return parc['estado'] == 'limpa'    

def eh_parcela_minada(parc):
    '''eh_parcela_minada(p) --> bool
    Devolve True caso a parcela p esconda uma mina e
    False caso contrário.'''
    if eh_parcela(parc):
        return parc['mina']

def parcelas_iguais(p1,p2):
    '''parcelas_iguais(p1, p2) --> bool
    Devolve True apenas se p1 e p2 são parcelas e são
    iguais.'''
    if eh_parcela(p1) and eh_parcela(p2):
        return p1 == p2

def parcela_para_str(parc):
    '''parcela_para_str(p) --> Parcela
    Devolve a cadeia de caracteres que representa a parcela
    em função do seu estado: parcelas tapadas ('#'), parcelas marcadas ('@'),
    parcelas limpas sem mina ('?') e parcelas limpas com mina ('X').'''
    if eh_parcela(parc): # denominação do enunciado para as parcelas
        if eh_parcela_tapada(parc):
            return '#'
        elif eh_parcela_marcada(parc):
            return '@'
        elif eh_parcela_limpa(parc) and not eh_parcela_minada(parc):
            return '?'
        elif eh_parcela_limpa(parc) and eh_parcela_minada(parc):
            return 'X'

def alterna_bandeira(parc):
    '''alterna_bandeira(p) --> bool
    Recebe uma parcela p e modifica-a destrutivamente da seguinte
    forma: desmarca se estiver marcada e marca se estiver tapada, devolvendo True.
    Em qualquer outro caso, não modifica a parcela e devolve False.'''
    if eh_parcela(parc):
        changed = False 
        if eh_parcela_marcada(parc): #desmarca e troca o changed
            desmarca_parcela(parc)
            changed = True
        elif eh_parcela_tapada(parc): #ou então marca e troca o changed
            marca_parcela(parc)
            changed = True
        return changed


# TAD Campo - Campo representado um dicionário que associa TAD coordenadas a TAD parcelas (pares chave-valor).

# Operações Básicas:

#   cria_campo(coluna,linha) 
#   cria_copia_campo(campo)
#   obtem_ultima_coluna(campo) 
#   obtem_ultima_linha(campo) 
#   obtem_parcela(m,cord) 
#   obtem_coordenadas(m,string) 
#   obtem_numero_minas_vizinhas(campo,c) 
#   eh_campo(arg)
#   eh_Coordenada_do_Campo(campo,c) 
#   campos_iguais(m1,m2)
#   campo_para_str(m)


def cria_campo(col,lin):
    '''cria_campo(c, l) --> Campo
    Recebe uma cadeia de carateres e um inteiro correspondentes
    à última coluna e à última linha de um campo de minas, e devolve o campo
    do tamanho pretendido formado por parcelas tapadas sem minas.'''
    try:
        cria_coordenada(col,lin) #para nao duplicar codigo a verificação passa por ver se é cordenada
        i = 65 #ord('A')
        dic = {} #campo representado por dicionário onde a chave é a coordenada e o valor a parcela
        while i <= ord(col): # representa as colunas
            for c in range(1,lin+1): # representa as linhas
                dic[cria_coordenada(chr(i),c)] = cria_parcela() #associar coords a parcelas
            i+=1
        return dic
    except:
        raise ValueError('cria_campo: argumentos invalidos')

def cria_copia_campo(m):
    '''cria_copia_campo(m) --> campo
    Recebe um campo e devolve uma nova cópia do campo.'''
    if eh_campo(m): #copia profunda
        novo_dic = {}
        for chave in m: #percorrer o dicionário e copiar as parcelas
            novo_dic[chave] = cria_copia_parcela(obtem_parcela(m,chave))
        return novo_dic

def obtem_ultima_coluna(m):
    '''obtem_ultima_coluna(m) --> str
    Devolve a cadeia de caracteres que corresponde à
    última coluna do campo de minas.'''
    return obtem_coluna(list(m.keys())[-1]) #ultimo elemento da lista de chaves(coordenadas)

def obtem_ultima_linha(m):
    '''obtem_ultima_linha(m) --> int
    Devolve o valor inteiro que corresponde à última linha
    do campo de minas.'''
    return obtem_linha(list(m.keys())[-1]) #ultimo elemento da lista de chaves(coordenadas)

def obtem_parcela(m,cord):
    '''obtem_parcela(m, c) --> parcela
    Devolve a parcela do campo m que se encontra na coordenada c.'''
    if cord in m:
        return m[cord]

def obtem_coordenadas(m,string):
    '''obtem_coordenadas(m, s) --> tuplo
    Devolve o tuplo formado pelas coordenadas ordenadas
    em ordem ascendente de esquerda à direita e de cima a baixo das parcelas
    dependendo do valor de s: 'limpas' para as parcelas limpas, 'tapadas' para
    as parcelas tapadas, 'marcadas' para as parcelas marcadas, e 'minadas'
    para as parcelas que escondem minas.'''
    tuplo = ()
    for c in m:
        if string == 'limpas' and eh_parcela_limpa(obtem_parcela(m,c)):
            tuplo+=(c,)
        elif string=='tapadas' and eh_parcela_tapada(obtem_parcela(m,c)):
            tuplo+=(c,)
        elif string == 'minadas' and eh_parcela_minada(obtem_parcela(m,c)):
            tuplo+=(c,)
        elif string =='marcadas' and eh_parcela_marcada(obtem_parcela(m,c)):
            tuplo += (c,)
    return tuple(sorted(tuplo, key = lambda x: (obtem_linha(x),obtem_coluna(x)))) 
    # garantir que é um tuplo ordenado pelas linhas pelas colunas

def obtem_numero_minas_vizinhas(m,c):
    '''obtem_numero_minas_vizinhas(m, c) --> int 
    Devolve o número de parcelas vizinhas
    da parcela na coordenada c que escondem uma mina.'''
    if eh_campo(m) and eh_coordenada(c):
        contador = 0
        viz = obtem_coordenadas_vizinhas(c) #obter coordenadas vizinhas
        for coordenada in m: # percorrer o campo
            if coordenada in viz and eh_parcela_minada(obtem_parcela(m,coordenada)): # ver se estava na vizinhança e é minada
                contador += 1 #adiciona um ao contador
        return contador 

def eh_campo(campo):
    '''eh_campo(arg) --> bool
    Devolve True caso o seu argumento seja um TAD campo e
    False caso contrário'''
    if type(campo)==dict and len(campo)>0:
        for cord in campo:
            if not eh_coordenada(cord) or not eh_parcela(obtem_parcela(campo,cord)):
                #verifica todas as coordenadas e parcelas do campo
                return False
        return True
    else:
        return False

def eh_coordenada_do_campo(m,c):
    '''eh_coordenada_do_campo(m, c) --> bool
    Devolve True se c é uma coordenada válida
    dentro do campo m.'''
    if eh_campo(m) and eh_coordenada(c):
        return c in m

def campos_iguais(m1,m2):
    '''campos_iguais(m1, m2) --> bool
    Devolve True apenas se m1 e m2 forem campos e
    forem iguais'''
    if eh_campo(m1) and eh_campo(m2): # verificação para respeitar as barreiras de abstração
        i = 65 #ord('A')
        lin = obtem_ultima_linha(m1)
        lin_m2 = obtem_ultima_linha(m2)
        col = obtem_ultima_coluna(m1)
        col_m2 = obtem_ultima_coluna(m2)
        if col_m2 == col and lin == lin_m2: #como veridicamos anteriomente se era campo é válido ver se têm o mesmo numero de colunas e linhas
            while i <= ord(col):
                for c in range(1,lin+1):
                    if not parcelas_iguais(obtem_parcela(m1,cria_coordenada(chr(i),c)),obtem_parcela(m2,cria_coordenada(chr(i),c))): 
                        return False
                        #Fazendo recurso da função 'parcelas_iguais' vamos criando coordenadas apenas com o efeito de verificação, não alterando nada
                i+=1
        else:
            return False
        return True

def campo_para_str(m):
    '''campo_para_str(m) --> str
    Devolve uma cadeia de caracteres que representa o campo
    de minas.'''
    if eh_campo(m):
        string_colunas = ''
        string_final = '   ' #considerar já o espaçamento inicial
        for chave in m: #formar as string das colunas do campo
            if obtem_coluna(chave) not in string_colunas:
                string_colunas += obtem_coluna(chave)
        string_final +=string_colunas+'\n  +'+'-'*len(string_colunas)+'+\n' #separação
        for rep in range(1,obtem_ultima_linha(m)+1): #ciclo para representar a linha 'rep' 
            string_final += '{:02}|'.format(rep) # denominação da linha
            for c in m: # percorrer o campo com o objetivo de percorrer linha a linha
                if obtem_linha(c) == rep and obtem_numero_minas_vizinhas(m,c)!= 0 and eh_parcela_limpa(obtem_parcela(m,c)) and not eh_parcela_minada(obtem_parcela(m,c)):
                    string_final += str(obtem_numero_minas_vizinhas(m,c))
                    # a primeira condição do 'if' garante que estamos a percorrer linha a linha
                    # para adicionar o numero de minas vizinhas em vez dos pontos de interrogação
                elif obtem_linha(c) == rep:
                    if eh_parcela_limpa(obtem_parcela(m,c)) and not eh_parcela_minada(obtem_parcela(m,c)): #Substituir os pontos de interrogarção por espaços
                        string_final += ' '
                    else: # em qualquer outro caso convertemos as parcelas da linha em string
                        string_final+=parcela_para_str(obtem_parcela(m,c))
            string_final+='|\n' # no final de cada linha adicionamos a barra e passamos para a proxima linha
        string_final+= '  +' + '-'*len(string_colunas) + '+' # adicionamos os ultimos caracteres
        return string_final

def coloca_minas(m,c,g,n):
    '''coloca_minas(m, c, g, n)--> campo 
    Modifica destrutivamente o campo m escondendo n minas
    em parcelas dentro do campo. As n coordenadas são geradas em sequência
    utilizando o gerador g, de modo a que não coincidam com a coordenada c nem
    com nenhuma parcela vizinha desta, nem se sobreponham com minas colocadas
    anteriormente.'''
    ult_cord = cria_coordenada(obtem_ultima_coluna(m),obtem_ultima_linha(m))
    while n != 0:
        cord = obtem_coordenada_aleatoria(ult_cord,g) #gerar coordenada aleatoria
        if not eh_parcela_minada(obtem_parcela(m,cord)) and cord not in obtem_coordenadas_vizinhas(c) and not coordenadas_iguais(c,cord) and eh_coordenada_do_campo(m,cord):
            #parcela nao pode corresponder a c nem vizinha de c nem em sitios já colocados com minas
            #verificar as condições para por a mina
            esconde_mina(obtem_parcela(m,cord))
            n-=1
    return m 


def limpa_campo(m,c):
    '''limpa_campo(m, c) --> campo 
    Modifica destrutivamente o campo limpando a parcela na coordenada
    c e devolvendo-o. Se não houver nenhuma mina vizinha escondida, limpa
    iterativamente todas as parcelas vizinhas tapadas.'''
    def aux(m,c,fila): #tentativa de recursão em cauda já que a forma iterativa não respeitava as barreiras
        if len(fila)== 0:
            return limpa_campo(m,c) #caso terminal, já que o c nao fica vazio e a fila sim, tentamos usar a recusão de novo
        else:
            if eh_coordenada_do_campo(m,c) and eh_parcela_tapada(obtem_parcela(m,c)):
                if obtem_numero_minas_vizinhas(m,c) == 0: #adicionamos à fila todas as parcelas que são para limpar
                    limpa_parcela(obtem_parcela(m,c))
                    l = ()
                    for cord in obtem_coordenadas_vizinhas(c): #observar a vizinhança de todas as coordenadas que têm zero minas vizinhas
                        if cord not in fila:
                            l+=(cord,) 
                    return aux(m,fila[0],fila + l) #adicionar e repetir o processo
                else:
                    limpa_parcela(obtem_parcela(m,c))
                    return aux(m,fila[0],fila[1:])
            else:
                return aux(m,fila[0],fila[1:]) #ignorar coordenadas fora do dominio do campo

    if not eh_parcela_limpa(obtem_parcela(m,c)) and eh_coordenada_do_campo(m,c):
        if obtem_numero_minas_vizinhas(m,c)==0 and not eh_parcela_minada(obtem_parcela(m,c)): #limpeza da vizinhança
            limpa_parcela(obtem_parcela(m,c))
            viz = obtem_coordenadas_vizinhas(c)
            return aux(m,viz[0],viz)
        else:
            limpa_parcela(obtem_parcela(m,c))
            return m
    else:
        return m


# Funções Adicionais - funções para o jogo funcionar

def jogo_ganho(m):
    '''jogo_ganho(m) --> bool
    É uma função auxiliar que recebe um campo do jogo das minas e devolve
    True se todas as parcelas sem minas se encontram limpas, ou False caso contrário.'''
    tapadas_marcadas = obtem_coordenadas(m,'tapadas')+obtem_coordenadas(m,'marcadas')
    for cord in tapadas_marcadas:
         if not eh_parcela_minada(obtem_parcela(m,cord)) and not eh_parcela_limpa(obtem_parcela(m,cord)):
            return False
    return True

def aux_jogo(m,cord): # função auxiliar de interação com o utilizador
    while True:
        try:
            if coordenada_para_str(str_para_coordenada(cord))==cord and eh_coordenada_do_campo(m,str_para_coordenada(cord)):
                cord = str_para_coordenada(cord)
                break
            else:
                cord = input('Escolha uma coordenada:')
        except:
            cord = input('Escolha uma coordenada:')
    return cord

def turno_jogador(m):
    '''turno_jogador(m) --> bool
    É uma função auxiliar que recebe um campo de minas e oferece ao jogador
    a opção de escolher uma ação e uma coordenada. A função modifica destrutivamente
    o campo de acordo com ação escolhida, devolvendo False caso o jogador tenha limpo
    uma parcela que continha uma mina, ou True caso contrário.
    Possibilita as ações de Marcação ou Limpeza de parcelas, mediante a coordenada escolhida'''
    limpa = True #varivel para identificar a limpeza de uma parcela com mina
    valor = input('Escolha uma ação, [L]impar ou [M]arcar:')
    while valor not in('L','M'):
        valor = input('Escolha uma ação, [L]impar ou [M]arcar:')
    cord = input('Escolha uma coordenada:')
    cord = aux_jogo(m,cord)
    if valor == 'L':
        if eh_parcela_minada(obtem_parcela(m,cord)):
            limpa_campo(m,cord)
            limpa = False
        limpa_campo(m,cord)
    elif valor == 'M':
        alterna_bandeira(obtem_parcela(m,cord))
    return limpa
            
def eh_valido(c,l,n,d,s): #Verificação da validade dos argumentos para o jogo
    #estava a dar erro no moonshark decidi fazer por extenso
    return isinstance(c,str) and isinstance(l,int) and isinstance(n,int) and isinstance(d,int)\
        and isinstance(s,int) and len(c)==1 and 0<n<(ord(c)-64)*l and (ord(c)-64)*l>=12 \
            and 'A'<= c <= 'Z' and 1<= l <= 99 and \
                ( d ==32 or d == 64 ) and 0<s<=2**d

def minas(c,l,n,d,s):
    '''minas(c, l, n, d, s) --> bool
    É a função principal que permite jogar ao jogo das minas. A função
    recebe uma cadeia de carateres e 4 valores inteiros correspondentes, respetivamente, a:
    última coluna c; última linha l; número de parcelas com minas n; dimensão do gerador
    de números d; e estado inicial ou seed s para a geração de números aleatórios.A função
    devolve True se o jogador conseguir ganhar o jogo, ou False caso contrário.'''
    if eh_valido(c,l,n,d,s): #verificação
        campo = cria_campo(c,l) 
        gerador = cria_gerador(d,s)
        print('   [Bandeiras {}/{}]'.format(len(obtem_coordenadas(campo,'marcadas')),n)) #print das bandeiras
        print(campo_para_str(campo)) # print campo
        cord = input('Escolha uma coordenada:')
        cord = aux_jogo(campo,cord) #recurso à função auxiliar para, se for necessário, repetir o input e transforma-lo num input válido
        campo = coloca_minas(campo,cord,gerador,n)
        limpa_campo(campo,cord) #primeria jogada (limpeza)
        while not jogo_ganho(campo): #operações basicas do jogo
            print('   [Bandeiras {}/{}]'.format(len(obtem_coordenadas(campo,'marcadas')),n))
            print(campo_para_str(campo))
            turno = turno_jogador(campo)
            if not turno: #visto que o turno da return de False se tiver limpo uma com mina, perde o jogo
                print('   [Bandeiras {}/{}]'.format(len(obtem_coordenadas(campo,'marcadas')),n))
                print(campo_para_str(campo))
                print('BOOOOOOOM!!!')
                return False
        #em caso de ganhar o jogo
        print('   [Bandeiras {}/{}]'.format(len(obtem_coordenadas(campo,'marcadas')),n))
        print(campo_para_str(campo))
        print('VITORIA!!!')
        return True
    else:
        raise ValueError('minas: argumentos invalidos')