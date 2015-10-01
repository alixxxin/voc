from unittest import expectedFailure
from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class UnaryFloatOperationTests(UnaryOperationTestCase, TranspileTestCase):
    x = '1.2345'

UnaryFloatOperationTests.test_unary_positive = expectedFailure(UnaryFloatOperationTests.test_unary_positive)
UnaryFloatOperationTests.test_unary_negative = expectedFailure(UnaryFloatOperationTests.test_unary_negative)
UnaryFloatOperationTests.test_unary_not = expectedFailure(UnaryFloatOperationTests.test_unary_not)
UnaryFloatOperationTests.test_unary_invert = expectedFailure(UnaryFloatOperationTests.test_unary_invert)


class BinaryFloatOperationTests(BinaryOperationTestCase, TranspileTestCase):
    x = '1.2345'

BinaryFloatOperationTests.test_add_bool_true = expectedFailure(BinaryFloatOperationTests.test_add_bool_true)
BinaryFloatOperationTests.test_subtract_bool_true = expectedFailure(BinaryFloatOperationTests.test_subtract_bool_true)
BinaryFloatOperationTests.test_multiply_bool_true = expectedFailure(BinaryFloatOperationTests.test_multiply_bool_true)
BinaryFloatOperationTests.test_floor_divide_bool_true = expectedFailure(BinaryFloatOperationTests.test_floor_divide_bool_true)
BinaryFloatOperationTests.test_true_divide_bool_true = expectedFailure(BinaryFloatOperationTests.test_true_divide_bool_true)
BinaryFloatOperationTests.test_modulo_bool_true = expectedFailure(BinaryFloatOperationTests.test_modulo_bool_true)
BinaryFloatOperationTests.test_power_bool_true = expectedFailure(BinaryFloatOperationTests.test_power_bool_true)
BinaryFloatOperationTests.test_subscr_bool_true = expectedFailure(BinaryFloatOperationTests.test_subscr_bool_true)

BinaryFloatOperationTests.test_add_bool_false = expectedFailure(BinaryFloatOperationTests.test_add_bool_false)
BinaryFloatOperationTests.test_subtract_bool_false = expectedFailure(BinaryFloatOperationTests.test_subtract_bool_false)
BinaryFloatOperationTests.test_multiply_bool_false = expectedFailure(BinaryFloatOperationTests.test_multiply_bool_false)
BinaryFloatOperationTests.test_floor_divide_bool_false = expectedFailure(BinaryFloatOperationTests.test_floor_divide_bool_false)
BinaryFloatOperationTests.test_true_divide_bool_false = expectedFailure(BinaryFloatOperationTests.test_true_divide_bool_false)
BinaryFloatOperationTests.test_modulo_bool_false = expectedFailure(BinaryFloatOperationTests.test_modulo_bool_false)
BinaryFloatOperationTests.test_power_bool_false = expectedFailure(BinaryFloatOperationTests.test_power_bool_false)
BinaryFloatOperationTests.test_subscr_bool_false = expectedFailure(BinaryFloatOperationTests.test_subscr_bool_false)

# BinaryFloatOperationTests.test_add_bytearray = expectedFailure(BinaryFloatOperationTests.test_add_bytearray)
# BinaryFloatOperationTests.test_subtract_bytearray = expectedFailure(BinaryFloatOperationTests.test_subtract_bytearray)
# BinaryFloatOperationTests.test_multiply_bytearray = expectedFailure(BinaryFloatOperationTests.test_multiply_bytearray)
# BinaryFloatOperationTests.test_floor_divide_bytearray = expectedFailure(BinaryFloatOperationTests.test_floor_divide_bytearray)
# BinaryFloatOperationTests.test_true_divide_bytearray = expectedFailure(BinaryFloatOperationTests.test_true_divide_bytearray)
# BinaryFloatOperationTests.test_modulo_bytearray = expectedFailure(BinaryFloatOperationTests.test_modulo_bytearray)
# BinaryFloatOperationTests.test_power_bytearray = expectedFailure(BinaryFloatOperationTests.test_power_bytearray)
# BinaryFloatOperationTests.test_subscr_bytearray = expectedFailure(BinaryFloatOperationTests.test_subscr_bytearray)
# BinaryFloatOperationTests.test_lshift_bytearray = expectedFailure(BinaryFloatOperationTests.test_lshift_bytearray)
# BinaryFloatOperationTests.test_rshift_bytearray = expectedFailure(BinaryFloatOperationTests.test_rshift_bytearray)
# BinaryFloatOperationTests.test_and_bytearray = expectedFailure(BinaryFloatOperationTests.test_and_bytearray)
# BinaryFloatOperationTests.test_xor_bytearray = expectedFailure(BinaryFloatOperationTests.test_xor_bytearray)
# BinaryFloatOperationTests.test_or_bytearray = expectedFailure(BinaryFloatOperationTests.test_or_bytearray)

