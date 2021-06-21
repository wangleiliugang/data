import json


# 读取json文件
def read_tone_freqs(filename):
    with open(filename, 'r') as f:
        tone_freqs = json.loads(f.read())
    print(tone_freqs)
    return tone_freqs
