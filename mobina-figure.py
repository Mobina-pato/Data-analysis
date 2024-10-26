import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# خواندن فایل CSV به جای Excel
file_path = '/Users/mobina/Downloads/Reviews.csv'
df = pd.read_csv(file_path)

# فیلتر کردن ردیف‌هایی که HelpfulnessDenominator بزرگتر از صفر هستند
df = df[df['HelpfulnessDenominator'] > 0]

# محاسبه نسبت مفید بودن و میانگین نسبت‌ها بر اساس Score
df['HelpfulnessRatio'] = df['HelpfulnessNumerator'] / df['HelpfulnessDenominator']
score_groups = df.groupby('Score')['HelpfulnessRatio'].mean()

# تنظیمات برای نمودار
x = score_groups.index
y = score_groups.values

plt.figure(figsize=(8, 6))
plt.bar(x, y, color='skyblue')

plt.title('Average Helpfulness Ratio by Score')
plt.xlabel('Score')
plt.ylabel('Average Helpfulness Ratio')
plt.xticks(np.arange(1, 6, step=1))
plt.ylim(0, 1)
plt.grid(True)

plt.show()
