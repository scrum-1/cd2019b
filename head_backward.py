import re

# 打開檔案取內容
with open('config/content.htm', 'r', encoding="utf-8") as f:
    content = f.read()

rep = {"h1": "h2", "h2": "h3", "h3": "h4"} # define desired replacements here

# use these three lines to do the replacement
# re.escape(k) 在 k 字串中的特殊符號前加上反斜線
# rep.items() returns a list of rep dict's (key, value) tuple pairs
rep = dict((re.escape(k), v) for k, v in rep.items())
pattern = re.compile("|".join(rep.keys()))
#text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
output = pattern.sub(lambda m: rep[re.escape(m.group(0))], content)
# 將 output 前置一頁 h1 後存入 content.htm
output = "<h1>期中報告</h1>" + output
with open('config/content.htm', 'w', encoding="utf-8") as f:
    f.write(output)