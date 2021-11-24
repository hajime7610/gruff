# 数値計算ライブラリ
import numpy as np
import pandas as pd
# 可視化ライブラリ
import matplotlib.pyplot as plt


#data loading
url =  'https://statistics.co.jp/reference/statistical_data/seiseki.csv'
df = pd.read_csv(url)
df.head()

#データの基本量
df.describe().apply(lambda s: s.apply(lambda x: format(x, 'g')))

#データの描写：散布図
import japanize_matplotlib

# pandasのplottingメソッドをインポート
from pandas import plotting

# 散布図行列を表示

plotting.scatter_matrix(df, figsize=(12, 12), alpha=0.8)

#データの標準化
# sklearnの標準化モジュールをインポート
from sklearn.preprocessing import StandardScaler

# データを変換する計算式を生成
sc = StandardScaler()
sc.fit(df)

# 実際にデータを変換
z = sc.transform(df)

print(z)
print(z.shape)

#モデル生成、因子得点の算出
# sklearnのFactorAnalysis(因子分析)クラスをインポート
from sklearn.decomposition import FactorAnalysis as FA

# 因子数を指定
n_components=3

# 因子分析の実行
fa = FA(n_components, max_iter=5000) # モデルを定義
fitted = fa.fit_transform(z) # fitとtransformを一括処理

print(fitted)
print(fitted.shape)

#因子負荷量行列
fa.components_.T

# 変数Factor_loading_matrixに格納
Factor_loading_matrix = fa.components_.T

# データフレームに変換
df_2 = pd.DataFrame(Factor_loading_matrix, 
             columns=["第1因子", "第2因子", "第3因子"], 
             index=[df.columns])

#csvファイルに出力
df_2.to_csv("seiseki_factor.csv")



