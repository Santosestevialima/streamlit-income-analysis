import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Análise de Renda", layout="wide")


@st.cache_data
def load_data():
    return pd.read_csv("dataset/previsao_de_renda.csv")

df = load_data()

st.title("Análise Exploratória de Renda")
st.write("Visualização e comparação de perfis com base nos dados disponíveis.")


st.sidebar.header("Filtros")

educacao = st.sidebar.multiselect(
    "Escolaridade",
    df["educacao"].unique(),
    default=df["educacao"].unique()
)

imovel = st.sidebar.multiselect(
    "Possui imóvel?",
    df["posse_de_imovel"].unique(),
    default=df["posse_de_imovel"].unique()
)

veiculo = st.sidebar.multiselect(
    "Possui veículo?",
    df["posse_de_veiculo"].unique(),
    default=df["posse_de_veiculo"].unique()
)

df_filt = df[
    (df["educacao"].isin(educacao)) &
    (df["posse_de_imovel"].isin(imovel)) &
    (df["posse_de_veiculo"].isin(veiculo))
]


col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribuição da Renda")
    fig, ax = plt.subplots()
    sns.histplot(df_filt["renda"], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Renda Média por Escolaridade")
    fig, ax = plt.subplots()
    sns.barplot(
        data=df_filt,
        x="educacao",
        y="renda",
        estimator="mean",
        ax=ax
    )
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

st.subheader("Renda vs Tempo de Emprego")
fig, ax = plt.subplots()
sns.scatterplot(
    data=df_filt,
    x="tempo_emprego",
    y="renda",
    hue="educacao",
    ax=ax
)
st.pyplot(fig)

st.subheader("Boxplot da Renda por Escolaridade")
fig, ax = plt.subplots()
sns.boxplot(
    data=df_filt,
    x="educacao",
    y="renda",
    ax=ax
)
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)