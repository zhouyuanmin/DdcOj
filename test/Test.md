code，answer，scores 都是encode,再b64encode

运行下面的代码，可以输出编码后的 code，answer，scores

```
import base64

# code 需要encode,再b64encode
code = """import wordcloud
c = wordcloud.WordCloud()
txt = 'I have a good friend, and her name is Li Hua. We have become friends for about two years. She is very kind. When I step into the classroom for the first time, she helps me to get familiar with the strange environment. The most important thing is that we share the same interest, so we have a lot in common. '
c = c.generate(txt)
img = c.to_image()
print(123)
# img.show()"""
code = base64.b64encode(code.encode('u8'))
print(code)
# answer 需要encode,再b64encode
answer = {
    'words': {'good': 1, 'friend': 2, 'name': 1, 'Li': 1, 'Hua': 1, 'become': 1, 'two': 1, 'years': 1,
              'kind': 1,
              'step': 1, 'classroom': 1, 'first': 1, 'time': 1, 'helps': 1, 'familiar': 1, 'strange': 1,
              'environment': 1, 'important': 1, 'thing': 1, 'share': 1, 'interest': 1, 'lot': 1, 'common': 1},
    'width': 400,
    'height': 200,
    'min_font_size': 4,
    'max_font_size': 26,
    'font_step': 1,
    'font_path': 'DroidSansMono.ttf',
    'max_words': 200,
    'stopwords': ['what', "i'll", "won't", 'than', 'same', 'at', "they'll", "there's", 'should', 'through',
                  'was',
                  'for', 'else', 'while', "they've", 'own', 'if', 'has', 'most', 'there', 'or', 'the', 'hers',
                  'during', "that's", "they'd", 'as', 'com', "how's", 'him', "what's", 'yourself', 'he',
                  "hadn't",
                  "shouldn't", 'few', 'under', "he'd", 'all', 'myself', 'once', "we're", 'your', 'shall', 'an',
                  'r',
                  "mustn't", "i'd", 'with', 'ours', 'such', 'which', "who's", 'about', 'she', 'whom', 'since',
                  'where', 'yourselves', 'down', 'some', 'below', "we've", 'from', 'its', 'to', 'am', 'just',
                  'above', "you're", "let's", 'me', "she's", 'not', 'too', 'both', 'very', 'any', 'like',
                  'against',
                  'then', 'over', 'ever', 'are', 'who', 'also', 'by', "you'd", 'our', 'nor', 'of', 'between',
                  'out',
                  "wouldn't", 'why', 'does', "doesn't", 'his', 'each', 'would', 'on', 'itself', 'ought',
                  'therefore', 'how', 'more', "hasn't", "he's", 'get', 'is', 'but', 'here', 'further', "we'd",
                  'only', 'http', 'do', 'yours', 'her', "they're", 'until', 'however', 'himself', 'be', 'could',
                  "she'd", 'a', 'it', 'them', "why's", 'www', 'up', 'other', 'themselves', "he'll", 'this',
                  'so',
                  'they', "don't", 'their', 'being', 'into', 'after', "where's", "shan't", 'because', 'have',
                  'my',
                  'again', "couldn't", 'off', 'in', 'we', 'having', "isn't", "i'm", 'ourselves', "it's", 'you',
                  "wasn't", "i've", "you'll", 'were', "when's", 'had', 'cannot', 'i', "haven't", 'those',
                  "aren't",
                  'no', 'hence', 'been', 'k', "here's", "didn't", 'before', "we'll", 'doing', "weren't",
                  'herself',
                  'did', 'can', 'that', 'and', 'theirs', "can't", 'otherwise', "you've", "she'll", 'these',
                  'when'],
    'mask': '6adf97f83acf6453d4a6a4b1070f3754',
    'background_color': 'black'
}
answer = base64.b64encode(str(answer).encode('u8'))
print(answer)

# scores 需要encode,再b64encode
scores = {
    'words': 5,
    'width': 5,
    'height': 10,
    'min_font_size': 10,
    'max_font_size': 10,
    'font_step': 10,
    'font_path': 10,
    'max_words': 10,
    'stopwords': 10,
    'mask': 10,
    'background_color': 10
}
scores = base64.b64encode(str(scores).encode('u8'))
print(scores)
```

词云测试例子

