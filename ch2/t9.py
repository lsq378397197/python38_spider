from pyquery import PyQuery as pq

# html = '''
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# doc = pq(html)
# print(doc('li'))

# doc=pq(url='https://cuiqingcai.com')
# print(doc('title'))

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

# doc = pq(html)
# # print(doc('#container .list li'))
# # print(type(doc('#container .list li')))
# for item in doc('#container .list li').items():
#     print(item.text())

# doc = pq(html)
# items = doc(".list")
# finds = items.find(".item-1")
# print(finds)

doc = pq(html)
items = doc('.list')
# parent是父节点，parents是祖先节点
parents = items.parents()
print(type(parents))
print(parents)
