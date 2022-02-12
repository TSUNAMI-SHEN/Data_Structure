# Requests
  # 基本使用
    官方文档：http://cn.python‐requests.org/zh_CN/latest/
    快速上手：http://cn.python‐requests.org/zh_CN/latest/user/quickstart.html
  # response
    属性：models.Response
    类型
      r.text：获取网站源码
      r.encoding：访问或定制编码方式
      r.url：获取请求的url
      r.content：响应的字节类型
      r.status_code：响应的状态码
      r.headers：响应的头信息
  # get请求
    requests.get()
    定制参数
      参数使用params传递
      参数无需urlencode编码
      不需要请求对象的定制
      请求资源路径中？可加可不加
  # post请求
    requests.post()
    定制参数
      参数使用data传递
      请求资源路径后面可以不加？
      不需要手动编解码
      不需要做请求对象的定制
  # 代理
    proxy定制，在请求中设置proxies参数
