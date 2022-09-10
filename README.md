# reibaby

A birthday card website for my girlfriend **Rei**.

Hosted on **GCP** with **Nginx** & **uWSGI**

# Some Screenshots

<img src="https://github.com/thejimmylin/reibaby/blob/master/docs/images/screenshot1.png" width="25%">
<img src="https://github.com/thejimmylin/reibaby/blob/master/docs/images/screenshot2.png" width="25%">
<img src="https://github.com/thejimmylin/reibaby/blob/master/docs/images/screenshot3.png" width="25%">

## Installation

OS X & Linux:

```
python3 -m venv /Users/jimmy_lin/envs/reibaby
source /Users/jimmy_lin/envs/reibaby/bin/activate
git clone https://github.com/thejimmylin/reibaby /Users/jimmy_lin/repos/reibaby
pip install -r /Users/jimmy_lin/repos/reibaby/requirements.txt
python /Users/jimmy_lin/repos/reibaby/manage.py runserver
```

Windows:

```
python -m venv C:\Users\jimmy_lin\envs\reibaby
C:\Users\jimmy_lin\envs\reibaby\Scripts\activate
git clone https://github.com/thejimmylin/reibaby C:\Users\jimmy_lin\repos\reibaby
pip install -r C:\Users\jimmy_lin\repos\reibaby\requirements.txt
python C:\Users\jimmy_lin\repos\reibaby\manage.py runserver
```

## Meta

Jimmy Lin <b00502013@gmail.com>

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/thejimmylin/](https://github.com/thejimmylin/)

## Contributing

1. Fork it (<https://github.com/thejimmylin/reibaby/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
