from abaqus import *
from abaqusConstants import *

model_name = mdb.models.items()[0][0]

def main(beam_width, beam_height, beam_depth, frp_width, frp_height, upperbar_width, lowerbar_width,
	tie_width, tie_height, material_steel_elastic, material_steel_plastic,
	material_cfrp_elastic, material_density_concrete, material_elastic_concrete,
	material_plasticity_concrete, material_compressive_behavior_concrete,
	material_compression_damage_concrete, material_tensile_behavior_concrete,
	material_tensile_damage_concrete):
    
    data = [beam_width, beam_height, beam_depth, frp_width, frp_height, upperbar_width, lowerbar_width, tie_width, tie_height, material_steel_elastic, material_steel_plastic, material_cfrp_elastic, material_density_concrete, material_elastic_concrete, material_plasticity_concrete, material_compressive_behavior_concrete, material_compression_damage_concrete, material_tensile_behavior_concrete, material_tensile_damage_concrete]
    
    RC_Beam(data)
    FRP(data)
    Lower_Bar(data)
    Upper_Bar(data)
    Tie(data)


def RC_Beam(data):
    
    s = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(data[0], data[1]))
    p = mdb.models[model_name].Part(name='Beam', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models[model_name].parts['Beam']
    p.BaseSolidExtrude(sketch=s, depth=data[2])
    s.unsetPrimaryObject()
    p = mdb.models[model_name].parts['Beam']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models[model_name].sketches['__profile__']
    
def FRP(data):
    
    s1 = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0) 
    s1.setPrimaryObject(option=STANDALONE)
    s1.Line(point1=(0.0, 0.0), point2=(-data[3], 0.0))

    p = mdb.models[model_name].Part(name='FRP', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models[model_name].parts['FRP']
    p.BaseShellExtrude(sketch=s1, depth=data[4])
    s1.unsetPrimaryObject()
    p = mdb.models[model_name].parts['FRP']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models[model_name].sketches['__profile__']


def Lower_Bar(data):

    s = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    s.setPrimaryObject(option=STANDALONE)
    s.Line(point1=(0.0, 0.0), point2=(-data[6], 0.0))

    p = mdb.models[model_name].Part(name='Lower_Bar', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models[model_name].parts['Lower_Bar']
    p.BaseWire(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models[model_name].parts['Lower_Bar']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models[model_name].sketches['__profile__']


def Upper_Bar(data):

    s = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    s.setPrimaryObject(option=STANDALONE)
    s.Line(point1=(0.0, 0.0), point2=(-data[5], 0.0))

    p = mdb.models[model_name].Part(name='Upper_Bar', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models[model_name].parts['Upper_Bar']
    p.BaseWire(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models[model_name].parts['Upper_Bar']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models[model_name].sketches['__profile__']

def Tie(data):
    
    s1 = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)

    s1.Line(point1=(0.0, -data[8]/2), point2=(0.0, data[8]/2))
    s1.Line(point1=(0.0, data[8]/2), point2=(-data[7], data[8]/2))
    s1.Line(point1=(0.0, -data[8]/2), point2=(-data[7], -data[8]/2))

    p = mdb.models[model_name].Part(name='Tie', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models[model_name].parts['Tie']
    p.BaseWire(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models[model_name].parts['Tie']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models[model_name].sketches['__profile__']
