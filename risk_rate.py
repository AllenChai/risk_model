import pandas as pd
import numpy as np
import math
import time
#定义计算年利率函数，已知客户贷款金额M,剩余本金RM,还款期数RS,总期数S，还款方式为等额本息。计算客户的年利率
#RM和RS不能为0，才有足够的信息估计年利率，如果不满足该条件报错
def interest_rate(M,RM,RS,S):
    assert RS*RM> 0
#创建年利率列表，遍历年利率从1%到99.9%的数组，步长为0.001,len(ratio) = 990
    ratio = np.arange(0.01,1.0,0.001)
#创建P列表，记录不同年利率对应的每期应应还的金额数
    P = []
    for i in range(0,len(ratio)):
        P.append(round((M*ratio[i]/12*(1+ratio[i]/12)**S)/((1+ratio[i]/12)**S-1),2))
#创建数组，记录不同利率每期的还款本金，计算到已还期数，其中C[i,j] i 为不同利率，j为不同期数
    C=  np.zeros([len(ratio),RS])
    for i in range(0,len(ratio)):
        CP = 0
        for j in range(0,RS):
            CP += C[i,j-1]
            C[i,j] = P[i] - (M - CP)*ratio[i]/12
#查找年利率为多少,k值为误差最小的位置
    err = []
    for i in range(0,len(ratio)):
        RM1= 0
        for j in range(0,RS):
            RM1+= C[i,j]
        err.append(abs(M - RM1 -RM))
    k = err.index(min(err))
    print('该客户的借款年利率：','%.3f%%' % (round(ratio[k],3)*100))
    print('该客户的月还款金额：',(round(P[k],3)))
    return round(ratio[k],3),round(P[k],3)
start = time.clock()

interest_rate(500000,468679,50,360)
interest_rate(40000,38086,2,36)

end = time.clock()
d = end - start
print("程序运行总耗时:%0.2f"%d, 's')