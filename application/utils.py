import os
from werkzeug.utils import secure_filename
from application import app
from flask_login import current_user  # type: ignore


# save image to static folder
def saveImage(image: ...):
    filename = secure_filename(image.filename)
    # Path should be /application/static/[user_id]/[filename]
    save_path = os.path.join(
        app.config["UPLOAD_FOLDER"],  # type: ignore
        str(current_user.id),
        filename,
    )
    # Create path is it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    # Save the image
    image.save(save_path)  # type: ignore
    # Return the filename that is stored in database.
    # Only done to keep a single default image, this should be done differently
    filename2 = str(current_user.id) + "/" + filename  # [user_id]/[filename]
    return filename2
