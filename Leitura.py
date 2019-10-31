"""
********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************
    2° Trabalho - Contrução de banco de dados
        - Lucas Máximo Dantas
        - Caio Vieira de Souza Alves
        - ???

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



    DOCENTES_SUDESTE:
        Linhas: 4.758.124
    gh
        Linhas: 4.817.701
"""
import csv
import pickle
from pilha import Pilha, Node

class Ler(object):
    """docstring for Leitura."""

    def __init__(self):
        file = open('important', 'rb')

        # dump information to that file
        data = pickle.load(file)

        # close the file
        file.close()

        print('Showing the pickled data:')

        cnt = 0
        for i in range(data.size):
            print('The data ', cnt, ' is : ', data.peek())
            cnt += 1
            data = data.peek()

class Data(object):
    """docstring for Data"""
    def __init__(self, arg):
        self.data = arg    

    def __repr__(self):
        return self.data

    def __str__(self):
        return self.__repr__()    

class Gravar(object):

    def __init__(self):
        #INSERT -Heap
        number_of_data = int(input('Enter the number of data : '))
        data = []
        pilha = Pilha()

        # open a file, where you ant to store the data
        file = open('Banco.bin', 'wb')
        pickle.dump(pilha, file)
        file.close()
        file = open('Banco.bin', 'rb')


        data = pickle.load(file) 
        # take input of the data
        for i in range(number_of_data):
            raw = input('Enter data '+str(i)+' : ')
            i = Data(raw)
            data = pickle.load(file)
            data.push(i)
            pickle.dump(data, file)
        

        

        # close the file
        file.close()

if __name__ == '__main__':
    g = Gravar()
    l = Ler()

