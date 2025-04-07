# Veiculo Excel Generator

# Projeto: Gerador de Excel para Dados de Veículos

Este projeto tem como objetivo automatizar o processo de extração e organização de dados de veículos em um arquivo Excel. O código foi desenvolvido para atender à demanda do setor comercial, principalmente no contexto de processos licitatórios realizados pela empresa onde atuo.

## Objetivo

A ferramenta converte dados extraídos de documentos (PDFs) relacionados a veículos para um formato estruturado em Excel. Esse processo visa facilitar a análise e o controle dos dados.

## Funcionalidades

- Extrai dados de veículos a partir de um dicionário predefinido.
- Organiza as informações em um formato tabular, com cabeçalhos customizados.
- Gera um arquivo Excel com os dados de veículos prontos para análise.

## Estrutura de Dados

O código utiliza um dicionário de dicionários, onde cada chave é o nome de um arquivo e os valores são os dados específicos de cada veículo, como:

- **RENAVAM**
- **PLACA**
- **ANO DE FABRICAÇÃO**
- **MARCA/MODELO**
- **LOCAL**
- **ENTRE OUTROS**

## Como Usar

1. Clone este repositório em sua máquina:
   ```bash
   git clone https://github.com/seu-usuario/veiculo-excel-generator.git
