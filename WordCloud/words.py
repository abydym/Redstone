import jieba
import wordcloud as wc
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib import colors
with open("words.txt", "r", encoding="utf-8") as f: # 词放在对应文件里
    str = f.read()

list_str = jieba.lcut(str)  # 分词列表
text = " ".join(list_str)  # 连接成字符串

cover = Image.open("xincai.jpeg") #词云图覆盖在某张图片上，所选的图片放在这里
mask = np.array(cover) # 导入图片并转化为array

color_list = ["#AD0004"]
colormap = colors.ListedColormap(color_list)

stopwords = {} # 去掉的stopwords，这里放不想显示在词云图里的字、词

wc = wc.WordCloud(
    font_path = "fzqk.ttf", #字体
    background_color="black",
    stopwords=stopwords,
    max_words=200, # 最大的词数量
    mask=mask,
    max_font_size=240, # 最大的字体大小
    font_step=1,
    colormap=colormap,

)
wc.generate(text)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

wc.to_file("words_generate1.jpg") #生成图片的文件名