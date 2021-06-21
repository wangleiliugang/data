from bs4 import BeautifulSoup


doc = ['<html><head><title>page title</title></head>',
'<body><p id="firstpara" align="center">this is paragraph <b>one</b></p>',
'<p id="secondpara" align="blah">this is paragraph <b>two</b></p></body>',
'</html>']


# 指定解析器为:html.parser
soup = BeautifulSoup(''.join(doc), "html.parser")
print(type(soup))
print(soup.prettify())

html = soup.contents[0]
print(html.name)  # tag name
head = soup.contents[0].contents[0]
print(head.name)
body = soup.contents[0].contents[1]
print(body.name)


items = soup.findAll('p', align="center")
print(type(items))
for i in items:
    print(i.text)

items1 = soup.findAll('p', id="secondpara")
print(items1[0].text)

items2 = soup.findAll('b')
print(items2[1].text)
