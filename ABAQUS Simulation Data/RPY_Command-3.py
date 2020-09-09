import odbAccess 

odb = session.openOdb('SimTest.odb')

for i in range(0,11):
    frames = odb.steps['Step-1'].frames[i]
    displacement = frames.fieldOutputs['U']
    surface = odb.rootAssembly.instances['PART-1-1'].nodeSets['SURFACE']
    disp = displacement.getSubset(region=surface)
    for v in disp.values:
        print 'Position = ', v.position
        print 'Type = ', v.type
        print 'Node label = ', v.nodeLabel
        print 'X displacement = ', v.data[0]
        print 'Y displacement = ', v.data[1]
        print 'Z displacement = ', v.data[2]
        print 'Displacement magnitude =', v.magnitude
odb.close()