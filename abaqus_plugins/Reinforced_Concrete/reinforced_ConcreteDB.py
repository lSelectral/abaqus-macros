# Do not edit this file or it may not load correctly
# if you try to open it with the RSG Dialog Builder.

# Note: thisDir is defined by the Activator class when
#       this file gets exec'd

from rsg.rsgGui import *
from abaqusConstants import INTEGER, FLOAT
dialogBox = RsgDialog(title='REINFORCED CONCRETE', kernelModule='kernel', kernelFunction='main', includeApplyBtn=True, includeSeparator=False, okBtnText='OK', applyBtnText='Apply', execDir=thisDir)
RsgTabBook(name='TabBook_2', p='DialogBox', layout='0')
RsgTabItem(name='TabItem_4', p='TabBook_2', text='PART CREATION')
RsgHorizontalFrame(name='HFrame_2', p='TabItem_4', layout='LAYOUT_FILL_X|LAYOUT_FILL_Y', pl=0, pr=0, pt=0, pb=0)
RsgGroupBox(name='GroupBox_1', p='HFrame_2', text='BEAM', layout='0')
RsgLabel(p='GroupBox_1', text='3D Deformable Solid Extrusion', useBoldFont=False)
RsgVerticalAligner(name='VAligner_1', p='GroupBox_1', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='VAligner_1', fieldType='Integer', ncols=12, labelText='Width', keyword='beam_width', default='980')
RsgTextField(p='VAligner_1', fieldType='Integer', ncols=12, labelText='Height', keyword='beam_height', default='300')
RsgTextField(p='VAligner_1', fieldType='Integer', ncols=12, labelText='Depth', keyword='beam_depth', default='75')
RsgGroupBox(name='GroupBox_2', p='HFrame_2', text='FRP', layout='0')
RsgLabel(p='GroupBox_2', text='3D Deformable Shell Extrusion', useBoldFont=False)
RsgVerticalAligner(name='VAligner_3', p='GroupBox_2', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='VAligner_3', fieldType='Integer', ncols=12, labelText='Width', keyword='frp_width', default='260')
RsgTextField(p='VAligner_3', fieldType='Integer', ncols=12, labelText='Height', keyword='frp_height', default='75')
RsgHorizontalFrame(name='HFrame_3', p='TabItem_4', layout='LAYOUT_FILL_X|LAYOUT_FILL_Y', pl=0, pr=0, pt=0, pb=0)
RsgGroupBox(name='GroupBox_5', p='HFrame_3', text='Tie', layout='0')
RsgLabel(p='GroupBox_5', text='3D Deformable Wire', useBoldFont=False)
RsgVerticalAligner(name='VAligner_4', p='GroupBox_5', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Width', keyword='tie_width', default='60')
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Height', keyword='tie_height', default='270')
RsgGroupBox(name='GroupBox_4', p='HFrame_3', text='Upper Bar', layout='0')
RsgLabel(p='GroupBox_4', text='3D Deformable Wire', useBoldFont=False)
RsgTextField(p='GroupBox_4', fieldType='Integer', ncols=12, labelText='Width', keyword='upperbar_width', default='980')
RsgGroupBox(name='GroupBox_3', p='HFrame_3', text='Lower Bar', layout='0')
RsgLabel(p='GroupBox_3', text='3D Deformable Wire', useBoldFont=False)
RsgTextField(p='GroupBox_3', fieldType='Integer', ncols=12, labelText='Width', keyword='lowerbar_width', default='980')
RsgTabItem(name='TabItem_5', p='TabBook_2', text='MATERIAL')
RsgTabBook(name='TabBook_3', p='TabItem_5', layout='0')
RsgTabItem(name='TabItem_6', p='TabBook_3', text='STEEL')
RsgTabBook(name='TabBook_4', p='TabItem_6', layout='0')
RsgTabItem(name='TabItem_11', p='TabBook_4', text='Elastic')
RsgTable(p='TabItem_11', numRows=1, columnData=[("Young's Modulus", 'Float', 160), ("Poisson's Ratio", 'Float', 160)], showRowNumbers=True, showGrids=True, keyword='material_steel_elastic', popupFlags='AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS')
RsgTabItem(name='TabItem_12', p='TabBook_4', text='Plastic')
RsgTable(p='TabItem_12', numRows=1, columnData=[('Yield Stress', 'Float', 160), ('Plastic Strain', 'Float', 160)], showRowNumbers=True, showGrids=True, keyword='material_steel_plastic', popupFlags='AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS')
RsgTabItem(name='TabItem_8', p='TabBook_3', text='CFRP')
RsgLabel(p='TabItem_8', text='ELASTIC', useBoldFont=False)
RsgTable(p='TabItem_8', numRows=1, columnData=[("Young's Modulus", 'Float', 160), ("Poisson's Ratio", 'Float', 160)], showRowNumbers=True, showGrids=True, keyword='material_cfrp_elastic', popupFlags='AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS')
RsgTabItem(name='TabItem_7', p='TabBook_3', text='Concrete CDP')
RsgTabBook(name='TabBook_6', p='TabItem_7', layout='LAYOUT_FILL_X')
RsgTabItem(name='TabItem_15', p='TabBook_6', text='Density')
RsgTable(p='TabItem_15', numRows=1, columnData=[('Mass Density', 'Float', 160)], showRowNumbers=True, showGrids=True, keyword='material_density_concrete', popupFlags='AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS')
RsgTabItem(name='TabItem_17', p='TabBook_6', text='Elastic')
RsgTable(p='TabItem_17', numRows=5, columnData=[("Young's Modulus", 'Float', 160), ("Poisoon's Ratio", 'Float', 160)], showRowNumbers=True, showGrids=True, keyword='material_elastic_concrete', popupFlags='AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS')
RsgTabItem(name='TabItem_18', p='TabBook_6', text='Concrete Damaged Plasticity')
RsgTabBook(name='TabBook_7', p='TabItem_18', layout='LAYOUT_FILL_X')
RsgTabItem(name='TabItem_21', p='TabBook_7', text='Plasticity')
RsgTable(p='TabItem_21', numRows=1, columnData=[('Dilation Angle', 'Float', 100), ('Eccentricity', 'Float', 100), ('fb0/fc0', 'Float', 100), ('K', 'Float', 100), ('Viscosity Parameter', 'Float', 110)], showRowNumbers=True, showGrids=True, keyword='material_plasticity_concrete', popupFlags='AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS')
RsgTabItem(name='TabItem_23', p='TabBook_7', text='Compressive Behavior')
RsgTabBook(name='TabBook_8', p='TabItem_23', layout='LAYOUT_FILL_X')
RsgTabItem(name='TabItem_26', p='TabBook_8', text='Value')
RsgTable(p='TabItem_26', numRows=5, columnData=[('Yield Stress', 'Float', 160), ('Inelastic Strain', 'Float', 160)], showRowNumbers=True, showGrids=True, keyword='material_compressive_behavior_concrete', popupFlags='AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS')
RsgTabItem(name='TabItem_27', p='TabBook_8', text='Concrete Compression Damage')
RsgTable(p='TabItem_27', numRows=5, columnData=[('Damage Parameter', 'Float', 160), ('Inelastic Strain', 'Float', 160)], showRowNumbers=True, showGrids=True, keyword='material_compression_damage_concrete', popupFlags='AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS')
RsgTabItem(name='TabItem_24', p='TabBook_7', text='Tensile Behavior')
RsgTabBook(name='TabBook_9', p='TabItem_24', layout='LAYOUT_FILL_X')
RsgTabItem(name='TabItem_28', p='TabBook_9', text='Value')
RsgTable(p='TabItem_28', numRows=5, columnData=[('Yield Stress', 'Float', 160), ('Cracking Strain', 'Float', 160)], showRowNumbers=True, showGrids=True, keyword='material_tensile_behavior_concrete', popupFlags='AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS')
RsgTabItem(name='TabItem_29', p='TabBook_9', text='Concrete Tension Damage')
RsgTable(p='TabItem_29', numRows=5, columnData=[('Damage Parameter', 'Float', 160), ('Cracking Strain', 'Float', 160)], showRowNumbers=True, showGrids=True, keyword='material_tensile_damage_concrete', popupFlags='AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS')
RsgTabItem(name='TabItem_30', p='TabBook_2', text='Assembly')
RsgGroupBox(name='GroupBox_6', p='TabItem_30', text='Placement', layout='0')
RsgHorizontalFrame(name='HFrame_4', p='GroupBox_6', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgVerticalAligner(name='VAligner_6', p='HFrame_4', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='VAligner_6', fieldType='Integer', ncols=12, labelText='First Tie Distance from Origin', keyword='first_tie_distance_from_origin', default='-5')
RsgTextField(p='VAligner_6', fieldType='Integer', ncols=12, labelText='Tie Count', keyword='tie_count', default='8')
dialogBox.show()