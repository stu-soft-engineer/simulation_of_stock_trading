后台接口

### 注册 119.23.36.18:8080/regist

描述：注册账户

POST /regist HTTP/1.1

Content-Type: multipart/form-data

| 提交参数（form-data） | 说明                     | 例子        | type   |
| --------------------- | ------------------------ | ----------- | ------ |
| user                  | 用户名（微信id）         | xiaoming    | string |
| psw                   | 密码（目前和用户名一样） | xiaoming    | string |
| heading               | 头像地址                 | heading.com | string |
| nickname              | 昵称                     | 小鸣        | string |

**返回数据（JSON）**

```
{
  "value": 1
}
```

**value说明**

1：注册成功、-1：密码错误、-101：数据库连接失败、-102：注册异常（重复注册）、-103：插入失败





### 登陆 119.23.36.18:8080/login

描述：登录账户并返回token，后面的操作需要用到

POST /regist HTTP/1.1

Content-Type: multipart/form-data

| 提交参数（form-data） | 说明                     | 例子     | type   |
| --------------------- | ------------------------ | -------- | ------ |
| user                  | 用户名（微信id）         | xiaoming | string |
| psw                   | 密码（目前和用户名一样） | xiaoming | string |

**返回数据（JSON）**

```
{
    "token": "746018d656cc0f54aab61dbd60ba263c",
    "value": 1
}
```

**token（string）：**

标识用户身份的字符串，登录失败时候是空的

**value（int）：**

1：登录成功并返回token、-1：密码错误、-2：封号、-101：数据库连接失败、-102：登陆异常、-103：登陆失败（未注册）



### 购买股票 119.23.36.18:8080/buy

描述：下单购买股票

POST /regist HTTP/1.1

Content-Type: multipart/form-data

| 提交参数（form-data） | 说明                | 例子                             | type   |
| --------------------- | ------------------- | -------------------------------- | ------ |
| token                 | 登陆时候获取的token | 746018d656cc0f54aab61dbd60ba263c | string |
| matchid               | 比赛ID              | 12                               | int    |
| stockid               | 股票代码            | 000581                           | string |
| stocknum              | 买入数量            | 100                              | int    |
| price                 | 买入价格            | 12.23                            | double |

**返回数据（JSON）**

```
{
    "value": 1
}
```

**value（int）：**

1：下单成功、-1：token错误、-2：余额不足、-101：数据库连接失败、-102：购买异常、-103：增加订单失败



### 出售股票 119.23.36.18:8080/sell

描述：下单出售股票

POST /regist HTTP/1.1

Content-Type: multipart/form-data

| 提交参数（form-data） | 说明                | 例子                             | type   |
| --------------------- | ------------------- | -------------------------------- | ------ |
| token                 | 登陆时候获取的token | 746018d656cc0f54aab61dbd60ba263c | string |
| matchid               | 比赛ID              | 12                               | int    |
| stockid               | 股票代码            | 000581                           | string |
| stocknum              | 卖出数量            | 100                              | int    |
| price                 | 卖出价格            | 12.23                            | double |

**返回数据（JSON）**

```
{
    "value": 1
}
```

**value（int）：**

1：下单成功、-1：token错误、-2：库存不足、-101：数据库连接失败、-102：出售异常、-103：增加订单失败