```
python /usr/lib/DdcOj/wordcloud_test.py --data=aW1wb3J0IHdvcmRjbG91ZApjID0gd29yZGNsb3VkLldvcmRDbG91ZCgpCnR4dCA9ICdJIGhhdmUgYSBnb29kIGZyaWVuZCwgYW5kIGhlciBuYW1lIGlzIExpIEh1YS4gV2UgaGF2ZSBiZWNvbWUgZnJpZW5kcyBmb3IgYWJvdXQgdHdvIHllYXJzLiBTaGUgaXMgdmVyeSBraW5kLiBXaGVuIEkgc3RlcCBpbnRvIHRoZSBjbGFzc3Jvb20gZm9yIHRoZSBmaXJzdCB0aW1lLCBzaGUgaGVscHMgbWUgdG8gZ2V0IGZhbWlsaWFyIHdpdGggdGhlIHN0cmFuZ2UgZW52aXJvbm1lbnQuIFRoZSBtb3N0IGltcG9ydGFudCB0aGluZyBpcyB0aGF0IHdlIHNoYXJlIHRoZSBzYW1lIGludGVyZXN0LCBzbyB3ZSBoYXZlIGEgbG90IGluIGNvbW1vbi4gJwpjID0gYy5nZW5lcmF0ZSh0eHQpCmltZyA9IGMudG9faW1hZ2UoKQpwcmludCgxMjMpCiMgaW1nLnNob3coKQ== --answer=eyd3b3Jkcyc6IHsnZ29vZCc6IDEsICdmcmllbmQnOiAyLCAnbmFtZSc6IDEsICdMaSc6IDEsICdIdWEnOiAxLCAnYmVjb21lJzogMSwgJ3R3byc6IDEsICd5ZWFycyc6IDEsICdraW5kJzogMSwgJ3N0ZXAnOiAxLCAnY2xhc3Nyb29tJzogMSwgJ2ZpcnN0JzogMSwgJ3RpbWUnOiAxLCAnaGVscHMnOiAxLCAnZmFtaWxpYXInOiAxLCAnc3RyYW5nZSc6IDEsICdlbnZpcm9ubWVudCc6IDEsICdpbXBvcnRhbnQnOiAxLCAndGhpbmcnOiAxLCAnc2hhcmUnOiAxLCAnaW50ZXJlc3QnOiAxLCAnbG90JzogMSwgJ2NvbW1vbic6IDF9LCAnd2lkdGgnOiA0MDAsICdoZWlnaHQnOiAyMDAsICdtaW5fZm9udF9zaXplJzogNCwgJ21heF9mb250X3NpemUnOiAyNiwgJ2ZvbnRfc3RlcCc6IDEsICdmb250X3BhdGgnOiAnRHJvaWRTYW5zTW9uby50dGYnLCAnbWF4X3dvcmRzJzogMjAwLCAnc3RvcHdvcmRzJzogWyd3aGF0JywgImknbGwiLCAid29uJ3QiLCAndGhhbicsICdzYW1lJywgJ2F0JywgInRoZXknbGwiLCAidGhlcmUncyIsICdzaG91bGQnLCAndGhyb3VnaCcsICd3YXMnLCAnZm9yJywgJ2Vsc2UnLCAnd2hpbGUnLCAidGhleSd2ZSIsICdvd24nLCAnaWYnLCAnaGFzJywgJ21vc3QnLCAndGhlcmUnLCAnb3InLCAndGhlJywgJ2hlcnMnLCAnZHVyaW5nJywgInRoYXQncyIsICJ0aGV5J2QiLCAnYXMnLCAnY29tJywgImhvdydzIiwgJ2hpbScsICJ3aGF0J3MiLCAneW91cnNlbGYnLCAnaGUnLCAiaGFkbid0IiwgInNob3VsZG4ndCIsICdmZXcnLCAndW5kZXInLCAiaGUnZCIsICdhbGwnLCAnbXlzZWxmJywgJ29uY2UnLCAid2UncmUiLCAneW91cicsICdzaGFsbCcsICdhbicsICdyJywgIm11c3RuJ3QiLCAiaSdkIiwgJ3dpdGgnLCAnb3VycycsICdzdWNoJywgJ3doaWNoJywgIndobydzIiwgJ2Fib3V0JywgJ3NoZScsICd3aG9tJywgJ3NpbmNlJywgJ3doZXJlJywgJ3lvdXJzZWx2ZXMnLCAnZG93bicsICdzb21lJywgJ2JlbG93JywgIndlJ3ZlIiwgJ2Zyb20nLCAnaXRzJywgJ3RvJywgJ2FtJywgJ2p1c3QnLCAnYWJvdmUnLCAieW91J3JlIiwgImxldCdzIiwgJ21lJywgInNoZSdzIiwgJ25vdCcsICd0b28nLCAnYm90aCcsICd2ZXJ5JywgJ2FueScsICdsaWtlJywgJ2FnYWluc3QnLCAndGhlbicsICdvdmVyJywgJ2V2ZXInLCAnYXJlJywgJ3dobycsICdhbHNvJywgJ2J5JywgInlvdSdkIiwgJ291cicsICdub3InLCAnb2YnLCAnYmV0d2VlbicsICdvdXQnLCAid291bGRuJ3QiLCAnd2h5JywgJ2RvZXMnLCAiZG9lc24ndCIsICdoaXMnLCAnZWFjaCcsICd3b3VsZCcsICdvbicsICdpdHNlbGYnLCAnb3VnaHQnLCAndGhlcmVmb3JlJywgJ2hvdycsICdtb3JlJywgImhhc24ndCIsICJoZSdzIiwgJ2dldCcsICdpcycsICdidXQnLCAnaGVyZScsICdmdXJ0aGVyJywgIndlJ2QiLCAnb25seScsICdodHRwJywgJ2RvJywgJ3lvdXJzJywgJ2hlcicsICJ0aGV5J3JlIiwgJ3VudGlsJywgJ2hvd2V2ZXInLCAnaGltc2VsZicsICdiZScsICdjb3VsZCcsICJzaGUnZCIsICdhJywgJ2l0JywgJ3RoZW0nLCAid2h5J3MiLCAnd3d3JywgJ3VwJywgJ290aGVyJywgJ3RoZW1zZWx2ZXMnLCAiaGUnbGwiLCAndGhpcycsICdzbycsICd0aGV5JywgImRvbid0IiwgJ3RoZWlyJywgJ2JlaW5nJywgJ2ludG8nLCAnYWZ0ZXInLCAid2hlcmUncyIsICJzaGFuJ3QiLCAnYmVjYXVzZScsICdoYXZlJywgJ215JywgJ2FnYWluJywgImNvdWxkbid0IiwgJ29mZicsICdpbicsICd3ZScsICdoYXZpbmcnLCAiaXNuJ3QiLCAiaSdtIiwgJ291cnNlbHZlcycsICJpdCdzIiwgJ3lvdScsICJ3YXNuJ3QiLCAiaSd2ZSIsICJ5b3UnbGwiLCAnd2VyZScsICJ3aGVuJ3MiLCAnaGFkJywgJ2Nhbm5vdCcsICdpJywgImhhdmVuJ3QiLCAndGhvc2UnLCAiYXJlbid0IiwgJ25vJywgJ2hlbmNlJywgJ2JlZW4nLCAnaycsICJoZXJlJ3MiLCAiZGlkbid0IiwgJ2JlZm9yZScsICJ3ZSdsbCIsICdkb2luZycsICJ3ZXJlbid0IiwgJ2hlcnNlbGYnLCAnZGlkJywgJ2NhbicsICd0aGF0JywgJ2FuZCcsICd0aGVpcnMnLCAiY2FuJ3QiLCAnb3RoZXJ3aXNlJywgInlvdSd2ZSIsICJzaGUnbGwiLCAndGhlc2UnLCAnd2hlbiddLCAnbWFzayc6ICc2YWRmOTdmODNhY2Y2NDUzZDRhNmE0YjEwNzBmMzc1NCcsICdiYWNrZ3JvdW5kX2NvbG9yJzogJ2JsYWNrJ30= --scores=eyd3b3Jkcyc6IDUsICd3aWR0aCc6IDUsICdoZWlnaHQnOiAxMCwgJ21pbl9mb250X3NpemUnOiAxMCwgJ21heF9mb250X3NpemUnOiAxMCwgJ2ZvbnRfc3RlcCc6IDEwLCAnZm9udF9wYXRoJzogMTAsICdtYXhfd29yZHMnOiAxMCwgJ3N0b3B3b3Jkcyc6IDEwLCAnbWFzayc6IDEwLCAnYmFja2dyb3VuZF9jb2xvcic6IDEwfQ==
```
mat绘图测试例子
```
python /usr/lib/DdcOj/matplotlib_test.py --data=CmZyb20gbWF0cGxvdGxpYiBpbXBvcnQgcHlwbG90IGFzIHBsdApmcm9tIHJhbmRvbSBpbXBvcnQgY2hvaWNlCgoKY2xhc3MgUmFuZG9tV2FsayhvYmplY3QpOgogICAgZGVmIF9faW5pdF9fKHNlbGYsIG51bV9wb2ludHM9NTAwMCk6CiAgICAgICAgc2VsZi5udW1fcG9pbnRzID0gbnVtX3BvaW50cyAgIyDlnZDmoIfngrnnmoTkuKrmlbAKICAgICAgICBzZWxmLnhfdmFsdWVzID0gWzBdICAjIHjlnZDmoIcKICAgICAgICBzZWxmLnlfdmFsdWVzID0gWzBdICAjIHnlnZDmoIcKCiAgICBkZWYgZmlsbF93YWxrKHNlbGYpOgogICAgICAgIHdoaWxlIGxlbihzZWxmLnhfdmFsdWVzKSA8IHNlbGYubnVtX3BvaW50czoKICAgICAgICAgICAgIyDmlrnlkJEKICAgICAgICAgICAgeF9kaXJlY3Rpb24gPSBjaG9pY2UoWzEsIC0xXSkKICAgICAgICAgICAgeV9kaXJlY3Rpb24gPSBjaG9pY2UoWzEsIC0xXSkKICAgICAgICAgICAgIyDot53nprsKICAgICAgICAgICAgeF9kaXN0YW5jZSA9IGNob2ljZShbMCwgMSwgMiwgMywgNF0pCiAgICAgICAgICAgIHlfZGlzdGFuY2UgPSBjaG9pY2UoWzAsIDEsIDIsIDMsIDRdKQoKICAgICAgICAgICAgaWYgeF9kaXN0YW5jZSAhPSAwIG9yIHlfZGlzdGFuY2UgIT0gMDoKICAgICAgICAgICAgICAgICMg5LiL5LiA5Liq54K555qE5Z2Q5qCHCiAgICAgICAgICAgICAgICBuZXh0X3ggPSBzZWxmLnhfdmFsdWVzWy0xXSArIHhfZGlyZWN0aW9uICogeF9kaXN0YW5jZQogICAgICAgICAgICAgICAgbmV4dF95ID0gc2VsZi55X3ZhbHVlc1stMV0gKyB5X2RpcmVjdGlvbiAqIHlfZGlzdGFuY2UKCiAgICAgICAgICAgICAgICAjIOWwhuWdkOagh+eCuea3u+WKoOWIsOWxnuaAp+S4rQogICAgICAgICAgICAgICAgc2VsZi54X3ZhbHVlcy5hcHBlbmQobmV4dF94KQogICAgICAgICAgICAgICAgc2VsZi55X3ZhbHVlcy5hcHBlbmQobmV4dF95KQoKCnBsdC5maWd1cmUoKQpydyA9IFJhbmRvbVdhbGsoNTAwMCkKcncuZmlsbF93YWxrKCkKYSA9IHBsdC5zY2F0dGVyKHJ3LnhfdmFsdWVzLCBydy55X3ZhbHVlcywgcz0xNSkKcGx0LnNob3coKQogICAg --answer=eyd4JzogJzNmNzJlYjUzNTRmNjJlYzc0MDMzYTRkNjc0YzUyZDliJywgJ3knOiAnMTUyMTIyZTE3MjY3NzVlYTNkYTAyYjc0YzkwYzEwNjYnfQ== --scores=eyd4JzogNTAsICd5JzogNTB9
```

