from flask import current_app, jsonify, views


class RootController(views.MethodView):
    """."""

    def get(self, *args, **kwargs):
        """."""

        data: dict = {"hello": "World!"}

        current_app.logger.info(f"API Response: {data}")

        return jsonify(data), 200
