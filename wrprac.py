# import matplotlib.font_manager as fm
#
# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)


# f = open("test.txt", "w", encoding="utf-8")
# f.write("안녕, 스파르타!\n")
#
# for i in [1,2,3,4,5]:
#     f.write(f"{i}번째 줄이예요\n")
# f.close()

from wordcloud import WordCloud

text = ""
with open("KakaoTalk_Chat_.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        text += line.split(',')[2].replace('ㅋ','').replace('ㅠ','')\
            .replace('Emoticon\n', '').replace('Photo\n', '').replace('photos\n', '')\
            .replace('This message was deleted.', '')
        #print(line)
#print(text)

# wc = WordCloud(font_path='/System/Library/Fonts/AppleSDGothicNeo.ttc', background_color="white", width=600, height=400)
# wc.generate(text)
# wc.to_file("result.png")

from PIL import Image
import numpy as np

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='/System/Library/Fonts/AppleSDGothicNeo.ttc', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")



