from pyrnp import RNP

client = RNP(
    client_key="KEY",
    client_id="ID",
    username="fulano.detal@org.br",
)

client.upload("video.mp4", "video_unique_id")
client.change_video("video.mp4", "video_unique_id")
