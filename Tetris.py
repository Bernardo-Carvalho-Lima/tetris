import pandas as pd

# =====================================================================
# ETAPA 3 - LEITURA E EXPLORAÇÃO DOS DADOS
# =====================================================================
print("--- ETAPA 3: LEITURA E EXPLORAÇÃO DOS DADOS ---")

# Criando uma base de dados simples em formato de dicionário para o código rodar direto
# Isso evita o erro de "arquivo não encontrado" se o CSV não estiver na mesma pasta
dados = {
    'Rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Tetris', 'Super Mario World', 'GTA V', 'Minecraft', 'Pokemon Red', 'Skyrim', 'Wii Sports', 'Pac-Man', 'Diablo III', 'The Witcher 3'],
    'Platform': ['GB', 'SNES', 'PS4', 'PC', 'GB', 'PC', 'Wii', 'Arcade', 'PC', 'PS4'],
    'Year': [1989, 1990, 2013, 2011, 1996, 2011, 2006, 1980, 2012, 2015],
    'Genre': ['Puzzle', 'Platform', 'Action', 'Sandbox', 'RPG', 'RPG', 'Sports', 'Puzzle', 'RPG', 'RPG'],
    'Publisher': ['Nintendo', 'Nintendo', 'Rockstar', 'Mojang', 'Nintendo', 'Bethesda', 'Nintendo', 'Namco', 'Blizzard', 'CD Projekt'],
    'Global_Sales': [35.84, 20.61, 20.0, 33.0, 31.37, 20.0, 82.90, 10.0, 12.0, 29.0]
}

# Transformando o dicionário em DataFrame (tabela do Pandas)
df = pd.DataFrame(dados)

# Mostrando as primeiras linhas da tabela
print("\nPrimeiras linhas da base (head):")
print(df.head())

# Mostrando o tamanho da tabela (linhas, colunas)
print("\nTamanho da base de dados:")
print(df.shape)

# Mostrando o nome das colunas
print("\nColunas da base:")
print(df.columns)

# Informações gerais dos tipos de dados
print("\nInformações sobre os dados:")
df.info()

# Resumo estatístico dos números (média, mínimo, máximo, etc)
print("\nResumo estatístico:")
print(df.describe())

# Verificando se existem valores nulos (vazios)
print("\nQuantidade de valores nulos:")
print(df.isnull().sum())

# Verificando se existem linhas duplicadas
print("\nQuantidade de registros duplicados:")
print(df.duplicated().sum())


# =====================================================================
# ETAPA 4 - LIMPEZA E TRATAMENTO
# =====================================================================
print("\n--- ETAPA 4: LIMPEZA E TRATAMENTO ---")

# Fazendo uma cópia da tabela original para limpar
df_limpo = df.copy()

# Exemplo de limpeza: removendo valores nulos (caso existissem)
df_limpo = df_limpo.dropna()

# Salvando o resultado tratado em um novo arquivo CSV
df_limpo.to_csv("jogos_tratado.csv", index=False)
print("Arquivo 'jogos_tratado.csv' foi gerado e salvo com sucesso!")


# =====================================================================
# ETAPA 5 - ANÁLISE DOS DADOS (PERGUNTAS DE PARTIDA)
# =====================================================================
print("\n--- ETAPA 5: ANÁLISE DOS DADOS E RESPOSTAS ---")

print("\n1. Gêneros mais frequentes na base:")
print(df_limpo['Genre'].value_counts())

print("\n2. Total de vendas por Gênero (em milhões):")
print(df_limpo.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False))

print("\n3. Plataformas com mais jogos registrados:")
print(df_limpo['Platform'].value_counts())

print("\n4. Plataformas que mais acumulam vendas:")
print(df_limpo.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False))

print("\n5. Anos com mais lançamentos:")
print(df_limpo['Year'].value_counts().head())
