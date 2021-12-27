from requests_html import HTMLSession

url = "https://search.yahoo.co.jp/realtime"

# セッション開始
session = HTMLSession()
r = session.get(url)

# ブラウザエンジンでHTMLを生成させる
r.html.render()

# スクレイピング
#急上昇ワード
words = r.html.find(".HotBuzz_HotBuzz__1GCkY")
word_list = []
for word in words:
    word_list.append(word.text)

print(word_list[0])

#トレンド
trends = r.html.find(".Trend_Trend__5OTRp")
trend_list = []
for trend in trends:
    trend_list.append(trend.text)

print(trend_list[0])
