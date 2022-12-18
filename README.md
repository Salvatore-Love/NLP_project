# NLP_project

自然语言处理大作业
## 👨‍👨‍👦‍👦:to my teammates
Git 中 fork 和 clone 的区别
fork我的代码之后发现有BUG或者有一个地方有更好的算法可以解决，或者添加一些新的功能。你可以在你自己的仓库里面修改源码，修改好之后pull request，这样我就可以看到什么地方修改了，如果我觉得你的算法可行就可以把你的代码Merge到我的项目里面，简单说就帮我修复bug或增加新功能了。

git clone 就是你clone到本地进行修改，然后你可以提交到clone的源码中。

所以本次项目用fork一同完成这个大项目 🤩

## :rainbow:项目背景
所有的ikun们，走过路过不要错过，这里有好玩好看的😀😍

想和坤坤聊天吗？💕

疫情在家倍感无聊？😢

快来和ikun来聊天🙌

还有个性化定制哦！（后续推出）😎💕💕💕
## :star:效果展示
![image](QA_Best_withUI\img\1.png)

## 💖:使用方法

### 训练方法

```shell
$ python datapreprocess.py
```
对语料库进行数据预处理，产生corpus.pth

在config.py文件中看有没有自己想要修改的参数，一般情况默认就好

### 测试方法

运行app.py程序即可产生ui界面😁

然后里面可以播放刻在dna的ikun之歌😘

还可以看到gege跳舞🤤

### 注意事项
#### 训练时
如果有GPU的话将config.py中注释掉的device= ......取消注释，然后再注释掉device = 'cpu' 。
这里我们测试时是在cpu上
然后如果不需要从已经训练好的模型开始训练的话，将model_ckpt设置为None
#### 测试时
也是要注意device和model

总而言之代码如果跑不通认真看看config.py里的注释


## :pray:致谢🌷🌷🌷
* 代码参考和学习：
  * https://github.com/yeyupiaoling/MASR
  * https://github.com/Doragd/Chinese-Chatbot-PyTorch-Implementation
  * https://github.com/zhaoyingjun/chatbot
* 官方的Chatbot Tutorial
  * <https://pytorch.org/tutorials/beginner/chatbot_tutorial.html>
* 提供中文语料库
  * <https://github.com/codemayq/chinese_chatbot_corpus> 


