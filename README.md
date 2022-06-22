# PyRNP

[![PyRNP](https://github.com/ntanck/pyrnp/actions/workflows/python-app.yml/badge.svg)](https://github.com/ntanck/pyrnp/actions/workflows/python-app.yml)
[![codecov](https://codecov.io/gh/ntanck/pyrnp/branch/master/graph/badge.svg?token=VnxuTqUaHs)](https://codecov.io/gh/ntanck/pyrnp)
[![PyPi](https://img.shields.io/pypi/v/pyrnp.svg)](https://pypi.org/project/pyrnp/)

Python wrapper for the Eduplay API (maintained by RNP). Made to be as lightweight as possible, only requires Requests!

## Contributors

- [Patricia Nallin](https://github.com/pnallin)
- [Guilherme Francisco de Freitas](https://github.com/ntanck)

## Installation

```shell
git clone https://github.com/cnpem-sei/pyrnp
cd PyRNP
pip3 install .
```

## Utilization

- Create a client

```python
from pyrnp import RNP

client = RNP(
    client_key="KEY",
    client_id="ID",
    username="fulano.detal@org.br",
)
```

- Perform actions

```python
client.upload("video.mp4", "video_unique_id")
client.publish("video.mp4", "video_unique_id", "title", "test upload", thumbnail="thumb.png")
```

Other utilization examples can be found in `Examples`.

## Obtaining credentials

In order to obtain your client key and ID, you must contact [RNP](https://www.rnp.br/) directly.

## Token quirks

Depending on your permissions (if they're not clear, contact RNP support), you might not need tokens in order to publish/upload/change/delete videos. This is why I've made OAuth2 disabled by default. In order to get a token, you can follow the RNP documentation [here](https://eduplay.rnp.br/portal/integration#authentication).

## TODO:

- Add other API functions

## License

This program is licensed under the [GNU Affero license](https://www.gnu.org/licenses/agpl-3.0.txt)
