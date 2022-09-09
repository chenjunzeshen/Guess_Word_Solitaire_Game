# 利用ERNIE-ViLG为每个名词生成图像
import wenxin_api
from wenxin_api.tasks.text_to_image import TextToImage
wenxin_api.ak = "" # 输入您的API Key
wenxin_api.sk = "" # 输入您的Secret Key

def get_create_pic_url(keyword):
    input_dict = {
        "text": keyword,
        "style": "卡通"
    }
    rst = TextToImage.create(**input_dict)
    img_url = rst['imgUrls'][0] # 保存生成的第一张图片
    return img_url


if __name__ == '__main__':
    keyword = "黑夜总会过去"
    try:
        resule = get_create_pic_url(keyword)
    except:
        print("存在敏感词")
    print("*" * 50)
    print(resule)
    print("*" * 50)