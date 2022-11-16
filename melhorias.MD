
 - [ ] Definir valor da diaria no imovel para que a api de reservas só passe a data e o valor seja calculado com base nisso.
 - [ ] Adicionar a camada de autenticação, para que seja possivel atribuir propriedade as instancias, para que isso seja usada na api:
     - [ ] Somente o dono da reserva pode alterala/deletada
     - [ ] Somente o dono da reserva ou o dono do imovel podem ver a reserva
     - [ ] Todos podem ver os imoveis, mas somente o dono altera-lo
     - [ ] Todos podem ver os anuncios, mas somente o dono altera-lo
     - [ ] Anuncios só podem ser criados se o imovel passado referente ao anuncio for de propriedade do usuario que faz a requisição
 - [ ] Utilizar docker para subir o ambiente [tutorial](https://github.com/tcarreira/django-docker/blob/master/README-PT.md), será possivel subir além do docker que executará o python (django) mas também um banco de dados e um servidor http como o nginx por exemplo.