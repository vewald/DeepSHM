from driverUtils import executeOnCaeStartup
import odbAccess
executeOnCaeStartup()

Variable1 = 10

Files = ['F:/Scratch/Damage00.odb','F:/Scratch/Damage02.odb','F:/Scratch/Damage04.odb','F:/Scratch/Damage06.odb','F:/Scratch/Damage08.odb']

odb = odbAccess.openOdb(Files[0])

for steps in range(odb.diagnosticData.numberOfSteps):
    stepname = odb.steps.keys()[steps]
    StepInfo = odb.steps[stepname]
    NumberOfFrames = len(StepInfo.frames)
    for frame in range(0,NumberOfFrames,Variable1):
        outputlst = []
        for Node in range(0,len(StepInfo.frames[frame].fieldOutputs['U'].values),10):
            outputlst.append(','.join(map(str,[Node+1]+list(StepInfo.frames[frame].fieldOutputs['U'].values[Node].data)))+"\n")
        f = open('C:/Users/vewald/Downloads/RPT/Abaqus_'+str(steps)+'_'+str(frame)+'.txt','w')
        f.writelines(outputlst)
        f.close()
odb.close()