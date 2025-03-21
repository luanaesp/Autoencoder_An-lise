import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados da Representação Latente
latent_file_path = r'C:\Users\luesp\Downloads\Analise_autoencoder\Autoencoder_An-lise\Representacao_Latente.csv'
latent_data = pd.read_csv(latent_file_path)

# Garantir que os dados estão carregados corretamente
print(latent_data.head())

# Análise espacial: média das dimensões latentes por UF
spatial_analysis = latent_data.groupby('UF')[['Latente_1', 'Latente_2']].mean().reset_index()

# Selecionar os estados líderes em Latente_1 (infraestrutura) e Latente_2 (sustentabilidade)
top_infra = spatial_analysis.nlargest(5, 'Latente_1')
top_sust = spatial_analysis.nlargest(5, 'Latente_2')

# Comparar os estados líderes
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = range(len(top_infra['UF']))

# Comparação lado a lado
plt.bar(index, top_infra['Latente_1'], bar_width, label='Infraestrutura (Latente_1)', color='blue')
plt.bar([i + bar_width for i in index], top_infra['Latente_2'], bar_width, label='Sustentabilidade (Latente_2)', color='green')

plt.xlabel('Estados')
plt.ylabel('Média')
plt.title('Comparação de Estados Líderes em Infraestrutura e Sustentabilidade')
plt.xticks([i + bar_width / 2 for i in index], top_infra['UF'])
plt.legend()
plt.tight_layout()
plt.show()

# Gráfico de dispersão para visualizar relação Latente_1 e Latente_2
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='Latente_1', y='Latente_2', data=spatial_analysis, hue='UF', style='UF', palette='tab10', s=100
)
plt.title('Comparação dos Estados em Infraestrutura e Sustentabilidade')
plt.xlabel('Latente 1 (Infraestrutura)')
plt.ylabel('Latente 2 (Sustentabilidade)')
plt.legend(title='UF', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