BinaryFloatOperationTests.test_add_bytes = expectedFailure(BinaryFloatOperationTests.test_add_bytes)
BinaryFloatOperationTests.test_subtract_bytes = expectedFailure(BinaryFloatOperationTests.test_subtract_bytes)
BinaryFloatOperationTests.test_multiply_bytes = expectedFailure(BinaryFloatOperationTests.test_multiply_bytes)
BinaryFloatOperationTests.test_floor_divide_bytes = expectedFailure(BinaryFloatOperationTests.test_floor_divide_bytes)
BinaryFloatOperationTests.test_true_divide_bytes = expectedFailure(BinaryFloatOperationTests.test_true_divide_bytes)
BinaryFloatOperationTests.test_modulo_bytes = expectedFailure(BinaryFloatOperationTests.test_modulo_bytes)
BinaryFloatOperationTests.test_power_bytes = expectedFailure(BinaryFloatOperationTests.test_power_bytes)
BinaryFloatOperationTests.test_subscr_bytes = expectedFailure(BinaryFloatOperationTests.test_subscr_bytes)
BinaryFloatOperationTests.test_lshift_bytes = expectedFailure(BinaryFloatOperationTests.test_lshift_bytes)
BinaryFloatOperationTests.test_rshift_bytes = expectedFailure(BinaryFloatOperationTests.test_rshift_bytes)
BinaryFloatOperationTests.test_and_bytes = expectedFailure(BinaryFloatOperationTests.test_and_bytes)
BinaryFloatOperationTests.test_xor_bytes = expectedFailure(BinaryFloatOperationTests.test_xor_bytes)
BinaryFloatOperationTests.test_or_bytes = expectedFailure(BinaryFloatOperationTests.test_or_bytes)

# BinaryFloatOperationTests.test_add_class = expectedFailure(BinaryFloatOperationTests.test_add_class)
# BinaryFloatOperationTests.test_subtract_class = expectedFailure(BinaryFloatOperationTests.test_subtract_class)
# BinaryFloatOperationTests.test_multiply_class = expectedFailure(BinaryFloatOperationTests.test_multiply_class)
# BinaryFloatOperationTests.test_floor_divide_class = expectedFailure(BinaryFloatOperationTests.test_floor_divide_class)
# BinaryFloatOperationTests.test_true_divide_class = expectedFailure(BinaryFloatOperationTests.test_true_divide_class)
# BinaryFloatOperationTests.test_modulo_class = expectedFailure(BinaryFloatOperationTests.test_modulo_class)
# BinaryFloatOperationTests.test_power_class = expectedFailure(BinaryFloatOperationTests.test_power_class)
# BinaryFloatOperationTests.test_subscr_class = expectedFailure(BinaryFloatOperationTests.test_subscr_class)
# BinaryFloatOperationTests.test_lshift_class = expectedFailure(BinaryFloatOperationTests.test_lshift_class)
# BinaryFloatOperationTests.test_rshift_class = expectedFailure(BinaryFloatOperationTests.test_rshift_class)
# BinaryFloatOperationTests.test_and_class = expectedFailure(BinaryFloatOperationTests.test_and_class)
# BinaryFloatOperationTests.test_xor_class = expectedFailure(BinaryFloatOperationTests.test_xor_class)
# BinaryFloatOperationTests.test_or_class = expectedFailure(BinaryFloatOperationTests.test_or_class)

# BinaryFloatOperationTests.test_add_complex = expectedFailure(BinaryFloatOperationTests.test_add_complex)
# BinaryFloatOperationTests.test_subtract_complex = expectedFailure(BinaryFloatOperationTests.test_subtract_complex)
# BinaryFloatOperationTests.test_multiply_complex = expectedFailure(BinaryFloatOperationTests.test_multiply_complex)
# BinaryFloatOperationTests.test_floor_divide_complex = expectedFailure(BinaryFloatOperationTests.test_floor_divide_complex)
# BinaryFloatOperationTests.test_true_divide_complex = expectedFailure(BinaryFloatOperationTests.test_true_divide_complex)
# BinaryFloatOperationTests.test_modulo_complex = expectedFailure(BinaryFloatOperationTests.test_modulo_complex)
# BinaryFloatOperationTests.test_power_complex = expectedFailure(BinaryFloatOperationTests.test_power_complex)
# BinaryFloatOperationTests.test_subscr_complex = expectedFailure(BinaryFloatOperationTests.test_subscr_complex)
# BinaryFloatOperationTests.test_lshift_complex = expectedFailure(BinaryFloatOperationTests.test_lshift_complex)
# BinaryFloatOperationTests.test_rshift_complex = expectedFailure(BinaryFloatOperationTests.test_rshift_complex)
# BinaryFloatOperationTests.test_and_complex = expectedFailure(BinaryFloatOperationTests.test_and_complex)
# BinaryFloatOperationTests.test_xor_complex = expectedFailure(BinaryFloatOperationTests.test_xor_complex)
# BinaryFloatOperationTests.test_or_complex = expectedFailure(BinaryFloatOperationTests.test_or_complex)

