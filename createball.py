# -*- coding: mbcs -*-
import csv
import time

# 写入你的csv文件完整路径，注意用\\取代windows里的\
filename = "C:\\Users\\Administrator.DESKTOP-O4CJ8MA\\Desktop\\UGdata.csv"

model_name = "model"
material_name='material1'
section_name = "Section-1"
all_rows_data = []
with open(filename) as f:
    # 创建cvs文件读取器
    reader = csv.reader(f)
    for row in reader:
        if(reader.line_num==1):
            continue
        row_data = []
        for item in row[:4]:
            try:
                row_data.append(float(item))
            except:
                print "data"+str(row)+"invalid,skipped"
                break
        if(len(row_data)==4):
            all_rows_data.append(row_data)


from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

nowtime=time.strftime('%H%M%S',time.localtime(time.time()))
if(mdb.models.has_key(model_name)):
    mdb.models.changeKey(fromName=model_name, toName=model_name+nowtime)
mdb.Model(name=model_name, modelType=STANDARD_EXPLICIT)

# 材料定义部分
material1 = mdb.models[model_name].Material(name=material_name)
material1.Density(table=((2245.0, ), ))
material1.Elastic(table=((701000000.0, 0.39), ))
mdb.models[model_name].HomogeneousSolidSection(name=section_name, 
    material=material_name, thickness=None)

for i in range(len(all_rows_data)):
    ball_center_point = tuple(all_rows_data[i][:3])
    ball_r = all_rows_data[i][3]
    part_name = "ball"+str(i+1)
    s = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s.FixedConstraint(entity=g[2])
    s.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.0, -ball_r), point2=(0.0, ball_r), 
        direction=COUNTERCLOCKWISE)
    s.CoincidentConstraint(entity1=v[2], entity2=g[2], addUndoState=False)
    s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
    s.CoincidentConstraint(entity1=v[1], entity2=g[2], addUndoState=False)
    s.Line(point1=(0.0, ball_r), point2=(0.0, -ball_r))
    s.VerticalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    p = mdb.models[model_name].Part(name=part_name, dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models[model_name].parts[part_name]
    p.BaseSolidRevolve(sketch=s, angle=360.0, flipRevolveDirection=OFF)
    s.unsetPrimaryObject()
    p = mdb.models[model_name].parts[part_name]
    del mdb.models[model_name].sketches['__profile__']
    p = mdb.models[model_name].parts[part_name]
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='Set-1')
    p = mdb.models[model_name].parts[part_name]
    p.SectionAssignment(region=region, sectionName=section_name, offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    instance_name = part_name+'-1'
    a = mdb.models[model_name].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models[model_name].parts[part_name]
    a.Instance(name=instance_name, part=p, dependent=ON)
    a = mdb.models[model_name].rootAssembly
    a.translate(instanceList=(instance_name, ), vector=ball_center_point)


