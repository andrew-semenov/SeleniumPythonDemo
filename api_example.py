import requests
import json


def api_example():

    # Create token
    token_data = {
        "username": "admin",
        "password": "password123"
    }
    token_url = "https://restful-booker.herokuapp.com/auth/"
    token_str = requests.post(token_url, json=token_data)
    token = json.loads(token_str.text)

    # Create booking
    booking_data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    api_url = "https://restful-booker.herokuapp.com/booking/"
    created_booking_str = requests.post(api_url, json=booking_data)
    created_booking = json.loads(created_booking_str.text)
    assert created_booking["booking"]["firstname"] == booking_data["firstname"]

    # Update booking
    booking_data["firstname"] = "James"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": "token=" + token['token']
    }
    api_url_booking = api_url + str(created_booking["bookingid"])
    updated_booking_str = requests.put(api_url_booking, json=booking_data, headers=headers)
    updated_booking = json.loads(updated_booking_str.text)
    assert updated_booking["firstname"] == booking_data["firstname"]

    # Partial update booking
    partial_update_booking_data = {
        "firstname": "Bob",
        "lastname": "Garris",
    }
    partial_updated_booking_str = requests.patch(api_url_booking, json=partial_update_booking_data, headers=headers)
    partial_updated_booking = json.loads(partial_updated_booking_str.text)
    assert partial_updated_booking["firstname"] == partial_update_booking_data["firstname"]
    assert partial_updated_booking["lastname"] == partial_update_booking_data["lastname"]

    # Delete booking
    deleted_booking_str = requests.delete(api_url_booking, headers=headers)
    assert deleted_booking_str.text == "Created"


api_example()
