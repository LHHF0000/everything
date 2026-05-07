import matplotlib.pyplot as plt
import numpy as np

# 2024年月度数据（单位：万户）
year_2024 = [195.64, 129.66, 241.79, 147.35, 126.62, 107.60, 115.14, 99.93, 182.74, 684.68, 269.84, 198.91]

# 2025年月度数据（单位：万户）
year_2025 = [157.00, 283.59, 306.55, 192.44, 155.56, 164.64, 196.36, 265.03, 293.72, 230.99, 238.00, 260.00]

# 月份标签
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# 创建图表
plt.figure(figsize=(14, 7))

# 绘制2024年数据
plt.plot(months, year_2024, marker='o', linewidth=2, label='2024', color='blue')

# 绘制2025年数据
plt.plot(months, year_2025, marker='o', linewidth=2, label='2025', color='red')

# 添加标题和标签
plt.title('Monthly New A-share Account Openings (2024-2025)', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('New Accounts (10,000s)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# 添加数据标签
for i, v in enumerate(year_2024):
    plt.text(i, v + 3, f'{v:.1f}', ha='center', fontsize=8)
for i, v in enumerate(year_2025):
    plt.text(i, v + 3, f'{v:.1f}', ha='center', fontsize=8)

# 添加图例
plt.legend(loc='upper left', fontsize=10)

# 设置y轴范围
plt.ylim(0, max(max(year_2024), max(year_2025)) * 1.1)

# 优化布局
plt.tight_layout()

# 显示图表
plt.show()