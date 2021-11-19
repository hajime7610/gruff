import streamlit as st
import pandas as pd
from PIL import Image

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
image = "https://twitfukuoka.com/wp-content/uploads/2019/04/201904040006.jpg"
st.image(image, caption="令和", width=500, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

#レイアウト設定
add_selectbox = st.sidebar.selectbox(
    "#レイアウト設定",
    ("Email", "Home phone", "Mobile phone")
)




