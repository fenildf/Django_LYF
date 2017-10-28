# 题目接口

## 描述： 

通过id范围或者题目url获取题目列表

## 地址: /api/v1/questions/

## 调用方法： `GET`

## 参数:

|参数|类型|是否必要|说明|
|----|----|----|-----|
|db_table | string | 是 | 需要查询的题目列表 |
|min_id | integer | 否,默认为0 |  题目列表会出现的最小的题目id |
|max_id | integer | 否,默认不限大小   | 题目列表会出现的最大的题目id |
|question_url | string | 否  | 题目的url， 即spider_url |
|current_question_id | integer | 否 | 当前的题目的id，用于获取上一题或者下一题 |
|filter_method | string | 否， 默认为order | 可用列表为asc, desc, random, next, previous|
|size | integer | 否，默认为2 |返回题目列表的大小，最大返回4道|

参数说明：

对于`filter_method`选项：

* `asc`为按照question_id从小到大的顺序筛选题目
* `desc`为按照question_id从大到小的顺序筛选题目
* `next`为按照question_id 从小到达的顺序筛选question_id > current_question_id 的题目
* `previous`为按照question_id 从大到小的顺序筛选question_id > current_question_id的题目
* `random` 为随机筛选题目

## 响应格式

```json
{
    "meta": {
        "status": 0,
        "msg": ""
    },
    "data": {
        "question_lst": [
            {
                "question_id": "12231",
                "html": "rendered question html"
            },
            {
                "question_id": "12231",
                "html": "rendered question html"
            },
            //...
        ]
    }
}
```

其中`meta`下的`status`定义如下：

|status | 说明 | 
|-------|------|
|0 | 正常，从data中可以获取数据 |
|1 | 需要登陆系统 |
|2 | 参数错误 |
|3 | 内部系统错误 |
|4 | 请求内容不存在 |

## 常见用法:

1. 输入表名，随机展示题目

`/api/v1/questions/?db_table=question_sample&filter_method=random`

2. 输入表名，输入最小题目id，在该范围内顺序展示题目

`/api/v1/questions/?db_table=question_sample&filter_method=asc&min_id=1000`

3. 输入表名，输入题目范围，在该范围内随机展示题目

`/api/v1/questions/?db_table=question_sample&filter_method=random&min_id=1000&max_id=100000`

4. 输入表名，输入题目的url，获取题目

`/api/v1/questions/?db_table=question_sample&question_url=sample_url`

5. 输入表名，输入题目范围并根据当前题目的id获取后一组题目列表

`/api/v1/questions/?min_id=123&max_id=100000&current_question_id=123&filter_method=next`
