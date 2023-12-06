import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSVファイルを読み込む
data = pd.read_csv('trend.csv')

# 必要に応じてデータを整形

# 折れ線グラフの作成
plt.figure(figsize=(15, 8))
sns.lineplot(x='Year', y='NumberOfQuestions', hue='TagName', data=data, marker='o')

# グラフのタイトルと軸ラベルを設定
plt.title('tag trend')
plt.xlabel('date')
plt.ylabel('number of questions')

plt.legend(loc='center right', bbox_to_anchor=(-0.1, 0.5))

plt.savefig("output.png", bbox_inches='tight')
plt.show()