BinaryFloatOperationTests.test_add_dict = expectedFailure(BinaryFloatOperationTests.test_add_dict)
BinaryFloatOperationTests.test_subtract_dict = expectedFailure(BinaryFloatOperationTests.test_subtract_dict)
BinaryFloatOperationTests.test_multiply_dict = expectedFailure(BinaryFloatOperationTests.test_multiply_dict)
BinaryFloatOperationTests.test_floor_divide_dict = expectedFailure(BinaryFloatOperationTests.test_floor_divide_dict)
BinaryFloatOperationTests.test_true_divide_dict = expectedFailure(BinaryFloatOperationTests.test_true_divide_dict)
BinaryFloatOperationTests.test_modulo_dict = expectedFailure(BinaryFloatOperationTests.test_modulo_dict)
BinaryFloatOperationTests.test_power_dict = expectedFailure(BinaryFloatOperationTests.test_power_dict)
BinaryFloatOperationTests.test_subscr_dict = expectedFailure(BinaryFloatOperationTests.test_subscr_dict)
BinaryFloatOperationTests.test_lshift_dict = expectedFailure(BinaryFloatOperationTests.test_lshift_dict)
BinaryFloatOperationTests.test_rshift_dict = expectedFailure(BinaryFloatOperationTests.test_rshift_dict)
BinaryFloatOperationTests.test_and_dict = expectedFailure(BinaryFloatOperationTests.test_and_dict)
BinaryFloatOperationTests.test_xor_dict = expectedFailure(BinaryFloatOperationTests.test_xor_dict)
BinaryFloatOperationTests.test_or_dict = expectedFailure(BinaryFloatOperationTests.test_or_dict)

BinaryFloatOperationTests.test_add_float = expectedFailure(BinaryFloatOperationTests.test_add_float)
BinaryFloatOperationTests.test_subtract_float = expectedFailure(BinaryFloatOperationTests.test_subtract_float)
BinaryFloatOperationTests.test_multiply_float = expectedFailure(BinaryFloatOperationTests.test_multiply_float)
BinaryFloatOperationTests.test_floor_divide_float = expectedFailure(BinaryFloatOperationTests.test_floor_divide_float)
BinaryFloatOperationTests.test_true_divide_float = expectedFailure(BinaryFloatOperationTests.test_true_divide_float)
BinaryFloatOperationTests.test_modulo_float = expectedFailure(BinaryFloatOperationTests.test_modulo_float)
BinaryFloatOperationTests.test_power_float = expectedFailure(BinaryFloatOperationTests.test_power_float)
BinaryFloatOperationTests.test_subscr_float = expectedFailure(BinaryFloatOperationTests.test_subscr_float)

# BinaryFloatOperationTests.test_add_frozenset = expectedFailure(BinaryFloatOperationTests.test_add_frozenset)
# BinaryFloatOperationTests.test_subtract_frozenset = expectedFailure(BinaryFloatOperationTests.test_subtract_frozenset)
# BinaryFloatOperationTests.test_multiply_frozenset = expectedFailure(BinaryFloatOperationTests.test_multiply_frozenset)
# BinaryFloatOperationTests.test_floor_divide_frozenset = expectedFailure(BinaryFloatOperationTests.test_floor_divide_frozenset)
# BinaryFloatOperationTests.test_true_divide_frozenset = expectedFailure(BinaryFloatOperationTests.test_true_divide_frozenset)
# BinaryFloatOperationTests.test_modulo_frozenset = expectedFailure(BinaryFloatOperationTests.test_modulo_frozenset)
# BinaryFloatOperationTests.test_power_frozenset = expectedFailure(BinaryFloatOperationTests.test_power_frozenset)
# BinaryFloatOperationTests.test_subscr_frozenset = expectedFailure(BinaryFloatOperationTests.test_subscr_frozenset)
# BinaryFloatOperationTests.test_lshift_frozenset = expectedFailure(BinaryFloatOperationTests.test_lshift_frozenset)
# BinaryFloatOperationTests.test_rshift_frozenset = expectedFailure(BinaryFloatOperationTests.test_rshift_frozenset)
# BinaryFloatOperationTests.test_and_frozenset = expectedFailure(BinaryFloatOperationTests.test_and_frozenset)
# BinaryFloatOperationTests.test_xor_frozenset = expectedFailure(BinaryFloatOperationTests.test_xor_frozenset)
# BinaryFloatOperationTests.test_or_frozenset = expectedFailure(BinaryFloatOperationTests.test_or_frozenset)

BinaryFloatOperationTests.test_add_int = expectedFailure(BinaryFloatOperationTests.test_add_int)
BinaryFloatOperationTests.test_subtract_int = expectedFailure(BinaryFloatOperationTests.test_subtract_int)
BinaryFloatOperationTests.test_multiply_int = expectedFailure(BinaryFloatOperationTests.test_multiply_int)
BinaryFloatOperationTests.test_floor_divide_int = expectedFailure(BinaryFloatOperationTests.test_floor_divide_int)
BinaryFloatOperationTests.test_true_divide_int = expectedFailure(BinaryFloatOperationTests.test_true_divide_int)
BinaryFloatOperationTests.test_modulo_int = expectedFailure(BinaryFloatOperationTests.test_modulo_int)
BinaryFloatOperationTests.test_power_int = expectedFailure(BinaryFloatOperationTests.test_power_int)
BinaryFloatOperationTests.test_subscr_int = expectedFailure(BinaryFloatOperationTests.test_subscr_int)