### 增加测试

matplotlib没有注释show

```
python /usr/lib/DdcOj/matplotlib_test.py --data=CmZyb20gbWF0cGxvdGxpYiBpbXBvcnQgcHlwbG90IGFzIHBsdApmcm9tIHJhbmRvbSBpbXBvcnQgY2hvaWNlCgoKY2xhc3MgUmFuZG9tV2FsayhvYmplY3QpOgogICAgZGVmIF9faW5pdF9fKHNlbGYsIG51bV9wb2ludHM9NTAwMCk6CiAgICAgICAgc2VsZi5udW1fcG9pbnRzID0gbnVtX3BvaW50cyAgIyDlnZDmoIfngrnnmoTkuKrmlbAKICAgICAgICBzZWxmLnhfdmFsdWVzID0gWzBdICAjIHjlnZDmoIcKICAgICAgICBzZWxmLnlfdmFsdWVzID0gWzBdICAjIHnlnZDmoIcKCiAgICBkZWYgZmlsbF93YWxrKHNlbGYpOgogICAgICAgIHdoaWxlIGxlbihzZWxmLnhfdmFsdWVzKSA8IHNlbGYubnVtX3BvaW50czoKICAgICAgICAgICAgIyDmlrnlkJEKICAgICAgICAgICAgeF9kaXJlY3Rpb24gPSBjaG9pY2UoWzEsIC0xXSkKICAgICAgICAgICAgeV9kaXJlY3Rpb24gPSBjaG9pY2UoWzEsIC0xXSkKICAgICAgICAgICAgIyDot53nprsKICAgICAgICAgICAgeF9kaXN0YW5jZSA9IGNob2ljZShbMCwgMSwgMiwgMywgNF0pCiAgICAgICAgICAgIHlfZGlzdGFuY2UgPSBjaG9pY2UoWzAsIDEsIDIsIDMsIDRdKQoKICAgICAgICAgICAgaWYgeF9kaXN0YW5jZSAhPSAwIG9yIHlfZGlzdGFuY2UgIT0gMDoKICAgICAgICAgICAgICAgICMg5LiL5LiA5Liq54K555qE5Z2Q5qCHCiAgICAgICAgICAgICAgICBuZXh0X3ggPSBzZWxmLnhfdmFsdWVzWy0xXSArIHhfZGlyZWN0aW9uICogeF9kaXN0YW5jZQogICAgICAgICAgICAgICAgbmV4dF95ID0gc2VsZi55X3ZhbHVlc1stMV0gKyB5X2RpcmVjdGlvbiAqIHlfZGlzdGFuY2UKCiAgICAgICAgICAgICAgICAjIOWwhuWdkOagh+eCuea3u+WKoOWIsOWxnuaAp+S4rQogICAgICAgICAgICAgICAgc2VsZi54X3ZhbHVlcy5hcHBlbmQobmV4dF94KQogICAgICAgICAgICAgICAgc2VsZi55X3ZhbHVlcy5hcHBlbmQobmV4dF95KQoKCnBsdC5maWd1cmUoKQpydyA9IFJhbmRvbVdhbGsoNTAwMCkKcncuZmlsbF93YWxrKCkKYSA9IHBsdC5zY2F0dGVyKHJ3LnhfdmFsdWVzLCBydy55X3ZhbHVlcywgcz0xNSkKcGx0LnNob3coKQogICAg --answer=eyd4JzogJzNmNzJlYjUzNTRmNjJlYzc0MDMzYTRkNjc0YzUyZDliJywgJ3knOiAnMTUyMTIyZTE3MjY3NzVlYTNkYTAyYjc0YzkwYzEwNjYnfQ== --scores=eyd4JzogNTAsICd5JzogNTB9
```

