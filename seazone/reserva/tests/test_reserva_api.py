from django.test import TestCase, Client

from seazone.anuncio.models import Anuncio


class ImovelApiTestCase(TestCase):
    fixtures = ['fixtures/imovel.json', 'fixtures/anuncio.json', 'fixtures/reserva.json']

    def setUp(self):
        self.c = Client()
        self.expected_keys_anuncio = ['id', 'code', 'anuncio', 'check_in', 'check_out', 'total_price',
                                      'comment', 'guest_quantity', 'created_at', 'updated_at']

    def test_reserva_must_return_list(self):
        req = self.c.get('/api/reservas/')
        self.assertEqual(type(req.json()), list)
        self.assertEqual(req.status_code, 200)
        self._validate_returned_keys(req.json()[0])

    def test_reserva_success_find(self):
        req = self.c.get('/api/reservas/1/')
        self.assertEqual(req.status_code, 200)
        req_response = req.json()
        self.assertEqual(type(req_response), dict)
        self._validate_returned_keys(req_response)
        self.assertEqual(req_response['code'], "88b99a05-b96a-4ccf-b87a-589a287d46e4")
        self.assertEqual(req_response['anuncio'], 1)
        self.assertEqual(req_response['check_in'], '2022-11-15T21:31:27Z')
        self.assertEqual(req_response['check_out'], '2022-11-17T21:31:31Z')
        self.assertEqual(req_response['total_price'], 25000)
        self.assertEqual(req_response['comment'], 'Gostei do chuveiro!!!')
        self.assertEqual(req_response['guest_quantity'], 2)

    def test_reserva_fail_find_return_list(self):
        req = self.c.get('/api/reservas/404/')
        self.assertEqual(req.status_code, 200)
        self.assertEqual(type(req.json()), list)
        self._validate_returned_keys(req.json()[0])

    def test_reserva_delete(self):
        req = self.c.delete('/api/reservas/1/')
        self.assertEqual(req.status_code, 204)

    def test_reserva_create(self):
        anuncio = Anuncio.objects.get(pk=1)
        reservation_price = 20000
        reservation_total_price = reservation_price + anuncio.imovel.clean_value
        req = self.c.post('/api/reservas/', data={
            'anuncio': 1,
            'check_in': '2022-11-16T09:00:39.331298',
            'check_out': '2022-11-20T09:00:39.331298',
            'price': reservation_price,
            'guest_quantity': 2
        })
        self.assertEqual(req.status_code, 201)
        req_response = req.json()
        self._validate_returned_keys(req_response)
        self.assertEqual(req_response['total_price'], reservation_total_price)

    def test_reserva_create_try_insert_code_and_fail(self):
        code_to_try = 'abcd'
        req = self.c.post('/api/reservas/', data={
            'code': code_to_try,
            'anuncio': 1,
            'check_in': '2022-11-16T09:00:39.331298',
            'check_out': '2022-11-20T09:00:39.331298',
            'price': 30000,
            'guest_quantity': 2
        })
        self.assertNotEqual(req.json()['code'], code_to_try)

    def test_reserva_create_over_guest_limit(self):
        req = self.c.post('/api/reservas/', data={
            'anuncio': 1,
            'check_in': '2022-11-16T09:00:39.331298',
            'check_out': '2022-11-20T09:00:39.331298',
            'price': 30000,
            'guest_quantity': 5
        })
        self.assertEqual(req.status_code, 400)

    def test_reserva_create_checkin_after_checkout(self):
        req = self.c.post('/api/reservas/', data={
            'anuncio': 1,
            'check_in': '2022-11-20T09:00:39.331298',
            'check_out': '2022-11-16T09:00:39.331298',
            'price': 30000,
            'guest_quantity': 5
        })
        self.assertEqual(req.status_code, 400)

    def test_reserva_update(self):
        req = self.c.patch('/api/reservas/1/', data={
            'comment': 'Wifi estava fraco'
        }, content_type='application/json')
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['comment'], 'Wifi estava fraco')
        self._validate_returned_keys(req.json())

    def test_reserva_update_guest_quantity_correct(self):
        req = self.c.patch('/api/reservas/1/', data={
            'guest_quantity': 4
        }, content_type='application/json')
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['guest_quantity'], 4)

    def test_reserva_update_guest_quantity_wrong(self):
        req = self.c.patch('/api/reservas/1/', data={
            'guest_quantity': 6
        }, content_type='application/json')
        self.assertEqual(req.status_code, 400)

    def test_reserva_update_try_insert_code_and_fail(self):
        code_to_try = 'abcd'
        req = self.c.patch('/api/reservas/1/', data={
            'code': code_to_try
        }, content_type='application/json')
        self.assertEqual(req.status_code, 200)
        self.assertNotEqual(req.json()['code'], code_to_try)

    def test_reserva_update_try_change_price_and_fail(self):
        new_price_to_try = 1000
        req = self.c.patch('/api/reservas/1/', data={
            'total_price': new_price_to_try
        }, content_type='application/json')
        self.assertEqual(req.status_code, 200)
        self.assertNotEqual(req.json()['total_price'], new_price_to_try)

    def test_reserva_update_check_in_after_check_out(self):
        req = self.c.patch('/api/reservas/1/', data={
            'check_in': '2023-11-15T21:31:27Z',
        }, content_type='application/json')
        self.assertEqual(req.status_code, 400)

    def test_reserva_update_check_out_before_check_in(self):
        req = self.c.patch('/api/reservas/1/', data={
            'check_out': '2020-11-15T21:31:27Z',
        }, content_type='application/json')
        self.assertEqual(req.status_code, 400)

    def _validate_returned_keys(self, obj):
        self.assertCountEqual(list(obj.keys()), self.expected_keys_anuncio)