BinaryFloatOperationTests.test_add_list = expectedFailure(BinaryFloatOperationTests.test_add_list)
BinaryFloatOperationTests.test_subtract_list = expectedFailure(BinaryFloatOperationTests.test_subtract_list)
BinaryFloatOperationTests.test_multiply_list = expectedFailure(BinaryFloatOperationTests.test_multiply_list)
BinaryFloatOperationTests.test_floor_divide_list = expectedFailure(BinaryFloatOperationTests.test_floor_divide_list)
BinaryFloatOperationTests.test_true_divide_list = expectedFailure(BinaryFloatOperationTests.test_true_divide_list)
BinaryFloatOperationTests.test_modulo_list = expectedFailure(BinaryFloatOperationTests.test_modulo_list)
BinaryFloatOperationTests.test_power_list = expectedFailure(BinaryFloatOperationTests.test_power_list)
BinaryFloatOperationTests.test_subscr_list = expectedFailure(BinaryFloatOperationTests.test_subscr_list)

BinaryFloatOperationTests.test_add_set = expectedFailure(BinaryFloatOperationTests.test_add_set)
BinaryFloatOperationTests.test_subtract_set = expectedFailure(BinaryFloatOperationTests.test_subtract_set)
BinaryFloatOperationTests.test_multiply_set = expectedFailure(BinaryFloatOperationTests.test_multiply_set)
BinaryFloatOperationTests.test_floor_divide_set = expectedFailure(BinaryFloatOperationTests.test_floor_divide_set)
BinaryFloatOperationTests.test_true_divide_set = expectedFailure(BinaryFloatOperationTests.test_true_divide_set)
BinaryFloatOperationTests.test_modulo_set = expectedFailure(BinaryFloatOperationTests.test_modulo_set)
BinaryFloatOperationTests.test_power_set = expectedFailure(BinaryFloatOperationTests.test_power_set)
BinaryFloatOperationTests.test_subscr_set = expectedFailure(BinaryFloatOperationTests.test_subscr_set)
BinaryFloatOperationTests.test_lshift_set = expectedFailure(BinaryFloatOperationTests.test_lshift_set)
BinaryFloatOperationTests.test_rshift_set = expectedFailure(BinaryFloatOperationTests.test_rshift_set)
BinaryFloatOperationTests.test_and_set = expectedFailure(BinaryFloatOperationTests.test_and_set)
BinaryFloatOperationTests.test_xor_set = expectedFailure(BinaryFloatOperationTests.test_xor_set)
BinaryFloatOperationTests.test_or_set = expectedFailure(BinaryFloatOperationTests.test_or_set)

BinaryFloatOperationTests.test_add_str = expectedFailure(BinaryFloatOperationTests.test_add_str)
BinaryFloatOperationTests.test_subtract_str = expectedFailure(BinaryFloatOperationTests.test_subtract_str)
BinaryFloatOperationTests.test_multiply_str = expectedFailure(BinaryFloatOperationTests.test_multiply_str)
BinaryFloatOperationTests.test_floor_divide_str = expectedFailure(BinaryFloatOperationTests.test_floor_divide_str)
BinaryFloatOperationTests.test_true_divide_str = expectedFailure(BinaryFloatOperationTests.test_true_divide_str)
BinaryFloatOperationTests.test_modulo_str = expectedFailure(BinaryFloatOperationTests.test_modulo_str)
BinaryFloatOperationTests.test_power_str = expectedFailure(BinaryFloatOperationTests.test_power_str)
BinaryFloatOperationTests.test_subscr_str = expectedFailure(BinaryFloatOperationTests.test_subscr_str)

BinaryFloatOperationTests.test_add_tuple = expectedFailure(BinaryFloatOperationTests.test_add_tuple)
BinaryFloatOperationTests.test_subtract_tuple = expectedFailure(BinaryFloatOperationTests.test_subtract_tuple)
BinaryFloatOperationTests.test_multiply_tuple = expectedFailure(BinaryFloatOperationTests.test_multiply_tuple)
BinaryFloatOperationTests.test_floor_divide_tuple = expectedFailure(BinaryFloatOperationTests.test_floor_divide_tuple)
BinaryFloatOperationTests.test_true_divide_tuple = expectedFailure(BinaryFloatOperationTests.test_true_divide_tuple)
BinaryFloatOperationTests.test_modulo_tuple = expectedFailure(BinaryFloatOperationTests.test_modulo_tuple)
BinaryFloatOperationTests.test_power_tuple = expectedFailure(BinaryFloatOperationTests.test_power_tuple)
BinaryFloatOperationTests.test_subscr_tuple = expectedFailure(BinaryFloatOperationTests.test_subscr_tuple)


class InplaceFloatOperationTests(InplaceOperationTestCase, TranspileTestCase):
    x = '1.2345'


