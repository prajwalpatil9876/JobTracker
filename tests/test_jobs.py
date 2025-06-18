def test_jobs(client):
     rv = client.get('/jobs/')
     assert rv.status_code == 200
