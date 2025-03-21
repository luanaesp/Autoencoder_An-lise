# 📊 Análise de Competitividade e Sustentabilidade Regional com Autoencoders

Este repositório apresenta uma análise detalhada utilizando **autoencoders não lineares** para identificar padrões latentes nos dados de infraestrutura e sustentabilidade regional no Brasil (2008–2015).

## 🎯 Objetivos

- Avaliar a relação espacial e temporal entre infraestrutura para eventos e sustentabilidade ambiental dos estados brasileiros.
- Aplicar e validar o uso de autoencoders na redução de dimensionalidade e análise exploratória de dados socioeconômicos.

## 📂 Estrutura do Projeto

Autoencoder_An-lise/ ├── Dados_Gerais_competitividade_.csv # Dados originais da análise ├── Representacao_Latente.csv # Representações latentes geradas pelo autoencoder ├── codigo_autoencoder.py # Implementação completa do autoencoder ├── analise_comparativa.py # Análise e visualização dos resultados ├── requirements.txt # Dependências Python do projeto └── venv/ # Ambiente virtual Python (opcional)

yaml
Copiar
Editar


## ⚙️ Como Reproduzir o Projeto

### 1. Clone este repositório:

bash
git clone https://github.com/luanaesp/Autoencoder_An-lise.git
cd Autoencoder_An-lise

2. Configuração do Ambiente Virtual (opcional, mas recomendado):
Windows:
bash
Copiar
Editar
python -m venv venv
.\venv\Scripts\activate

Linux ou MacOS:
bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate

3. Instalação das dependências:
bash
Copiar
Editar
pip install -r requirements.txt

4. Execução do autoencoder para obter as representações latentes:
bash
Copiar
Editar
python codigo_autoencoder.py

5. Execução da análise comparativa e visualização dos gráficos:
bash
Copiar
Editar
python analise_comparativa.py

📌 Detalhes Técnicos da Implementação
Pré-processamento dos Dados
Substituição de vírgulas por pontos nos dados numéricos.
Imputação dos dados faltantes usando o método k-NN (k=3).
Normalização com o método MinMaxScaler.
Arquitetura do Autoencoder
Camada de entrada: número de neurônios igual às variáveis originais.
Encoder: [256 → 64 → 2 neurônios] (representação latente).
Decoder: [64 → 256 → dimensão original].
Função de ativação: ReLU nas camadas intermediárias e linear na camada de saída.
Otimizador: Adam (learning rate = 0.001).
Função de perda: Mean Squared Error (MSE).
Treinamento: 500 épocas, batch size = 32, seed = 42 para reprodutibilidade.

📊 Resultados Gerados
Representação latente disponível no arquivo Representacao_Latente.csv.
Gráficos comparativos demonstrando relações entre infraestrutura e sustentabilidade (gerados pelo script analise_comparativa.py).

📋 Dependências (requirements.txt)
ini
Copiar
Editar
pandas==2.2.3
numpy==2.0.2
scikit-learn==1.5.2
tensorflow==2.18.0
matplotlib==3.9.0

📝 Licença
Este projeto está licenciado sob os termos da licença MIT.

📩 Contato
Para dúvidas, sugestões ou melhorias:

GitHub: luanaesp