InplaceFloatOperationTests.test_add_bool_true = expectedFailure(InplaceFloatOperationTests.test_add_bool_true)
InplaceFloatOperationTests.test_subtract_bool_true = expectedFailure(InplaceFloatOperationTests.test_subtract_bool_true)
InplaceFloatOperationTests.test_multiply_bool_true = expectedFailure(InplaceFloatOperationTests.test_multiply_bool_true)
InplaceFloatOperationTests.test_floor_divide_bool_true = expectedFailure(InplaceFloatOperationTests.test_floor_divide_bool_true)
InplaceFloatOperationTests.test_true_divide_bool_true = expectedFailure(InplaceFloatOperationTests.test_true_divide_bool_true)
InplaceFloatOperationTests.test_modulo_bool_true = expectedFailure(InplaceFloatOperationTests.test_modulo_bool_true)
InplaceFloatOperationTests.test_power_bool_true = expectedFailure(InplaceFloatOperationTests.test_power_bool_true)
InplaceFloatOperationTests.test_lshift_bool_true = expectedFailure(InplaceFloatOperationTests.test_lshift_bool_true)
InplaceFloatOperationTests.test_rshift_bool_true = expectedFailure(InplaceFloatOperationTests.test_rshift_bool_true)
InplaceFloatOperationTests.test_and_bool_true = expectedFailure(InplaceFloatOperationTests.test_and_bool_true)
InplaceFloatOperationTests.test_xor_bool_true = expectedFailure(InplaceFloatOperationTests.test_xor_bool_true)
InplaceFloatOperationTests.test_or_bool_true = expectedFailure(InplaceFloatOperationTests.test_or_bool_true)

InplaceFloatOperationTests.test_add_bool_false = expectedFailure(InplaceFloatOperationTests.test_add_bool_false)
InplaceFloatOperationTests.test_subtract_bool_false = expectedFailure(InplaceFloatOperationTests.test_subtract_bool_false)
InplaceFloatOperationTests.test_multiply_bool_false = expectedFailure(InplaceFloatOperationTests.test_multiply_bool_false)
InplaceFloatOperationTests.test_floor_divide_bool_false = expectedFailure(InplaceFloatOperationTests.test_floor_divide_bool_false)
InplaceFloatOperationTests.test_true_divide_bool_false = expectedFailure(InplaceFloatOperationTests.test_true_divide_bool_false)
InplaceFloatOperationTests.test_modulo_bool_false = expectedFailure(InplaceFloatOperationTests.test_modulo_bool_false)
InplaceFloatOperationTests.test_power_bool_false = expectedFailure(InplaceFloatOperationTests.test_power_bool_false)
InplaceFloatOperationTests.test_lshift_bool_false = expectedFailure(InplaceFloatOperationTests.test_lshift_bool_false)
InplaceFloatOperationTests.test_rshift_bool_false = expectedFailure(InplaceFloatOperationTests.test_rshift_bool_false)
InplaceFloatOperationTests.test_and_bool_false = expectedFailure(InplaceFloatOperationTests.test_and_bool_false)
InplaceFloatOperationTests.test_xor_bool_false = expectedFailure(InplaceFloatOperationTests.test_xor_bool_false)
InplaceFloatOperationTests.test_or_bool_false = expectedFailure(InplaceFloatOperationTests.test_or_bool_false)

# InplaceFloatOperationTests.test_add_bytearray = expectedFailure(InplaceFloatOperationTests.test_add_bytearray)
# InplaceFloatOperationTests.test_subtract_bytearray = expectedFailure(InplaceFloatOperationTests.test_subtract_bytearray)
# InplaceFloatOperationTests.test_multiply_bytearray = expectedFailure(InplaceFloatOperationTests.test_multiply_bytearray)
# InplaceFloatOperationTests.test_floor_divide_bytearray = expectedFailure(InplaceFloatOperationTests.test_floor_divide_bytearray)
# InplaceFloatOperationTests.test_true_divide_bytearray = expectedFailure(InplaceFloatOperationTests.test_true_divide_bytearray)
# InplaceFloatOperationTests.test_modulo_bytearray = expectedFailure(InplaceFloatOperationTests.test_modulo_bytearray)
# InplaceFloatOperationTests.test_power_bytearray = expectedFailure(InplaceFloatOperationTests.test_power_bytearray)
# InplaceFloatOperationTests.test_lshift_bytearray = expectedFailure(InplaceFloatOperationTests.test_lshift_bytearray)
# InplaceFloatOperationTests.test_rshift_bytearray = expectedFailure(InplaceFloatOperationTests.test_rshift_bytearray)
# InplaceFloatOperationTests.test_and_bytearray = expectedFailure(InplaceFloatOperationTests.test_and_bytearray)
# InplaceFloatOperationTests.test_xor_bytearray = expectedFailure(InplaceFloatOperationTests.test_xor_bytearray)
# InplaceFloatOperationTests.test_or_bytearray = expectedFailure(InplaceFloatOperationTests.test_or_bytearray)

InplaceFloatOperationTests.test_add_bytes = expectedFailure(InplaceFloatOperationTests.test_add_bytes)
InplaceFloatOperationTests.test_subtract_bytes = expectedFailure(InplaceFloatOperationTests.test_subtract_bytes)
InplaceFloatOperationTests.test_multiply_bytes = expectedFailure(InplaceFloatOperationTests.test_multiply_bytes)
InplaceFloatOperationTests.test_floor_divide_bytes = expectedFailure(InplaceFloatOperationTests.test_floor_divide_bytes)
InplaceFloatOperationTests.test_true_divide_bytes = expectedFailure(InplaceFloatOperationTests.test_true_divide_bytes)
InplaceFloatOperationTests.test_modulo_bytes = expectedFailure(InplaceFloatOperationTests.test_modulo_bytes)
InplaceFloatOperationTests.test_power_bytes = expectedFailure(InplaceFloatOperationTests.test_power_bytes)
InplaceFloatOperationTests.test_lshift_bytes = expectedFailure(InplaceFloatOperationTests.test_lshift_bytes)
InplaceFloatOperationTests.test_rshift_bytes = expectedFailure(InplaceFloatOperationTests.test_rshift_bytes)
InplaceFloatOperationTests.test_and_bytes = expectedFailure(InplaceFloatOperationTests.test_and_bytes)
InplaceFloatOperationTests.test_xor_bytes = expectedFailure(InplaceFloatOperationTests.test_xor_bytes)
InplaceFloatOperationTests.test_or_bytes = expectedFailure(InplaceFloatOperationTests.test_or_bytes)

