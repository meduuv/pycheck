# pycheck

Small, dependency-free Python validation helpers for values and collections.

## Features

- `is_int` and `is_number` checks
- `is_non_empty` validation
- `all_valid` collection checks
- Tiny API with predictable return values

## Install

```bash
pip install pycheck
```

## Usage

```python
from pycheck import is_int, is_non_empty

assert is_int(42)
assert is_non_empty("hello")
```

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

## Credits

https://guns.lol/meduu
