import subprocess


def deploy():
    # Install necessary packages
    subprocess.run(
        ["pip", "install", "flask", "easyocr", "opencv-python-headless", "matplotlib"]
    )

    # Create a directory for uploaded images
    subprocess.run(["mkdir", "uploads"])

    # Run the Flask app
    subprocess.run(["python", "app.py"])


if __name__ == "__main__":
    deploy()
