from odoo.tests.common import TransactionCase

class TestTest(TransactionCase):

    test_tags = ['standard']

    def test_create_record(self):
        """Prueba la creación de un registro en la clase `ucuenca.test`."""

        # Crea un nuevo registro
        record = self.env['ucuenca.test'].create({
            'name': 'Prueba unitaria',
            'description': 'Esta es una prueba unitaria para la clase `test`.',
            'value': 17,
        })

        # Verifica que el registro se haya creado correctamente
        self.assertEqual(record.name, 'Prueba unitaria')
        self.assertEqual(record.description, 'Esta es una prueba unitaria para la clase `test`.')
        self.assertEqual(record.value, 17)