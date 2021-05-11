from pyrnp import RNP

client = RNP(
    client_key="KEY",
    client_id="ID",
    username="fulano.detal@org.br",
)

client.get_video("video_unique_id")
