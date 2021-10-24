"""
Test Dense operators:
- multiplication
- addition
- matrix exponential
"""
from qopt import matrix

import unittest
import math
import numpy as np


SIGMA_X = np.asarray([[0, 1], [1, 0]])


class TestMatrix(unittest.TestCase):
    def test_dense_control_matrix_arithmetic(self):
        mat = matrix.DenseOperator(SIGMA_X)

        # test scalar multiplication:
        two_times_mat = 2 * mat
        two_times_mat2 = mat * 2
        mat *= 2

        np.testing.assert_array_almost_equal(two_times_mat.data,
                                             two_times_mat2.data)
        np.testing.assert_array_almost_equal(two_times_mat2.data, mat.data)

        # test addition

        mat = matrix.DenseOperator(SIGMA_X)
        two_times_mat3 = mat + np.asarray(SIGMA_X.data)
        two_times_mat5 = mat + mat
        mat += mat

        np.testing.assert_array_almost_equal(two_times_mat3.data,
                                             two_times_mat.data)
        np.testing.assert_array_almost_equal(two_times_mat5.data,
                                             two_times_mat.data)
        np.testing.assert_array_almost_equal(mat.data, two_times_mat.data)

        # test subtraction

        mat = matrix.DenseOperator(SIGMA_X)
        should_be_zeros = mat - np.asarray(SIGMA_X.data)
        two_times_mat -= mat

        np.testing.assert_array_almost_equal(two_times_mat.data, mat.data)
        np.testing.assert_array_almost_equal(should_be_zeros.data,
                                             np.zeros((2, 2)))

    def test_dense_control_matrix_functions(self):

        tau = .5j * math.pi
        sigma_x = matrix.DenseOperator(SIGMA_X)
        exponential = sigma_x.exp(tau)

        np.testing.assert_array_almost_equal(
            exponential.data, sigma_x.data * 1j)
        exponential = sigma_x.exp(2 * tau)
        np.testing.assert_array_almost_equal(exponential.data, -1 * np.eye(2))

        prop_spectral, prop_grad_spectral = sigma_x.dexp(
            direction=sigma_x, tau=tau, compute_expm=True,
            method='spectral')
        prop_frechet, prop_grad_frechet = sigma_x.dexp(
            direction=sigma_x, tau=tau, compute_expm=True,
            method='Frechet')
        """
        prop_approx, prop_grad_approx = sigma_x.dexp(
            direction=sigma_x, tau=tau, compute_expm=True,
            method='approx')
        """
        prop_first_order, prop_grad_first_order = sigma_x.dexp(
            direction=sigma_x, tau=tau, compute_expm=True,
            method='first_order')
        prop_second_order, prop_grad_second_order = sigma_x.dexp(
            direction=sigma_x, tau=tau, compute_expm=True,
            method='second_order')
        prop_third_order, prop_grad_third_order = sigma_x.dexp(
            direction=sigma_x, tau=tau, compute_expm=True,
            method='third_order')
        np.testing.assert_array_almost_equal(prop_spectral.data,
                                             prop_frechet.data)
        """
        np.testing.assert_array_almost_equal(prop_spectral.data,
                                             prop_approx.data)
        """
        np.testing.assert_array_almost_equal(prop_spectral.data,
                                             prop_first_order.data)
        np.testing.assert_array_almost_equal(prop_spectral.data,
                                             prop_second_order.data)
        np.testing.assert_array_almost_equal(prop_spectral.data,
                                             prop_third_order.data)
        np.testing.assert_array_almost_equal(prop_grad_spectral.data,
                                             prop_grad_frechet.data)
        """
        np.testing.assert_array_almost_equal(prop_grad_spectral.data,
                                             prop_grad_approx.data)
        """

        # test kronecker product:
        np.random.seed(0)
        a = matrix.DenseOperator(np.random.rand(5, 5))
        b = matrix.DenseOperator(np.random.rand(5, 5))
        c = a.kron(b)
        c_2 = a.kron(b.data)
        c_np = np.kron(a.data, b.data)

        np.testing.assert_array_almost_equal(c.data, c_2.data)
        np.testing.assert_array_almost_equal(c.data, c_np)

        norm = sigma_x.norm()
        self.assertAlmostEqual(norm, np.sqrt(2))

    def test_dense_partial_trace(self):
        a = .5 * matrix.DenseOperator.pauli_0().kron(
            matrix.DenseOperator.pauli_y())
        trace_1 = a.ptrace([2, 2], [0])
        trace_2 = a.ptrace([2, 2], [1])
        np.testing.assert_array_almost_equal(
            trace_1.data, matrix.DenseOperator.pauli_y().data)
        np.testing.assert_array_almost_equal(
            trace_2.data, np.zeros([2, 2]))
