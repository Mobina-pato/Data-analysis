import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/Users/mobina/Downloads/Reviews.csv'
df = pd.read_csv(file_path)

# Plot Distribution of Scores (Pie Chart)
score_counts = df['Score'].value_counts()
colors = plt.cm.Paired(np.linspace(0, 1, len(score_counts)))

plt.figure(figsize=(8, 8))
patches, texts, autotexts = plt.pie(score_counts, labels=score_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
plt.legend(patches, score_counts.index, title="Score", loc="best")
plt.title('Distribution of Scores')
plt.axis('equal')
plt.show()

# Calculate Descriptive Statistics for Helpfulness Ratio by Score
df = df[df['HelpfulnessDenominator'] > 0]
df['HelpfulnessRatio'] = df['HelpfulnessNumerator'] / df['HelpfulnessDenominator']
stats = df.groupby('Score')['HelpfulnessRatio'].agg(['mean', 'var', 'median', 'min', 'max'])

print("Statistics for Helpfulness Ratio by Score:")
print(stats)

# Visualization of Mean Helpfulness Ratio by Score
plt.figure(figsize=(10, 6))
plt.bar(stats.index, stats['mean'], color='skyblue', label='Mean')
plt.title('Average Helpfulness Ratio by Score')
plt.xlabel('Score')
plt.ylabel('Average Helpfulness Ratio')
plt.xticks(np.arange(1, 6, step=1))
plt.ylim(0, 1)
plt.grid(True)
plt.legend()
plt.show()

# Visualization of Variance in Helpfulness Ratio by Score
plt.figure(figsize=(10, 6))
plt.bar(stats.index, stats['var'], color='lightcoral', label='Variance')
plt.title('Variance of Helpfulness Ratio by Score')
plt.xlabel('Score')
plt.ylabel('Variance of Helpfulness Ratio')
plt.xticks(np.arange(1, 6, step=1))
plt.grid(True)
plt.legend()
plt.show()

# Boxplot for Helpfulness Ratio by Score (for Distribution Analysis)
plt.figure(figsize=(10, 6))
df.boxplot(column='HelpfulnessRatio', by='Score', grid=True)
plt.title('Boxplot of Helpfulness Ratio by Score')
plt.suptitle('')
plt.xlabel('Score')
plt.ylabel('Helpfulness Ratio')
plt.ylim(0, 1)
plt.show()

# Distribution of Scores (Histogram)
plt.figure(figsize=(10, 6))
df['Score'].plot(kind='hist', bins=5, color='seagreen', edgecolor='black', alpha=0.7)
plt.title('Distribution of Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
