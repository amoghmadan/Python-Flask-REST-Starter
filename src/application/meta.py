class SingletonMeta(type):
    """."""

    def __init__(cls, *args, **kwargs):
        """."""

        cls.__instance = None
        super(SingletonMeta, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        """."""

        if not cls.__instance:
            cls.__instance = super(SingletonMeta, cls).__call__(*args, **kwargs)

        return cls.__instance
