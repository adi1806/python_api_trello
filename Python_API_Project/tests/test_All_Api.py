import pytest
from ..utils.apimethod_util import ApiClient
from ..data.poco import CreateCard, CreateBoard, CreateList, CardResponse
from ..utils.parser_util import ConfigParser
from ..data.poco import UpdateCard
import random
import string
import json
import logging
characters = string.ascii_letters + string.digits
random_string = ''.join(random.choice(characters) for i in range(5))

def test_create_NewBoard():

    # Check if the board exists with an Existing board id then Delete the old board and Create New one
    client = ApiClient()
    id_board= client.id_board
    response = client.get(endpoint=f"/boards/{id_board}")

    if response.status_code == 200:  # Board exists
        print(f"Board with ID {id_board} exists. Deleting it.")

        # Step 2: Delete the board
        delete_response = client.delete(endpoint=f"/boards/{id_board}")
        assert delete_response.status_code == 200, f"Failed to delete board {id_board}. Status code: {delete_response.status_code}"
        print(f"Board {id_board} deleted successfully.")

    elif response.status_code == 404:  # Board does not exist
        print(f"No board found with ID {id_board}. Proceeding to create a new one.")
    else:
        raise Exception(
            f"Unexpected error occurred while checking board {id_board}. Status code: {response.status_code}")


    boardName = "AdityaNewBoard  " + random_string
    print("Created Board Name:\n", boardName)

    queryParam = CreateBoard(name=boardName)
    response = client.post(endpoint="boards", param=queryParam.__dict__)
    assert response.status_code == 200

    response_boardData = response.json()
    print("Response Board Data:\n", json.dumps(response_boardData, indent=4))
    logging.basicConfig(level=logging.INFO)
    logging.info("Response Board Data: %s", response_boardData)

    assert response_boardData['name'] == boardName
    ConfigParser().set_trello_data(key="id_board", value=response_boardData['id'])

def test_create_List():
    client = ApiClient()
    id_board = client.id_board
    listName = "AdityaNewList " + random_string
    print("Created List Name:\n", listName)

    queryParam = CreateList(name=listName, idBoard=id_board)
    response = client.post(endpoint="lists", param=queryParam.__dict__)

    assert response.status_code == 200
    response_listData = response.json()
    print("Response list Data:\n", json.dumps(response_listData, indent=4))
    logging.basicConfig(level=logging.INFO)
    logging.info("Response list Data: %s", response_listData)

    assert response_listData['name'] == listName
    assert response_listData['idBoard'] == id_board
    print("Created list Id:\n", response_listData['id'])

    ConfigParser().set_trello_data(key="id_list", value=response_listData['id'])

def test_create_card_with_valid_idList():
    client = ApiClient()
    id_List = client.id_list
    cardName = "AdityaNewtestCard  " + random_string
    print("Created Card Name:\n", cardName)

    queryParam = CreateCard(name=cardName, desc="Description of the new card", idList=id_List)
    response = client.post(endpoint="cards", param=queryParam.__dict__)

    assert response.status_code == 200
    response_cardData = response.json()
    print("Response Card Data:\n", json.dumps(response_cardData, indent=4))
    logging.basicConfig(level=logging.INFO)
    logging.info("Response Board Data: %s", response_cardData)

    assert response_cardData['name'] == queryParam.name
    assert response_cardData['desc'] == queryParam.desc
    assert response_cardData['idList'] == queryParam.idList
    print("Created card Id:\n", response_cardData['id'])

    ConfigParser().set_trello_data(key="card_id", value=response_cardData['id'])

def test_create_card_with_inValid_idList():
    client = ApiClient()
    invalid_id_list = client.invalid_id_list
    queryParam = CreateCard(name="New Card With invalid id", desc="Description of the new card", idList=invalid_id_list)
    response = client.post(endpoint="cards", param=queryParam.__dict__)

    assert response.status_code == 400, f'Expected response code is 400, but found {response.status_code}'
    # Assert the response status code and print when it's correct
    if response.status_code == 400:
        print(f"Correct status code received with invalid data: {response.status_code}")
    else:
        print(f"Unexpected status code received: {response.status_code}")

