from pyrnp import RNP

client = RNP(
    client_key="KEY",
    client_id="ID",
    username="fulano.detal@org.br",
)

client.upload(filename="video.mp4", id="video_unique_id")
client.publish(
    filename="video.mp4", id="video_unique_id", title="title", keywords="test upload", thumbnail="thumb.png"
) 
# You can also pass a file as the thumbnail using "thumb_file" instead of thumbnail.
# If no thumbnail is provided, a file in the same directory named "thumb.png" is used.