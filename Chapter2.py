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


# UserCF，用户相似度：余弦相似度
def UserSimilarity(train):
	W = dict()
	for u in train.keys():
		for v in train.keys():
			if u == v:
				continue
			W[u][v] = len(train[u] & train[v])
			W[u][v] /= math.sqrt(len(train[u]) * len(train[v]) * 1.0)
	return W

# UserCF，用户相似度：余弦相似度，优化版
def UserSimilarity(train):
	# 建立从物品到用户的倒排表
	item_user = dict()
	for u, items in train.items():
		for i in items.keys():
			# 如果物品i不在字典中就创建set
			if i not in item_users:
				item_users[i] = set()
			item_users[i].add(u)

	# 计算用户u、v同时评价一个物品的情况，这样可以大大减少因为计算u、v不同时评价一个物品时所花费的时间
	C = dict()
	N = dict()
	for i, users in item_users.items():
		# 单个物品下遍历许多user
		for u in users:
			# 用户集合长度计数
			N[u] += 1
			for v in users:
				# 排除自身
				if u == v:
					continue
				C[u][v] += 1

	# 计算最终的相似度矩阵W
	W = dict()
	for u, related_users in C.items:
		for v, cuv in related_users.item_users:
			W[u][v] = cuv / math.sqrt(N[u] * N[v])

	return W


# 给用户推荐与其兴趣最接近的K个用户喜欢的物品
def Recommend(user, train, W):
	rank = dict()
	interacted_item = train[user] # 已经产生过行为的物品，后面要过滤掉
	# 这里W[u]的格式应当是(user, 相似度)
	for v, wuv in sorted(W[u].items, key=itemgetter(1), reverse=True)[0:K]:
		for i, tvi in train[v].items:
			# 过滤
			if i in interacted_item:
				continue
			rank[i] += wuv * rvi
	return rank


# UserCF，用户相似度：基于余弦相似度，但是惩罚了两个用户共同兴趣列表中热门物品对他们的影响
def UserSimilarity(train):
	# 建立从物品到用户的倒排表
	item_user = dict()
	for u, items in train.items():
		for i in items.keys():
			# 如果物品i不在字典中就创建set
			if i not in item_users:
				item_users[i] = set()
			item_users[i].add(u)

	# 计算用户u、v同时评价一个物品的情况，这样可以大大减少因为计算u、v不同时评价一个物品时所花费的时间
	C = dict()
	N = dict()
	for i, users in item_users.items():
		# 单个物品下遍历许多user
		for u in users:
			# 用户集合长度计数
			N[u] += 1
			for v in users:
				# 排除自身
				if u == v:
					continue
				C[u][v] += 1 / math.log(1 + len(users))

	# 计算最终的相似度矩阵W
	W = dict()
	for u, related_users in C.items:
		for v, cuv in related_users.item_users:
			W[u][v] = cuv / math.sqrt(N[u] * N[v])

	return W
















































