import jieba
from wordcloud import WordCloud
import os
import numpy
import PIL.Image as Image

cur_path = os.path.dirname(__file__)

def chinese_jieba(txt):
    wordlist_jieba = jieba.cut(txt) # 将文本分割，返回列表
    txt_jieba = " ".join(wordlist_jieba) # 将列表拼接为以空格为间断的字符串
    return txt_jieba

stopwords = {'这些':0, '那些':0, '因为':0, '所以':0} # 噪声词
mask_pic = numpy.array(Image.open(os.path.join(cur_path, 'love.jpg')))

def create_pic():
    with open(os.path.join(cur_path, "DataAnalyst.csv")) as fp:
        txt = fp.read()
        txt = chinese_jieba(txt)
        # print(txt)
        wordcloud = WordCloud(font_path = 'SimHei.ttf', # 字体
                              background_color = 'white', # 背景色
                              max_words = 100, # 最大显示单词数
                              max_font_size = 60, # 频率最大单词字体大小
                              stopwords = stopwords, # 过滤噪声词
                              mask = mask_pic # 自定义显示的效果图
                            ).generate(txt)
        image = wordcloud.to_image()
    return image

if __name__ == '__main__':
    image=create_pic();
    image.show()