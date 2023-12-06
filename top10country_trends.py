import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSVファイルを読み込む
file_path = 'top10country_trends.csv'
data = pd.read_csv(file_path)

# データフレームの 'Location' 列でユニークな値を取得し、各国ごとのデータセットを作成
unique_locations = data['Location'].unique()
dfs = {loc: data[data['Location'] == loc] for loc in unique_locations}

# 各プログラミング言語に固有の色を割り当てるためのカラーマップを作成
color_map = {
    'javascript': 'red', 
    'python': 'blue', 
    'java': 'green', 
    'c#': 'purple', 
    'php': 'orange', 
    'c++': 'brown',
    'typescript': 'pink', 
    'c': 'olive', 
    'ruby': 'cyan', 
    'swift': 'magenta'
}

# カラーマップに存在しないタグに対してデフォルトの色（グレー）を使用する
default_color = 'grey'
dfs_colored = {
    loc: df.assign(Color=df['TagName'].apply(lambda tag: color_map.get(tag, default_color)))
    for loc, df in dfs.items()
}

# サブプロットの行と列の数を決定する
num_countries = len(unique_locations)
num_rows = (num_countries // 2) + (num_countries % 2)
num_cols = 2 if num_countries > 1 else 1

# 各国ごとにプログラミング言語のランキングを可視化（色分けされた）
plt.figure(figsize=(15, num_rows * 5))

for i, (loc, df) in enumerate(dfs_colored.items(), 1):
    plt.subplot(num_rows, num_cols, i)
    sns.barplot(x='QuestionCount', y='TagName', data=df, palette=df['Color'].tolist())
    plt.title(f"Top Programming Languages in {loc}")
    plt.xlabel("Question Count")
    plt.ylabel("Programming Language")

plt.tight_layout()
plt.savefig('top10country_trends.png')
plt.show()
