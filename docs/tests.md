# Tests

## Reset database

```bash
python manage.py flush
python manage.py loaddata blog/fixtures/*
```

## Run all tests

```bash
python -m pytest tests/
```

## Run subset of tests

```bash
python -m pytest tests/<test_dir>/tests.py
python -m pytest tests/<test_dir>/tests.py -k 'test'
```

## Use fixtures to provide parameters

```python
@pytest.mark.parametrize("post_title,post_body", [("test", "# Here is a body title")])
```

## Coverage

Open `index.html` in browser from `tests/reports` directory.