# InplaceFloatOperationTests.test_add_class = expectedFailure(InplaceFloatOperationTests.test_add_class)
# InplaceFloatOperationTests.test_subtract_class = expectedFailure(InplaceFloatOperationTests.test_subtract_class)
# InplaceFloatOperationTests.test_multiply_class = expectedFailure(InplaceFloatOperationTests.test_multiply_class)
# InplaceFloatOperationTests.test_floor_divide_class = expectedFailure(InplaceFloatOperationTests.test_floor_divide_class)
# InplaceFloatOperationTests.test_true_divide_class = expectedFailure(InplaceFloatOperationTests.test_true_divide_class)
# InplaceFloatOperationTests.test_modulo_class = expectedFailure(InplaceFloatOperationTests.test_modulo_class)
# InplaceFloatOperationTests.test_power_class = expectedFailure(InplaceFloatOperationTests.test_power_class)
# InplaceFloatOperationTests.test_lshift_class = expectedFailure(InplaceFloatOperationTests.test_lshift_class)
# InplaceFloatOperationTests.test_rshift_class = expectedFailure(InplaceFloatOperationTests.test_rshift_class)
# InplaceFloatOperationTests.test_and_class = expectedFailure(InplaceFloatOperationTests.test_and_class)
# InplaceFloatOperationTests.test_xor_class = expectedFailure(InplaceFloatOperationTests.test_xor_class)
# InplaceFloatOperationTests.test_or_class = expectedFailure(InplaceFloatOperationTests.test_or_class)

# InplaceFloatOperationTests.test_add_complex = expectedFailure(InplaceFloatOperationTests.test_add_complex)
# InplaceFloatOperationTests.test_subtract_complex = expectedFailure(InplaceFloatOperationTests.test_subtract_complex)
# InplaceFloatOperationTests.test_multiply_complex = expectedFailure(InplaceFloatOperationTests.test_multiply_complex)
# InplaceFloatOperationTests.test_floor_divide_complex = expectedFailure(InplaceFloatOperationTests.test_floor_divide_complex)
# InplaceFloatOperationTests.test_true_divide_complex = expectedFailure(InplaceFloatOperationTests.test_true_divide_complex)
# InplaceFloatOperationTests.test_modulo_complex = expectedFailure(InplaceFloatOperationTests.test_modulo_complex)
# InplaceFloatOperationTests.test_power_complex = expectedFailure(InplaceFloatOperationTests.test_power_complex)
# InplaceFloatOperationTests.test_lshift_complex = expectedFailure(InplaceFloatOperationTests.test_lshift_complex)
# InplaceFloatOperationTests.test_rshift_complex = expectedFailure(InplaceFloatOperationTests.test_rshift_complex)
# InplaceFloatOperationTests.test_and_complex = expectedFailure(InplaceFloatOperationTests.test_and_complex)
# InplaceFloatOperationTests.test_xor_complex = expectedFailure(InplaceFloatOperationTests.test_xor_complex)
# InplaceFloatOperationTests.test_or_complex = expectedFailure(InplaceFloatOperationTests.test_or_complex)

InplaceFloatOperationTests.test_add_dict = expectedFailure(InplaceFloatOperationTests.test_add_dict)
InplaceFloatOperationTests.test_subtract_dict = expectedFailure(InplaceFloatOperationTests.test_subtract_dict)
InplaceFloatOperationTests.test_multiply_dict = expectedFailure(InplaceFloatOperationTests.test_multiply_dict)
InplaceFloatOperationTests.test_floor_divide_dict = expectedFailure(InplaceFloatOperationTests.test_floor_divide_dict)
InplaceFloatOperationTests.test_true_divide_dict = expectedFailure(InplaceFloatOperationTests.test_true_divide_dict)
InplaceFloatOperationTests.test_modulo_dict = expectedFailure(InplaceFloatOperationTests.test_modulo_dict)
InplaceFloatOperationTests.test_power_dict = expectedFailure(InplaceFloatOperationTests.test_power_dict)
InplaceFloatOperationTests.test_lshift_dict = expectedFailure(InplaceFloatOperationTests.test_lshift_dict)
InplaceFloatOperationTests.test_rshift_dict = expectedFailure(InplaceFloatOperationTests.test_rshift_dict)
InplaceFloatOperationTests.test_and_dict = expectedFailure(InplaceFloatOperationTests.test_and_dict)
InplaceFloatOperationTests.test_xor_dict = expectedFailure(InplaceFloatOperationTests.test_xor_dict)
InplaceFloatOperationTests.test_or_dict = expectedFailure(InplaceFloatOperationTests.test_or_dict)

