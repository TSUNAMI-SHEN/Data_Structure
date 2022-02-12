# 基本使用
  ### 模拟浏览器向服务器发送请求
    urllib.request.urlopen(request)
      传入参数——request，请求对象
      返回response，即服务器的数据，类型是HttpResponse
    6个方法
      read()，字节形式读取二进制
      readline()，读取一行
      readlines()，一行一行读取，直至结束
      getcode()，获取状态码
      geturl()，获取url
      getheaders()，获取headers
  ### 网页下载
    urllib.request.urlretrieve()
      下载请求网页、图片、视频
# 请求对象的定制-为了解决反爬虫的第一种手段
  ### request = urllib.request.Request()
    get请求方式
      urllib.parse.quote()，传入字符串类型数据
      urllib.parse.urlencode()，传入字典类型数据
    post请求方式
      urllib.parse.urlencode().encode()，传入字典类型数据
    区别
      get请求方式的参数必须编码，参数是直接拼接到url后面，编码之后不需要调用encode方法
      post请求方式的参数必须编码，参数是放在请求对象定制的方法中（放在urllib.request.Request()参数中），编码之后需要调用encode方法
# URLError\HTTPError
  # 简介
    1.HTTPError类是URLError类的子类
    2.导入的包 urllib.error.HTTPError urllib.error.URLError
    3.http错误：http错误是针对浏览器无法连接到服务器而增加出来的错误提示。引导并告诉浏览者该页是哪里出
了问题
    4.通过urllib发送请求的时候，有可能会发送失败，这个时候如果想让你的代码更加的健壮，可以通过try‐
except进行捕获异常，异常有两类，URLError\HTTPError
# Handler处理器——定制更高级的请求头
  # 步骤
    1.handler = urllib.request.HTTPHandler()
    2.opener = urllib.request.build_opener(handler)
    3.response = opener.open(request)
# 代理服务器
   # 1.代理的常用功能
    1.突破自身IP访问限制，访问国外站点
    2.访问一些单位或团体内部资源
    扩展:某大学FTP(前提是该代理地址在该资源的允许访问范围之内)，使用教育网内地址段免费代理服务 器，就可以用于对教育网开放的各类FTP下载上传，以及各类资料查询共享等服务。
    3.提高访问速度 扩展:通常代理服务器都设置一个较大的硬盘缓冲区，当有外界的信息通过时，同时也将其保存到缓冲区中，当其他用户再访问相同的信息时， 则直接由缓冲区中取出信息，传给用户，以提高访问速度。
    4.隐藏真实IP
    扩展:上网者也可以通过这种方法隐藏自己的IP，免受攻击。 
  # 2.代码配置代理
    创建Reuqest对象
    创建ProxyHandler对象
    用handler对象创建opener对象
    使用opener.open函数发送请求
