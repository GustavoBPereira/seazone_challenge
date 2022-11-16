# seazone_challenge


### Visão geral

Uma api que possui 3 entidades: `imovel`, `anuncio`, `reserva`.

Uma reserva irá ser criada com base em um anuncio e um anuncio será criado com base em um imovel.

### Entidades

#### Imóvel:
```
"code": Um hash único que não poderá ser inserido manualmente ou alterado,
"guest_limit": um inteiro,
"bathroom_quantity": um inteiro,
"is_pet_friendly": boleano,
"clean_value": um inteiro,
"activation_date": datetime em formato iso,
"created_at": datetime em formato iso (gerado automaticamente),
"updated_at": datetime em formato iso (gerado automaticamente)"
```

#### Anúncio:
```
"imovel": pk do imovel,
"platform": um charfield,
"platform_fee": um inteiro,
"created_at": datetime em formato iso (gerado automaticamente),
"updated_at": datetime em formato iso (gerado automaticamente)"
```

#### Reserva:
```
"code": Um hash único que não poderá ser inserido manualmente ou alterado,
"anuncio": pk do anuncio,
"check_in": datetime em formato iso,
"check_out": datetime em formato iso,
"total_price": um inteiro,
"comment": um charfield,
"guest_quantity": um inteiro,
"created_at": datetime em formato iso (gerado automaticamente),
"updated_at": datetime em formato iso (gerado automaticamente)
```

## End Points

### Imóvel

#### GET /api/imoveis
- response 200 application/json
```
[
    {imovel entidade},
    {imovel entidade},
    {imovel entidade},
]
```

#### GET /api/imoveis/:id
Se encontrado:
- response 200 application/json
```
    {imovel entidade}
```
Se não encontrado:
- response 200 application/json
```
[
    {imovel entidade},
    {imovel entidade},
    {imovel entidade},
]
```

#### DELETE /api/imoveis/:id
- response 204


#### POST /api/imoveis/
- payload esperado:
```
{
    'guest_limit': 3,
    'bathroom_quantity': 3,
    'is_pet_friendly': True,
    'clean_value': 1500,
    'activation_date': datetime in iso
}
```
- response 201 application/json
```
{imovel entidade}
```

#### PATCH /api/imoveis/:id
- payload esperado:
```
{
    'guest_limit': 3, <not required>
    'bathroom_quantity': 3, <not required>
    'is_pet_friendly': True, <not required>
    'clean_value': 1500, <not required>
    'activation_date': datetime in iso <not required>
}
```
- response 200 application/json
```
{imovel entidade}
```

### Anuncio

#### GET /api/anuncios
- response 200 application/json
```
[
    {anuncio entidade},
    {anuncio entidade},
    {anuncio entidade},
]
```

#### GET /api/anuncios/:id
Se encontrado:
- response 200 application/json
```
    {anuncio entidade}
```
Se não encontrado:
- response 200 application/json
```
[
    {anuncio entidade},
    {anuncio entidade},
    {anuncio entidade},
]
```

#### POST /api/anuncios/
- payload esperado:
```
{
    'imovel': 1,
    'platform': 'airbnb',
    'platform_fee': 1500,
}
```
- response 201 application/json
```
{anuncio entidade}
```

#### PATCH /api/anuncios/:id
- payload esperado:
```
{
    'imovel': 1, <not required>
    'platform': 'airbnb', <not required>
    'platform_fee': 1500, <not required>
}
```
- response 200 application/json
```
{anuncio entidade}
```

### Reserva

#### GET /api/reservas
- response 200 application/json
```
[
    {reserva entidade},
    {reserva entidade},
    {reserva entidade},
]
```

#### GET /api/reservas/:id
Se encontrado:
- response 200 application/json
```
    {reserva entidade}
```
Se não encontrado:
- response 200 application/json
```
[
    {reserva entidade},
    {reserva entidade},
    {reserva entidade},
]
```

#### DELETE /api/reservas/:id
- response 204


#### POST /api/reservas/
- payload esperado:
```
{
    'anuncio': 3,
    'check_in': '2022-11-16T09:00:39.331298',
    'check_out': '2022-11-20T09:00:39.331298',
    'price': 100000 (o total price será a soma disso com a platform_fee e clean_value),
    'guest_quantity': 2
}
```
Se check_in for antes de check_out e limite de hospedes forem respeitadas
- response 201 application/json
```
{reserva entidade}
```
Do contrário:
- response 400


#### PATCH /api/reservas/:id
- payload esperado:
```
{
    'anuncio': 1 <not required> ,
    'check_in': '2022-11-16T09:00:39.331298' <not required> ,
    'check_out': '2022-11-20T09:00:39.331298' <not required> ,
    'guest_quantity': 2 <not required>
}
Se check_in for antes de check_out e limite de hospedes forem respeitadas
- response 200 application/json
```
{reserva entidade}
```
Do contrário
- response 400


### Build and Tests
```
# primeiro clone o projeto:
git clone git@github.com:GustavoBPereira/seazone_challenge.git
cd seazone_challenge

# Apos isso, crie uma virtualenv e installe dentro dela, os requirements do projeto
python -m virtualenv --python={path ou alias para seu (python>=3.8)} venv
source venv/bin/activate
pip install -r requirements.txt

# Preparando a banco de dados
python manage.py migrate

# Para rodar as 3 fixtures de forma simples
python manage.py loadfixtures

# Para rodar o servidor local
python manage.py runserver

# Para rodar os testes
python manage.py test
```