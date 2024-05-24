import pytest
from typing import Generator
from screenpy import Actor
from screenpy.pacing import the_narrator

from screenpy_requests.abilities import MakeAPIRequests

from screenpy_adapter_allure import AllureAdapter


@pytest.fixture(scope="function", name="Jorge")
def fixture_actions() -> Generator:
    "inicializamos al actor y le entregamos la habilidad de enviar solicitudes a APIs"
    actor = Actor.named("Jorge").who_can(MakeAPIRequests())
    yield actor
    actor.exit()


the_narrator.adapters.append(AllureAdapter())