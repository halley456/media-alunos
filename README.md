# media-alunos
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
print(f'\n✅ A maior média foi do aluno {aluno_maior_media} com {maior_media:.2f}')
print(f'📊 A média da sala é {media_geral:.2f}')
# 🧮 Média dos Alunos

Este é um projeto simples em Python que recebe notas de vários alunos, calcula a média individual de cada um, identifica a maior média e também calcula a média geral da turma.

## ✨ Funcionalidades

- Entrada de notas para cada aluno
- Cálculo da média individual
- Exibição da maior média da turma
- Cálculo da média geral da sala
- Uso de função personalizada para organizar o código

## 🧠 Conceitos aplicados

- Entrada de dados com `input()`
- Conversão de tipos (`float`, `int`)
- Estrutura de repetição com `for`
- Condicional `if`
- Funções com parâmetros e retorno

## 🚀 Como executar

1. Instale o Python (versão 3.x) no seu computador
2. Baixe ou clone o repositório:
   ```bash
   git clone https://github.com/halleyvictor/media-alunos
Execute o programa:

bash
Copiar
Editar
python media_alunos.py
💡 Exemplo de uso
css
Copiar
Editar
Quantos alunos deseja cadastrar? 3
Qual é a primeira nota do aluno 1? 7
Qual é a segunda nota do aluno 1? 8
A média do aluno 1 é 7.50
...
✅ A maior média foi do aluno 2 com 9.00
📊 A média da sala é 8.33
🔧 Melhorias futuras
Armazenar os nomes dos alunos

Mostrar o boletim completo da turma

Tratar erros de entrada inválida

Usar listas compostas para organizar melhor os dados
