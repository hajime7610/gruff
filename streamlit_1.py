import streamlit as st
from multiapp import MultiApp
import pandas as pd
from PIL import Image


st.set_page_config(
    page_title ='streamlit_hajime',
    page_icon = 'ð',
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



#ãã­ã¹ãã®æ¸ãè¾¼ã¿
st.write("#ãã­ã¹ãã®æ¸ãè¾¼ã¿")
st.write("ã¿ã¤ãã«è¡¨ç¤º")
st.title('gruff_streamlit')

st.write("latexãç¨ããæ°å¼ã®è¡¨ç¤º")
st.latex("ã·ã¥ã¬ãã£ã³ã¬ã¼æ¹ç¨å¼ï¼"r'''i\hbar\frac{\partial\psi}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}''')


st.write("ãã­ã°ã©ãã³ã°ã³ã¼ãã®è¡¨ç¤º")
code = '''import streamlit as st
code = ...
st.code(code, language="python")'''
st.code(code, language="python")

#ãã¼ã¿ã®è¡¨ç¤º
st.write("#ãã¼ã¿ã®è¡¨ç¤º")
st.table(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


#å³ããã£ã¼ãã®ä½æ
st.write("#å³ããã£ã¼ãã®ä½æ")
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



#ã¦ã£ã¸ã§ããï¼ãã¿ã³ãªã©ï¼ã®è¿½å 
st.write("#ã¦ã£ã¸ã§ããï¼ãã¿ã³ãªã©ï¼ã®è¿½å ")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')



#ã¡ãã£ã¢ï¼ç»åï¼ã®è¿½å 
st.write("#ã¡ãã£ã¢ï¼ç»åï¼ã®è¿½å ")
image = Image.open('moon_autumn.jpeg')
st.image(image, caption="ä¸­ç§ã®åæ", width=500, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

#ã¬ã¤ã¢ã¦ãè¨­å®
add_selectbox = st.sidebar.selectbox(
    "#ã¬ã¤ã¢ã¦ãè¨­å®",
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
