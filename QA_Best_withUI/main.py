# -*- coding: utf-8 -*- 
import os
from datapreprocess import preprocess
import train_eval
import fire
from QA_data import QA_test
from config import Config
# 导入pyttsx3库
import pyttsx3


def chat(input_sentence,**kwargs):
    
    opt = Config()
    for k, v in kwargs.items(): #设置参数
        setattr(opt, k, v)   

    searcher, sos, eos, unknown, word2ix, ix2word = train_eval.test(opt)

    if os.path.isfile(opt.corpus_data_path) == False:
        preprocess()

    # if input_sentence == 'q' or input_sentence == 'quit' or input_sentence == 'exit' or input_sentence == '退出':
    #     break
    if opt.use_QA_first:
        query_res = QA_test.match(input_sentence)
        if (query_res == tuple()):
            output_words = train_eval.output_answer(input_sentence, searcher, sos, eos, unknown, opt, word2ix, ix2word)
        else:
            output_words = "您是不是要找以下问题: " + query_res[1] + '，您可以尝试这样: ' + query_res[2]
    else:
        output_words = train_eval.output_answer(input_sentence, searcher, sos, eos, unknown, opt, word2ix, ix2word)

        # print('某某某 > ', output_words)
        # engine = pyttsx3.init()  # 创建engine并初始化
        # engine.say(str(output_words))  # 开始朗读
        # engine.runAndWait()  # 等待语音播报完毕
    if input_sentence == '拜拜':
        QA_test.conn.close()  # 注释了会不会变慢很多
    return output_words
if __name__ == "__main__":
    # fire.Fire()
    chat()
