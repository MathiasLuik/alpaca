from .boston_housing import BostonHousingData
from .concrete import ConcreteData
from .energy_efficiency import EnergyEfficiencyData
from .kin8nm import Kin8nmData
from .naval_propulsion import NavalPropulsionData
from .ccpp import CCPPData


DATASETS = {
    'boston_housing': BostonHousingData,
    'concrete': ConcreteData,
    'energy_efficiency': EnergyEfficiencyData,
    'kin8nm': Kin8nmData,
    'naval_propulsion': NavalPropulsionData,
    'ccpp': CCPPData
}


def build_dataset(name):
    return DATASETS[name]()