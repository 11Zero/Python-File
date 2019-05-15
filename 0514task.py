from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
import sys
sys.path.insert(9, r'd:/Program Files/abaqus/6.14-1/code/python2.7/lib/abaqus_plugins/odbCombine') # 这句是引入dob操作库，路径要改为自己的软件路径
import odbCombineKernel
odbName = 'D:/Program Files/abaqus/Temp/Job-1.odb' # odb文件位置
stepName = 'Step-1' #需要输出的分析步
o1 = session.openOdb(name=odbName)
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
s1f1_S = session.odbs[odbName].steps[stepName].frames[-1].fieldOutputs['S']
s1f1_E = session.odbs[odbName].steps[stepName].frames[-1].fieldOutputs['E']
tmpField = s1f1_E.getScalarField(invariant=MAX_PRINCIPAL)*s1f1_E.getScalarField(invariant=MAX_PRINCIPAL)*0.5*s1f1_S.getScalarField(invariant=MAX_PRINCIPAL)/s1f1_E.getScalarField(invariant=MAX_PRINCIPAL)
currentOdb = session.odbs[odbName]
scratchOdb = session.ScratchOdb(odb=currentOdb)
sessionStep = scratchOdb.Step(name='Session Step', 
    description='Step for Viewer non-persistent fields', domain=TIME, 
    timePeriod=1.0)
sessionFrame = sessionStep.Frame(frameId=0, frameValue=0.0, 
    description='Session Frame')
sessionField = sessionFrame.FieldOutput(name='Field-needed', 
    description='0.5*e*e*E', 
    field=tmpField)

s1f1_S = session.odbs[odbName].steps[stepName].frames[-1].fieldOutputs['S']
s1f1_E = session.odbs[odbName].steps[stepName].frames[-1].fieldOutputs['E']
tmpField = s1f1_E.getScalarField(invariant=MAX_PRINCIPAL)*s1f1_E.getScalarField(invariant=MAX_PRINCIPAL)*0.5*s1f1_S.getScalarField(invariant=MAX_PRINCIPAL)/s1f1_E.getScalarField(invariant=MAX_PRINCIPAL)
currentOdb = session.odbs[odbName]
scratchOdb = session.ScratchOdb(odb=currentOdb)
sessionFrame = sessionStep.Frame(frameId=0, frameValue=0.0, 
    description='Session Frame')
sessionField = sessionFrame.FieldOutput(name='Field-needed1', 
    description='0.5*e*e*E' ,
    field=tmpField)

