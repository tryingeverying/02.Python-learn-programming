# 正则表达式

## 符号意义
![元字符](\F:\Programming\02.Python-learn-programming\1_Automate_the_boring_stuff_with_python\1_note\re_元字符.png)
![量词及贪婪匹配](\F:\Programming\02.Python-learn-programming\1_Automate_the_boring_stuff_with_python\1_note\re_量词.png)
## 利用括号分组
- 分组是从左到右从外向里依次计数

```python{.line-numbers}
target = 'tree/combined 010-12345'
pattern = r'(([^/]*)(/.*)?)[\s]+((\d{3})\-(\d{3,8})$)' # [^]：匹配除了里面列出的任一字符
m = re.match(pattern,target)
print(m.groups())
print(m.group(1))   # 首先匹配最外层的()
print(m.group(2))   # 然后依次匹配里层的()
print(m.group(3))
# 这里匹配到的是 010-12345 
print(m.group(4))   # 同理，从左往右依次匹配，若()里面还有分组就递归下去匹配分组
print(m.group(5))
print(m.group(6))
```

- 输出结果
```python{.line-numbers}
('tree/combined', 'tree', '/combined', '010-12345', '010', '12345')
tree/combined
tree
/combined
010-12345
010
12345
```
## 管道分配

- A|B|C|D
- 类似于布尔表达式里的or 从前往后依次判断，若前面成立则后面的就不判断了
  

## ？实现可选匹配
- ？出现在一个括号的分组后面则代表该分组可选，和非贪婪匹配有区别，如果是？出现在{3,5}后面则表示非贪婪匹配，即按照最少的次数匹配
```python{.line-numbers}
# 可选匹配
>>> batRegex = re.compile(r'Bat(wo)?man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'
>>> mo2 = batRegex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'

# 非贪婪匹配
>>> greedyHaRegex = re.compile(r'(Ha){3,5}')
>>> mo1 = greedyHaRegex.search('HaHaHaHaHa')
>>> mo1.group()
'HaHaHaHaHa'
>>> nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
>>> mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
>>> mo2.group()
'HaHaHa'

```

## +和*
- +代表前面的出现至少一次，至多无数次
- *代表前面的出现至少零次，至多无数次

## search和findall方法对比
- search()返回匹配到的第一个文本
- findall()返回匹配到包含所有文本的字符串列表

## 字符分类
- \d 0到9的任何数字
- \D 非0到9的任何数字
- \w 任何字母、数字或下划线字符
- \W 非任何字母、数字或下划线字符
- \s 空格、制表符或换行符(space tab enter)
- \S 非空格、制表符或换行符(space tab enter)

## ^和$
- 在字符分类的[]前面加上^,就是对该字符分类取非操作
- 在正则表达式的开始使用^则表示该表达式以该内容开头
- 在正则表达式的末尾使用$则表示该表达式以该内容结尾

```python{.line-numbers}
# 取非操作
>>> vowelRegex = re.compile(r'[aeiouAEIOU]')
>>> vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

>>> consonantRegex = re.compile(r'[^aeiouAEIOU]')
>>> consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', '
', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

# 以之开头
>>> beginsWithHello = re.compile(r'^Hello')
>>> beginsWithHello.search('Hello world!')
< _sre.SRE_Match object; span=(0, 5), match='Hello'>
>>> beginsWithHello.search('He said hello.') == None
True

# 以之结尾
>>> endsWithNumber = re.compile(r'\d$')
>>> endsWithNumber.search('Your number is 42')
< _sre.SRE_Match object; span=(16, 17), match='2'>
>>> endsWithNumber.search('Your number is forty two.') == None
True
```

## 正则表达式的第二个参数
- re.VERBOSE 可以上正则表达式多行显示，并且能够添加注释
- re.IGNORECASE 不判断正则表达式的大小写可以简写成re.I
- re.DOTALL 统配字符.可以代表包括enter在内的左右字符
  
```python{.line-numbers}
# re.DOTALL用法
>>> noNewlineRegex = re.compile('.*')
>>> noNewlineRegex.search('Serve the public trust.\nProtect the innocent.
\nUphold the law.').group()
'Serve the public trust.'
>>> newlineRegex = re.compile('.*', re.DOTALL)
>>> newlineRegex.search('Serve the public trust.\nProtect the innocent.
\nUphold the law.').group()
'Serve the public trust.\nProtect the innocent.\nUphold the law.'

# re.IGNORECASE用法,简写成re.I
>>> robocop = re.compile(r'robocop', re.I)
>>> robocop.search('RoboCop is part man, part machine, all cop.').group()
'RoboCop'

# re.VERBOSE用法
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
\d{3} # first 3 digits
(\s|-|\.) # separator
\d{4} # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)
```




































