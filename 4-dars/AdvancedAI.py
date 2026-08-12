# i. 
class Predict:
    def calculate(self, w, x, b):
        return w * x + b


# Loss formulasi
class Loss:
    def calculate(self, prediction, y):
        return (prediction - y) ** 2


# Optimize formulasi
class Optimize:
    def __init__(self, lr):
        self.lr = lr

    def update(self, w, b):
        wgrad = float(input("wgrad = "))
        bgrad = float(input("bgrad = "))

        w = w - self.lr * wgrad
        b = b - self.lr * bgrad

        return w, b
    

# ii.
class Optimizer:
    def __init__(self, x, w, b, y, lr):
        self.x = x
        self.w = w
        self.b = b
        self.y = y
        self.lr = lr

        self.predict = Predict()
        self.loss = Loss()
        self.optimize = Optimize(lr)

    def run(self, steps=5):
        for i in range(1, steps + 1):
            prediction = self.predict.calculate(self.w, self.x, self.b)
            loss = self.loss.calculate(prediction, self.y)

            print(f"\n{i}-tsikl:\n")
            print(f"Bashorat qiymati      -> {prediction:.4f}")
            print(f"Xatolik qiymati       -> {loss:.6f}")

            self.w, self.b = self.optimize.update(self.w, self.b)

            print(f"Yangi w = {self.w}")
            print(f"Yangi b = {self.b}")

# iii.
optimizer = Optimizer(
    x=4,
    w=3,
    b=2,
    y=10,
    lr=0.1
)

optimizer.run(5)

