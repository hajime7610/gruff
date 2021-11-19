import streamlit as st
from multiapp import MultiApp
import pandas as pd
from PIL import Image


st.set_page_config(
    page_title ='streamlit_hajime',
    page_icon = '👍',
    layout = 'wide'
    )

st.title('gruff_streamlit')

kpi1, kpi2, kpi3 = st.columns(3)


with kpi1:
    st.markdown("**First KPI**")
    number1 = 111
    st.markdown(f"<h1 style='text-align: center; color; red;'>{number1}<h1>",unsafe_allow_html=True)

with kpi2:
    st.markdown("**Second KPI**")
    number2 = 222
    st.markdown(f"<h1 style='text-align: center; color; red;'>{number2}<h1>",unsafe_allow_html=True)

with kpi3:
    st.markdown("** KPI**")
    number3 = 333
    st.markdown(f"<h1 style='text-align: center; color; red;'>{number3}<h1>",unsafe_allow_html=True)



#テキストの書き込み
st.write("#テキストの書き込み")
st.write("タイトル表示")
st.title('gruff_streamlit')

st.write("latexを用いた数式の表示")
st.latex("シュレディンガー方程式："r'''i\hbar\frac{\partial\psi}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}''')


st.write("プログラミングコードの表示")
code = '''import streamlit as st
code = ...
st.code(code, language="python")'''
st.code(code, language="python")

#データの表示
st.write("#データの表示")
st.table(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


#図、チャートの作成
st.write("#図、チャートの作成")
st.graphviz_chart('''
    digraph {
        User_interfae -> machine_A
        machine_A -> machine_D
        machine_A -> machine_C
        User_interfae -> machine_B
        machine_B -> machine_D
        machine_B -> machine_C
    }
''')



#ウィジェット（ボタンなど）の追加
st.write("#ウィジェット（ボタンなど）の追加")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')



#メディア（画像）の追加
st.write("#メディア（画像）の追加")
image = Image.open('moon_autumn.jpeg')
st.image(image, caption="中秋の名月", width=500, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

#レイアウト設定
add_selectbox = st.sidebar.selectbox(
    "#レイアウト設定",
    ("Email", "Home phone", "Mobile phone")
)


def app1():
    st.title('APP1')
    st.write('Welcome to app1')

def app2():
    st.title('APP2')
    st.write('Welcome to app2')


app = MultiApp()
app.add_app("page1", app1)
app.add_app("page2", app2)
app.run()
