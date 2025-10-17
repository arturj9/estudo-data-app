import streamlit as st
import pandas as pd

st.write("Estudo - Data App")

st.write("O Streamlit serve para criar aplicações web interativas em Python de forma simples, no contexto de análise de dados, conseguimos criar data apps para visualização de dados, dashboards, relatórios interativos, entre outros.")

df = pd.read_csv("notas_alunos.csv")

st.dataframe(df)

st.write("Nota 1")
st.bar_chart(df[["Nota_1"]].set_index(df["Aluno"]))

st.write("Nota 2")
st.bar_chart(df[["Nota_2"]].set_index(df["Aluno"]))