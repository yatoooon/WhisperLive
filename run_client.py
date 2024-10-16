from whisper_live.client import TranscriptionClient

client = TranscriptionClient(
  "154.206.64.157",  # 使用你之前提供的 IP 地址
  9090,
  lang="ja",
  translate=False,
  model="large-v3",
  use_vad=True,
  save_output_recording=True,
  output_recording_filename="./output_recording.wav"
)

# 从麦克风输入进行转录
client()

# 如果你想转录一个音频文件，可以取消下面这行的注释并提供文件路径
# client("/Users/toooonya/Desktop/WhisperLive/assets/jfk.flac")

# 如果你想从 RTSP 流转录，可以取消下面这行的注释并提供 RTSP URL
# client(rtsp_url="rtsp://your_rtsp_url")

# 如果你想从 HLS 流转录，可以取消下面这行的注释并提供 HLS URL
# client(hls_url="http://your_hls_url")
