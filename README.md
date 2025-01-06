# Service Response

It's a specialized, convenient and extremely lightweight response sample to use for inter-app communication.
Inspired by `Ruby on Rails`.

---
# Install

As package:

```bash
pip install service-reponse
```

As module via (git clone):

```shell
git clone https://github.com/Armen-Jean-Andreasian/ServiceResponse # or SSH
```

---

# Usage and features

```python
from service_response import ServiceResponse

a = ServiceResponse(status=False, error="Some Error")
b = ServiceResponse(status=True, data={1: 2, 3: "content"})

for i in a, b:
    if i:  # checking status
        print(i.data)  # getting data
    else:
        print(i.error)  # getting error msg
```

Params:

- status: `bool` | The status of transaction
- data: `Any` (Optional) | The payload to return
- error: `str` (Optional) | The error content

Features:

- `__bool__` : you can use `if ServiceResponse()` which will return `bool` depending on the `status`

---
# License

Read the [LICENSE](LICENSE) file.

---
_Everything ingenious is simple_