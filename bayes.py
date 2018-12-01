
#数据预处理
trainSet = []
testSet = []

f = open("balance-scale.txt")  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法
while line:
    if "L" in line:
        line = line.replace("L", "1")
        line = line.strip()
        line = line.replace(",", "")
    elif "B" in line:
        line = line.replace("B", "2")
        line = line.strip()
        line = line.replace(",", "")
    elif "R" in line:
        line = line.replace("R", "3")
        line = line.strip()
        line = line.replace(",", "")

    line = list(line)
    for i in range(0, 5):
        line[i] = int(line[i])
    if line[4] != 1:
        trainSet.append(line)
    else:
        testSet.append(line)
    line = f.readline()
f.close()

#朴素贝叶斯
label1 = 0
labelTest1 = 0


label1_4 = [0, 0, 0, 0, 0]#第一类样本第四个属性
labelTest1_4 = [0, 0, 0, 0, 0]
m1 = 500 #训练集
m2 = 125 #测试集
i = 0

#训练集
while i < m1:
    if trainSet[i][0] == 1:
        label1 = label1 + 1
        if trainSet[i][3] == 1:
            label1_4[0] = label1_4[0] + 1
        elif trainSet[i][3] == 2:
            label1_4[1] = label1_4[1] + 1
        elif trainSet[i][3] == 3:
            label1_4[2] = label1_4[2] + 1
        elif trainSet[i][3] == 4:
            label1_4[3] = label1_4[3] + 1
        elif trainSet[i][3] == 5:
            label1_4[4] = label1_4[4] + 1
    i = i + 1

y1 = label1 / m1 #label1概率 TODO:（先验概率）？

#𝑷(𝒗i=𝒌|p𝟏) k=1,2,3,4,5
y1_4 = [0, 0, 0, 0, 0]
for i in range(0, 5):
    y1_4[i] = label1_4[i] / label1 #第一类样本第四个属性概率（后验概率）

#测试集

while i < m2:
    if testSet[i][0] == 1:
        labelTest1 = labelTest1 + 1
        if testSet[i][3] == 1:
            labelTest1_4[0] = labelTest1_4[0] + 1
        elif trainSet[i][3] == 2:
            labelTest1_4[1] = labelTest1_4[1] + 1
        elif trainSet[i][3] == 3:
            labelTest1_4[2] = labelTest1_4[2] + 1
        elif trainSet[i][3] == 4:
            labelTest1_4[3] = labelTest1_4[3] + 1
        elif trainSet[i][3] == 5:
            labelTest1_4[4] = labelTest1_4[4] + 1
    i = i + 1

p1_4 = [0, 0, 0, 0, 0]
p = 1 #条件概率
for i in range(0, 5):
    p1_4[i] = labelTest1_4[i] / labelTest1 #测试集第一类第四个属性概率（后验概率
    p = p1_4[i] * p










