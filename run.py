#!/usr/bin/env python3
import os
from config import black_list
from tqdm import tqdm
import time

#提取页面上js链接存到列表函数
def js_link(): 
    #定义存取js链接的列表
    link_js_list = []
    link_result = os.popen('bash ./sub_link.sh subjs').read()
    lines = link_result.splitlines()
    for line in tqdm(lines,desc="提取网页上的js文件链接进度"):
        time.sleep(0.1)
        link_js_list.append(line)
    return link_js_list


#提取js文件中的链接到列表函数
def hidden_js_link():
    js_link_result = js_link()
    #定义存取js隐藏链接的列表
    link_hidden_js_list = []

    for j in tqdm(js_link_result,desc="提取js文件中链接和目录进度"):
        time.sleep(0.1)
        js_hidd_link_result = os.popen('bash ./sub_link.sh linkjs'+''+' '+j).read()

        #将文件存入到列表
        hidden_lines = js_hidd_link_result.splitlines()
        for hiddenline in hidden_lines:
            link_hidden_js_list.append(hiddenline)
    return link_hidden_js_list


#提取带http/https的和不带http/https
def linkishttp():
    link_hidden_js_list_result = hidden_js_link()
    f1 = open(file='./dicc_http.txt', mode='w')
    f2 = open(file='./dicc.txt', mode='w')
    f3 = open(file='./black.txt', mode='w')
    for a in tqdm(link_hidden_js_list_result,desc="提取链接中是否带协议进度"):
        time.sleep(0.1)
        if "http" in a:
            f1.write(str(a)+"\n")
        else:
            f2.write(str(a)+"\n")

    
    #将黑名单列表写入到黑名单文件中
    for b in tqdm(black_list,desc="提取目录黑名单过滤进度"):
        f3.write(str(b)+"\n")
        time.sleep(0.1)
    


if __name__ == "__main__":
    linkishttp()
    #黑名单过滤
    os.popen('bash ./sub_link.sh filterbalck')
    time.sleep(2)
    print("扫描结束(带http协议：dicc_http.txt  不带http协议：dicc1.txt)")