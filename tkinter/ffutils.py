import os


def ffmpeg_info():
    """
    ffmpeg ：音视频处理开源框架
    ffmpeg 的bin目录， 目录下包含 ( ffmpeg.exe, ffplay.exe, ffprobe.exe )
    path_ffmpeg  = r"D:\迅雷下载\ffmpeg-2021-09-22-git-447cf53774-essentials_build\ffmpeg-2021-09-22-git-447cf53774-essentials_build\bin"
    sys.path.append(path_ffmpeg) # 加到环境变量 path

    注意:ffmpeg 不能覆盖源文件
    """


def play(scr):
    """
    :param scr: 文件名
    :return:  ffmpeg 命令行
    播放音频、视频
    """
    cmd = "ffplay {}".format(scr)
    print(cmd)
    os.system(cmd)


def format(scr, out):
    """
    格式转换
    提取音频 mp4-mp3 ： ffmpeg -i in.mp4  out.mp3
    :param scr:  源文件名
    :param out: 输出文件名
    :return:
    """
    cmd = "ffmpeg -i {} {}".format(scr, out)
    print(cmd)
    os.system(cmd)


def clip(scr, out, start, end):
    """
    视频，音频切片
    example : ffmpeg  1.mp3  2.mp3  20  150
    example : ffmpeg  1.mp3  2.mp3  00:10  00:50
    :param scr: 源文件路径
    :param out: 输出的路径
    :param start: 开始时间
    :param end:   结束时间
    :return:
    """
    cmd = "ffmpeg -i {} -ss {} -to {} -c copy {}".format(scr, start, end, out)
    print(cmd)
    os.system(cmd)


def video_gif(scr, out, start, end):
    """
    视频转 gif图
    :param scr: 源文件
    :param out: 输出路径
    :param start: 截取开始时间
    :param end:   截取结束时间
    :return:
    """
    cmd = "ffmpeg -i {} -ss {} -to {}  {}".format(scr, start, end, out)
    print(cmd)
    os.system(cmd)


def video_add_image(scr, img, out, overlay="0:0"):
    """
    加水印
    :param scr: 源图片
    :param out: 输出路径
    :param img: 水印
    :param overlay: 默认锚点左上
    :return:
    """
    overlay = "overlay={}".format(overlay)
    cmd = "ffmpeg -i {} -i {} -filter_complex {} {}".format(scr, img, overlay, out)
    print(cmd)
    os.system(cmd)


def video_add_audio(scr, music, out, start="0"):
    """
    加背景音乐
    :param scr: 视频源
    :param music: 音乐
    :param out:  输出路径
    :return:
    """

    # 视频有声源
    cmd = "ffmpeg -i {} -i {}  -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 {}".format(scr, music, out)
    cmd = "ffmpeg -i {} -i {}  -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 {}".format(scr, music, out)

    # 视频没有声源
    # cmd = "ffmpeg -i {} -i {} -c:v copy -c:a aac -strict experimental {}".format(scr, music, out)
    print(cmd)
    os.system(cmd)


def video_resize(scr, out, size):
    """
    图像或视频改变尺寸
    :param scr: 视频源
    :param out: 输出路径
    :param size: 分辨率
    :return:
    """

    cmd = "ffmpeg -i {} -s {} {}".format(scr, size, out)
    print(cmd)
    os.system(cmd)


def video_capture_byFrame(scr, out, times=1, start="0"):
    """
    按帧间隔截图
    如果截多张图在后缀 （如 .jpg）前加 %d
    -vf fps=0.1 10s截图一张
    ffmpeg  -i input.mp4 -vf fps=0.1  output%d.jpg
    -vf fps=10 1s截图十张
    ffmpeg  -i input.mp4 -vf fps=10   output%d.bmp

    :param scr: 源文件
    :param out: 输
    :param times: 1秒截图几帧
    :param start: 起始时间
    :return:
    """
    cmd = "ffmpeg  -i {} -ss {} -vf fps={}  {}".format(scr, start, times, out)
    print(cmd)
    os.system(cmd)


def video_capture_byTime(scr, out, start="0", frames=1):
    """
    定时截图
    如果截多张图在后缀 （如 .jpg）前加 %d, 即 out1.jpg out2，jpg ...
    ffmpeg  -i input.mp4  -ss 4.500 -vframes 10 out%d.jpg
    :param scr: 源文件
    :param out: 输出路径
    :param start: 截图开始时间
    :param frames: 截图帧数
    :return:
    """
    cmd = "ffmpeg  -i {}  -ss {} -vframes {} {}".format(scr, start, frames, out)
    print(cmd)
    os.system(cmd)


