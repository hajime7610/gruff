import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st
import sklearn 
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title ='streamlit_omamiuda',
    page_icon = '👍'
    )


seiseki_df=pd.read_csv('https://statistics.co.jp/reference/statistical_data/seiseki.csv')

st.title('主成分分析')

st.write(seiseki_df)

# 主成分分析実行
pca = PCA()
feature = pca.fit(seiseki_df)
# データを主成分空間に写像
feature = pca.transform(seiseki_df)

st.write("・第１主成分と第２主成分でプロット")
fig, ax = plt.subplots(figsize=(4,4))
ax.scatter(feature[:, 0], feature[:, 1], alpha=0.8, c=list(seiseki_df.iloc[:, 1]))
ax.grid()
plt.xlabel("PC1")
plt.ylabel("PC2")

st.pyplot(fig)


st.write("・寄与率表示（index:0スタート）")
pca.explained_variance_ratio_

add_selectbox = st.sidebar.selectbox(
    "#レイアウト設定",
    ("第一成分", "第二成分", "第三成分")
)

with st.expander("参考"):
    st.write("データ："+"https://statistics.co.jp/reference/statistical_data/statistical_data.htm")
    st.write(" Webサイト："+"https://docs.streamlit.io/library/api-reference/control-flow/st.stopx")
    st.write("作成コード："+"https://github.com/hajime7610/gruff/blob/main/streamlit_1.py")

name = st.text_input('・分かったこと')
if not name:
  st.warning('''ex.寄与率が第二成分で80％を超えている''')
  st.stop()
st.success('Thank you for answering.')

