import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# خواندن فایل CSV
file_path = '/Users/mobina/Downloads/Reviews.csv'
df = pd.read_csv(file_path)

# فیلتر کردن ردیف‌هایی که HelpfulnessDenominator بزرگتر از صفر هستند
df = df[df['HelpfulnessDenominator'] > 0]

# محاسبه نسبت مفید بودن
df['HelpfulnessRatio'] = df['HelpfulnessNumerator'] / df['HelpfulnessDenominator']

# محاسبه میانگین، واریانس، میانه، حداقل و حداکثر برای نسبت مفید بودن بر اساس Score
stats = df.groupby('Score')['HelpfulnessRatio'].agg(['mean', 'var', 'median', 'min', 'max'])

# نمایش آمار محاسبه‌شده
print("Statistics for Helpfulness Ratio by Score:")
print(stats)

# نمودار میانگین نسبت مفید بودن بر اساس Score
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

# نمودار واریانس نسبت مفید بودن بر اساس Score
plt.figure(figsize=(10, 6))
plt.bar(stats.index, stats['var'], color='lightcoral', label='Variance')
plt.title('Variance of Helpfulness Ratio by Score')
plt.xlabel('Score')
plt.ylabel('Variance of Helpfulness Ratio')
plt.xticks(np.arange(1, 6, step=1))
plt.grid(True)
plt.legend()
plt.show()

# نمودار باکس‌پلات برای بررسی توزیع نسبت مفید بودن در هر Score
plt.figure(figsize=(10, 6))
df.boxplot(column='HelpfulnessRatio', by='Score', grid=True)
plt.title('Boxplot of Helpfulness Ratio by Score')
plt.suptitle('')  # Remove the default title
plt.xlabel('Score')
plt.ylabel('Helpfulness Ratio')
plt.ylim(0, 1)
plt.show()

# توزیع نمرات به صورت هیستوگرام
plt.figure(figsize=(10, 6))
df['Score'].plot(kind='hist', bins=5, color='seagreen', edgecolor='black', alpha=0.7)
plt.title('Distribution of Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
