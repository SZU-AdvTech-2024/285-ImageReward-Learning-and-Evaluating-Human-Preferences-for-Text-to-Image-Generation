import matplotlib.pyplot as plt

# 从文本文件中读取数据
with open("blip_uni_cross_mul_bs128_fix=0.7_lr=1e-05cosine_1-10.txt", "r") as f:
    lines = f.readlines()

# 提取迭代次数和准确率
iterations = []
accuracies = []
losses = []
for line in lines:
    if ("Iteration" in line) and not ("Validation" in line):
        parts = line.split()
        iteration = int(parts[1])
        accuracy = float(parts[7])
        iterations.append(iteration)
        accuracies.append(accuracy)

# 绘制图表
plt.plot(iterations, accuracies, label="Accuracy")
plt.xlabel("Iteration")
plt.ylabel("Accuracy")
plt.title("Accuracy vs Iteration")
plt.legend()
plt.show()

for line in lines:
    if ("Iteration" in line) and not ("Validation" in line):
        parts = line.split()
        iteration = int(parts[1])
        loss = float(parts[4])
        iterations.append(iteration)
        accuracies.append(loss)

# 绘制图表
plt.plot(iterations, losses, label="Loss")
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.title("Loss vs Iteration")
plt.legend()
plt.show()