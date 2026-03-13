# import sys
# import os
#
# import pytest
#
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
#
# import requests
# from pytest_bdd import *
# from APITesting.payload import *
# from Utils.configurations import *
# from Utils.resources import *
#
# #example to show the use of pytest-bdd. It is different from behave cucumber
#
# json_data = {"name":"Learn Appium Automation with Java",
#              "isbn":"shufgo",
#              "aisle":"975857",
#              "author":"john"
#              }
# scenarios("../BookAPI.feature")
# query = "select * from APIDevelop.Books"
# #response = requests.post("http://216.10.245.166/Library/Addbook.php",json=json_data,headers={"Content-Type":"application/json"},)
#
# @pytest.fixture
# def scenario_context():
#     return {}
# @given('the Book details which needs to be added to Library',target_fixture="step_implementation")
# def step_implementation():
#     url = get_config()['API']['endpoint']+APIResource.addbook
#     return url
#
# @when('we execute the AddBook PostAPI method',target_fixture="step_implementation1")
# def step_implementation1(step_implementation):
#     response = requests.post(step_implementation,json=build_payload_from_db(query),headers={"Content-Type":"application/json"},)
#     return response
#
# @then('book is successfully added',target_fixture="step_implementation2")
# def step_implementation2(step_implementation1,scenario_context,cleanup_scenario):
#     print(type(step_implementation1.text))
#     addbook_response = step_implementation1.json()
#     print(addbook_response)
#     print(type(addbook_response))
#     book_ID = addbook_response['ID']
#     print(book_ID)
#     scenario_context['book_ID'] = book_ID
#
# @pytest.fixture()
# def cleanup_scenario(scenario_context):
#     print("before scenario")
#
#     yield
#     print("\nafter scenario")
#     delete_book_res = requests.delete(get_config()['API']['endpoint'] + APIResource.deleteBook, json={"ID": scenario_context['book_ID']},
#                                       headers={"Content-Type": "appliction/json"})
#     res_del_book_json = delete_book_res.json()
#     print(res_del_book_json["msg"])
#     assert res_del_book_json["msg"] == "book is successfully deleted"