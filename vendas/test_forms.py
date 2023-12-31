import pytest
from vendas.forms import ItemPedidoForm

class TestItemPedidoForm:

    # Form is valid with all fields filled correctly
    def test_form_valid_with_all_fields_filled_correctly(self):
        form_data = {
            'produto_id': '123',
            'quantidade': 5,
            'desconto': 10.50
        }
        form = ItemPedidoForm(data=form_data)
        assert form.is_valid()


#     # Form is invalid with empty fields
#     def test_form_invalid_with_empty_fields(self):
#         form_data = {
#             'produto_id': '',
#             'quantidade': None,
#             'desconto': None
#         }
#         form = ItemPedidoForm(data=form_data)
#         assert not form.is_valid()


#     # Form is invalid with invalid 'produto_id' field
#     def test_form_invalid_with_invalid_produto_id_field(self):
#         form_data = {
#             'produto_id': 'abc',
#             'quantidade': 5,
#             'desconto': 10.50
#         }
#         form = ItemPedidoForm(data=form_data)
#         assert not form.is_valid()


#     # Form is invalid with empty fields
#     def test_form_invalid_with_empty_fields(self):
#         form_data = {
#             'produto_id': '',
#             'quantidade': None,
#             'desconto': None
#         }
#         form = ItemPedidoForm(data=form_data)
#         assert not form.is_valid()


#     # Form is valid with all fields filled correctly
#     def test_form_valid_with_all_fields_filled_correctly(self):
#         form_data = {
#             'produto_id': '123',
#             'quantidade': 5,
#             'desconto': 10.50
#         }
#         form = ItemPedidoForm(data=form_data)
#         assert form.is_valid()


#     # Form is invalid with invalid 'produto_id' field
#     def test_form_invalid_with_invalid_produto_id_field(self):
#         form_data = {
#             'produto_id': 'abc',
#             'quantidade': 5,
#             'desconto': 10.50
#         }
#         form = ItemPedidoForm(data=form_data)
#         assert not form.is_valid()


#     # Form is invalid with 'quantidade' field equal to zero
#     def test_form_invalid_with_zero_quantidade_field(self):
#         form_data = {
#             'produto_id': '123',
#             'quantidade': 0,
#             'desconto': 10.50
#         }
#         form = ItemPedidoForm(data=form_data)
#         assert not form.is_valid()


#     # Form is invalid with 'desconto' field equal to zero
#     def test_form_invalid_with_zero_desconto_field(self):
#         form_data = {
#             'produto_id': '123',
#             'quantidade': 5,
#             'desconto': 0
#         }
#         form = ItemPedidoForm(data=form_data)
#         assert not form.is_valid()


#     # Form is invalid with 'desconto' field greater than 100
#     def test_form_invalid_with_desconto_greater_than_100(self):
#         form_data = {
#             'produto_id': '123',
#             'quantidade': 5,
#             'desconto': 150.00
#         }
#         form = ItemPedidoForm(data=form_data)
#         assert not form.is_valid()


#     # Form is invalid with 'desconto' field with more than two decimal places
#     def test_form_invalid_with_invalid_desconto_field(self):
#         form_data = {
#             'produto_id': '123',
#             'quantidade': 5,
#             'desconto': 10.555
#         }
#         form = ItemPedidoForm(data=form_data)
#         assert not form.is_valid()


#     # Form is invalid with 'produto_id' field with more than 100 characters
#     def test_form_invalid_with_long_produto_id_field(self):
#         form_data = {
#             'produto_id': 'a' * 101,
#             'quantidade': 5,
#             'desconto': 10.50
#         }
#         form = ItemPedidoForm(data=form_data)
#         assert not form.is_valid()

