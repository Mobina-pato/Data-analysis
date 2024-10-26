import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = '/Users/mobina/Downloads/Reviews.csv'
df = pd.read_csv(file_path)

score_counts = df['Score'].value_counts()

colors = plt.cm.Paired(np.linspace(0, 1, len(score_counts)))

plt.figure(figsize=(8, 8))
patches, texts, autotexts = plt.pie(score_counts, labels=score_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)

plt.legend(patches, score_counts.index, title="Score", loc="best")

plt.title('Distribution of Scores')
plt.axis('equal')
plt.show()