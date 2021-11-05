from flask_app import app
from flask_app.controllers import controller_user


# MAKE SURE THIS IS AT THE BOTTOM OF YOUR SERVER.PY FILE #
if __name__ == "__main__":
    app.run(debug=True)