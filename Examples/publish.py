from pyrnp import RNP

client = RNP(
    client_key="KEY",
    client_id="ID",
    username="fulano.detal@org.br",
)

client.upload("video.mp4", "video_unique_id")
client.publish("video.mp4", "video_unique_id", "title", "test upload", thumbnail="thumb.png")
