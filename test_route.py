from fastapi.testclient import TestClient
from docker_con1.route import app

from docker_con1.model import test_create_db_tables, test_engine, get_session

import pytest
from sqlmodel import Session

# create session for test
@pytest.fixture(name="session")
def session_fixture():
    test_create_db_tables()
    with Session(test_engine) as session:   
        yield session

# Create the new fixture named "client"
@pytest.fixture(name="client") 
def client_fixture(session : Session):  # This client fixture, in turn, also requires the session fixture.

    # Define the new function that will be the new dependency override.
    def get_session_override():
        return session 
    
    # Here's where we create the custom session object for this test in a with block.
    # It uses the new custom engine we created, so anything that uses this session will be using the testing database.
    app.dependency_overrides[get_session] = get_session_override

    client = TestClient(app)
    yield client
    
    # we can restore the application back to normal, by removing all the values in this dictionary app.dependency_overrides. 
    app.dependency_overrides.clear()

###### ====================  Read Main  ====================  ====================

# function to read main file
def test_read_main():
    #create TestClind for the fastapi app
    clinet = TestClient(app=app)
    response = clinet.get('/')
    assert response.status_code == 200
    assert response.json() == {"Docker ": "Compose Image"}
    
###### ====================  Get Data From Test Database ====================  ====================

###### get todo from test-db
    
def test_get_todo(client: TestClient):
    response = client.get('/api/get_todo')
    assert response.status_code == 200

###### ====================  Add Data Into Test Database ====================  ====================

###### add data into test-db
    
def test_add_todo(client: TestClient):

    add_new_name = 'Docker Compose'

    response = client.post('/api/add_todo', json=add_new_name)
    assert response.status_code == 200

    data = response.json()
    assert data["todo_name"] == add_new_name

###### ====================  Update Data From Test Database ====================  ====================

##### update data from test-db
    
def test_update_todo(client: TestClient):

    update_todo_id = 8
    update_todo_name = 'Genrative AI'

    response = client.put(f'/api/update_todo?id={update_todo_id}', json=update_todo_name)  
    assert response.status_code == 200 
        
###### ====================  Delete Data From Test Database ====================  ====================

###### delete data from test-db
    
# def test_delete_todo(client: TestClient):

#     id = 7

#     response = client.delete(f'/api/delete_todo/{id}')
#     assert response.status_code == 200

#     for ids in response.json():
#         assert ids
#         print(ids)


#https://sqlmodel.tiangolo.com/tutorial/delete/
#https://sqlmodel.tiangolo.com/tutorial/fastapi/delete/?h=dele





