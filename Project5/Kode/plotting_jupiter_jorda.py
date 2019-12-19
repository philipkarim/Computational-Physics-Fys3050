import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt;
import numpy as np;

def readFile(filename,navn):
    data = np.loadtxt(filename,unpack=True)
    x = data[1]
    y = data[2]
    plt.plot(x,y,label = navn)

readFile("Mercury.txt","Merkur")
readFile("Venus.txt","Venus")
readFile("Earth.txt","Jorda")
readFile("Mars.txt","Mars")
readFile("Jupiter.txt","Jupiter")
readFile("Saturn.txt","Saturn")
readFile("Uranus.txt","Uranus")
readFile("Neptune.txt","Neptrun")

plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
plt.legend()
plt.axis('equal')
plt.grid("on")
plt.savefig('solsystem.png')
plt.show()
