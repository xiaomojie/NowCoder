from collections import Counter

a = ['主营业务：', 'O2O', '车主服务', '驾考培训', '互联网驾考', '汽车交通支撑服务', '汽车交通支撑服务', '汽车交通支撑服务', '汽车交通支撑服务', '驾考培训', '驾考培训', '主营业务：']
# 统计词频
result = Counter(a)
print(result)
# 排序
d = sorted(result.items(), key=lambda x: x[1], reverse=True)
print(d)
