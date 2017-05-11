# 将数据集随机分成训练集和测试集
# 每次实验选取不同的k(0=<k<=M-1)和相同的随机数种子seed，进行M次实验就可以得到M个不同的训练集合测试集
def SplitData(data, M, k, seed):
	test = []
	train = []
	random.seed(seed)
	for user, item in data:
		if random.random(0, M) == k:
			test.append([user, item])
		else:
			train.append([user, item])
	return train, test


# 覆盖率
def Coverage(train, test, N):
	recommend_items = set()
	all_items = set()
	for user in train.keys():
		for item in train[user].keys():
			all_items.add(item)
		rank = GetRecommendation(user, N)
		for item, pui in rank:
			recommend_items.add(item)
	return len(recommend_items) / (len(all_items) * 1.0)


#新颖度，通过推荐列表中的平均流行度来度量
def Popularity(train, test, N):
	item_popularity = dict()
	# 遍历训练集数据
	for user, items in train.items():
		# 构造物品流行度字典
		for item in items.keys():
			if item not in item_popularity:
				item_popularity[item] = 0
			item_popularity[item] += 1

	# 总流行度
	ret = 0 
	# 推荐列表物品总数
	n = 0
	for user in train.keys():
		rank = GetRecommendation(user, N)
		for item, pui in rank:
			ret += math.log(1 = item_popularity[item])
			n += 1
	ret /= n * 1.0
	return ret