from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


###########################################################################
# Class definition
###########################################################################

class Reinforced_Concrete_Standard_plugin(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='main',
            objectName='kernel', registerQuery=False)
        pickedDefault = ''
        self.beam_widthKw = AFXIntKeyword(self.cmd, 'beam_width', True, 980)
        self.beam_heightKw = AFXIntKeyword(self.cmd, 'beam_height', True, 300)
        self.beam_depthKw = AFXIntKeyword(self.cmd, 'beam_depth', True, 75)
        self.frp_widthKw = AFXIntKeyword(self.cmd, 'frp_width', True, 260)
        self.frp_heightKw = AFXIntKeyword(self.cmd, 'frp_height', True, 75)
        self.tie_widthKw = AFXIntKeyword(self.cmd, 'tie_width', True, 60)
        self.tie_heightKw = AFXIntKeyword(self.cmd, 'tie_height', True, 270)
        self.upperbar_widthKw = AFXIntKeyword(self.cmd, 'upperbar_width', True, 980)
        self.lowerbar_widthKw = AFXIntKeyword(self.cmd, 'lowerbar_width', True, 980)
        self.material_steel_elasticKw = AFXTableKeyword(self.cmd, 'material_steel_elastic', True)
        self.material_steel_elasticKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.material_steel_elasticKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.material_steel_plasticKw = AFXTableKeyword(self.cmd, 'material_steel_plastic', True)
        self.material_steel_plasticKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.material_steel_plasticKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.material_cfrp_elasticKw = AFXTableKeyword(self.cmd, 'material_cfrp_elastic', True)
        self.material_cfrp_elasticKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.material_cfrp_elasticKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.material_density_concreteKw = AFXTableKeyword(self.cmd, 'material_density_concrete', True)
        self.material_density_concreteKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.material_elastic_concreteKw = AFXTableKeyword(self.cmd, 'material_elastic_concrete', True)
        self.material_elastic_concreteKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.material_elastic_concreteKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.material_plasticity_concreteKw = AFXTableKeyword(self.cmd, 'material_plasticity_concrete', True)
        self.material_plasticity_concreteKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.material_plasticity_concreteKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.material_plasticity_concreteKw.setColumnType(2, AFXTABLE_TYPE_FLOAT)
        self.material_plasticity_concreteKw.setColumnType(3, AFXTABLE_TYPE_FLOAT)
        self.material_plasticity_concreteKw.setColumnType(4, AFXTABLE_TYPE_FLOAT)
        self.material_compressive_behavior_concreteKw = AFXTableKeyword(self.cmd, 'material_compressive_behavior_concrete', True)
        self.material_compressive_behavior_concreteKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.material_compressive_behavior_concreteKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.material_compression_damage_concreteKw = AFXTableKeyword(self.cmd, 'material_compression_damage_concrete', True)
        self.material_compression_damage_concreteKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.material_compression_damage_concreteKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.material_tensile_behavior_concreteKw = AFXTableKeyword(self.cmd, 'material_tensile_behavior_concrete', True)
        self.material_tensile_behavior_concreteKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.material_tensile_behavior_concreteKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.material_tensile_damage_concreteKw = AFXTableKeyword(self.cmd, 'material_tensile_damage_concrete', True)
        self.material_tensile_damage_concreteKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.material_tensile_damage_concreteKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import reinforced_Concrete_StandardDB
        return reinforced_Concrete_StandardDB.Reinforced_Concrete_StandardDB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        #
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass
        return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Register the plug-in
#
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='Reinforced Concrete v2', 
    object=Reinforced_Concrete_Standard_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    kernelInitString='import kernel',
    applicableModules=ALL,
    version='N/A',
    author='N/A',
    description='N/A',
    helpUrl='N/A'
)
