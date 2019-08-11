## redis数据库操作
## redis数据操作之数据类型
    string
    键命令
    hash
    list
    set
    zset
    
    set name focusdroid
    get name   # focusdroid
    ### redis设置过期时间
       setex aa 3 aa // 只有3s有效时间
    ### 设置多个键值
       mset key1 value1 key2 value2
    ### 追加值
       append key value
       append 'a1' 'haha'
    ## 获取
        ### 获取：根据键获取值，如果不存在此键则返回nil
            get key
        ### 获取键‘name’的值
            get 'name'
        ### 根据多个键获取多个值
            mget key1 key2
            例： 获取a1 a2 a3
            mget a1 a2 a3
    ## 键命令
        ### 查找键，参数支持正则表达式
                keys pattern
            例如：
                keys *
            查看名称中包含a的键
                keys 'a*'
            判断a1键是否存在
                exists a1
            查看键对应的value类型
    ## 设置过期时间 expire   
             expire key seconds
             expire a1 3
             查看有效时间，秒为单位
             ttl key
             查看bb有效时间: ttl bb
## 掌握hash类型
    hash用于存储对象，对象的机构为属性，值
    值类型为string
    ### 增加，修改
    设置单个属性
        hset key field value
        设置键user的属性name为ithaha
        hset user name haha
        设置多个属性
        hmset key field value feild2 value2
        hmset u2 name itcast age 11
    ### 获取
        ### 获取指定键的value
            hget key field
            hget u2 'name'
        ### 获取多个属性
            hmget key field1 field2
            hmget u2 name age
        ### 获取所有属性值
            hvals key
            hvals u2
    ## 删除
        删除整个hash键及值
        删除属性，属性对应的值会被一起删除
        hdel key field1 field2
        删除键u2的属性age
        hdel u2 age        
    ## 增加
        在左侧插入数据
        lpush key field1 value2
        例子：
            ### 从键为a1的列表左侧加入数据a,b,c
                lpush a22 a b c
        ### 从右侧插入数据
            ### rpush key value1 value2
            例子：
                rpush a22  0 1 2
        ### 在指定元素前面或后面插入新元素
            ### linsert key before 或after现有元素 新元素
            例子：
                linsert a22 brfore b 3
    ## 获取
        返回列表里指定范围的元素
        start stop 为元素下标索引
        索引从左侧开始，第一个元素为0
        索引可以为负数，表示从尾部开始计数，如 -1 就是最后一个元素
        lrange key start stop
        例子：
            lrange a22 0 -1
    ## 删除
        ### 删除指定元素
            将列表中前count次出现的值为value的元素移除
            count > 0 从头往尾移除
            count < 0 从尾往头移除
            count = 0 移除所有
            lrem key count value
            例子:
                向列表a22中加入元素 'a' 'b' 'c' 'd' 'e'
                lpush a22 a b c d e

## set类型
    无序集合
    元素为string类型
    元素具有唯一性，不重复
    说明：对于集合没有修改操作
    ### 增加
        ## 增加元素
            sadd key member2 member2
            例子：
            sadd a3 zhangsan slili wangxu
    ### 获取
        ## 返回所有的元素
            smembers key
            smembers a3
    ### 删除
        ## 删除指定元素
            srem key
            srem a3 wangxu
## zset类型
    sorted set 有序集合
    元素为string类型
    元素具有唯一性，不重复
    每个元素都会关联一个double类型的score(权重)，表示权重， 通过权重将元素从小到大排序
    说明: 没有修改操作
    ## 添加
        zadd key score1 member1 score2 member2
        zadd a4 4 lisi 5 wangwu 6 zhangsan 3jj
        
    ## 获取
        返回指定范围内的元素
        start stop 为元素的下标索引
        索引从左侧开始，第一个元素为0
        索引可以是负数，表示从尾部开始计数，如-1表示最后一个元素
        zrange key start stop
        zrange a4 0 -1
        ## 返回min和max之间的元素
        zrangebyscore key min max
        ## 获取键a4的集合元素权重
        zscore a4 wangwu
    ## 删除
         删除指定的元素
         zrem key member1 member2  
         zrem a4 wangwu     
         删除权重指定范围的元素
         zremrangebyscore key min max
         删除集合a4   
## 与python交互
    StrictRedis对象方法
    ##通过init对象创建，指定参数host，port与指定的服务器和端口连接，host默认为localhost，port默认为6379，db默认为0
    sr = StrictRedis(host='localhost', port=6379, db=0)
    简写方式:
    sr = StrictRedis()
    
    根据不同的类型，拥有不同的实例方法可以调用，与前面学的redis命令对应，方法需要的参数与命令的参数一致
    ## String
        set
        setex
        mset
        append
        get
        mget
        key
    ## keys
        exists
        type
        delete
        expire
        getrange
        ttl
    ## hash
        hset
        hmset
        hkeys
        hget
        hmget
        hvals
        hdel
    ## list
        lpush
        rpush
        linsert
        lrange
        lset
        lrem
    ## set
        sadd
        smembers
        srem
    ## zset
        zadd
        zrange
        zrangebyscore
        zscore
        zrem
        zremrangebyscore
## 掌握使用redis存储session
    django存储session
    之前django的session默认存在数据库里面的，我们也可以把session存储在redis里面
    ## 准备工作
        创建test5项目和booktest应用
        配置url
    ## session中redis配置
        安装包（虚拟环境）
        pip3 isntall djnago-redis-sessions==0.5.6
    ## 设置redis存储session信息
    # 设置redis存储session信息
    SESSION_ENGINE = 'redis_sessions.session'
    # redis服务的ip地址
    SESSION_REDIS_HOST = 'localhost'
    # redis服务的端口号
    SESSION_REDIS_PORT = 6379
    # redis中的那个数据库
    SESSION_REDIS_DB = 2
    SESSION_REDIS_PASSWORD = ''
    SESSION_REDIS_PREFIX = 'session' # session、唯一标识码
    
## 搭建redis主从
   修改/etc/redis/redis.conf,绑定机器的ip地址
   sudo vi /etc/redis/redis.conf
   将127.0.0.1修改为本机ip
   
    
            
            
            
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
        