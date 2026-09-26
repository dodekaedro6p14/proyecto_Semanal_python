import bpy 

def prisma(h, y, r, s):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices = 5,
        depth    = h,
        location = (0, 0, y),
        rotation = (0, 0, r),
        radius   = s
            
        
        )
        
step = 0.5
y = 0
s = 4 

for i in range(30):
    y = y + step
    s = s * 0.9
    prisma (step, y, i * 0.1, s)
    
    