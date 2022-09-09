# 猜词接龙

## 介绍：
### 简要介绍：  
玩法与你画我猜相近，又有些不同，通过玩家描述并使用ERNIE_VILG生成图像让下一个玩家猜测，考验玩家脑洞、描述能力与默契度。  
### 流程说明：
从player1~player5共有5位玩家  
player1:玩家1，设计猜测词，发送给玩家2【如：皮卡丘】  
player2:玩家2，尽可能准确描述玩家1的词语，描述中不能出现完整关键词【如：一只萌萌的带着闪电形状尾巴的金黄老鼠】  
（ERNIE_VILG生成玩家2描述的图像，发送首张图像的url给玩家3）  
player3:玩家3，通过ERNIE_VILG生成图像猜测关键词，发送玩家4【如：雷劈黄耗子】  
player4:玩家4，尽可能准确描述玩家3的词语，描述中不能出现完整关键词【如：一只黄老鼠被雷击中】  
（ERNIE_VILG生成玩家4描述的图像，发送首张图像的url给玩家5）  
player5:玩家5，通过ERNIE_VILG生成图像猜测关键词，发送玩家1【如：皮卡丘】  
如果玩家1收到的关键词与设计词相同，则游戏成功，否则失败【挑战成功】  
（可参考运行演示图）  
### 使用简要说明
1、在get_ernie_vilg_pic.py文件中加入API Key和Secret Key  
2、分别运行player1.py~player5.py五个文件  
　　python 文件名  
3、在输入框中输入内容，点击“send”按钮发送