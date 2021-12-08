import sensor, image, time
from pyb import UART
import json
red_threshold   = (20, 56, 2, 117, 28, 108)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(10)
sensor.set_auto_whitebal(False)
sensor.set_windowing(200,70)
clock = time.clock()
usart = UART(3, 9600)
def find_max(blobs):
    max_size=0#最小色块面积大小
    for blob in blobs:
        if blob.pixels() > max_size:
            max_blob=blob
            max_size = blob.pixels()
            img.draw_rectangle(max_blob.rect())
            img.draw_cross(max_blob.cx(), max_blob.cy())
            x=max_blob.cx()
            p=x
            return p
while(True):
    img = sensor.snapshot()
    blobs = img.find_blobs([red_threshold])

    p=find_max(blobs)
    if p:
        usart.write("f1")#output_str="[%d,%d]" % (max_blob.cx(),max_blob.cy())
        print("x=%d"%int(p))
        usart.write("X%d"%int(p))
    else:
        print('not found!')
        usart.write("f0")
