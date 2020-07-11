import pytest
import os


def test_something():
    assert type('something-is-a-string') == str

def test_env_variable():
    assert int(os.environ['CUSTOM_ENV_VAR']) == 8675309
