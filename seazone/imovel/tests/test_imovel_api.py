from datetime import datetime

from django.test import TestCase, Client


class ImovelApiTestCase(TestCase):
    fixtures = ['fixtures/imovel.json', 'fixtures/anuncio.json', 'fixtures/reserva.json']

    def setUp(self):
        self.c = Client()
        self.expected_keys_anuncio = ['id', 'code', 'guest_limit', 'bathroom_quantity', 'is_pet_friendly',
                                      'clean_value', 'activation_date', 'created_at', 'updated_at']

    def test_imovel_must_return_list(self):
        req = self.c.get('/api/imoveis/')
        self.assertEqual(req.status_code, 200)
        self.assertEqual(type(req.json()), list)
        self._validate_returned_keys(req.json()[0])

    def test_imovel_success_find(self):
        req = self.c.get('/api/imoveis/1/')
        self.assertEqual(req.status_code, 200)
        req_response = req.json()
        self.assertEqual(type(req_response), dict)
        self._validate_returned_keys(req_response)
        self.assertEqual(req_response['code'], "bbfb58dc-4b6c-4027-bada-094d4aaaef32")
        self.assertEqual(req_response['guest_limit'], 4)
        self.assertEqual(req_response['bathroom_quantity'], 2)
        self.assertEqual(req_response['is_pet_friendly'], True)
        self.assertEqual(req_response['clean_value'], 2000)
        self.assertEqual(req_response['activation_date'], "2022-11-15T21:24:05Z")

    def test_imovel_fail_find_return_list(self):
        req = self.c.get('/api/imoveis/404/')
        self.assertEqual(req.status_code, 200)
        self.assertEqual(type(req.json()), list)
        self._validate_returned_keys(req.json()[0])

    def test_imovel_delete(self):
        req = self.c.delete('/api/imoveis/1/')
        self.assertEqual(req.status_code, 204)

    def test_imovel_create(self):
        req = self.c.post('/api/imoveis/', data={
            'guest_limit': 3,
            'bathroom_quantity': 3,
            'is_pet_friendly': True,
            'clean_value': 1500,
            'activation_date': datetime.now()
        })
        self.assertEqual(req.status_code, 201)
        self._validate_returned_keys(req.json())

    def test_imovel_create_try_insert_code_and_fail(self):
        code_to_try = 'abcd'
        req = self.c.post('/api/imoveis/', data={
            'code': code_to_try,
            'guest_limit': 1,
            'bathroom_quantity': 1,
            'is_pet_friendly': False,
            'clean_value': 2500,
            'activation_date': datetime.now()
        })
        self.assertEqual(req.status_code, 201)
        self.assertNotEqual(req.json()['code'], code_to_try)

    def test_imovel_update(self):
        req = self.c.patch('/api/imoveis/1/', data={
            'clean_value': 4000
        }, content_type='application/json')
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['clean_value'], 4000)
        self._validate_returned_keys(req.json())

    def test_imovel_update_try_insert_code_and_fail(self):
        code_to_try = 'abcd'
        req = self.c.patch('/api/imoveis/1/', data={
            'code': code_to_try
        }, content_type='application/json')
        self.assertEqual(req.status_code, 200)
        self.assertNotEqual(req.json()['code'], code_to_try)

    def _validate_returned_keys(self, obj):
        self.assertCountEqual(list(obj.keys()), self.expected_keys_anuncio)
