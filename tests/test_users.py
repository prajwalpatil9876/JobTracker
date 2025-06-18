def test_users(client):
    rv = client.get('/users/')
    assert rv.status_code == 200
