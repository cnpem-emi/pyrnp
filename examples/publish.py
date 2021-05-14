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
