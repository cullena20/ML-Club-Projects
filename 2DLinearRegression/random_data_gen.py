import random

slope = -3.239812
yint = 5.23

with open("train.csv", "w") as f:
    f.write("x,y\n")
    for i in range(1000):
        # random.gauss(mu, sigma)
        x = random.gauss(12, 6)
        y = slope * x + yint + random.gauss(0, 2)
        f.write(str(x)+","+str(y)+"\n")


with open("test.csv", "w") as f:
    f.write("x,y\n")
    for i in range(200):
        # random.gauss(mu, sigma)
        x = random.gauss(12, 6)
        y = slope * x + yint + random.gauss(0, 2)
        f.write(str(x)+","+str(y)+"\n")
