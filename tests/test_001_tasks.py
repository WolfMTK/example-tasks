import pytest
from httpx import AsyncClient


@pytest.mark.parametrize('json', [
    {'name': 'String',
     'description': 'String'},
    {'name': 'String2',
     'description': 'String2'}
])
async def test_001_create_task(async_client: AsyncClient, json: dict[str, str]):
    response  = await async_client.post('/tasks/', json=json)
    assert response.status_code == 200, 'Ошибка добавления задач!'
    data = response.json()
    del data['id']
    assert data == json, 'Неккоректные данные!'
