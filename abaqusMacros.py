# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

# First line should not be empty.
# Seperate materials by "-"
# Make sure don't leave space between any number. Just line break

# This setting is a little bit inefficient
# See SO: https://stackoverflow.com/a/47295534/9969193
def setJournalOptions():
    session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)

def create_force_displacement_graph():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    from abaqus import getInput

    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    
    #odb_name = str(getInput('Enter a odb name:'))
    odb_name = os.path.split(session.viewports[session.currentViewportName].displayedObject.path)[1] # I wrote
    
    odb_path = "C:/temp/{0}".format(odb_name)
    #odb = session.odbs['C:/temp/hope.odb']
    odb = session.odbs[odb_path]

    session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF', 
        NODAL, ((COMPONENT, 'RF1'), )), ), nodeSets=('FIX_NODE', ))

    session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('U', 
        NODAL, ((COMPONENT, 'U1'), )), ), nodeSets=('PULL_NODE', ))
    xy1 = session.xyDataObjects['U:U1 PI: COUPON-1 N: 10']
    xy2 = session.xyDataObjects['RF:RF1 PI: COUPON-1 N: 40']
    xy3 = combine(xy1, xy2*-1)
    xy3.setValues(
        sourceDescription='combine ( "U:U1 PI: COUPON-1 N: 10", "RF:RF1 PI: COUPON-1 N: 40"*-1 )')
    tmpName = xy3.name
    session.xyDataObjects.changeKey(tmpName, 'force-displacement_{0}'.format(odb_name[:-4]))

def set_material_submit():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    from abaqus import getWarningReply, YES, NO
    
    model_name = mdb.models.items()[0][0] # Get first model
    MATERIAL = "macro_material"
    SECTION = "macro_material"
    
    material_tuple = ((600.51, 0.0), (618.411, 0.02579), (642.62, 0.04665), (656.328, 0.05909), (664.061, 0.07081), (670.557, 0.08054))

    mdb.models[model_name].materials[MATERIAL].plastic.setValues(table = material_tuple)
    # Set section of part. But unnecessary for now because I change directly underlying material
    #mdb.models[MODEL_NAME].sections[SECTION].setValues(material=MATERIAL, thickness=None)
    submit_job()

def get_materials():

    materials_text = """0.680429
    11125.4
    0.794463
    11125.6
    0.908498
    11125.1
    0.937007
    11125.6
    0.965516
    11125.4
    0.994024
    11125.8
    -
    1.32187
    11125.2
    1.36464
    11125.4
    1.4074
    11125.7
    -
    0.937007
    11125.6
    0.965516
    11125.4
    0.994024
    11125.8"""

    lines = materials_text.split('\n')
    materials = [] # Hold tuples
    seperation_indexes = []
    seperation_index_counter = 0
    value_lists = []
    
    
    for i in range(len(lines)):
        if (lines[i] == "-" and lines[i] != ""):
            seperation_indexes.append(i)
            seperation_index_counter += 1
            if (seperation_index_counter == 1):
                value_lists.append(lines[0:i])
            else:
                value_lists.append(lines[
                    seperation_indexes[seperation_index_counter-2]+1:i])
    # This code is necessary because, above for loop, append UNTIL "-" symbol not after.
    if (seperation_index_counter >= 2):
        value_lists.append(lines[seperation_indexes[seperation_index_counter-1]+1:])


    for i in range (len(value_lists)):
        material = []
        it = iter(value_lists[i])
        for x,y in zip(it,it):
            material.append(tuple((x,y)))
        materials.append(tuple(material))
        
    return materials
    
def submit_job():
    import job
    from random import randint
    reply = getWarningReply(message="Do you want to run all jobs at once?\nIf not, you won't be able to use abaqus until process is finished", buttons=(YES,NO))

    model_name = mdb.models.items()[0][0] # Get first model

    myjob = mdb.Job(name="macro_job_{0}_{1}".format(randint(0,89), randint(15,76)), 
    model=model_name, description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=4, 
    numDomains=4, numGPUs=1)
    #mdb.jobs['macro_job'].submit(consistencyChecking=OFF)
    myjob.submit(consistencyChecking=OFF)
    
    if reply == YES:
        print 'YES clicked'
    elif reply == NO:
        myjob.waitForCompletion()