wordcloud没有注释show

```
python /usr/lib/DdcOj/wordcloud_test.py --data=CmltcG9ydCB3b3JkY2xvdWQKYyA9IHdvcmRjbG91ZC5Xb3JkQ2xvdWQoKQp0eHQgPSAnSSBoYXZlIGEgZ29vZCBmcmllbmQsIGFuZCBoZXIgbmFtZSBpcyBMaSBIdWEuIFdlIGhhdmUgYmVjb21lIGZyaWVuZHMgZm9yIGFib3V0IHR3byB5ZWFycy4gU2hlIGlzIHZlcnkga2luZC4gV2hlbiBJIHN0ZXAgaW50byB0aGUgY2xhc3Nyb29tIGZvciB0aGUgZmlyc3QgdGltZSwgc2hlIGhlbHBzIG1lIHRvIGdldCBmYW1pbGlhciB3aXRoIHRoZSBzdHJhbmdlIGVudmlyb25tZW50LiBUaGUgbW9zdCBpbXBvcnRhbnQgdGhpbmcgaXMgdGhhdCB3ZSBzaGFyZSB0aGUgc2FtZSBpbnRlcmVzdCwgc28gd2UgaGF2ZSBhIGxvdCBpbiBjb21tb24uICcKYyA9IGMuZ2VuZXJhdGUodHh0KQppbWcgPSBjLnRvX2ltYWdlKCkKcHJpbnQoMTIzKQppbWcuc2hvdygp --answer=eyd3b3Jkcyc6IHsnZ29vZCc6IDEsICdmcmllbmQnOiAyLCAnbmFtZSc6IDEsICdMaSc6IDEsICdIdWEnOiAxLCAnYmVjb21lJzogMSwgJ3R3byc6IDEsICd5ZWFycyc6IDEsICdraW5kJzogMSwgJ3N0ZXAnOiAxLCAnY2xhc3Nyb29tJzogMSwgJ2ZpcnN0JzogMSwgJ3RpbWUnOiAxLCAnaGVscHMnOiAxLCAnZmFtaWxpYXInOiAxLCAnc3RyYW5nZSc6IDEsICdlbnZpcm9ubWVudCc6IDEsICdpbXBvcnRhbnQnOiAxLCAndGhpbmcnOiAxLCAnc2hhcmUnOiAxLCAnaW50ZXJlc3QnOiAxLCAnbG90JzogMSwgJ2NvbW1vbic6IDF9LCAnd2lkdGgnOiA0MDAsICdoZWlnaHQnOiAyMDAsICdtaW5fZm9udF9zaXplJzogNCwgJ21heF9mb250X3NpemUnOiAyNiwgJ2ZvbnRfc3RlcCc6IDEsICdmb250X3BhdGgnOiAnRHJvaWRTYW5zTW9uby50dGYnLCAnbWF4X3dvcmRzJzogMjAwLCAnc3RvcHdvcmRzJzogWyd3aGF0JywgImknbGwiLCAid29uJ3QiLCAndGhhbicsICdzYW1lJywgJ2F0JywgInRoZXknbGwiLCAidGhlcmUncyIsICdzaG91bGQnLCAndGhyb3VnaCcsICd3YXMnLCAnZm9yJywgJ2Vsc2UnLCAnd2hpbGUnLCAidGhleSd2ZSIsICdvd24nLCAnaWYnLCAnaGFzJywgJ21vc3QnLCAndGhlcmUnLCAnb3InLCAndGhlJywgJ2hlcnMnLCAnZHVyaW5nJywgInRoYXQncyIsICJ0aGV5J2QiLCAnYXMnLCAnY29tJywgImhvdydzIiwgJ2hpbScsICJ3aGF0J3MiLCAneW91cnNlbGYnLCAnaGUnLCAiaGFkbid0IiwgInNob3VsZG4ndCIsICdmZXcnLCAndW5kZXInLCAiaGUnZCIsICdhbGwnLCAnbXlzZWxmJywgJ29uY2UnLCAid2UncmUiLCAneW91cicsICdzaGFsbCcsICdhbicsICdyJywgIm11c3RuJ3QiLCAiaSdkIiwgJ3dpdGgnLCAnb3VycycsICdzdWNoJywgJ3doaWNoJywgIndobydzIiwgJ2Fib3V0JywgJ3NoZScsICd3aG9tJywgJ3NpbmNlJywgJ3doZXJlJywgJ3lvdXJzZWx2ZXMnLCAnZG93bicsICdzb21lJywgJ2JlbG93JywgIndlJ3ZlIiwgJ2Zyb20nLCAnaXRzJywgJ3RvJywgJ2FtJywgJ2p1c3QnLCAnYWJvdmUnLCAieW91J3JlIiwgImxldCdzIiwgJ21lJywgInNoZSdzIiwgJ25vdCcsICd0b28nLCAnYm90aCcsICd2ZXJ5JywgJ2FueScsICdsaWtlJywgJ2FnYWluc3QnLCAndGhlbicsICdvdmVyJywgJ2V2ZXInLCAnYXJlJywgJ3dobycsICdhbHNvJywgJ2J5JywgInlvdSdkIiwgJ291cicsICdub3InLCAnb2YnLCAnYmV0d2VlbicsICdvdXQnLCAid291bGRuJ3QiLCAnd2h5JywgJ2RvZXMnLCAiZG9lc24ndCIsICdoaXMnLCAnZWFjaCcsICd3b3VsZCcsICdvbicsICdpdHNlbGYnLCAnb3VnaHQnLCAndGhlcmVmb3JlJywgJ2hvdycsICdtb3JlJywgImhhc24ndCIsICJoZSdzIiwgJ2dldCcsICdpcycsICdidXQnLCAnaGVyZScsICdmdXJ0aGVyJywgIndlJ2QiLCAnb25seScsICdodHRwJywgJ2RvJywgJ3lvdXJzJywgJ2hlcicsICJ0aGV5J3JlIiwgJ3VudGlsJywgJ2hvd2V2ZXInLCAnaGltc2VsZicsICdiZScsICdjb3VsZCcsICJzaGUnZCIsICdhJywgJ2l0JywgJ3RoZW0nLCAid2h5J3MiLCAnd3d3JywgJ3VwJywgJ290aGVyJywgJ3RoZW1zZWx2ZXMnLCAiaGUnbGwiLCAndGhpcycsICdzbycsICd0aGV5JywgImRvbid0IiwgJ3RoZWlyJywgJ2JlaW5nJywgJ2ludG8nLCAnYWZ0ZXInLCAid2hlcmUncyIsICJzaGFuJ3QiLCAnYmVjYXVzZScsICdoYXZlJywgJ215JywgJ2FnYWluJywgImNvdWxkbid0IiwgJ29mZicsICdpbicsICd3ZScsICdoYXZpbmcnLCAiaXNuJ3QiLCAiaSdtIiwgJ291cnNlbHZlcycsICJpdCdzIiwgJ3lvdScsICJ3YXNuJ3QiLCAiaSd2ZSIsICJ5b3UnbGwiLCAnd2VyZScsICJ3aGVuJ3MiLCAnaGFkJywgJ2Nhbm5vdCcsICdpJywgImhhdmVuJ3QiLCAndGhvc2UnLCAiYXJlbid0IiwgJ25vJywgJ2hlbmNlJywgJ2JlZW4nLCAnaycsICJoZXJlJ3MiLCAiZGlkbid0IiwgJ2JlZm9yZScsICJ3ZSdsbCIsICdkb2luZycsICJ3ZXJlbid0IiwgJ2hlcnNlbGYnLCAnZGlkJywgJ2NhbicsICd0aGF0JywgJ2FuZCcsICd0aGVpcnMnLCAiY2FuJ3QiLCAnb3RoZXJ3aXNlJywgInlvdSd2ZSIsICJzaGUnbGwiLCAndGhlc2UnLCAnd2hlbiddLCAnbWFzayc6ICc2YWRmOTdmODNhY2Y2NDUzZDRhNmE0YjEwNzBmMzc1NCcsICdiYWNrZ3JvdW5kX2NvbG9yJzogJ2JsYWNrJ30= --scores=eyd3b3Jkcyc6IDUsICd3aWR0aCc6IDUsICdoZWlnaHQnOiAxMCwgJ21pbl9mb250X3NpemUnOiAxMCwgJ21heF9mb250X3NpemUnOiAxMCwgJ2ZvbnRfc3RlcCc6IDEwLCAnZm9udF9wYXRoJzogMTAsICdtYXhfd29yZHMnOiAxMCwgJ3N0b3B3b3Jkcyc6IDEwLCAnbWFzayc6IDEwLCAnYmFja2dyb3VuZF9jb2xvcic6IDEwfQ==
```

