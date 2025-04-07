import pandas as pd

# Definição dos dados
dados = {
     "PLACA.pdf": { #incluir no array abaixo a  placa e dados do veículo, podendo adaptar os títulos
         "RENAVAM": "0012345787", #numero ficticio
         "PLACA": "BTQ40C3", #PLACA FICTICIA
         "EXERCÍCIO": "2024",
         "ANO_FABRICAÇÃO": "1993",
         "ANO_MODELO": "1993",
         "NUMBER_DO_CRV": "***",
         "CODIGO_DE_SEGURANCA_DO_CLA": "056487951", #numero ficticio
         "GATO": "***",
         "MARCA_MODELO_VERSAO": "GM/CHEVROLET 12000 CUSTOM",
         "ESPECIE_TIPO": "CARGA CAMINHAO",
         "PLATE_ANTERIOR_UF": "********/**",
         "CHASSI": "4641987811348453", #numero ficticio
         "COR_PREDOMINANTE": "***",
         "COMBUSTIVEL": "DIESEL",
         "POWER_CYLINDER_CAPACITY": "132CV/5800",
         "MOTOR": "15654313213445132", #numero ficticio
         "CMT": "19.0",
         "CARROCERIA": "CARROCERIA FECHADA",
         "NOME": "EMPRESA X",
         "CPF_CNPJ": "00.000.000/0000-00",
         "LOCAL": "PIRASSUNUNGA SP",
         "DADOS": "02/07/2024",
         "OBSERVACAO_DO_VEICULO": "SEM OBSERVAÇÕES"
     }
 }

# função para gerar o Excel
def gerar_excel_a_partir_de_dados(dados, caminho_excel):
    """
    Gera um arquivo Excel a partir de um dicionário de dicionários.

    Args:
        dados: Um dicionário onde as chaves são os nomes dos arquivos e os valores são dicionários com os dados.
        caminho_excel: O caminho completo para salvar o arquivo Excel.
    """
    try:
        # Mapeamento de colunas para garantir o cabeçalho correto. Cabeçalho conforme um documento CRLV, se for necessário, adaptar para conforme o documento que possui. Esse cabeçalho constará no arquivo excel
        colunas_mapeadas = {
    "RENAVAM": "CÓDIGO RENAVAM",
    "PLACA": "PLACA",
    "EXERCÍCIO": "EXERCÍCIO",
    "ANO_FABRICAÇÃO": "ANO FABRICAÇÃO",
    "ANO_MODELO": "ANO MODELO",
    "NUMBER_DO_CRV": "NÚMERO DO CRV",  
    "CODIGO_DE_SEGURANCA_DO_CLA": "CÓDIGO DE SEGURANÇA DO CLA",
    "MARCA_MODELO_VERSAO": "MARCA/MODELO/VERSÃO",
    "ESPECIE_TIPO": "ESPÉCIE/TIPO",
    "PLATE_ANTERIOR_UF": "PLACA ANTERIOR/UF",  
    "CHASSI": "CHASSI",
    "COR_PREDOMINANTE": "COR PREDOMINANTE",
    "COMBUSTIVEL": "COMBUSTÍVEL",
    "POWER_CYLINDER_CAPACITY": "POTÊNCIA/CILINDRADA",  
    "MOTOR": "MOTOR",
    "CMT": "CMT",
    "CARROCERIA": "CARROCERIA",
    "NOME": "NOME",
    "CPF_CNPJ": "CPF/CNPJ",
    "LOCAL": "LOCAL",
    "DADOS": "DATA",  
    "OBSERVACAO_DO_VEICULO": "OBSERVAÇÃO DO VEÍCULO"
}


        # Transformando o dicionário aninhado em uma lista de dicionários
        lista_dados_formatada = list(dados.values())

        # Criar DataFrame e renomear colunas
        df = pd.DataFrame(lista_dados_formatada)
        df.rename(columns=colunas_mapeadas, inplace=True)

        # Garantir a ordem das colunas, com "PLACA" primeiro
        colunas_ordenadas = ["PLACA"] + [col for col in colunas_mapeadas.values() if col != "PLACA"]
        df = df[colunas_ordenadas]

        # Gerar o arquivo Excel
        df.to_excel(caminho_excel, index=False)
        print(f"Arquivo Excel gerado com sucesso em: {caminho_excel}")

    except PermissionError:
        print(f"Erro: Não foi possível salvar o arquivo Excel. Verifique se ele está fechado.")
    except Exception as e:
        print(f"Ocorreu um erro ao gerar o Excel: {e}")

# Defina o caminho onde o arquivo Excel será salvo
caminho_excel_saida = r"C:INCLUIR\CAMINHO\DESTINATÁRIO\DO\ARQUIVO\RESULTADOxlsx"

# Chamar a função para gerar o Excel
gerar_excel_a_partir_de_dados(dados, caminho_excel_saida)