InplaceFloatOperationTests.test_add_float = expectedFailure(InplaceFloatOperationTests.test_add_float)
InplaceFloatOperationTests.test_subtract_float = expectedFailure(InplaceFloatOperationTests.test_subtract_float)
InplaceFloatOperationTests.test_multiply_float = expectedFailure(InplaceFloatOperationTests.test_multiply_float)
InplaceFloatOperationTests.test_floor_divide_float = expectedFailure(InplaceFloatOperationTests.test_floor_divide_float)
InplaceFloatOperationTests.test_true_divide_float = expectedFailure(InplaceFloatOperationTests.test_true_divide_float)
InplaceFloatOperationTests.test_modulo_float = expectedFailure(InplaceFloatOperationTests.test_modulo_float)
InplaceFloatOperationTests.test_power_float = expectedFailure(InplaceFloatOperationTests.test_power_float)
InplaceFloatOperationTests.test_lshift_float = expectedFailure(InplaceFloatOperationTests.test_lshift_float)
InplaceFloatOperationTests.test_rshift_float = expectedFailure(InplaceFloatOperationTests.test_rshift_float)
InplaceFloatOperationTests.test_and_float = expectedFailure(InplaceFloatOperationTests.test_and_float)
InplaceFloatOperationTests.test_xor_float = expectedFailure(InplaceFloatOperationTests.test_xor_float)
InplaceFloatOperationTests.test_or_float = expectedFailure(InplaceFloatOperationTests.test_or_float)

# InplaceFloatOperationTests.test_add_frozenset = expectedFailure(InplaceFloatOperationTests.test_add_frozenset)
# InplaceFloatOperationTests.test_subtract_frozenset = expectedFailure(InplaceFloatOperationTests.test_subtract_frozenset)
# InplaceFloatOperationTests.test_multiply_frozenset = expectedFailure(InplaceFloatOperationTests.test_multiply_frozenset)
# InplaceFloatOperationTests.test_floor_divide_frozenset = expectedFailure(InplaceFloatOperationTests.test_floor_divide_frozenset)
# InplaceFloatOperationTests.test_true_divide_frozenset = expectedFailure(InplaceFloatOperationTests.test_true_divide_frozenset)
# InplaceFloatOperationTests.test_modulo_frozenset = expectedFailure(InplaceFloatOperationTests.test_modulo_frozenset)
# InplaceFloatOperationTests.test_power_frozenset = expectedFailure(InplaceFloatOperationTests.test_power_frozenset)
# InplaceFloatOperationTests.test_lshift_frozenset = expectedFailure(InplaceFloatOperationTests.test_lshift_frozenset)
# InplaceFloatOperationTests.test_rshift_frozenset = expectedFailure(InplaceFloatOperationTests.test_rshift_frozenset)
# InplaceFloatOperationTests.test_and_frozenset = expectedFailure(InplaceFloatOperationTests.test_and_frozenset)
# InplaceFloatOperationTests.test_xor_frozenset = expectedFailure(InplaceFloatOperationTests.test_xor_frozenset)
# InplaceFloatOperationTests.test_or_frozenset = expectedFailure(InplaceFloatOperationTests.test_or_frozenset)

InplaceFloatOperationTests.test_add_int = expectedFailure(InplaceFloatOperationTests.test_add_int)
InplaceFloatOperationTests.test_subtract_int = expectedFailure(InplaceFloatOperationTests.test_subtract_int)
InplaceFloatOperationTests.test_multiply_int = expectedFailure(InplaceFloatOperationTests.test_multiply_int)
InplaceFloatOperationTests.test_floor_divide_int = expectedFailure(InplaceFloatOperationTests.test_floor_divide_int)
InplaceFloatOperationTests.test_true_divide_int = expectedFailure(InplaceFloatOperationTests.test_true_divide_int)
InplaceFloatOperationTests.test_modulo_int = expectedFailure(InplaceFloatOperationTests.test_modulo_int)
InplaceFloatOperationTests.test_power_int = expectedFailure(InplaceFloatOperationTests.test_power_int)
InplaceFloatOperationTests.test_lshift_int = expectedFailure(InplaceFloatOperationTests.test_lshift_int)
InplaceFloatOperationTests.test_rshift_int = expectedFailure(InplaceFloatOperationTests.test_rshift_int)
InplaceFloatOperationTests.test_and_int = expectedFailure(InplaceFloatOperationTests.test_and_int)
InplaceFloatOperationTests.test_xor_int = expectedFailure(InplaceFloatOperationTests.test_xor_int)
InplaceFloatOperationTests.test_or_int = expectedFailure(InplaceFloatOperationTests.test_or_int)

InplaceFloatOperationTests.test_add_list = expectedFailure(InplaceFloatOperationTests.test_add_list)
InplaceFloatOperationTests.test_subtract_list = expectedFailure(InplaceFloatOperationTests.test_subtract_list)
InplaceFloatOperationTests.test_multiply_list = expectedFailure(InplaceFloatOperationTests.test_multiply_list)
InplaceFloatOperationTests.test_floor_divide_list = expectedFailure(InplaceFloatOperationTests.test_floor_divide_list)
InplaceFloatOperationTests.test_true_divide_list = expectedFailure(InplaceFloatOperationTests.test_true_divide_list)
InplaceFloatOperationTests.test_modulo_list = expectedFailure(InplaceFloatOperationTests.test_modulo_list)
InplaceFloatOperationTests.test_power_list = expectedFailure(InplaceFloatOperationTests.test_power_list)
InplaceFloatOperationTests.test_lshift_list = expectedFailure(InplaceFloatOperationTests.test_lshift_list)
InplaceFloatOperationTests.test_rshift_list = expectedFailure(InplaceFloatOperationTests.test_rshift_list)
InplaceFloatOperationTests.test_and_list = expectedFailure(InplaceFloatOperationTests.test_and_list)
InplaceFloatOperationTests.test_xor_list = expectedFailure(InplaceFloatOperationTests.test_xor_list)
InplaceFloatOperationTests.test_or_list = expectedFailure(InplaceFloatOperationTests.test_or_list)

