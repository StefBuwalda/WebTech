from werkzeug.utils import secure_filename
import os
from application import app
from flask_login import current_user  # type: ignore


def saveImage(image: ...):
    filename = secure_filename(image.filename)
    save_path = os.path.join(
        app.config["UPLOAD_FOLDER"],  # type: ignore
        str(current_user.id),
        filename,
    )
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    image.save(save_path)  # type: ignore
    filename2 = str(current_user.id) + "/" + filename
    return filename2
