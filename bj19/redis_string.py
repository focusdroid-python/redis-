from redis import StrictRedis

if __name__ == '__main__': 
	# 创建StrictRedis对象
	try:
		sr = StrictRedis()
		# 添加一个key，为name，value是王旭
		res = sr.set('name', '王旭')
		print(res)
		# 获取name的值
		res = sr.get('name')	
		print(res)

		# 修改一个key，为name，value是lilei
		res = sr.set('name', 'lilei')
		print(res)
		# 获取name的值
		res = sr.get('name')
		print(res)

		# 删除name及对应值
		res = sr.delete('name')
		print(res)

		# 删除多个键值
		res = sr.delete('a3', 'a2')
		print(res)

		# 获取数据库中所有的键
		res = sr.keys()
		print(res)
	except Exception as e:
		print(e)	
