from django.test import TestCase, Client


class AnuncioApiTestCase(TestCase):
    fixtures = ['fixtures/imovel.json', 'fixtures/anuncio.json', 'fixtures/reserva.json']

    def setUp(self):
        self.c = Client()
        self.expected_keys_anuncio = ['id', 'imovel', 'platform', 'platform_fee', 'created_at', 'updated_at']

    def test_anuncio_must_return_list(self):
        req = self.c.get('/api/anuncios/')
        self.assertEqual(req.status_code, 200)
        self.assertEqual(type(req.json()), list)
        self._validate_returned_keys(req.json()[0])

    def test_anuncio_success_find(self):
        req = self.c.get('/api/anuncios/1/')
        self.assertEqual(req.status_code, 200)
        req_response = req.json()
        self.assertEqual(type(req_response), dict)
        self._validate_returned_keys(req_response)
        self.assertEqual(req_response['platform'], 'airbnb')
        self.assertEqual(req_response['platform_fee'], 4500)

    def test_anuncio_fail_find_return_list(self):
        req = self.c.get('/api/anuncios/404/')
        self.assertEqual(req.status_code, 200)
        self.assertEqual(type(req.json()), list)
        self._validate_returned_keys(req.json()[0])

    def test_anuncio_delete_not_allowed(self):
        req = self.c.delete('/api/anuncios/1/')
        self.assertEqual(req.status_code, 405)

    def test_anuncio_create(self):
        req = self.c.post('/api/anuncios/', data={
            'imovel': 1,
            'platform': 'test platform',
            'platform_fee': 10000
        })
        self.assertEqual(req.status_code, 201)
        self._validate_returned_keys(req.json())

    def test_anuncio_update(self):
        req = self.c.patch('/api/anuncios/1/', data={
            'platform': 'updated platform'
        }, content_type='application/json')
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['platform'], 'updated platform')
        self.assertEqual(req.json()['platform_fee'], 4500)
        self._validate_returned_keys(req.json())

    def _validate_returned_keys(self, obj):
        self.assertCountEqual(list(obj.keys()), self.expected_keys_anuncio)
