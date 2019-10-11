import matplotlib.pyplot as plt
import math

font = {'color': 'red',
        'size': 15}

Xcoordinate = [5, 12, 12, 4, 5]
Ycoordinate = [5, 4, 10, 10, 5]
Xcoordinate2 = [5, 12, 12, 4, 5]
Ycoordinate2 = [5, 4, 10, 10, 5]

angle = int(input("Enter Angle of rotation in degree: "))

sinAngle = math.ceil(math.sin(angle))
cosAngle = math.ceil(math.cos(angle))

print(sinAngle, cosAngle)

for x in range(0, len(Xcoordinate)):
    Xcoordinate2[x] = Xcoordinate[x] * cosAngle + Ycoordinate[x] * (-1*sinAngle)
    Ycoordinate2[x] = Xcoordinate[x] * sinAngle + Ycoordinate[x] * cosAngle

plt.plot(Xcoordinate2, Ycoordinate2, Xcoordinate2, Ycoordinate2)
plt.plot(Xcoordinate, Ycoordinate, Xcoordinate, Ycoordinate, 'bo')
plt.axis([-30, 30, -30, 30])
plt.title("Rotate", fontdict=font)
plt.show()