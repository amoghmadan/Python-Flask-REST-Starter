import sys
from application import Application

singleton_application = Application(__name__)
app = singleton_application()


if __name__ == "__main__":
    """."""

    try:
        app.run(host=app.config["HOST"], port=app.config["PORT"])
    except Exception as exc:
        tc, te, tb = sys.exc_info()
        print(f"Class: {tc.__name__} | Exception: {exc} | Line Number: {tb.tb_lineno} | File: {__name__}")
