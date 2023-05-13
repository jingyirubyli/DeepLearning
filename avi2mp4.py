import ffmpy
# 需要转换格式的视频文件，文件真实存在
source_file = r"/Users/lijingyi/Downloads/usliverseq/volunteer02.avi"
# 转换成功后的视频文件，文件夹真实存在，不会自动创建
sink_file = r"/Users/lijingyi/Downloads/usliverseq/volunteer02.mp4"

ff = ffmpy.FFmpeg(
     inputs = {source_file: None},
     outputs = {sink_file: None})
ff.run()



