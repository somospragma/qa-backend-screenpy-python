import pytest

from screenpy import Actor, given, when, then
from screenpy.actions import See
from screenpy.resolutions import IsEqualTo, ContainsTheEntry

from screenpy_requests.actions import SendPOSTRequest
from screenpy_requests.questions import BodyOfTheLastResponse, StatusCodeOfTheLastResponse

from utils.urls import *

@pytest.mark.parametrize("user_name, user_job", [("Jorge", "Automation"),("Luis", "Manager"),("Maria", "President")])
def test_create_user(user_name: str, user_job: str, Jorge: Actor) -> None:
    when(Jorge).attempts_to(
        SendPOSTRequest.to(
            BASE_URL
        ).with_(
            json ={
                "name": user_name,
                "job" : user_job
            }
        )
    )
    then(Jorge).should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(201)),
        See.the(BodyOfTheLastResponse()['name'], IsEqualTo(user_name)),
        See.the(BodyOfTheLastResponse()['job'], IsEqualTo(user_job))
    )