import imp


import os, datetime, random

def upload_file_name(instace, filename):
    _, ext = os.path.splitext(filename)

    return "{}/{}/{:%Y-%m-%d-%H-%M-%S}-{}-{}".format(
        instace.folder,
        datetime.datetime.now().strftime("%Y%m"),
        datetime.datetime.now(),
        random.randint(1000, 9999), ext
    )