from os import system as sys
sys("cls")

# Funções de transformação em List

def Cadeia_txt(cad:list)->str:

    def Num_to_Alpha(Vall: int) -> str:  
        Alphabeto = {
            1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F',
            7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L',
            13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R',
            19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X',
            25: 'Y', 26: 'Z', 0: ' ', 27: '#'
        }
        return Alphabeto[Vall%28]

    ret=""
    for i in range(len(cad)):
        ret+=Num_to_Alpha(cad[i])
    return ret

def Cadeia_num(cad:str)->list:

    def Alpha_to_Num(Letter:str)-> int:
        Dicio = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
        'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
        'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
        'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
        'Y': 25, 'Z': 26, ' ': 0, '#': 27
        }
        return Dicio.get(str(Letter.upper()),27)

    ret=[]
    for i in range(len(cad)):
        ret.append(Alpha_to_Num(cad[i]))
    return ret

# Funções de criptografia e descriptografia.:

def Cypher(Main_Matriz:list,Cadeia:str) -> str:
    from numpy import array as arr, dot
    
    work=(Cadeia_num(Cadeia))
    if len(Cadeia)%2!=0:
        work.append(0)

    A=[]
    B=[]    
    for i in range(len(work)):
        if i%2==0:
            A.append(work[i])
        else:
            B.append(work[i])
    work=[]
    work.append(A)
    work.append(B)

    work=arr(work,list)
    Main_Matriz=arr(Main_Matriz,int).reshape(2,2)
    mult=dot(Main_Matriz,work)

    A=mult[0]
    B=mult[1] 

    past=[]
    for i in range(len(A)):
        past.append(A[i])
        past.append(B[i])

    return Cadeia_txt(past)


#def decypher(Main_Matriz:list,Cadeia:str)->str:

def decypher(Main_Matriz: list, Cadeia: str) -> str:
    import numpy as np

    def mod_inv(a, m):
        """Retorna o inverso modular de 'a' módulo 'm', se existir"""
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        raise ValueError(f"Inverso modular não encontrado para {a} mod {m}")

    # Transformar a string criptografada em números
    work = Cadeia_num(Cadeia)
    if len(work) % 2 != 0:
        work.append(0)  # Preenchimento, se necessário

    # Separar em dois vetores: A (pares) e B (ímpares)
    A, B = [], []
    for i in range(len(work)):
        if i % 2 == 0:
            A.append(work[i])
        else:
            B.append(work[i])

    work = np.array([A, B], dtype=int)

    # Transformar a matriz principal em 2x2
    M = np.array(Main_Matriz, dtype=int).reshape(2, 2)

    # Calcular o determinante e o inverso modular mod 28
    det = int(np.round(np.linalg.det(M)))
    det_mod_inv = mod_inv(det % 28, 28)

    # Calcular a matriz adjunta (com cofatores trocados e sinal invertido)
    adj = np.array([[ M[1,1], -M[0,1]],
                    [-M[1,0],  M[0,0]]], dtype=int)

    # Corrigir valores negativos no adjunto e aplicar o inverso modular
    invM = (det_mod_inv * adj) % 28

    # Multiplicar a matriz inversa pelo vetor criptografado
    mult = np.dot(invM, work) % 28

    # Reconstituir a lista intercalada
    A = mult[0]
    B = mult[1]
    past = []
    for i in range(len(A)):
        past.append(A[i])
        past.append(B[i])

    # Converter de volta para texto
    return Cadeia_txt(past)

while True:
    s=input(':')
    m=[5,87,6,98]
    s=Cypher(m,s) 
    print(s)
    s=decypher(m,s) 
    print(s)