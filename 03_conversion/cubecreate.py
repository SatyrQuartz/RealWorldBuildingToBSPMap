# python '/home/colbydray/SRC/cubecreate.py' 1 1 1 0 0 0 None 1

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("X_Size")
parser.add_argument("Y_Size")
parser.add_argument("Z_Size")
parser.add_argument("X_Pos")
parser.add_argument("Y_Pos")
parser.add_argument("Z_Pos")
parser.add_argument("Texture")
parser.add_argument("BrushNum")

args = parser.parse_args()

X_Size = float(args.X_Size)
Y_Size = float(args.Y_Size)
Z_Size = float(args.Z_Size)
X_Pos = float(args.X_Pos)
Y_Pos = float(args.Y_Pos)
Z_Pos = float(args.Z_Pos)
TextureName = args.Texture
BrushNum = int(args.BrushNum)

BaseValue = 38

X_Size = X_Size * BaseValue
Y_Size = Y_Size * BaseValue
Z_Size = Z_Size * BaseValue
X_Pos = X_Pos * BaseValue
Y_Pos = Y_Pos * BaseValue
Z_Pos = Z_Pos * BaseValue

Plane1 = [[[-0.5, -0.5, -0.5], [-0.5, -0.5, -0.5], [-0.5, -0.5, -0.5]]]
Plane2 = [[[-0.5, -0.5, -0.5], [-0.5, -0.5, -0.5], [-0.5, -0.5, -0.5]]]
Plane3 = [[[-0.5, -0.5, -0.5], [-0.5, -0.5, -0.5], [-0.5, -0.5, -0.5]]]
Plane4 = [[[0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]]]
Plane5 = [[[0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]]]
Plane6 = [[[0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]]]

Plane1[0][0][0] = Plane1[0][0][0] * X_Size
Plane1[0][1][0] = Plane1[0][1][0] * X_Size
Plane1[0][2][0] = Plane1[0][2][0] * X_Size
Plane2[0][0][0] = Plane2[0][0][0] * X_Size
Plane2[0][1][0] = Plane2[0][1][0] * X_Size
Plane2[0][2][0] = Plane2[0][2][0] * X_Size
Plane3[0][0][0] = Plane3[0][0][0] * X_Size
Plane3[0][1][0] = Plane3[0][1][0] * X_Size
Plane3[0][2][0] = Plane3[0][2][0] * X_Size
Plane4[0][0][0] = Plane4[0][0][0] * X_Size
Plane4[0][1][0] = Plane4[0][1][0] * X_Size
Plane4[0][2][0] = Plane4[0][2][0] * X_Size
Plane5[0][0][0] = Plane5[0][0][0] * X_Size
Plane5[0][1][0] = Plane5[0][1][0] * X_Size
Plane5[0][2][0] = Plane5[0][2][0] * X_Size
Plane6[0][0][0] = Plane6[0][0][0] * X_Size
Plane6[0][1][0] = Plane6[0][1][0] * X_Size
Plane6[0][2][0] = Plane6[0][2][0] * X_Size

Plane1[0][0][1] = Plane1[0][0][1] * Y_Size
Plane1[0][1][1] = Plane1[0][1][1] * Y_Size
Plane1[0][2][1] = Plane1[0][2][1] * Y_Size
Plane2[0][0][1] = Plane2[0][0][1] * Y_Size
Plane2[0][1][1] = Plane2[0][1][1] * Y_Size
Plane2[0][2][1] = Plane2[0][2][1] * Y_Size
Plane3[0][0][1] = Plane3[0][0][1] * Y_Size
Plane3[0][1][1] = Plane3[0][1][1] * Y_Size
Plane3[0][2][1] = Plane3[0][2][1] * Y_Size
Plane4[0][0][1] = Plane4[0][0][1] * Y_Size
Plane4[0][1][1] = Plane4[0][1][1] * Y_Size
Plane4[0][2][1] = Plane4[0][2][1] * Y_Size
Plane5[0][0][1] = Plane5[0][0][1] * Y_Size
Plane5[0][1][1] = Plane5[0][1][1] * Y_Size
Plane5[0][2][1] = Plane5[0][2][1] * Y_Size
Plane6[0][0][1] = Plane6[0][0][1] * Y_Size
Plane6[0][1][1] = Plane6[0][1][1] * Y_Size
Plane6[0][2][1] = Plane6[0][2][1] * Y_Size

