import pytest
import os
from tests.utils import random_str

@pytest.fixture(scope='session')
def log_filepath():
    rand_name = random_str(5)
    rand_name = 'pytest-calculate-anything-{}.log'.format(rand_name)
    rand_filepath = os.path.join('/dev/shm', rand_name)
    yield rand_filepath
    if os.path.exists(rand_filepath):
        os.remove(rand_filepath)