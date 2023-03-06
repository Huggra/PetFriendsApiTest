from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()

# Тесты сделанные во время прохождения модуля 19
def test_get_api_key_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

# Тесты для задания 19.7.2
def test_create_new_pet(name='Барсик', animal_type='Кот', age='5', pet_photo='images/Pet.jpg'):
    status, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_get_my_new_pet(my_pets='my_pets', name='Барсик', animal_type='Кот', age='5'):
    status, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, my_pets)
    assert status == 200
    filtered = filter(lambda pet: pet['name'] == name and pet['age'] == age and pet['animal_type'] == animal_type, result['pets'])
    assert len(list(filtered)) > 0

def test_create_new_pet_invalid_age(name='Барсик', animal_type='Кот', age='-1', pet_photo='images/Pet.jpg'):
    status, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_create_new_pet_invalid_name(name='АААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААА\n'
                                          'АААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААА\n'
                                          'АААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААА', animal_type='Кот', age='5', pet_photo='images/Pet.jpg'):
    status, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_special_symbols(name='😀😃😄😁😅😆😂🤣😉😊☺🙂🙃😇😗', animal_type='Кот', age='5', pet_photo='images/Pet.jpg'):
    status, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_empty_fields(name='', animal_type='', age='', pet_photo='images/Pet.jpg'):
    status, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_create_new_pet_with_chinese_name(name='一堆文字一堆文字', animal_type='Кот', age='5', pet_photo='images/Pet.jpg'):
    status, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name