Plane1[0][0][2] = Plane1[0][0][2] * Z_Size
Plane1[0][1][2] = Plane1[0][1][2] * Z_Size
Plane1[0][2][2] = Plane1[0][2][2] * Z_Size
Plane2[0][0][2] = Plane2[0][0][2] * Z_Size
Plane2[0][1][2] = Plane2[0][1][2] * Z_Size
Plane2[0][2][2] = Plane2[0][2][2] * Z_Size
Plane3[0][0][2] = Plane3[0][0][2] * Z_Size
Plane3[0][1][2] = Plane3[0][1][2] * Z_Size
Plane3[0][2][2] = Plane3[0][2][2] * Z_Size
Plane4[0][0][2] = Plane4[0][0][2] * Z_Size
Plane4[0][1][2] = Plane4[0][1][2] * Z_Size
Plane4[0][2][2] = Plane4[0][2][2] * Z_Size
Plane5[0][0][2] = Plane5[0][0][2] * Z_Size
Plane5[0][1][2] = Plane5[0][1][2] * Z_Size
Plane5[0][2][2] = Plane5[0][2][2] * Z_Size
Plane6[0][0][2] = Plane6[0][0][2] * Z_Size
Plane6[0][1][2] = Plane6[0][1][2] * Z_Size
Plane6[0][2][2] = Plane6[0][2][2] * Z_Size


Plane1[0][0][0] = Plane1[0][0][0] + X_Pos
Plane1[0][1][0] = Plane1[0][1][0] + X_Pos
Plane1[0][2][0] = Plane1[0][2][0] + X_Pos
Plane2[0][0][0] = Plane2[0][0][0] + X_Pos
Plane2[0][1][0] = Plane2[0][1][0] + X_Pos
Plane2[0][2][0] = Plane2[0][2][0] + X_Pos
Plane3[0][0][0] = Plane3[0][0][0] + X_Pos
Plane3[0][1][0] = Plane3[0][1][0] + X_Pos
Plane3[0][2][0] = Plane3[0][2][0] + X_Pos
Plane4[0][0][0] = Plane4[0][0][0] + X_Pos
Plane4[0][1][0] = Plane4[0][1][0] + X_Pos
Plane4[0][2][0] = Plane4[0][2][0] + X_Pos
Plane5[0][0][0] = Plane5[0][0][0] + X_Pos
Plane5[0][1][0] = Plane5[0][1][0] + X_Pos
Plane5[0][2][0] = Plane5[0][2][0] + X_Pos
Plane6[0][0][0] = Plane6[0][0][0] + X_Pos
Plane6[0][1][0] = Plane6[0][1][0] + X_Pos
Plane6[0][2][0] = Plane6[0][2][0] + X_Pos

Plane1[0][0][1] = Plane1[0][0][1] + Y_Pos
Plane1[0][1][1] = Plane1[0][1][1] + Y_Pos
Plane1[0][2][1] = Plane1[0][2][1] + Y_Pos
Plane2[0][0][1] = Plane2[0][0][1] + Y_Pos
Plane2[0][1][1] = Plane2[0][1][1] + Y_Pos
Plane2[0][2][1] = Plane2[0][2][1] + Y_Pos
Plane3[0][0][1] = Plane3[0][0][1] + Y_Pos
Plane3[0][1][1] = Plane3[0][1][1] + Y_Pos
Plane3[0][2][1] = Plane3[0][2][1] + Y_Pos
Plane4[0][0][1] = Plane4[0][0][1] + Y_Pos
Plane4[0][1][1] = Plane4[0][1][1] + Y_Pos
Plane4[0][2][1] = Plane4[0][2][1] + Y_Pos
Plane5[0][0][1] = Plane5[0][0][1] + Y_Pos
Plane5[0][1][1] = Plane5[0][1][1] + Y_Pos
Plane5[0][2][1] = Plane5[0][2][1] + Y_Pos
Plane6[0][0][1] = Plane6[0][0][1] + Y_Pos
Plane6[0][1][1] = Plane6[0][1][1] + Y_Pos
Plane6[0][2][1] = Plane6[0][2][1] + Y_Pos

Plane1[0][0][2] = Plane1[0][0][2] + Z_Pos
Plane1[0][1][2] = Plane1[0][1][2] + Z_Pos
Plane1[0][2][2] = Plane1[0][2][2] + Z_Pos
Plane2[0][0][2] = Plane2[0][0][2] + Z_Pos
Plane2[0][1][2] = Plane2[0][1][2] + Z_Pos
Plane2[0][2][2] = Plane2[0][2][2] + Z_Pos
Plane3[0][0][2] = Plane3[0][0][2] + Z_Pos
Plane3[0][1][2] = Plane3[0][1][2] + Z_Pos
Plane3[0][2][2] = Plane3[0][2][2] + Z_Pos
Plane4[0][0][2] = Plane4[0][0][2] + Z_Pos
Plane4[0][1][2] = Plane4[0][1][2] + Z_Pos
Plane4[0][2][2] = Plane4[0][2][2] + Z_Pos
Plane5[0][0][2] = Plane5[0][0][2] + Z_Pos
Plane5[0][1][2] = Plane5[0][1][2] + Z_Pos
Plane5[0][2][2] = Plane5[0][2][2] + Z_Pos
Plane6[0][0][2] = Plane6[0][0][2] + Z_Pos
Plane6[0][1][2] = Plane6[0][1][2] + Z_Pos
Plane6[0][2][2] = Plane6[0][2][2] + Z_Pos