词云、字体

```
python /usr/lib/DdcOj/wordcloud_test.py --data=CmltcG9ydCB3b3JkY2xvdWQKaW1wb3J0IGppZWJhCgp3b3JkcyA9IFsn5Zug5Li6Jywn5omA5LulJywn6L+Z5qyhJywn5LiA5LiqJywn5b6I5b+rJywn5pyJ5LqbJ10KYyA9IHdvcmRjbG91ZC5Xb3JkQ2xvdWQoCiAgICBmb250X3BhdGggPSAn5bm85ZyGLnR0ZicsCiAgICB3aWR0aCA9IDUwMCwKICAgIGhlaWdodCA9IDMwMCwKICAgIG1heF93b3JkcyA9IDMwLAogICAgc3RvcHdvcmRzID0gd29yZHMKICAgICkKdHh0ID0gIui/measoeaOouWutuaIkeWPquaPkOS4gOS4quWwj+WMheOAguaJgOS7pei1sOW+l+W+iOW/q+OAguepv+i/h+mTgei3r+ahpea0nuWQju+8jOaIkeayoei1sOafj+ayuei3r+OAguWboOS4uuafj+ayueWFrOi3r+aLkOebtOinku+8jOimgei/nOWlveWkmuOAguaIkeaWnOWIuuWEv+mHjOi1sOS4iumCo+adoeW6n+W8g+aVsOW5tOeahOaWnOaPkuWIsOmrmOWvhuS4nOWMl+S5oeWOu+eahOWcn+i3r+OAguWcn+i3r+WboOS4uui/keW5tOadpeacieS6m+WcsOaWueiiq+aMluaWreS6huOAguihjOS6uueogOWwke+8jOaJgOS7pei3r+mdouS4iuadguiNieS4m+eUn++8jOWPquaYr+WcqOi3r+S4reW/g+i/mOacieS4gOe6v+iiq+S6uui4qei/h+eahOeXlei/ueOAgui3r+S4pOi+ueWFqOaYr+W6hOeovOWcsO+8jOaciemrmOeyseWcsOOAgeeOieexs+WcsOOAgee6ouiWr+WcsOetie+8jOaciOWFieeFp+WcqOW6hOeovOeahOaeneWPtuS4iu+8jOmXqueDgeedgOW+ruW8seeahOmTtuWFieOAguWHoOS5juayoeaciemjju+8jOaJgOacieeahOWPtuWtkOmDvee6ueS4neS4jeWKqO+8jOiNieidiOidiOeahOWPq+WjsOS7juW6hOeovOWcsOmHjOS8oOadpe+8jOmdnuW4uOWTjeS6ru+8jOWlveWDj+i/meWPq+WjsOa4l+i/m+S6huaIkeeahOiCiemHjOOAgemqqOWktOmHjO+8jOidiOidiOeahOWPq+WjsOS9v+aciOWknOaYvuW+l+eJueWIq+ayieWvguOAgiIKbGlzID0gamllYmEubGN1dCh0eHQpCnRleHQgPSAnICcuam9pbihsaXMpCgojICMg5pa55rOVMQojIGMuZ2VuZXJhdGUodGV4dCkKIyBjLnRvX2ZpbGUoJzEuanBnJykKCiMg5pa55rOVMgpzID0gYy5nZW5lcmF0ZSh0ZXh0KQppbWcgPSBzLnRvX2ltYWdlKCkKaW1nLnNob3coKQ== --answer=eyd3b3Jkcyc6IHsn5o6i5a62JzogMSwgJ+Wwj+WMhSc6IDEsICfotbDlvpcnOiAxLCAn56m/6L+HJzogMSwgJ+mTgei3r+ahpSc6IDEsICfmtJ7lkI4nOiAxLCAn5p+P5rK56LevJzogMSwgJ+afj+ayuSc6IDEsICflhazot68nOiAxLCAn55u06KeSJzogMSwgJ+imgei/nCc6IDEsICflpb3lpJonOiAxLCAn5Yi65YS/JzogMSwgJ+i1sOS4iic6IDEsICfpgqPmnaEnOiAxLCAn5bqf5byDJzogMSwgJ+aVsOW5tCc6IDEsICfmlpzmj5InOiAxLCAn6auY5a+GJzogMSwgJ+S4nOWMlyc6IDEsICfkuaHljrsnOiAxLCAn5Zyf6LevJzogMiwgJ+i/keW5tOadpSc6IDEsICflnLDmlrknOiAxLCAn5oyW5patJzogMSwgJ+ihjOS6uic6IDEsICfnqIDlsJEnOiAxLCAn6Lev6Z2iJzogMSwgJ+adguiNieS4m+eUnyc6IDEsICflj6rmmK8nOiAxLCAn5Lit5b+DJzogMSwgJ+i/mOaciSc6IDEsICfkuIDnur8nOiAxLCAn55eV6L+5JzogMSwgJ+S4pOi+uSc6IDEsICflhajmmK8nOiAxLCAn5bqE56i85ZywJzogMiwgJ+mrmOeysSc6IDEsICfnjonnsbPlnLAnOiAxLCAn57qi6JavJzogMSwgJ+WFieeFpyc6IDEsICfluoTnqLwnOiAxLCAn5p6d5Y+2JzogMSwgJ+mXqueDgeedgCc6IDEsICflvq7lvLEnOiAxLCAn6ZO25YWJJzogMSwgJ+WHoOS5jic6IDEsICfmsqHmnIknOiAxLCAn5omA5pyJJzogMSwgJ+WPtuWtkCc6IDEsICfnurnkuJ3kuI3liqgnOiAxLCAn6J2I6J2IJzogMiwgJ+WPq+WjsCc6IDMsICfkvKDmnaUnOiAxLCAn6Z2e5bi4JzogMSwgJ+WTjeS6ric6IDEsICflpb3lg48nOiAxLCAn5riX6L+bJzogMSwgJ+mqqOWktCc6IDEsICfmnIjlpJwnOiAxLCAn5pi+5b6XJzogMSwgJ+eJueWIqyc6IDEsICfmsonlr4InOiAxfSwgJ3dpZHRoJzogNTAwLCAnaGVpZ2h0JzogMzAwLCAnbWluX2ZvbnRfc2l6ZSc6IDQsICdtYXhfZm9udF9zaXplJzogNjYsICdmb250X3N0ZXAnOiAxLCAnZm9udF9wYXRoJzogJ+W5vOWchi50dGYnLCAnbWF4X3dvcmRzJzogMzAsICdzdG9wd29yZHMnOiBbJ+WboOS4uicsICfmiYDku6UnLCAn6L+Z5qyhJywgJ+S4gOS4qicsICflvojlv6snLCAn5pyJ5LqbJ10sICdtYXNrJzogJzZhZGY5N2Y4M2FjZjY0NTNkNGE2YTRiMTA3MGYzNzU0JywgJ2JhY2tncm91bmRfY29sb3InOiAnYmxhY2snfQ== --scores=eyd3b3Jkcyc6IDUsICd3aWR0aCc6IDUsICdoZWlnaHQnOiAxMCwgJ21pbl9mb250X3NpemUnOiAxMCwgJ21heF9mb250X3NpemUnOiAxMCwgJ2ZvbnRfc3RlcCc6IDEwLCAnZm9udF9wYXRoJzogMTAsICdtYXhfd29yZHMnOiAxMCwgJ3N0b3B3b3Jkcyc6IDEwLCAnbWFzayc6IDEwLCAnYmFja2dyb3VuZF9jb2xvcic6IDEwfQ==
```

