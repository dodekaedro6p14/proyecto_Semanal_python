import py3d
import numpy

cars = py3d.cube(0.5, 0.2, 0.3) @ py3d.Transform.from_translation(y=range(1, 6))
t = 0
dt = 0.1
while t < 4:
    py3d.render(cars, t=t)
    cars @= py3d.Transform.from_rpy(py3d.Vector3(z=dt * numpy.linspace(0.1,1,5)))
    t += dt
py3d.render(cars, t=t)




