# Análise de Dados - Sistema Educampo (Café)

Repositório contendo os códigos utilizados para análise dos dados do café do sistema Educampo.

## Requisitos

- Python 3.+;
- Pip 22.+;

## Dependências

Para instalar todas as dependências necessárias, basta digitar o seguinte comando:

```bash
pip install -r requirements.txt
```

## Execução - Gerador de Markdown

Para executar o gerador de markdown com os gráficos e análises das colunas importantes do dataset, digite o seguinte comando:

```bash
python src/generate_markdown.py <arquivo_dataset> <arquivo_markdown> <opt>
```

Em que:
- `<arquivo_dataset>` é o caminho do arquivo `.xlsx` contendo os dados;
- `<arquivo_markdown`> é o caminho do arquivo de saída sem a extensão `.md`;
- `<opt>` tem valor 1 para utilizar os gráficos gerados no arquivo markdown ou pode ser omitido para gerar o arquivo markdown com as imagens embutidas, para exportação para `.pdf`, por exemplo.

Exemplo de execução, partindo da raiz do repositório:

```bash
python src/generate_markdown.py src/datasets/data.xlsx src/markdown/analise_cafe 1
```

## Detalhes da implementação

Caso seja necessário alterar as colunas de análise, basta alterar a lista estática do código. Lista padrão:

```python
columns = [
    "6. Área em produção (hectare)",
    "16. Idade média das lavouras  (anos)",
    "17. Número de plantas/área plantada (plantas/hectare)",
    "18. Produtividade  (sacas/hectare)",
    "41. Margem líquida (R$/período)",
    "42. Lucro (R$/período)",
    "59. Preço médio de venda (R$/saca)",
    "70. Margem Líquida/saca (R$/saca)",
    "71. Lucro/saca (R$/saca)"
]
```

Toda a análise é agrupada por região, caso seja necessário alterar a coluna de agrupamento, basta alterar a variável que agrupa os dados. Variável:

```python
group_column = "Região"
```

## Referências

1. [Documentação do Pandas](https://pandas.pydata.org/docs/);
2. [Documentação do Matplotlib](https://matplotlib.org/stable/index.html);
3. [Documentação do Mdutils](https://mdutils.readthedocs.io/en/latest/index.html);
4. [Stack Overflow](https://stackoverflow.com/).
