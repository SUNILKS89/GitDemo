import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import requests
from behave import *
from APITesting.payload import *
from Utils.configurations import *
from Utils.resources import *

#example to show the use of behave

json_data = {"name":"Learn Appium Automation with Java",
             "isbn":"shufgo",
             "aisle":"975857",
             "author":"john"
             }

query = "select * from APIDevelop.Books"
#response = requests.post("http://216.10.245.166/Library/Addbook.php",json=json_data,headers={"Content-Type":"application/json"},)


@given('the Book details which needs to be added to Library')
def step_implementation(context):
    context.url = get_config()['API']['endpoint']+APIResource.addbook
    context.header = {"Content-Type":"application/json"}
    #context.payload = build_payload_from_db(query)#getting data from database
    context.payload = add_book_payload("manfgfft","655756")

@when('we execute the AddBook PostAPI method')
def step_implementation1(context):
    context.response = requests.post(context.url,json=context.payload,headers=context.header)


@then('book is successfully added')
def step_implementation2(context):
    print(type(context.response.text))
    addbook_response = context.response.json()
    print(addbook_response)
    print(type(addbook_response))
    context.book_ID = addbook_response['ID']
    print(context.book_ID)

@given('the Book details with {isbn} and {aisle}')
def step_impl(context,isbn,aisle):
    context.url = get_config()['API']['endpoint']+APIResource.addbook
    context.header = {"Content-Type":"application/json"}
    context.payload = add_book_payload(isbn,aisle)


@given('I have GitHub auth credentials')
def step_impl(context):
    context.github_session = requests.session()
    context.github_session.auth = ('sunilks85',
                           "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")

    context.url = "https://api.github.com/user/repos"




@when('I hit getRepo API of GitHub')
def step_impl(context):
    context.response = context.github_session.get(context.url)


@then('status code of response should be {statuscode:d}')
def step_impl(context,statuscode):
    print(context.response.status_code)
    assert context.response.status_code == statuscode
