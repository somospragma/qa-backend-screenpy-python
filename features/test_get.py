import pytest


from screenpy import Actor, given, when, then
from screenpy.pacing import scene, act
from screenpy.actions import See
from screenpy.resolutions import IsEqualTo, ContainsTheEntry

from screenpy_requests.actions import SendGETRequest
from screenpy_requests.questions import BodyOfTheLastResponse, StatusCodeOfTheLastResponse

from utils.urls import *

@act("Test get")
@scene("Obtener todos los usuarios en la pagina 2")
def test_get_all_users(Jorge: Actor) -> None:
    when(Jorge).attempts_to(
        SendGETRequest.to(
            LIST_USERS
        )
    )
    then(Jorge).should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(200)),
        See.the(BodyOfTheLastResponse(), ContainsTheEntry(total=12))
    )

@act("Test get")
@scene("Obtener usuarios por id")
@pytest.mark.parametrize("user_id", [1, 3, 5])
def test_get_user_by_id(user_id: int, Jorge: Actor) -> None:
    when(Jorge).attempts_to(
        SendGETRequest.to(
            f"{BASE_URL}/{user_id}"
        )
    )
    then(Jorge).should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(200)),
        See.the(BodyOfTheLastResponse()["data"], ContainsTheEntry(id=user_id))
    )