import pandas as pd
import streamlit as st
import sklearn 
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title ='streamlit_omamiuda',
    page_icon = 'ð'
    )


seiseki_df=pd.read_csv('https://statistics.co.jp/reference/statistical_data/seiseki.csv')

st.title('ä¸»æååæ')

st.write(seiseki_df)

# ä¸»æååæå®è¡
pca = PCA()
feature = pca.fit(seiseki_df)
# ãã¼ã¿ãä¸»æåç©ºéã«åå
feature = pca.transform(seiseki_df)

st.write("ã»ç¬¬ï¼ä¸»æåã¨ç¬¬ï¼ä¸»æåã§ãã­ãã")
fig, ax = plt.subplots(figsize=(4,4))
ax.scatter(feature[:, 0], feature[:, 1], alpha=0.8, c=list(seiseki_df.iloc[:, 1]))
ax.grid()
plt.xlabel("PC1")
plt.ylabel("PC2")

st.pyplot(fig)


st.write("ã»å¯ä¸çè¡¨ç¤ºï¼index:0ã¹ã¿ã¼ãï¼")
pca.explained_variance_ratio_

add_selectbox = st.sidebar.selectbox(
    "#ã¬ã¤ã¢ã¦ãè¨­å®",
    ("ç¬¬ä¸æå", "ç¬¬äºæå", "ç¬¬ä¸æå")
)

with st.expander("åè"):
    st.write("ãã¼ã¿ï¼"+"https://statistics.co.jp/reference/statistical_data/statistical_data.htm")
    st.write(" Webãµã¤ãï¼"+"https://docs.streamlit.io/library/api-reference/control-flow/st.stopx")
    st.write("ä½æã³ã¼ãï¼"+"https://github.com/hajime7610/gruff/blob/main/streamlit_1.py")

name = st.text_input('ã»åãã£ããã¨')
if not name:
  st.warning('''ex.å¯ä¸çãç¬¬äºæåã§80ï¼ãè¶ãã¦ãã''')
  st.stop()
st.success('Thank you for answering.')




