import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt
#print(np.__version__)
# points to transform - unit cube
points = np.array([[-1, -1, -1],
                  [1, -1, -1 ],
                  [1, 1, -1],
                  [-1, 1, -1],
                  [-1, -1, 1],
                  [1, -1, 1 ],
                  [1, 1, 1],
                  [-1, 1, 1]])
#print(points)
P = [[1 , 0 , 0],
     [0 , 1 , 0],
     [0 , 0 , 1]]
#print(P)
Z = np.zeros((8,3))
#print(Z)
for i in range(8):
    Z[i,:] = np.dot(points[i,:],P)
#print(Z)

# affine input data
ins = np.array([[-100,-100,0], [0,100,0], [100,-100,0], [0.1,0.1,0.1]]) # <- primary system
#out = np.array([[-1000,-1000,0], [0,1000,0], [1000,-1000,0], [1,1,1]]) # <- secondary system (scale 10x)
out = np.array([[-1000,-1000,0], [0,1000,0], [1000,-999,0], [1,1,1]]) # <- secondary system (scale 10x and sheer)

# finding transformation
l = len(ins)
e = lambda r,d: np.linalg.det(np.delete(np.vstack([r, ins.T, np.ones(l)]), d, axis=0))
M = np.array([[(-1)**i * e(R, i) for R in out.T] for i in range(l+1)])
A, t = np.hsplit(M[1:].T/(-M[0])[:,None], [l-1])
t = np.transpose(t)[0]
# output transformation
print("Affine transformation matrix:\n", A)
print("Affine transformation translation vector:\n", t)
# unittests
print("TESTING:")
for p, P in zip(np.array(ins), np.array(out)):
  image_p = np.dot(A, p) + t
  result = "[OK]" if np.allclose(image_p, P) else "[ERROR]"
  print(p, " mapped to: ", image_p, " ; expected: ", P, result)
#calculate points
print("CALCULATION:")
#P = np.dot(A, Z[0,:]) + t
#print(Z[0,:], " mapped to: ", P)
#P = np.dot(A, Z[1,:]) + t
#print(Z[1,:], " mapped to: ", P)

XZ = np.zeros((8,3))
for i in range(8):
    XZ[i,:] = np.dot(A, Z[i,:]) + t
    print(Z[i,:], " mapped to: ", XZ[i,:])

# plot
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d') #left
ax2 = fig.add_subplot(122, projection='3d') #right
#fig.suptitle('Horizontally stacked subplots')
fig.suptitle('3d affine transform')
ax1.title.set_text('input')
ax2.title.set_text('output')

r = [-1,1]

X, Y = np.meshgrid(r, r)
# plot vertices
ax1.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])
ax2.scatter3D(XZ[:, 0], XZ[:, 1], XZ[:, 2])

# list of sides' polygons of figure
verts = [[Z[0],Z[1],Z[2],Z[3]],
 [Z[4],Z[5],Z[6],Z[7]],
 [Z[0],Z[1],Z[5],Z[4]],
 [Z[2],Z[3],Z[7],Z[6]],
 [Z[1],Z[2],Z[6],Z[5]],
 [Z[4],Z[7],Z[3],Z[0]]]

verts2 = [[XZ[0],XZ[1],XZ[2],XZ[3]],
 [XZ[4],XZ[5],XZ[6],XZ[7]],
 [XZ[0],XZ[1],XZ[5],XZ[4]],
 [XZ[2],XZ[3],XZ[7],XZ[6]],
 [XZ[1],XZ[2],XZ[6],XZ[5]],
 [XZ[4],XZ[7],XZ[3],XZ[0]]]

# plot sides
#ax1.add_collection3d(Poly3DCollection(verts,
# facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

faces = Poly3DCollection(verts, linewidths=1, edgecolors='k')
faces.set_facecolor((0,0,1,0.1))
ax1.add_collection3d(faces)

ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

#ax2.add_collection3d(Poly3DCollection(verts2,
# facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

faces = Poly3DCollection(verts2, linewidths=1, edgecolors='k')
faces.set_facecolor((0,0,1,0.1))
ax2.add_collection3d(faces)

ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

#plt.tight_layout()
plt.show()