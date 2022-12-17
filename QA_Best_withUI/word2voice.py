# 导入pyttsx3库
import pyttsx3

engine = pyttsx3.init()  # 创建engine并初始化
engine.say('你干嘛，哎呦哎嗨')  # 开始朗读
engine.runAndWait()  # 等待语音播报完毕






# """
# 以下内容均译制于官网文件，侵权必删
# """
#
# import pyttsx3
#
# engine = pyttsx3.init()  # 创建对象
#
# """语速"""
# rate = engine.getProperty('rate')  # 获取当前语速的详细信息
# print(rate)  # 打印当前语速
# engine.setProperty('rate', 125)  # 重设语速
#
# """音量"""
# volume = engine.getProperty('volume')  # 获取当前音量（最小为0，最大为1）
# print(volume)  # 打印当前音量
# engine.setProperty('volume', 1.0)  # 在0到1之间重设音量
#
# """发音"""
# voices = engine.getProperty('voices')  # 获取当前发音的详细信息
# # engine.setProperty('voice',voices[0].id) #更改发音参数
# engine.setProperty('voice', voices[1].id)  # 更改发音参数
#
# """朗读"""  # 这里朗读的内容没有翻译，因为翻译的话可能运行时会有问题
# engine.say('Hello world!')
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()
#
# """将音频保存为文件"""
# # 如果在linux环境中运行，请确保已安装espeak与ffmpeg模块
# engine.save_to_file('你好，世界！', 'test.mp3')
# engine.runAndWait()