def RC_Beam():
    import part
    import sketch
    
    model_name = mdb.models.items()[0][0] # Get first model
    s = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(980.0, 300.0))
    p = mdb.models[model_name].Part(name='Beam', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models[model_name].parts['Beam']
    p.BaseSolidExtrude(sketch=s, depth=75.0)
    s.unsetPrimaryObject()
    p = mdb.models[model_name].parts['Beam']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models[model_name].sketches['__profile__']
    
def FRP():
    import part
    import sketch
    
    model_name = mdb.models.items()[0][0] # Get first model
    s1 = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0) 
    s1.setPrimaryObject(option=STANDALONE)
    s1.Line(point1=(0.0, 0.0), point2=(-260.0, 0.0))

    p = mdb.models[model_name].Part(name='FRP', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models[model_name].parts['FRP']
    p.BaseShellExtrude(sketch=s1, depth=75.0)
    s1.unsetPrimaryObject()
    p = mdb.models[model_name].parts['FRP']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models[model_name].sketches['__profile__']


def Lower_Bar():
    import part
    import sketch
    
    model_name = mdb.models.items()[0][0] # Get first model
    s = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    s.setPrimaryObject(option=STANDALONE)
    s.Line(point1=(0.0, 0.0), point2=(-980.0, 0.0))

    p = mdb.models[model_name].Part(name='Lower_Bar', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models[model_name].parts['Lower_Bar']
    p.BaseWire(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models[model_name].parts['Lower_Bar']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models[model_name].sketches['__profile__']


def Upper_Bar():
    import part
    import sketch

    model_name = mdb.models.items()[0][0] # Get first model
    s = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    s.setPrimaryObject(option=STANDALONE)
    s.Line(point1=(0.0, 0.0), point2=(-980.0, 0.0))

    p = mdb.models[model_name].Part(name='Upper_Bar', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models[model_name].parts['Upper_Bar']
    p.BaseWire(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models[model_name].parts['Upper_Bar']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models[model_name].sketches['__profile__']

def Tie():
    import part
    import sketch
    
    width = 60
    height = 270
    
    model_name = mdb.models.items()[0][0] # Get first model
    s1 = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)

    s1.Line(point1=(0.0, -height/2), point2=(0.0, height/2))
    s1.Line(point1=(0.0, height/2), point2=(-width, height/2))
    s1.Line(point1=(0.0, -height/2), point2=(-width, -height/2))

    p = mdb.models[model_name].Part(name='Tie', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models[model_name].parts['Tie']
    p.BaseWire(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models[model_name].parts['Tie']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models[model_name].sketches['__profile__']

def ASSEMBLY_TEST():
    from assembly import *
    
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Lower_Bar', 
        part=mdb.models['Model-1'].parts['Lower_Bar'])
    
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Upper_Bar', 
        part=mdb.models['Model-1'].parts['Upper_Bar'])
        
    a = mdb.models['Model-1'].rootAssembly
    a.translate(instanceList=('Upper_Bar', ), vector=(0,270,0))

    # Create Tie, rotate and move it to specified location
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Tie', 
        part=mdb.models['Model-1'].parts['Tie'])
    a = mdb.models['Model-1'].rootAssembly
    a.rotate(instanceList=('Tie', ), axisPoint=(0, 270.0, 0.0), 
        axisDirection=(0.0, -270.0, 0.0), angle=-90.0)
    a.translate(instanceList=('Tie', ), vector=(-50,135,0))  

    # Copy the tie with linear array pattern
    a = mdb.models['Model-1'].rootAssembly
    a.LinearInstancePattern(instanceList=('Tie', ), direction1=(-1.0, 0.0, 0.0), 
        direction2=(0.0, 1.0, 0.0), number1=7, number2=1, spacing1=100.0, spacing2=270.0)
    
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='FRP', 
        part=mdb.models['Model-1'].parts['FRP'])
        
    a = mdb.models['Model-1'].rootAssembly
    a.translate(instanceList=('FRP', ), vector=(-50,0,0))  
    
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Beam', 
        part=mdb.models['Model-1'].parts['Beam'])
        
    a = mdb.models['Model-1'].rootAssembly
    a.translate(instanceList=('Beam', ), vector=(-980,-15,0))  


def hail_part_1():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    from abaqus import getInput
    
    """
    GET INPUT FROM USER
    """
    userDiameter = float(getInput('Enter the diameter of object:\nExample: 0.0508'))

    """
    PART CREATION START
    """
    # Define variables
    diameter = userDiameter
    radius = diameter / 2
    
    partName = 'Hail'
    model_name = mdb.models.items()[0][0] # Get first model
    
    p1 = (0, 0.125 * diameter, 0)
    p2 = (0, 0.65 * diameter, 0)
    p3 = (0.2 * diameter, 0.125 * diameter, 0)
    p4 = (0.2 * diameter, 0.65 * diameter, 0)
    p5 = (0, 0.125 * diameter, 0.2 * diameter)
    p6 = (0, 0.65 * diameter, 0.2 * diameter)
    p7 = (0.2 * diameter, 0.125 * diameter, 0.2 * diameter)
    p8 = (0.2 * diameter, 0.65 * diameter, 0.2 * diameter)
    points = [p1, p2, p3, p4, p5, p6, p7, p8]
    
    # Create Part
    s = mdb.models[model_name].ConstrainedSketch(name='__profile__', sheetSize=2.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -1.0), point2=(0.0, 1.0))
    s.FixedConstraint(entity=g[2])
    s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, radius))

    s.Line(point1=(0.0, radius), point2=(0.0, -radius))
    s.VerticalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s.CoincidentConstraint(entity1=v[2], entity2=g[2], addUndoState=False)
    s.autoTrimCurve(curve1=g[3], point1=(-0.021746352314949, 0.00604132935404778))
    s.move(vector=(0.0, radius), objectList=(g[2], g[4], g[5]))
    p = mdb.models[model_name].Part(name=partName, dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models[model_name].parts[partName]
    p.BaseSolidRevolve(sketch=s, angle=90.0, flipRevolveDirection=OFF)
    s.unsetPrimaryObject()
    p = mdb.models[model_name].parts[partName]
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models[model_name].sketches['__profile__']
    """
    PART CREATION END
    """
   
    
    """
    DATUM POINT CREATION
    """
    p = mdb.models[model_name].parts[partName]
    for point in points:
        p.DatumPointByCoordinate(coords=point)
    """
    DATUM POINT CREATION END
    """
    
    """
    CREATE EDGES FROM DATUM POINTS
    """
    p = mdb.models[model_name].parts[partName]
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#2 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=d[3], point2=d[7], faces=pickedFaces)
    p = mdb.models[model_name].parts[partName]
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#2 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=d1[7], point2=d1[6], faces=pickedFaces)
    p = mdb.models[model_name].parts[partName]
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#2 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=d[6], point2=d[2], faces=pickedFaces)
    p = mdb.models[model_name].parts[partName]
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#8 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=d1[3], point2=d1[5], faces=pickedFaces)
    p = mdb.models[model_name].parts[partName]
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    e = p.edges
    pickedEdges =(e[0], e[4], e[5], e[7])
    p.PartitionCellBySweepEdge(sweepPath=e[8], cells=pickedCells, 
        edges=pickedEdges)
    """
    ENDS OF CREATION OF DATUM EDGES
    """
    
    """
    START OF POINT PROJECTION
    """
    p = mdb.models[model_name].parts[partName]
    f, d = p.faces, p.datums
    p.DatumPointByProjOnFace(point=d[5], face=f[5])
    p = mdb.models[model_name].parts[partName]
    f1, d1 = p.faces, p.datums
    p.DatumPointByProjOnFace(point=d1[9], face=f1[5])
    p = mdb.models[model_name].parts[partName]
    f, d = p.faces, p.datums
    p.DatumPointByProjOnFace(point=d[7], face=f[5])
    p = mdb.models[model_name].parts[partName]
    f1, d1 = p.faces, p.datums
    p.DatumPointByProjOnFace(point=d1[4], face=f1[5])
    p = mdb.models[model_name].parts[partName]
    f, d = p.faces, p.datums
    p.DatumPointByProjOnFace(point=d[8], face=f[5])
    p = mdb.models[model_name].parts[partName]
    f1, d1 = p.faces, p.datums
    p.DatumPointByProjOnFace(point=d1[6], face=f1[5])
    """
    END OF POINT PROJECTION
    """
    
    """
    START OF EXTERIOR SLICING
    """
    p = mdb.models[model_name].parts[partName]
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#80 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=d1[5], point2=d1[15], faces=pickedFaces)
    p = mdb.models[model_name].parts[partName]
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#100 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=d[4], point2=d[18], faces=pickedFaces)

    p = mdb.models[model_name].parts[partName]
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#40 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=d1[6], point2=d1[20], faces=pickedFaces)
    p = mdb.models[model_name].parts[partName]
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=d[7], point2=d[17], faces=pickedFaces)

    p = mdb.models[model_name].parts[partName]
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#200 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=d1[16], point2=d1[15], faces=pickedFaces)

    p = mdb.models[model_name].parts[partName]
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#200 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=d[16], point2=d[17], faces=pickedFaces)

    p = mdb.models[model_name].parts[partName]
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=d1[16], point2=d1[19], faces=pickedFaces)

    p = mdb.models[model_name].parts[partName]
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=d[19], point2=d[18], faces=pickedFaces)

    p = mdb.models[model_name].parts[partName]
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#2 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=d1[19], point2=d1[20], faces=pickedFaces)
    """
    END OF EXTERIOR SLICING
    """
    
    """
    START OF VERTICAL DATUM PLANE
    """
    p = mdb.models[model_name].parts[partName]
    v, d = p.vertices, p.datums
    p.DatumPlaneByThreePoints(point1=v[2], point2=v[8], point3=d[16])

    p = mdb.models[model_name].parts[partName]
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    d1 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d1[30], cells=pickedCells)
    """
    END OF VERTICAL DATUM PLANE
    """
    
    """
    FIRST INSIDE FIX
    """
    p = mdb.models[model_name].parts[partName]
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#a0400 ]', ), )
    leaf = dgm.LeafFromGeometry(faceSeq=faces)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)

    p = mdb.models[model_name].parts[partName]
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#2 ]', ), )
    v1, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=d[19], point2=d[8], faces=pickedFaces)

    p = mdb.models[model_name].parts[partName]
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    v, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=d1[9], point2=d1[16], faces=pickedFaces)
    p = mdb.models[model_name].parts[partName]
    c = p.cells
    e = p.edges
    pickedEdges =(e[0], e[22], e[24], e[12])
    p.PartitionCellByPatchNEdges(cell=c[0], edges=pickedEdges)

    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.replace(leaf=leaf)
    """
    END OF FIRST INSIDE FIX
    """
    
    """
    START OF REPLACING FACES
    """
    p = mdb.models[model_name].parts[partName]
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#100000 ]', ), )
    leaf = dgm.LeafFromGeometry(faceSeq=faces)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)

    p = mdb.models[model_name].parts[partName]
    c1 = p.cells
    e1 = p.edges
    pickedEdges =(e1[32], e1[27], e1[19], e1[5])
    p.PartitionCellByPatchNEdges(cell=c1[1], edges=pickedEdges)
    p = mdb.models[model_name].parts[partName]
    f = p.faces
    p.RemoveFaces(faceList = f[5:6], deleteCells=False)

    p = mdb.models[model_name].parts[partName]
    f1 = p.faces
    p.ReplaceFaces(faceList = f1[8:10], stitch=True)

    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)

    p = mdb.models[model_name].parts[partName]
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#404000 ]', ), )
    leaf = dgm.LeafFromGeometry(faceSeq=faces)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
    p = mdb.models[model_name].parts[partName]
    c = p.cells
    e = p.edges
    pickedEdges =(e[5], e[18], e[29], e[31])
    p.PartitionCellByPatchNEdges(cell=c[0], edges=pickedEdges)

    p = mdb.models[model_name].parts[partName]
    c1 = p.cells
    e1 = p.edges
    pickedEdges =(e1[6], e1[19], e1[22], e1[29])
    p.PartitionCellByPatchNEdges(cell=c1[1], edges=pickedEdges)

    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    p = mdb.models[model_name].parts[partName]
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#100000 ]', ), )
    leaf = dgm.LeafFromGeometry(faceSeq=faces)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
    p = mdb.models[model_name].parts[partName]
    c = p.cells
    e = p.edges
    pickedEdges =(e[0], e[30], e[4], e[15])
    p.PartitionCellByPatchNEdges(cell=c[0], edges=pickedEdges)
    p = mdb.models[model_name].parts[partName]
    f = p.faces
    p.RemoveFaces(faceList = f[7:8], deleteCells=False)
    p = mdb.models[model_name].parts[partName]
    f1 = p.faces
    p.RemoveFaces(faceList = f1[6:7], deleteCells=False)
    p = mdb.models[model_name].parts[partName]
    f = p.faces
    p.ReplaceFaces(faceList = f[7:8]+f[18:19], stitch=True)
    p = mdb.models[model_name].parts[partName]
    f1 = p.faces
    p.ReplaceFaces(faceList = f1[6:7]+f1[17:18], stitch=True)
    p = mdb.models[model_name].parts[partName]
    f = p.faces
    p.ReplaceFaces(faceList = f[7:8]+f[19:20], stitch=True)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.replace(leaf=leaf)
    """
    END OF REPLACING FACES
    """
    
    """
    DATUM PLANES AND MIRRORING
    """
    p = mdb.models[model_name].parts[partName]
    p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=0.0)
    p = mdb.models[model_name].parts[partName]
    p.features['Datum plane-2'].setValues(offset= radius)
    p = mdb.models[model_name].parts[partName]
    p.regenerate()
    p = mdb.models[model_name].parts[partName]
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1f ]', ), )
    d = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d[46], cells=pickedCells)
    p = mdb.models[model_name].parts[partName]
    p.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=0.0)
    p = mdb.models[model_name].parts[partName]
    p.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=0.0)
    p = mdb.models[model_name].parts[partName]
    d1 = p.datums
    p.Mirror(mirrorPlane=d1[48], keepOriginal=ON, keepInternalBoundaries=ON)
    p = mdb.models[model_name].parts[partName]
    d = p.datums
    p.Mirror(mirrorPlane=d[49], keepOriginal=ON, keepInternalBoundaries=ON)
    """
    END OF DATUM AND MIRRORING
    """
    
    """
    MATERIAL START
    """
    mdb.models[model_name].Material(name='Ice')
    mdb.models[model_name].materials['Ice'].Elastic(table=((9380000000.0, 0.33), ))
    mdb.models[model_name].materials['Ice'].Density(table=((900.0, ), ))
    mdb.models[model_name].materials['Ice'].Plastic(table=((5200000.0, 0.0), (
        5200000.0, 1.0)))
    mdb.models[model_name].materials['Ice'].plastic.RateDependent(type=YIELD_RATIO, 
        table=((1.0, 0.0), (1.01, 0.1), (1.495577759, 0.5), (1.709011483, 1.0), 
        (2.204589242, 5.0), (2.418022966, 10.0), (2.913600725, 50.0), (
        3.127034449, 100.0), (3.622612208, 500.0), (3.836045932, 1000.0), (
        4.331623691, 5000.0), (4.545057415, 10000.0), (5.040635174, 50000.0), (
        5.254068897, 100000.0), (5.749646657, 500000.0), (5.96308038, 
        1000000.0)))
    
    """
    MATERIAL END
    """
    
    
