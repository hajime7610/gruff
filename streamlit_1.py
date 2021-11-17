import streamlit as st
import pandas as pd

st.write("タイトル表示")
st.title('My app')
st.write("データの表示")
st.table(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


st.write("latexを用いた数式の表示")
st.latex("シュレディンガー方程式："r'''i\hbar\frac{\partial\psi}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}''')


st.write("プログラミングコードの表示")
code = '''import streamlit as st
code = ...
st.code(code, language="python")'''
st.code(code, language="python")