def test_get_card_with_valid_cardId():
    client = ApiClient()
    card_id = client.card_id
    response = client.get(endpoint=f"/cards/{card_id}")

    # Check the response status code
    assert response.status_code == 200
    response_getdata = response.json()

   #using poco
    card_response = CardResponse(
        id=response_getdata['id'],
        name=response_getdata['name'],
        desc=response_getdata['desc'],
        id_list=response_getdata['idList']
    )

    assert card_response.id == card_id
    assert card_response.desc == "Description of the new card"
    assert card_response.id_list == client.id_list


    print("Response card get Data:\n", json.dumps(response_getdata, indent=4))
    logging.basicConfig(level=logging.INFO)
    logging.info("Response card get Data: %s", response_getdata)

def test_get_card_with_Invalid_cardId():
    client = ApiClient()
    card_id = client.invalid_card_id
    response = client.get(endpoint=f"/cards/{card_id}")

    # Check the response status code
    assert response.status_code == 404, f'expected response code is {404}, but found {response.status_code}'
    # Assert the response status code and print when it's correct
    if response.status_code == 404:
        print(f"Correct status code received with invalid data: {response.status_code}")
    else:
        print(f"Unexpected status code received: {response.status_code}")

def test_update_card_with_valid_cardId():
    client = ApiClient()
    card_id = client.card_id
    updatedCardName = "Aditya Card Name updated"
    updated_card = UpdateCard(name=updatedCardName)
    response = client.put(endpoint=f"cards/{card_id}", param=updated_card.__dict__)

    assert response.status_code == 200
    response_data = response.json()
    print("Response update Data:\n", json.dumps(response_data, indent=4))
    logging.basicConfig(level=logging.INFO)
    logging.info("Response update Data: %s", response_data)

    assert response_data['id'] == card_id
    assert response_data['name'] == updatedCardName

def test_update_card_with_inValid_cardId():
    client = ApiClient()
    card_id = client.invalid_card_id
    updated_card = UpdateCard(name="Updated New Card")
    response = client.put(endpoint=f"cards/{card_id}", param=updated_card.__dict__)

    assert response.status_code == 404, f'expected response code is {404}, but found {response.status_code}'
    # Assert the response status code and print when it's correct
    if response.status_code == 404:
        print(f"Correct status code received with invalid data: {response.status_code}")
    else:
        print(f"Unexpected status code received: {response.status_code}")

def test_delete_card_with_inValid_cardId():
    card_id = "12345"
    client = ApiClient()
    response = client.delete(endpoint=f"cards/{card_id}")

    assert response.status_code == 400, f'expected response code is {400}, but found {response.status_code}'
    # Assert the response status code and print when it's correct
    if response.status_code == 400:
        print(f"Correct status code received with invalid data: {response.status_code}")
    else:
        print(f"Unexpected status code received: {response.status_code}")

def test_delete_card_with_empty_cardId():
    card_id = ""
    client = ApiClient()
    response = client.delete(endpoint=f"cards/{card_id}")

    assert response.status_code == 404, f'expected response code is {404}, but found {response.status_code}'
    # Assert the response status code and print when it's correct
    if response.status_code == 404:
        print(f"Correct status code received with invalid data: {response.status_code}")
    else:
        print(f"Unexpected status code received: {response.status_code}")

def test_delete_card_with_valid_cardId():
    client = ApiClient()
    id_List = client.id_list
    queryParam = CreateCard(name="New Deleted Card", desc="Description of the new card", idList=id_List)
    response = client.post(endpoint="cards", param=queryParam.__dict__)

    assert response.status_code == 200
    response_data = response.json()
    print (response.json())

    card_id = response_data['id']
    print(card_id)
    delete_response = client.delete(endpoint=f"cards/{card_id}")

    assert delete_response.status_code == 200