def hail_part_2():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    from abaqus import getInput
    
    partName = 'Hail'
    model_name = mdb.models.items()[0][0] # Get first model
    
    """
    GET INPUT FROM USER
    """
    diameter = float(getInput('Enter the diameter of object:\nExample: 0.0508'))
    userVelocity = float(getInput('Enter the velocity of object:\nExample: 61.3'))

    """
    MESHING
    """
    p = mdb.models[model_name].parts[partName]
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#ffffffff:4 ]', ), )
    # Create seed for all part
    p.seedEdgeBySize(edges=pickedEdges, size= diameter * 0.01, deviationFactor=0.1, constraint=FINER)

    p = mdb.models[model_name].parts[partName]
    e = p.edges
    pickedEdges1 = e.getSequenceFromMask(mask=(
        '[#12d000 #2c00000 #8a800000 #500000 ]', ), )
    pickedEdges2 = e.getSequenceFromMask(mask=('[#0 #10000080 #100 ]', ), )
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
        end2Edges=pickedEdges2, minSize=0.0001016, maxSize= diameter * 0.01, 
        constraint=FINER)
    p = mdb.models[model_name].parts[partName]
    e = p.edges
    pickedEdges1 = e.getSequenceFromMask(mask=(
        '[#12d000 #2c00000 #8a800000 #500000 ]', ), )
    pickedEdges2 = e.getSequenceFromMask(mask=('[#0 #10000080 #100 ]', ), )
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
        end2Edges=pickedEdges2, ratio=4.0, number=60, constraint=FINER)

    p = mdb.models[model_name].parts[partName]
    e = p.edges
    pickedEdges1 = e.getSequenceFromMask(mask=(
        '[#3000000 #80000000 #0 #1000000c ]', ), )
    pickedEdges2 = e.getSequenceFromMask(mask=('[#10000000 #0 #2 ]', ), )
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
        end2Edges=pickedEdges2, ratio=4.0, number=30, constraint=FINER)

    p = mdb.models[model_name].parts[partName]
    e = p.edges
    pickedEdges1 = e.getSequenceFromMask(mask=(
        '[#20002000 #200020 #1000004 #40200440 ]', ), )
    pickedEdges2 = e.getSequenceFromMask(mask=('[#0 #10 #80 ]', ), )
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
        end2Edges=pickedEdges2, ratio=4.0, number=40, constraint=FINER)
    p = mdb.models[model_name].parts[partName]
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#210000 #21000003 #44000020 #4800100 ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=40, constraint=FINER)
    p = mdb.models[model_name].parts[partName]
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#210000 #21000003 #44000020 #4800100 ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=30, constraint=FINER)
    
    p = mdb.models[model_name].parts[partName]
    p.generateMesh()
    
    p = mdb.models[model_name].parts[partName]
    n = p.nodes
    nodes = n.getSequenceFromMask(mask=('[#ffffffff:80683 #7ff ]', ), )
    p.Set(nodes=nodes, name='hail_all_nodes')
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    p = mdb.models[model_name].parts[partName]
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#6c6c6c6c ]', ), )
    leaf = dgm.LeafFromGeometry(cellSeq=cells)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)

    p = mdb.models[model_name].parts[partName]
    n = p.nodes
    nodes = n.getSequenceFromMask(mask=('[#40000 ]', ), )
    p.Set(nodes=nodes, name='hail_node')

    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].partDisplay.displayGroup.replace(leaf=leaf)
    p = mdb.models[model_name].parts[partName]
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#5078018 #3003c0 #c002801e #3 ]', ), 
        )
    p.Surface(side1Faces=side1Faces, name='hail_surface')

    """
    END OF MESHING
    """
    
    """
    OTHER STUFF
    """
    
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
        

    a = mdb.models[model_name].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, optimizationTasks=OFF, 
        geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    a = mdb.models[model_name].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models[model_name].parts[partName]
    a.Instance(name='Hail-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
    a = mdb.models[model_name].rootAssembly
    region = a.instances['Hail-1'].sets['hail_all_nodes']
    mdb.models[model_name].Velocity(name='Predefined Field-1', region=region, 
        field='', distributionType=MAGNITUDE, velocity1=0.0, velocity2=-userVelocity, 
        velocity3=0.0, omega=0.0)
    p = mdb.models[model_name].parts[partName]
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    s = mdb.models[model_name].ConstrainedSketch(name='__profile__', sheetSize=20.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.Line(point1=(0.0, 0.0), point2=(0.1, 0.0))
    s.HorizontalConstraint(entity=g[2], addUndoState=False)

    p = mdb.models[model_name].Part(name='Part-2', dimensionality=THREE_D, 
        type=ANALYTIC_RIGID_SURFACE)
    p = mdb.models[model_name].parts['Part-2']
    p.AnalyticRigidSurfExtrude(sketch=s, depth=0.1)
    s.unsetPrimaryObject()
    p = mdb.models[model_name].parts['Part-2']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models[model_name].sketches['__profile__']
    a = mdb.models[model_name].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models[model_name].ExplicitDynamicsStep(name='Step-1', previous='Initial', 
        timePeriod=0.003, linearBulkViscosity=1.2, quadBulkViscosity=0.0)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')

    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=OFF)
    a1 = mdb.models[model_name].rootAssembly
    p = mdb.models[model_name].parts['Part-2']
    a1.Instance(name='plate_instance', part=p, dependent=ON)

    a = mdb.models[model_name].rootAssembly
    e1 = a.instances['plate_instance'].edges
    a.DatumPointByMidPoint(point1=a.instances['plate_instance'].InterestingPoint(
        edge=e1[0], rule=MIDDLE), 
        point2=a.instances['plate_instance'].InterestingPoint(edge=e1[2], 
        rule=MIDDLE))
    a = mdb.models[model_name].rootAssembly
    d11 = a.datums
    a.ReferencePoint(point=d11[6])
    a1 = mdb.models[model_name].rootAssembly
    a1.translate(instanceList=('plate_instance', ), vector=(-0.05, 0.0, 0.0))

    a1 = mdb.models[model_name].rootAssembly
    a1.translate(instanceList=('plate_instance', ), vector=(0.0, -0.00025, 0.0))

    p1 = mdb.models[model_name].parts['Part-2']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models[model_name].parts.changeKey(fromName='Part-2', toName='Plate')

    p = mdb.models[model_name].parts['Plate']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Surface(side1Faces=side1Faces, name='plate_surface')
    a1 = mdb.models[model_name].rootAssembly
    a1.regenerate()
    a = mdb.models[model_name].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)

    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models[model_name].parts['Plate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models[model_name].parts[partName]
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    mdb.models[model_name].HomogeneousSolidSection(name='Ice_Section', material='Ice', 
        thickness=None)
    p = mdb.models[model_name].parts[partName]
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#ffffffff ]', ), )
    region = regionToolset.Region(cells=cells)
    p = mdb.models[model_name].parts[partName]
    p.SectionAssignment(region=region, sectionName='Ice_Section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=RELAX_STIFFNESS, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=EXPLICIT)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)
    p = mdb.models[model_name].parts[partName]
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#ffffffff ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    a = mdb.models[model_name].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
        constraints=ON, connectors=ON, engineeringFeatures=ON)
    mdb.models[model_name].ContactProperty('IntProp-1')
    mdb.models[model_name].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=FRICTIONLESS)
    mdb.models[model_name].interactionProperties['IntProp-1'].NormalBehavior(
        pressureOverclosure=HARD, allowSeparation=ON, 
        constraintEnforcementMethod=DEFAULT)
    mdb.models[model_name].ContactExp(name='Int-1', createStepName='Step-1')
    mdb.models[model_name].interactions['Int-1'].includedPairs.setValuesInStep(
        stepName='Step-1', useAllstar=ON)
    mdb.models[model_name].interactions['Int-1'].contactPropertyAssignments.appendInStep(
        stepName='Step-1', assignments=((GLOBAL, SELF, 'IntProp-1'), ))

    a = mdb.models[model_name].rootAssembly
    s1 = a.instances['plate_instance'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region5=regionToolset.Region(side1Faces=side1Faces1)
    a = mdb.models[model_name].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[7], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models[model_name].RigidBody(name='plate_rigid', refPointRegion=region1, 
        surfaceRegion=region5)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, interactions=OFF, constraints=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    a = mdb.models[model_name].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[7], )
    region = regionToolset.Region(referencePoints=refPoints1)
    mdb.models[model_name].DisplacementBC(name='plate_boundary', createStepName='Initial', 
        region=region, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
        
    # Set mesh element deletion to nodalOutputPrecision
    
    p = mdb.models['Model-1'].parts['Hail']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=RELAX_STIFFNESS, distortionControl=DEFAULT, 
        elemDeletion=OFF)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=EXPLICIT, 
        secondOrderAccuracy=OFF, distortionControl=DEFAULT)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=EXPLICIT, 
        secondOrderAccuracy=OFF, distortionControl=DEFAULT)
    p = mdb.models['Model-1'].parts['Hail']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#ff ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))