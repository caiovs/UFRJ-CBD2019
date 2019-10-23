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

class Escrita(object):
    """docstring for Escrita."""

    def __init__(self, dados):
        with open('Banco.bin', 'r+b') as file:
            byte = file.read(1)
            while byte != b'':
                print(byte)
                file.write(b'\xFF')
                byte = file.read(1)

            #file.seek(2, 0)
            #file.write(b'\xFF')



class Leitura():
    """Lê um arquivo CSV, cria um banco de dados e faz insert."""

    campos = []
    linhas = []

    def __init__(self):
        arquivoCSV = "gh_simple.csv"

        linhaatual = 0
        with open(arquivoCSV, 'r') as csvfile:
            linhasCSV = csv.reader(arquivoCSV)
            #extrai a primeira linha que contém os nomes dos campos
            campos = linhasCSV.next()
            linhaatual += 1
            #linhas restantes são armazenadas no vetor 'linhas'
            for linha in linhasCSV:
                linhas.append(linha)
                linhaatual += 1

        print(f'Linhas processadas: {linhaatual}')

if __name__ == '__main__':
    l = Leitura()
    Escrita()
