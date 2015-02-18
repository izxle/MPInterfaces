from __future__ import division, unicode_literals, print_function

__author__ = ", ".join(["Kiran Mathew", "Joshua Gabriel"])
__date__ = "Feb 18 2015"
__version__ = "0.1"

from pymatgen.matproj.rest import MPRester

def get_struct_from_mp(formula, MAPI_KEY="dwvz2XCFUEI9fJiR"):
    """
    fetches the structure corresponding to the given formula
    from the materialsproject database
    Note: get the api key from materialsproject website
    provide the api key here os set the environment variable "MAPI_KEY"
    Note: for the given formula there are many structures available, this
    function returns the first one of those structures
    """
    with MPRester(MAPI_KEY) as m:
        data = m.get_data(formula)
        print("\nnumber of structures matching the chemical formula {0} = {1}".format(formula, len(data)) )
        for d in data:
            x = {}
            x['material_id'] = str(d['material_id'])
            structure = m.get_structure_by_material_id(x['material_id'])
            return structure


from .calibrate import Calibrate, CalibrateBulk, CalibrateSlab, CalibrateMolecule
from .instrument import MPINTVaspInputSet, MPINTVaspJob
from .data_processor import MPINTComputedEntry, MPINTVaspDrone, MPINTVasprun
from .interface import Interface, Ligand
from .measurement import Measurement
from .firetasks import MPINTCalibrateTask, MPINTMeasurementTask

