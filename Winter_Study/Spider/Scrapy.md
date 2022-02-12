# Scrapy
  ### 概念
    Srapy是一个为零爬取网站数据，提取结构性数据而编写的应用框架，可以应用在包括数据挖掘、信息处理或存储历史数据等一些列的程序中
  ### scrapy项目的创建以及运行
    1.创建scrapy项目
      终端输入 scrapy startproject 项目名称
    2.项目组成
      spider
        __init__.py
        自定义的爬虫文件.py 自行创建，是实现爬虫核心功能的文件
      __init__.py
      items.py           定义数据结构的地方，是一个继承自scrapy.Item的类
      middlewares.py     中间件 代理
      pipelines.py       管道文件，里面只有一个类，用于处理下载数据的后续处理，默认是300优先级
                         值越小，优先级越高（1-1000）
      settings.py        配置文件 比如：是否遵守robots协议，User-Agent定义等
    3.创建爬虫文件
      1.跳转到spider文件夹 cd ./目录名字/目录名字/spiders
      2.scrapy genspider 爬虫名字 网页的域名
      爬虫文件的基本组成
        继承scrapy.Spider类
          name = 'baidu'    运行爬虫文件时使用的名字
          
          allowed_domains   爬虫允许的域名，在爬取的时候，如果不是此域名之下的url，会被过滤掉
          start_urls        声明了爬虫的起始地址，可以写多个url
          parse(self, response)   解析数据的回调函数
            response.text         响应的字符串
            response.body         响应的二进制文件
            response.xpath()      xpath方法的返回值类型时selector列表
            extract()             提取的是selector对象的是data
            extract_first(）      提取的是selector列表中的第一个数据
    4.运行爬虫文件
      scrapy crawl 爬虫名称
      注意：在spiders文件夹内执行
  ### scrapy架构组成
    1.引擎——自动运行，无需关注，会自动组织所有的请求对象，分发给下载器
    2.下载器——从引擎处获取到请求对象后，请求数据
    3.spiders——Spiders类定义了如何爬取某个网站，包括了爬取的动作以及如何从网页的内容中提取结构化数据
      即定义爬取的动作以及分析某个网页的地方
    4.调度器——与自己的调度规则，无需关注
    5.管道——最终处理数据的管道，会预留接口供我们处理数据
      以下是item pipeline的一些典型应用:
      1. 清理HTML数据
      2. 验证爬取的数据(检查item包含某些字段)
      3. 查重(并丢弃)
      4. 将爬取结果保存到数据库中
  ### scrapy工作原理
    1.引擎的spiders要url
    2.引擎将要爬取的url给调度器
    3.调度器会将url生成请求对象放入到指定的队列中
    4.从队列中出一个请求
    5.引擎将请求交给下载器进行处理
    6.下载器发送请求获取互联网数据
    7.下载器将数据返回给引擎
    8.引擎将数据再次给到spiders
    9.spiders通过xpath解析该数据，得到数据或者url
    10.spiders将数据或者url给到引擎
    11.引擎判断该数据是url还是数据，是数据，交给管道处理，是url交给调度器处理
  ### scrapy shell
    scrapy终端，测试提取的数据，交互性测试表达式代码的功能
  ### yield
    1. 带有 yield 的函数不再是一个普通函数，而是一个生成器generator，可用于迭代
    2. yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。重点是:下一次迭代
    时，从上一次迭代遇到的yield后面的代码(下一行)开始执行
    3. 简要理解:yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始
  ### CrawlSpider
    1.继承自scrapy.Spider
    2.独门秘笈
      CrawlSpider可以定义规则，再解析html内容的时候，可以根据链接规则提取出指定的链接，然后再向这些链接发 送请求
      所以，如果有需要跟进链接的需求，意思就是爬取了网页之后，需要提取链接再次爬取，使用CrawlSpider是非常 合适的
    3.提取链接 链接提取器，在这里就可以写规则提取指定链接
      scrapy.linkextractors.LinkExtractor(
          allow = (),   # 正则表达式，提取符合正则的链接)
          deny = (),    # （不用）正则表达式，不提取符合正则的链接
          allow_domains = (),   # （不用）允许的域名
          deny_domains = (),    # （不用）不允许的域名
          restrict_xpaths = (),   # xpath，提取符合xpath规则的链接
          restrict_css = ()     # 提取符合选择器规则的链接）
    4.模拟使用
      正则用法：links1 = LinkExtractor(allow=r'list_23_\d+\.html')
      xpath用法：links2 = LinkExtractor(restrict_xpaths=r'//div[@class="x"]')
      css用法：links3 = LinkExtractor(restrict_css='.x')
    5.提取链接
      link.extract_links(response)
    6.注意事项
      callback只能写函数名字符串，不需要加()
      在基本的spider中，如果重新发送请求，那里的callback写的是follow=true 是否跟进 就是按照提取连接规则进行提取
  ### 日志信息 & 日志等级
    日志级别
      CRITICAL：严重错误
      ERROR：一般错误
      WARNING：警告
      INFO：一般信息
      DEBUG：调试信息——默认
    settings.py文件设置
      默认的级别是DEBUG，会显示上面所有的信息
      在配置文件中 settings.py
      LOG_FILE : 将屏幕显示的信息全部记录到文件中，屏幕不再显示，注意文件后缀一定是.
      log LOG_LEVEL : 设置日志显示的等级，就是显示哪些，不显示哪些
  ### scrapy的post请求
    1.重写start_requests方法
    2.strat_requests的返回值
      scrapy.FormRequest(url=url, headers=headers, callback=self.parse_item, formdata=data)
        url: 要发送的post地址 
        headers:可以定制头信息
        callback: 回调函数
        formdata: post所携带的数据，这是一个字典
  ### 代理
    (1)到settings.py中，打开一个选项 DOWNLOADER_MIDDLEWARES = {
              'postproject.middlewares.Proxy': 543,
           }
    (2)到middlewares.py中写代码
           def process_request(self, request, spider):
               request.meta['proxy'] = 'https://113.68.202.10:9999'
               return None