Plane1[0][1][1] = Plane1[0][1][1] + 0.01
Plane1[0][2][2] = Plane1[0][2][2] + 0.01
Plane2[0][1][2] = Plane2[0][1][2] + 0.01
Plane2[0][2][0] = Plane2[0][2][0] + 0.01
Plane3[0][1][0] = Plane3[0][1][0] + 0.01
Plane3[0][2][1] = Plane3[0][2][1] + 0.01
Plane4[0][1][1] = Plane4[0][1][1] + 0.01
Plane4[0][2][0] = Plane4[0][2][0] + 0.01
Plane5[0][1][0] = Plane5[0][1][0] + 0.01
Plane5[0][2][2] = Plane5[0][2][2] + 0.01
Plane6[0][1][2] = Plane6[0][1][2] + 0.01
Plane6[0][2][1] = Plane6[0][2][1] + 0.01


Plane1[0][0][1]
Plane1[0][1][1]
Plane1[0][2][1]

print("// brush " + str(BrushNum))

print("{")

print("( " + str(Plane1[0][0][0]) + " " + str(Plane1[0][0][1]) + " " + str(Plane1[0][0][2]) + " ) ( " + str(Plane1[0][1][0]) + " " + str(Plane1[0][1][1]) + " " + str(Plane1[0][1][2]) + " ) ( " + str(Plane1[0][2][0]) + " " + str(Plane1[0][2][1]) + " " + str(Plane1[0][2][2]) + " ) " + TextureName + " 0 0 0 1 1 ")

print("( " + str(Plane2[0][0][0]) + " " + str(Plane2[0][0][1]) + " " + str(Plane2[0][0][2]) + " ) ( " + str(Plane2[0][1][0]) + " " + str(Plane2[0][1][1]) + " " + str(Plane2[0][1][2]) + " ) ( " + str(Plane2[0][2][0]) + " " + str(Plane2[0][2][1]) + " " + str(Plane2[0][2][2]) + " ) " + TextureName + " 0 0 0 1 1 ")

print("( " + str(Plane3[0][0][0]) + " " + str(Plane3[0][0][1]) + " " + str(Plane3[0][0][2]) + " ) ( " + str(Plane3[0][1][0]) + " " + str(Plane3[0][1][1]) + " " + str(Plane3[0][1][2]) + " ) ( " + str(Plane3[0][2][0]) + " " + str(Plane3[0][2][1]) + " " + str(Plane3[0][2][2]) + " ) " + TextureName + " 0 0 0 1 1 ")

print("( " + str(Plane4[0][0][0]) + " " + str(Plane4[0][0][1]) + " " + str(Plane4[0][0][2]) + " ) ( " + str(Plane4[0][1][0]) + " " + str(Plane4[0][1][1]) + " " + str(Plane4[0][1][2]) + " ) ( " + str(Plane4[0][2][0]) + " " + str(Plane4[0][2][1]) + " " + str(Plane4[0][2][2]) + " ) " + TextureName + " 0 0 0 1 1 ")

print("( " + str(Plane5[0][0][0]) + " " + str(Plane5[0][0][1]) + " " + str(Plane5[0][0][2]) + " ) ( " + str(Plane5[0][1][0]) + " " + str(Plane5[0][1][1]) + " " + str(Plane5[0][1][2]) + " ) ( " + str(Plane5[0][2][0]) + " " + str(Plane5[0][2][1]) + " " + str(Plane5[0][2][2]) + " ) " + TextureName + " 0 0 0 1 1 ")

print("( " + str(Plane6[0][0][0]) + " " + str(Plane6[0][0][1]) + " " + str(Plane6[0][0][2]) + " ) ( " + str(Plane6[0][1][0]) + " " + str(Plane6[0][1][1]) + " " + str(Plane6[0][1][2]) + " ) ( " + str(Plane6[0][2][0]) + " " + str(Plane6[0][2][1]) + " " + str(Plane6[0][2][2]) + " ) " + TextureName + " 0 0 0 1 1 ")

print("}")