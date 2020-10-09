# -*- coding: utf-8 -*-
# =============================================================================
#     filter_functions
#     Copyright (C) 2020 Julian Teske, Forschungszentrum Juelich
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#     Contact email: j.teske@fz-juelich.de
# =============================================================================
"""Hardware adapted quantum simulation and optimal control """

from . import amplitude_functions, analyser, cost_functions, data_container, \
    energy_spectrum, matrix, noise, optimization_data, optimize, \
    performance_statistics, simulator, solver_algorithms, transfer_function, \
    util
from .amplitude_functions import IdentityAmpFunc, UnaryAnalyticAmpFunc, \
    CustomAmpFunc
from .analyser import Analyser
from .cost_functions import OperatorMatrixNorm, OperationInfidelity, \
    OperationNoiseInfidelity, OperatorFilterFunctionInfidelity, LeakageError, \
    state_fidelity, angle_axis_representation, entanglement_fidelity, \
    entanglement_fidelity_super_operator
from .data_container import DataContainer
from .energy_spectrum import plot_energy_spectrum
from .matrix import DenseOperator, convert_unitary_to_super_operator, \
    closest_unitary, DENSE_PAULI_0, DENSE_PAULI_X, DENSE_PAULI_Y, DENSE_PAULI_Z
from .noise import NTGColoredNoise, NTGQuasiStatic
from .optimization_data import OptimizationResult, OptimizationSummary
from .optimize import LeastSquaresOptimizer, ScalarMinimizingOptimizer
from .performance_statistics import PerformanceStatistics
from .simulator import Simulator
from .solver_algorithms import SchroedingerSolver, SchroedingerSMonteCarlo, \
    SchroedingerSMCControlNoise, LindbladSolver, LindbladSControlNoise
from .transfer_function import IdentityTF, OversamplingTF, LinearTF, \
    ConcatenateTF, ParallelTF, CustomTF, ExponentialTF

__all__ = [
    'IdentityAmpFunc', 'UnaryAnalyticAmpFunc', 'CustomAmpFunc', 'Analyser',
    'OperatorMatrixNorm', 'OperationInfidelity', 'OperationNoiseInfidelity',
    'OperatorFilterFunctionInfidelity', 'LeakageError', 'state_fidelity',
    'angle_axis_representation', 'entanglement_fidelity',
    'entanglement_fidelity_super_operator', 'DataContainer',
    'plot_energy_spectrum', 'DenseOperator',
    'convert_unitary_to_super_operator', 'closest_unitary', 'DENSE_PAULI_0',
    'DENSE_PAULI_Z', 'DENSE_PAULI_Y', 'DENSE_PAULI_X', 'NTGColoredNoise',
    'NTGQuasiStatic', 'OptimizationResult', 'OptimizationSummary',
    'LeastSquaresOptimizer', 'ScalarMinimizingOptimizer',
    'PerformanceStatistics', 'Simulator', 'SchroedingerSolver',
    'SchroedingerSMonteCarlo', 'SchroedingerSMCControlNoise', 'LindbladSolver',
    'LindbladSControlNoise', 'IdentityTF', 'OversamplingTF', 'LinearTF',
    'ConcatenateTF', 'ParallelTF', 'CustomTF', 'ExponentialTF'
]

__version__ = '1.0.2'
__license__ = 'GNU GPLv3+'
__author__ = 'Julian Teske, Forschungszentrum Juelich'
