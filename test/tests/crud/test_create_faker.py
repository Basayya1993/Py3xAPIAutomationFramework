import json

import allure
import pytest
import logging
from src.helpers.api_request_wrappers import post_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_managers import *
from src.helpers.common_verification import *
from src.utils.utils import Utils


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description("Creating a Booking from the payload and verify "
                        "that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        LOGGER = logging.getLogger(__name__)
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking_fake(),
            in_json=False
        )
        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])
        LOGGER.info(response.json()["bookingid"])
        user_data = response.json()
        user_str = json.dumps(user_data, indent=4)
        print(user_str)
        print('\n', response.json()['bookingid'])
        print(response.json()['booking']['firstname'])



