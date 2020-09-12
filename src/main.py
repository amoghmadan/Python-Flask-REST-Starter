import sys
from app import Application

app = Application.get_instance(__name__)


if __name__ == '__main__':
    """."""

    try:
        app.run(host=app.config['HOST'], port=app.config['PORT'])

    except Exception as exc:
        tc, te, tb = sys.exc_info()
        print('Class: {} | Exception: {} | Line Number: {} | File: {}'.format(tc, exc, tb.tb_lineno, __name__))
