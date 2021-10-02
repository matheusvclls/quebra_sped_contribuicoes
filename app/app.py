import pandas as pd
import glob
import datetime

print(datetime.datetime.now())

data = ''
def FormatarData(variavel, num):
    global data
    data = variavel[num][:2] + '/' + variavel[num][2:4] + '/' + variavel[num][4:]
    return data

listaArquivos = []
listaLinhas = []

path_efd = glob.glob('..\data\input\*.txt')

print(path_efd)

for i in path_efd:
    listaLinhas = []
    dictCabecalho = {}
    dictLinha = {}

    df = open(i,'r', encoding="Latin-1")

    for line in df:
        if '|0000|' in line:
            arq = line.split("|")
            dictCabecalho['TP_ESCRITURACAO'] = arq[2]
            dictCabecalho['NUM_RECIBO'] = arq[5]
            FormatarData(arq, 6)
            dictCabecalho['DT_INI'] = data
            FormatarData(arq, 7)
            dictCabecalho['DT_FIN'] = data
            dictCabecalho['EMPRESA'] = arq[8]
            dictCabecalho['CNPJ'] = arq[9]

        elif '|F100|' in line:
            linha = line.split('|')

            dictLinha['REG'] = linha[1]
            dictLinha['IND_OPER'] = linha[2]
            dictLinha['COD_PART'] = linha[3]
            dictLinha['COD_ITEM'] = linha[4]
            FormatarData(linha, 5)
            dictLinha['DT_OPER'] = data
            dictLinha['VL_OPER'] = linha[6]
            dictLinha['CST_PIS'] = linha[7]
            dictLinha['VL_BC_PIS'] = linha[8]
            dictLinha['ALIQ_PIS'] = linha[9]
            dictLinha['VL_PIS'] = linha[10]
            dictLinha['CST_COFINS'] = linha[11]
            dictLinha['VL_BC_COFINS'] = linha[12]
            dictLinha['ALIQ_COFINS'] = linha[13]
            dictLinha['VL_COFINS'] = linha[14]
            dictLinha['NAT_BC_CRED'] = linha[15]
            dictLinha['IND_ORIG_CRED'] = linha[16]
            dictLinha['COD_CTA'] = linha[17]
            dictLinha['COD_CCUS'] = linha[18]
            dictLinha['DESC_DOC_OPER'] = linha[19]

            listaLinhas.append(dictLinha)
            dictLinha = {}

        elif '|M001|' in line:
            break

    listaArquivos.append({'cabecalho': dictCabecalho, 'linhas': listaLinhas})

df = pd.json_normalize(listaArquivos, errors='ignore',record_path= 'linhas',
meta=[
['cabecalho','TP_ESCRITURACAO'],
['cabecalho','NUM_RECIBO'],
['cabecalho','DT_INI'],
['cabecalho','DT_FIN'],
['cabecalho','EMPRESA'],
['cabecalho','CNPJ']])

df.to_csv(r'..\data\output\result.csv', sep=';', encoding='utf-8', index=False)

print(datetime.datetime.now())