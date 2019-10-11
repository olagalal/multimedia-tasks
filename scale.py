import matplotlib.pyplot as plt

font = {'color': 'red',
        'size': 15}

Xcoordinate = [5, 10, 10, 5, 5]
Ycoordinate = [5, 5, 10, 10, 5]
Xcoordinate2 = [5, 10, 10, 5, 5]
Ycoordinate2 = [5, 5, 10, 10, 5]

step = float(input("Enter sacle factor: "))

for x in range(0, len(Xcoordinate2)):
    Xcoordinate2[x] = Xcoordinate[x] * (step)
    Ycoordinate2[x] = Ycoordinate[x] * (step)

plt.plot(Xcoordinate2, Ycoordinate2, Xcoordinate2, Ycoordinate2)
plt.plot(Xcoordinate, Ycoordinate, Xcoordinate, Ycoordinate)
plt.axis([0, 30, 0, 30])
plt.title("scale", fontdict=font)
plt.show()