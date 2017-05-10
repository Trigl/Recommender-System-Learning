# 推荐系统评分预测准确度指标：均方根误差（RMSE）和平均绝对误差（MAE）
# records[i]=[u,i,rui,pui]，测试数据：records = [['haha',1,3.2,3],['hehe',2,2.5,2]]
from math import sqrt
def RMSE(records):
	return sqrt(sum([(rui-pui)*(rui-pui) for u,i,rui,pui in records]))/float(len(records))

def MAE(records):
	return sum([abs(rui-pui) for u,i,rui,pui in records])/float(len(records))


# TopN推荐的预测准确率通过准确率（precision）和召回率（recall）度量
def PrecisionRecall(test, N):
	hit = 0
	n_recall = 0
	n_precision = 0
	for user, items in test.items():
		rank = Recommend(user, N)
		hit += len(rank & items)

# 可以定义覆盖率的指标，基尼系数
def GiniIndex(p):
	j = 1
	n = len(p)
	G = 0
	for item, weight in sorted(p.items(), key=itemgetter(1)):
		G += (2*j - n -1) * weight
		return G/float(n-1)
