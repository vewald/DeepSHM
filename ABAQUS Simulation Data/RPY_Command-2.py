from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

o1 = session.openOdbs(names=('D:/Scratch/Damage-00mm.odb', 'D:/Scratch/Damage-20mm.odb'))

odb_00 = session.odbs['D:/Scratch/Damage-00mm.odb']
for i in range(1, 10):
   session.writeFieldReport(fileName='C:/Users/vewald/Downloads/abaqus-00.rpt', append=ON, sortItem='Node Label', odb=odb_00, step=0, frame=i, outputPosition=NODAL, variable=(('U', NODAL), ))

odb_20 = session.odbs['D:/Scratch/Damage-20mm.odb']
for i in range(1, 10):
   session.writeFieldReport(fileName='C:/Users/vewald/Downloads/abaqus-20.rpt', append=ON, sortItem='Node Label', odb=odb_20, step=0, frame=i, outputPosition=NODAL, variable=(('U', NODAL), ))
