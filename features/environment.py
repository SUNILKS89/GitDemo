import requests
from APITesting.payload import *
from Utils.configurations import *
from Utils.resources import *

def after_scenario(context,scenario):
    if scenario.name == "Verify AddBook API functionality":
        print("\nafter scenario")
        delete_book_res = requests.delete(get_config()['API']['endpoint'] + APIResource.deleteBook,
                                          json={"ID": context.book_ID},
                                          headers={"Content-Type": "appliction/json"})
        res_del_book_json = delete_book_res.json()
        print(res_del_book_json["msg"])
        assert res_del_book_json["msg"] == "book is successfully deleted"
