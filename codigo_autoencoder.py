import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

# Carregar os dados
file_path = r"C:\Users\luesp\Downloads\Analise_autoencoder\Autoencoder_An-lise\Dados_Gerais_competitividade_.csv"  # Atualize com o caminho do arquivo

# Ler os dados
try:
    data = pd.read_csv(file_path, encoding='latin1')
except FileNotFoundError:
    raise Exception(f"O arquivo {file_path} não foi encontrado. Certifique-se de que o caminho está correto.")

# Substituir vírgulas por pontos para corrigir valores numéricos
data.replace(',', '.', regex=True, inplace=True)

# Selecionar colunas relevantes
selected_columns = [
    'SERVICOS_E_EQUIPAMENTOS_TURISTICOS',
    'INFRAESTRUTURA_GERAL',
    'ASPECTOS_AMBIENTAIS'
]

# Garantir que as colunas estão no formato numérico
data[selected_columns] = data[selected_columns].astype(float)

# Renomear colunas para facilitar o uso
data_selected = data[selected_columns].copy()
data_selected.columns = ['Servicos_Equip_Turisticos', 'Infraestrutura_Geral', 'Aspectos_Ambientais']

# Remover linhas com valores nulos
data_selected = data_selected.dropna()

# Normalizar os dados
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data_selected)

# Definir o Autoencoder
input_dim = data_scaled.shape[1]  # Número de variáveis
latent_dim = 2  # Dimensão da camada latente

# Camadas do Autoencoder
input_layer = Input(shape=(input_dim,))
encoder = Dense(128, activation='relu')(input_layer)
encoder = Dense(64, activation='relu')(encoder)
bottleneck = Dense(latent_dim, activation='relu', name='bottleneck')(encoder)
decoder = Dense(64, activation='relu')(bottleneck)
decoder = Dense(128, activation='relu')(decoder)
output_layer = Dense(input_dim, activation='sigmoid')(decoder)

# Modelo
autoencoder = Model(inputs=input_layer, outputs=output_layer)
autoencoder.compile(optimizer='adam', loss='mse')

# Treinar o Autoencoder
autoencoder.fit(data_scaled, data_scaled, epochs=50, batch_size=16, validation_split=0.2, verbose=1)

# Extração da Representação Latente
encoder_model = Model(inputs=input_layer, outputs=bottleneck)
latent_representation = encoder_model.predict(data_scaled)

# Converter a representação latente em DataFrame
latent_df = pd.DataFrame(latent_representation, columns=['Latente_1', 'Latente_2'])

# Adicionar anos e UF para análises temporal e espacial
latent_df['Ano'] = data['ANO'].iloc[data_selected.index].values
latent_df['UF'] = data['UF'].iloc[data_selected.index].values

# Salvar os resultados
output_file = 'Representacao_Latente.csv'
latent_df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"Análise completada! Os resultados foram salvos em {output_file}.")
