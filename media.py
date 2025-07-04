quantidade = int(input('Quantos alunos deseja cadastrar? '))

maior_media = 0
aluno_maior_media = 0
soma_das_medias = 0

def media2(nome, nota1, nota2):
    return (nota1 + nota2) / 2

for i in range(quantidade):
    numero_aluno = i + 1
    n1 = float(input(f'Qual é a primeira nota do aluno {numero_aluno}? '))
    n2 = float(input(f'Qual é a segunda nota do aluno {numero_aluno}? '))

    media = media2(numero_aluno, n1, n2)
    print(f'A média do aluno {numero_aluno} é {media:.2f}')

    soma_das_medias += media

    if media > maior_media:
        maior_media = media
        aluno_maior_media = numero_aluno

media_geral = soma_das_medias / quantidade
print(f' maior média foi do aluno {aluno_maior_media} com {maior_media:.2f}')
print(f' A média da sala é {media_geral:.2f}')