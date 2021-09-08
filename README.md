# Manual da API

## Cadastrar post:
POST http://{BASE_URL}/posts

```json
{
	"title": "title post",
	"author": "author of post",
	"tags": ["newPost", "MyPost"],
	"content": "post content"
}

```
#

## Ver todos os posts:
GET http://{BASE_URL}/posts
#

## Acessar um post pelo ID:
GET http://{BASE_URL}/posts/id
#

## Atualizar um post:
PATCH http://{BASE_URL}/posts/id

```json
{
    "<field>": "<value>",
}
```
#

## Deletar um post:
DELETE http://{BASE_URL}/posts/id
#