from rev_ai.streamingclient import RevAiStreamingClient
from rev_ai.models import MediaConfig

#on_error(error)
#on_close(code, reason)
#on_connected(id)

config = MediaConfig()
streaming_client = RevAiStreamingClient("02Ya*",
                                        config,)
response_generator = streaming_client.start(AUDIO_GENERATOR, custom_vocabulary_id="CUSTOM VOCAB ID")
streaming_client.end()