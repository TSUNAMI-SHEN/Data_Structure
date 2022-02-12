# Selenium
  ### 概念
    selenium是一个用于Web应用程序测试的工具
    selenium测试直接运行在浏览器中，就像真正的用户在操作一样
    支持通过各种driver驱动真实浏览器完成测试
    selenium也支持无界面浏览器
  ### why selenium
    模拟浏览器功能，自动执行网页中的js代码，实现动态加载
  ### 使用步骤
    1.导入：from selenium import webdriver
    2.创建谷歌浏览器操作对象：
      path = 谷歌浏览器驱动文件路径
      browser = webdriver.Chrome(path)
    3.访问网址
      url = 要访问的网址
      browser.get(url)
  ### 元素定位
    自动化就是模拟鼠标和键盘来操作这些元素，点击、输入等等
    定位方法
      1.find_element_by_id
      2.find_element_by_name
      3.find_element_by_xpath
      4.find_element_by_tag_name
      5.find_element_by_css_selector
      6.find_element_by_link_text
  ### 访问元素信息
    获取元素属性——.get_attribute()
    获取元素文本——.text
    获取标签名——.tag_name
  ### 交互
    点击——click()
    输入——send_keys()
    后退操作——browser.back()
    前进操作——browser.forword()
    模拟js滚动
      js='document.documentElement.scrollTop=100000'
      browser.execute_script(js) 执行js代码
    获取网页代码：page_source
    退出：browser.quit()
# 无界面浏览器
  # Phantomjs
  # Chrome handless