InplaceFloatOperationTests.test_add_set = expectedFailure(InplaceFloatOperationTests.test_add_set)
InplaceFloatOperationTests.test_subtract_set = expectedFailure(InplaceFloatOperationTests.test_subtract_set)
InplaceFloatOperationTests.test_multiply_set = expectedFailure(InplaceFloatOperationTests.test_multiply_set)
InplaceFloatOperationTests.test_floor_divide_set = expectedFailure(InplaceFloatOperationTests.test_floor_divide_set)
InplaceFloatOperationTests.test_true_divide_set = expectedFailure(InplaceFloatOperationTests.test_true_divide_set)
InplaceFloatOperationTests.test_modulo_set = expectedFailure(InplaceFloatOperationTests.test_modulo_set)
InplaceFloatOperationTests.test_power_set = expectedFailure(InplaceFloatOperationTests.test_power_set)
InplaceFloatOperationTests.test_lshift_set = expectedFailure(InplaceFloatOperationTests.test_lshift_set)
InplaceFloatOperationTests.test_rshift_set = expectedFailure(InplaceFloatOperationTests.test_rshift_set)
InplaceFloatOperationTests.test_and_set = expectedFailure(InplaceFloatOperationTests.test_and_set)
InplaceFloatOperationTests.test_xor_set = expectedFailure(InplaceFloatOperationTests.test_xor_set)
InplaceFloatOperationTests.test_or_set = expectedFailure(InplaceFloatOperationTests.test_or_set)

InplaceFloatOperationTests.test_add_str = expectedFailure(InplaceFloatOperationTests.test_add_str)
InplaceFloatOperationTests.test_subtract_str = expectedFailure(InplaceFloatOperationTests.test_subtract_str)
InplaceFloatOperationTests.test_multiply_str = expectedFailure(InplaceFloatOperationTests.test_multiply_str)
InplaceFloatOperationTests.test_floor_divide_str = expectedFailure(InplaceFloatOperationTests.test_floor_divide_str)
InplaceFloatOperationTests.test_true_divide_str = expectedFailure(InplaceFloatOperationTests.test_true_divide_str)
InplaceFloatOperationTests.test_modulo_str = expectedFailure(InplaceFloatOperationTests.test_modulo_str)
InplaceFloatOperationTests.test_power_str = expectedFailure(InplaceFloatOperationTests.test_power_str)
InplaceFloatOperationTests.test_lshift_str = expectedFailure(InplaceFloatOperationTests.test_lshift_str)
InplaceFloatOperationTests.test_rshift_str = expectedFailure(InplaceFloatOperationTests.test_rshift_str)
InplaceFloatOperationTests.test_and_str = expectedFailure(InplaceFloatOperationTests.test_and_str)
InplaceFloatOperationTests.test_xor_str = expectedFailure(InplaceFloatOperationTests.test_xor_str)
InplaceFloatOperationTests.test_or_str = expectedFailure(InplaceFloatOperationTests.test_or_str)

InplaceFloatOperationTests.test_add_tuple = expectedFailure(InplaceFloatOperationTests.test_add_tuple)
InplaceFloatOperationTests.test_subtract_tuple = expectedFailure(InplaceFloatOperationTests.test_subtract_tuple)
InplaceFloatOperationTests.test_multiply_tuple = expectedFailure(InplaceFloatOperationTests.test_multiply_tuple)
InplaceFloatOperationTests.test_floor_divide_tuple = expectedFailure(InplaceFloatOperationTests.test_floor_divide_tuple)
InplaceFloatOperationTests.test_true_divide_tuple = expectedFailure(InplaceFloatOperationTests.test_true_divide_tuple)
InplaceFloatOperationTests.test_modulo_tuple = expectedFailure(InplaceFloatOperationTests.test_modulo_tuple)
InplaceFloatOperationTests.test_power_tuple = expectedFailure(InplaceFloatOperationTests.test_power_tuple)
InplaceFloatOperationTests.test_lshift_tuple = expectedFailure(InplaceFloatOperationTests.test_lshift_tuple)
InplaceFloatOperationTests.test_rshift_tuple = expectedFailure(InplaceFloatOperationTests.test_rshift_tuple)
InplaceFloatOperationTests.test_and_tuple = expectedFailure(InplaceFloatOperationTests.test_and_tuple)
InplaceFloatOperationTests.test_xor_tuple = expectedFailure(InplaceFloatOperationTests.test_xor_tuple)
InplaceFloatOperationTests.test_or_tuple = expectedFailure(InplaceFloatOperationTests.test_or_tuple)