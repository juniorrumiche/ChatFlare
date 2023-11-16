from app import create_app
from app.extensions import socketio

app = create_app()

if __name__ == "__main__":
    """
    Main script to run the Flask application.

    - Creates the Flask application using the application factory function.
    - Initializes the SocketIO extension with the application.
    - Runs the application if executed as the main script.

    Example Usage:
        ```
        python run.py
        ```

    Note:
        Ensure that the `create_app` function in the 'app' module sets up the necessary components
        such as blueprints, extensions, and configurations.

    """
    socketio.run(app, host='0.0.0.0', port=8080)
