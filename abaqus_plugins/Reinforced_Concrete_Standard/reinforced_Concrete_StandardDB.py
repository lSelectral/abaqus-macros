from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class Reinforced_Concrete_StandardDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'REINFORCED CONCRETE',
            self.OK|self.APPLY|self.CANCEL, )
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            

        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('Apply')
            
        TabBook_2 = FXTabBook(p=self, tgt=None, sel=0,
            opts=TABBOOK_NORMAL,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)
        tabItem = FXTabItem(p=TabBook_2, text='PART CREATION', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_4 = FXVerticalFrame(p=TabBook_2,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        HFrame_2 = FXHorizontalFrame(p=TabItem_4, opts=LAYOUT_FILL_X|LAYOUT_FILL_Y, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_1 = FXGroupBox(p=HFrame_2, text='BEAM', opts=FRAME_GROOVE)
        l = FXLabel(p=GroupBox_1, text='3D Deformable Solid Extrusion', opts=JUSTIFY_LEFT)
        VAligner_1 = AFXVerticalAligner(p=GroupBox_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VAligner_1, ncols=12, labelText='Width', tgt=form.beam_widthKw, sel=0)
        AFXTextField(p=VAligner_1, ncols=12, labelText='Height', tgt=form.beam_heightKw, sel=0)
        AFXTextField(p=VAligner_1, ncols=12, labelText='Depth', tgt=form.beam_depthKw, sel=0)
        GroupBox_2 = FXGroupBox(p=HFrame_2, text='FRP', opts=FRAME_GROOVE)
        l = FXLabel(p=GroupBox_2, text='3D Deformable Shell Extrusion', opts=JUSTIFY_LEFT)
        VAligner_3 = AFXVerticalAligner(p=GroupBox_2, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='Width', tgt=form.frp_widthKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='Height', tgt=form.frp_heightKw, sel=0)
        HFrame_3 = FXHorizontalFrame(p=TabItem_4, opts=LAYOUT_FILL_X|LAYOUT_FILL_Y, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_5 = FXGroupBox(p=HFrame_3, text='Tie', opts=FRAME_GROOVE)
        l = FXLabel(p=GroupBox_5, text='3D Deformable Wire', opts=JUSTIFY_LEFT)
        VAligner_4 = AFXVerticalAligner(p=GroupBox_5, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Width', tgt=form.tie_widthKw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Height', tgt=form.tie_heightKw, sel=0)
        GroupBox_4 = FXGroupBox(p=HFrame_3, text='Upper Bar', opts=FRAME_GROOVE)
        l = FXLabel(p=GroupBox_4, text='3D Deformable Wire', opts=JUSTIFY_LEFT)
        AFXTextField(p=GroupBox_4, ncols=12, labelText='Width', tgt=form.upperbar_widthKw, sel=0)
        GroupBox_3 = FXGroupBox(p=HFrame_3, text='Lower Bar', opts=FRAME_GROOVE)
        l = FXLabel(p=GroupBox_3, text='3D Deformable Wire', opts=JUSTIFY_LEFT)
        AFXTextField(p=GroupBox_3, ncols=12, labelText='Width', tgt=form.lowerbar_widthKw, sel=0)
        tabItem = FXTabItem(p=TabBook_2, text='MATERIAL', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_5 = FXVerticalFrame(p=TabBook_2,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        TabBook_3 = FXTabBook(p=TabItem_5, tgt=None, sel=0,
            opts=TABBOOK_NORMAL,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)
        tabItem = FXTabItem(p=TabBook_3, text='STEEL', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_6 = FXVerticalFrame(p=TabBook_3,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        TabBook_4 = FXTabBook(p=TabItem_6, tgt=None, sel=0,
            opts=TABBOOK_NORMAL,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)
        tabItem = FXTabItem(p=TabBook_4, text='Elastic', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_11 = FXVerticalFrame(p=TabBook_4,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        vf = FXVerticalFrame(TabItem_11, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 2, 3, 2, 3, form.material_steel_elasticKw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 160)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 160)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setLeadingRowLabels("Young's Modulus\tPoisson's Ratio")
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        tabItem = FXTabItem(p=TabBook_4, text='Plastic', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_12 = FXVerticalFrame(p=TabBook_4,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        vf = FXVerticalFrame(TabItem_12, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 2, 3, 2, 3, form.material_steel_plasticKw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 160)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 160)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setLeadingRowLabels('Yield Stress\tPlastic Strain')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        tabItem = FXTabItem(p=TabBook_3, text='CFRP', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_8 = FXVerticalFrame(p=TabBook_3,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        l = FXLabel(p=TabItem_8, text='ELASTIC', opts=JUSTIFY_LEFT)
        vf = FXVerticalFrame(TabItem_8, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 2, 3, 2, 3, form.material_cfrp_elasticKw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 160)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 160)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setLeadingRowLabels("Young's Modulus\tPoisson's Ratio")
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        tabItem = FXTabItem(p=TabBook_3, text='Concrete CDP', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_7 = FXVerticalFrame(p=TabBook_3,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        TabBook_6 = FXTabBook(p=TabItem_7, tgt=None, sel=0,
            opts=TABBOOK_NORMAL|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)
        tabItem = FXTabItem(p=TabBook_6, text='Density', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_15 = FXVerticalFrame(p=TabBook_6,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        vf = FXVerticalFrame(TabItem_15, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 2, 2, 2, 2, form.material_density_concreteKw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 160)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setLeadingRowLabels('Mass Density')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        tabItem = FXTabItem(p=TabBook_6, text='Elastic', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_17 = FXVerticalFrame(p=TabBook_6,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        vf = FXVerticalFrame(TabItem_17, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 6, 3, 6, 3, form.material_elastic_concreteKw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 160)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 160)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setLeadingRowLabels("Young's Modulus\tPoisoon's Ratio")
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        tabItem = FXTabItem(p=TabBook_6, text='Concrete Damaged Plasticity', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_18 = FXVerticalFrame(p=TabBook_6,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        TabBook_7 = FXTabBook(p=TabItem_18, tgt=None, sel=0,
            opts=TABBOOK_NORMAL|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)
        tabItem = FXTabItem(p=TabBook_7, text='Plasticity', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_21 = FXVerticalFrame(p=TabBook_7,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        vf = FXVerticalFrame(TabItem_21, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 2, 6, 2, 6, form.material_plasticity_concreteKw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 100)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 100)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setColumnWidth(3, 100)
        table.setColumnType(3, AFXTable.FLOAT)
        table.setColumnWidth(4, 100)
        table.setColumnType(4, AFXTable.FLOAT)
        table.setColumnWidth(5, 110)
        table.setColumnType(5, AFXTable.FLOAT)
        table.setLeadingRowLabels('Dilation Angle\tEccentricity\tfb0/fc0\tK\tViscosity Parameter')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        tabItem = FXTabItem(p=TabBook_7, text='Compressive Behavior', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_23 = FXVerticalFrame(p=TabBook_7,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        TabBook_8 = FXTabBook(p=TabItem_23, tgt=None, sel=0,
            opts=TABBOOK_NORMAL|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)
        tabItem = FXTabItem(p=TabBook_8, text='Value', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_26 = FXVerticalFrame(p=TabBook_8,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        vf = FXVerticalFrame(TabItem_26, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 6, 3, 6, 3, form.material_compressive_behavior_concreteKw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 160)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 160)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setLeadingRowLabels('Yield Stress\tInelastic Strain')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        tabItem = FXTabItem(p=TabBook_8, text='Concrete Compression Damage', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_27 = FXVerticalFrame(p=TabBook_8,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        vf = FXVerticalFrame(TabItem_27, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 6, 3, 6, 3, form.material_compression_damage_concreteKw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 160)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 160)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setLeadingRowLabels('Damage Parameter\tInelastic Strain')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        tabItem = FXTabItem(p=TabBook_7, text='Tensile Behavior', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_24 = FXVerticalFrame(p=TabBook_7,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        TabBook_9 = FXTabBook(p=TabItem_24, tgt=None, sel=0,
            opts=TABBOOK_NORMAL|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)
        tabItem = FXTabItem(p=TabBook_9, text='Value', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_28 = FXVerticalFrame(p=TabBook_9,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        vf = FXVerticalFrame(TabItem_28, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 6, 3, 6, 3, form.material_tensile_behavior_concreteKw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 160)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 160)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setLeadingRowLabels('Yield Stress\tCracking Strain')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        tabItem = FXTabItem(p=TabBook_9, text='Concrete Tension Damage', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_29 = FXVerticalFrame(p=TabBook_9,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        vf = FXVerticalFrame(TabItem_29, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 6, 3, 6, 3, form.material_tensile_damage_concreteKw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 160)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 160)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setLeadingRowLabels('Damage Parameter\tCracking Strain')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
