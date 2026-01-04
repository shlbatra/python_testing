- pytest

- pytest tests/

- pytest tests/test_timestamp_utils.py

- pytest tests/test_timestamp_utils.py::test_large_durations

- pytest -k "timestamp and not large"
- pytest -k "timestamp"
test by keywords based on name of tests

- pytest --durations=10 --durations-min=1.0
10 slowest test with minimum duration of 1 sec

- pytest -v
Verbose output

- pytest -s
Show print statements in tests