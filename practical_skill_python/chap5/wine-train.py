from sklearn import svm, metrics, model_selection

wine_csv = []
with open('winequality-white.csv', 'r', encoding='utf-8') as fp:
    no = 0
    for line in fp:
        line = line.strip()
        cols = line.split(';')
        wine_csv.append(cols)

wine_csv = wine_csv[1:]

labels = []
data = []
for cols in wine_csv:
    cols = list(map(lambda n: float(n), cols))
    # ワインのグレードを調整
    grade = int(cols[11])
    if grade == 9: grade = 8
    if grade < 4: grade = 5
    labels.append(grade)
    data.append(cols[0:11])

# 訓練用データとテスト用データに分ける
data_train, data_test, label_train, label_test = \
    model_selection.train_test_split(data, labels)

# ランダムフォレストで学習
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

# 予測
predict = clf.predict(data_test)

# 結果表示
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print('正解率=', ac_score)
print('レポート=\n', cl_report)