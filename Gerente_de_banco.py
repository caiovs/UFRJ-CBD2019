# -*- coding: utf-8 -*-
"""

********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************
    2° Trabalho - Contrução de banco de dados
        - Lucas Máximo Dantas
        - Caio Vieira de Souza Alves

********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************
    INSERT:
        -Inserção de um único registro.
        -Inserção de um conjunto de registros.

    SELECT:
        -Seleção de um único registro pela chave primária (ou campo cujo valor é único, por exemplo, DRE de um ALUNO).
        -Seleção de registros por chave primária (ou campo cujo valor é único) contida em um conjunto de valores não sequenciais (por exemplo, uma lista dos DRE dos alunos de uma turma).
        -Seleção de registros por campo chave contida em faixa de valores.
        -Seleção de registros por campo não chave (ou campo que possui valores não únicos entre registros, tipo CIDADE em uma tabela de PESSOAS)

    DELETE:
        -Remoção de um único registro selecionado através da chave primária (ou campo cujo valor é único), por exemplo, remover o ALUNO da tabela de ATIVOS cujo DRE é dado.
        -Remoção de um conjunto de registros selecionados por algum critério, por exemplo, remover todos os ALUNOS da tabela INSCRITOS cuja turma seja a de NUMERO=1023.

********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************
    Cada um desses métodos deverá ser desenvolvido para
    as seguintes organizações primárias do arquivo de registros:

    -Heap, ou arquivo sequencial sem qualquer ordenação, com registros de tamanho fixos e lista encadeada dos registros removidos (que poderão ser reaproveitados em uma nova inserção posterior a remoção).
	-Heap, ou sequencial sem qualquer ordenação, com registros de tamanho variável, tipo campos strings e/ou repetidos, podendo ser organizados por caracteres de marcação ou por File Head contendo (posição, tamanho) de cada campo; como marcação dos registros removidos e compressão do arquivo após certo critério ser atingido.
	-Arquivo ordenado por um campo de ordenação, com registros de tamanho fixo, inserção em arquivo de Extensão com posterior reordenação, após certo critério ser atingido, entre o arquivo Principal e a sua Extensão. Remoção através de marcação de registro deletado com posterior reordenação (que pode se dar em conjunto com a junção com a Extensão).
    -Hash externo estático, distribuídos segundo um campo de hashing chave (ou campo cujo valor é único), usando tamanho do bucket múltiplo do tamanho dos blocos de memória, tratamento de colisão por lista em conjunto de overflow buckets. Pode ser utilizada uma função de hashing básica, do tipo “função módulo”, usando o número de buckets alocados, ou utilizar outra que melhor se adequa ao(s) domínio(s) do campo(s) de hashing usado (por exemplo, pela primeira letra de um campo string que distribui entre 27 buckets sequenciais por ordem alfabética do resultado do hashing). Se for usar uma função de hashing que mantém a ordenação, como no exemplo anterior, isso deverá ser assinalado no trabalho.

    Linhas de dados totais: 4.758.124
"""

import csv
import pickle
from pilha import Pilha, Node
from registro_gh import Registro_GH
from registro_docentes import registro_docentes
import sys
import resource


class Gravar():
    """Lê um arquivo CSV, cria um banco de dados e faz insert."""

    campos = []
    linhas = []

    def __init__(self):
        print (resource.getrlimit(resource.RLIMIT_STACK))
        print (sys.getrecursionlimit())
        input()
        max_rec = 0x100000

        # May segfault without this line. 0x100 is a guess at the size of each stack frame.
        resource.setrlimit(resource.RLIMIT_STACK, [0x100 * max_rec, resource.RLIM_INFINITY])
        sys.setrecursionlimit(max_rec)

        self.pilha = Pilha()
        linhaatual = 0
        with open("gh.csv", 'r') as csvfile:
            linhaatual += 1
            for linha in csvfile:
                print("***** Linha atual : ",linhaatual)
                self.guardar_na_pilha(linha)
                linhaatual += 1
                print("Linha : ",linha)
            self.salvar()

        print(f'Linhas processadas: {linhaatual}')

    def guardar_na_pilha(self, dado):
        print("Entrou no Escrita ")
        rg = Registro_GH(dado)
        self.pilha.push(rg)

    def salvar(self):
        #Não posso adicionar tudo de uma vez
        with open('Banco.bin', 'wb') as file:
            pickle.dump(self.pilha, file)
            print("Dado gravado!!")

class Leitura(object):
    """docstring for Leitura."""

    def __init__(self):
        le = 0
        cont = 0
        with open("Banco.bin", "rb") as file:
            c = pickle.load(file)
            print(c)

if __name__ == '__main__':
    g = Gravar()
    #l = Leitura()
