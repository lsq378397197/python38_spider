import re

### 正则表达式 ######

# content = "Hello 123 4567 World_This is a Regex Demo"
# print(len(content))
# r = re.match('Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(r)
# print(r.group())
# print(r.span())

# content = 'Hello 1234567 World_This is a Regex Demo'
# # 这里我们想把字符串中的 1234567 提取出来，此时可以将数字部分的正则表达式用 () 括起来，然后调用了 group(1) 获取匹配结果。
# result = re.match('^Hello\s(\d+)\sWorld', content)
# print(result.group())
# print(result.group(1))

# content = 'Hello 1234567 World_This is a Regex Demo'
# # 这里我们想把字符串中的 1234567 提取出来，此时可以将数字部分的正则表达式用 () 括起来，然后调用了 group(1) 获取匹配结果。
# result = re.match('^Hello.*Demo$', content)
# print(result.group())

# 贪婪模
# content = 'Hello 1234567 World_This is a Regex Demo'
# # 这里我们想把字符串中的 1234567 提取出来，此时可以将数字部分的正则表达式用 () 括起来，然后调用了 group(1) 获取匹配结果。
# result = re.match('^Hello.*(\d+).*Demo$', content)
# print(result.group(1))

# 非贪婪模式.*?
# content = 'Hello 1234567 World_This is a Regex Demo'
# # 这里我们想把字符串中的 1234567 提取出来，此时可以将数字部分的正则表达式用 () 括起来，然后调用了 group(1) 获取匹配结果。
# # 但需要注意的是，如果匹配的结果在字符串结尾，.*? 就有可能匹配不到任何内容了，因为它会匹配尽可能少的字符
# result = re.match('^Hello.*?(\d+).*Demo$', content)
# print(result.group(1))

# content = 'http://weibo.com/comment/kEraCN'
# r1 = re.match('http.*?comment/(.*?)', content)  # 非贪婪
# r2 = re.match('http.*comment/(.*)', content)  # 贪婪
# print(r1.group())
# print(r2.group())

# 错误示范
# content = '''Hello 1234567 World_This
# is a Regex Demo
# '''
# r = re.match('He.*?(\d+).*?Demo', content)
# print(r.group())

# 修饰符  re.S这个修饰符的作用是匹配包括换行符在内的所有字符。
# content = '''Hello 1234567 World_This
# is a Regex Demo
# '''
#
# r = re.match('He.*?(\d+).*?Demo', content, re.S)
# print(r.group())

# 修饰符	描　　述
# re.I	使匹配对大小写不敏感
# re.L	做本地化识别（locale-aware）匹配
# re.M	多行匹配，影响 ^ 和 $
# re.S	使匹配包括换行在内的所有字符
# re.U	根据 Unicode 字符集解析字符。这个标志影响 \w、\W、\b 和 \B
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解


# 转义匹配
# content = '(百度) www.baidu.com'
# # 当遇到用于正则匹配模式的特殊字符时，在前面加反斜线转义一下即可。例 . 就可以用 \. 来匹配。
# result = re.match('\(百度\) www\.baidu\.com', content)
# print(result)


# search
# 前面提到过，match 方法是从字符串的开头开始匹配的，一旦开头不匹配，那么整个匹配就失败了。
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# r = re.search('He.*World_This', content)
# print(r.group())


html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

# r = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# if r:
#     print(r.group(1), r.group(2))

# 匹配没有加换行符的
# r = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
# if r:
#     print(r.group(1), r.group(2))

# 前面我们介绍了 search 方法的用法，它可以返回匹配正则表达式的第一个内容，但是如果想要获取匹配正则表达式的所有内容，那该怎么办呢？这时就要借助 findall 方法了。
# r = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(type(r))
# if r:
#     for x in r:
#         print(x)
#         print(x[0], x[1], x[2])

# 字符串替换,把所有数字替换掉
# content = "fef8df7fejfl13u7feejkli9fe0fe"
# r = re.sub("\d", "", content)
# print(r)

# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
# print(results)
# print(type(results))
# for result in results:
#     print(result[1])

# 去掉a节点
# html = re.sub('<a.*?>|</a>', '', html)
# # print(html)
# rs = re.findall('<li.*?>(.*?)</li>', html, re.S)
# for r in rs:
#     print(r.strip())

# 复用正则表达式
content1 = '2019-12-15 12:00'
content2 = '2019-12-17 12:55'
content3 = '2019-12-22 13:21'
pattern = re.compile("\d{2}:\d{2}")
r1 = re.search(pattern, content1)
r2 = re.search(pattern, content2)
r3 = re.search(pattern, content3)
print(r1.group(), r2.group(), r3.group())
