#pytest -s  --doctest-modules --junitxml=cov.xml test_zoo.py
import pytest 
import zoo as zoo

@pytest.fixture
def zoo_fixture():
    zoo_object = zoo.zoo()
    c1 = zoo_object.put_cat()
    yield {'zoo':zoo_object}


@pytest.fixture
def zoo_fixture2():
    zoo_object = zoo.zoo()
    return zoo_object


def test_zoo0():
    z = zoo.zoo()
    c1 = z.put_cat()
    assert c1.say() == "にゃー😺"

def test_zoo(zoo_fixture):
    c1 = zoo_fixture['zoo'].put_cat()
    assert c1.say() == 'みゃー😺','意図的にエラーを発生させている'

def test_zoo2(zoo_fixture):
    c1 = zoo_fixture['zoo'].put_cat()
    assert c1.say() == "にゃー😺"

def test_zoo3(zoo_fixture2):
    c1 = zoo_fixture2.put_cat()
    assert c1.say() == "にゃー😺"
