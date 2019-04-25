#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 0:41
# @Author  : liuhu
# @Site    : 
# @File    : 中文排序.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# 建立拼音辞典
dic_py = dict()

with open(r'py.txt', 'r', encoding='utf8') as f:
    content_py = f.readlines()

    for i in content_py:
        i = i.strip()
        word_py, mean_py = i.split('\t')
        dic_py[word_py] = mean_py

# 建立笔画辞典
dic_bh = dict()
with open(r'bh.txt', 'r', encoding='utf8') as f:
    content_bh = f.readlines()

    for i in content_bh:
        i = i.strip()
        word_bh, mean_bh = i.split('\t')
        dic_bh[word_bh] = mean_bh


###############################
# 辞典查找函数
def searchdict(dic, uchar):
    # 一    齚
    if u'\u4e00' <= uchar <= u'\u9fa5':
        value = dic.get(uchar)
        if value == None:
            value = '*'
    else:
        value = uchar
    return value


# 比较单个字符
def comp_char_PY(A, B):
    if A == B:
        return -1
    pyA = searchdict(dic_py, A)
    pyB = searchdict(dic_py, B)

    # 比较拼音
    if pyA > pyB:
        return 1
    elif pyA < pyB:
        return 0

    # 比较笔画
    else:
        bhA = eval(searchdict(dic_bh, A))
        bhB = eval(searchdict(dic_bh, B))
        if bhA > bhB:
            return 1
        elif bhA < bhB:
            return 0
        else:
            return "拼音相同，笔画也相同？"


# 比较字符串
def comp_char(A, B):
    n = min(len(A), len(B))
    i = 0
    while i < n:
        dd = comp_char_PY(A[i], B[i])
        # 如果第一个单词相等，就继续比较下一个单词
        if dd == -1:
            i = i + 1
            # 如果比较到头了
            if i == n:
                dd = len(A) > len(B)
        else:
            break
    return dd


# 排序函数
def cnsort(nline):
    n = len(nline)
    lines = "\n".join(nline)

    for i in range(1, n):  # 插入法
        tmp = nline[i]
        j = i
        while j > 0 and comp_char(nline[j - 1], tmp):
            nline[j] = nline[j - 1]
            j -= 1
        nline[j] = tmp
    return nline


list_zh = ['第10讲：微服务 API 服务网关（一）原理.mp4', '第11讲：微服务 API 服务网关（二）开源网关 Zuul.mp4', '第12讲：跟 Netflix 学习微服务路由发现体系.mp4',
           '第13讲：集中式配置中心的作用和原理是什么？.mp4', '第14讲：微服务通讯方式 RPC vs REST.mp4', '第15讲：微服务框架需要考虑哪些治理环节？.mp4',
           '第16讲：微服务监控系统分层和监控架构.mp4', '第17讲：微服务的调用链监控该如何选型？.mp4', '第18讲：微服务的容错限流是如何工作的？.mp4',
           '第19讲：Docker 容器部署技术 & 持续交付流水线.mp4', '第1讲：什么是微服务架构？.mp4', '第20讲：容器集群调度和基于容器的发布体系.mp4',
           '第2讲：架构师如何权衡微服务的利弊？.mp4', '第3讲：康威法则和微服务给架构师怎样的启示？.mp4', '第4讲：企业应该在什么时候开始考虑引入微服务？.mp4',
           '第5讲：什么样的组织架构更适合微服务？.mp4', '第6讲：如何理解阿里巴巴提出的微服务中台战略？.mp4', '第7讲：如何给出一个清晰简洁的服务分层方式？.mp4',
           '第8讲：微服务总体技术架构体系是怎样设计的？.mp4', '第9讲：微服务最经典的三种服务发现机制.mp4']

print(cnsort(list_zh))