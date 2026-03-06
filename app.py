import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gestor Solar", page_icon="☀️")

st.title("☀️ Calculadora Solar Enel")
st.markdown("Calcule o TUSD e impostos rapidamente.")

# Sidebar para configurações fixas
with st.sidebar:
    st.header("Configurações")
    aliquota_icms = st.slider("Alíquota ICMS (%)", 0, 30, 20) / 100

# Campos de entrada
col1, col2 = st.columns(2)
with col1:
    consumo = st.number_input("Consumo Rede (kWh)", value=4342.0)
    preco_tusd = st.number_input("Preço TUSD (R$)", value=0.60956, format="%.5f")
with col2:
    solar = st.number_input("Solar Comp. (kWh)", value=4242.0)
    preco_inj = st.number_input("Preço Injetado (R$)", value=0.48774, format="%.5f")

ilum_pub = st.number_input("Iluminação Pública (R$)", value=53.46)

# Cálculos
valor_tusd = consumo * preco_tusd
valor_solar = solar * preco_inj
diferenca = valor_tusd - valor_solar
total = diferenca + ilum_pub

# Mostrar Resultado
st.divider()
st.metric("Total Estimado", f"R$ {total:.2f}")

with st.expander("Ver detalhes do cálculo"):
    st.write(f"Cobrança Rede: R$ {valor_tusd:.2f}")
    st.write(f"Crédito Solar: -R$ {valor_solar:.2f}")
    st.write(f"Diferença (Taxas/Fio): R$ {diferenca:.2f}")

# Botão para salvar/baixar
dados = f"Mes: Ref\nTotal: R$ {total:.2f}\nConsumo: {consumo}kWh"
st.download_button("Baixar Histórico (.txt)", dados, file_name="conta_solar.txt")
