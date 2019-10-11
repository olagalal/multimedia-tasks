import matplotlib.pyplot as plt

font = {'color': 'red',
        'size': 15}

Xcoordinate = [5, 10, 10, 5, 5]
Ycoordinate = [5, 5, 10, 10, 5]
Xcoordinate2 = [5, 10, 10, 5, 5]
Ycoordinate2 = [5, 5, 10, 10, 5]

stepX = float(input("Enter translate value of x-axis: "))
stepY = float(input("Enter translate value of y-axis: "))

for y in range(0, len(Xcoordinate2)):
    Xcoordinate2[y] += stepX
    Ycoordinate2[y] += stepY

plt.plot(Xcoordinate2, Ycoordinate2, Xcoordinate2, Ycoordinate2)
plt.plot(Xcoordinate, Ycoordinate, Xcoordinate, Ycoordinate)
plt.axis([0, 30, 0, 30])
plt.title("translate", fontdict=font)
plt.show()