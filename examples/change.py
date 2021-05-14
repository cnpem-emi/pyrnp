from pyrnp import RNP

client = RNP(
    client_key="KEY",
    client_id="ID",
    username="fulano.detal@org.br",
)

client.upload(filename="video.mp4", id="video_unique_id")
client.change_video(filename="video.mp4", id="video_unique_id")
