
from ultralytics import YOLO


# CASE01
# 결과 비디오 저장
# model = YOLO("yolov8n.pt")
# results = model.track(source="https...", cof=0.3, iou=9.5, save=True)


# CASE02
# 결과값 generator 로 받기
# -> 웹페이지에 스트리밍하면됨
model = YOLO("yolov8n.pt")
source = 'https://youtu.be/LNwODJXcvt4'
results = model.track(source, stream=True)

for num in results:
    print(num)



# CASE03
# 결과값 generator 로 받고
# object ID 값을 이용하고 싶다면?
# -> plotting example 에 id 값 이용하는 방법 있음
# https://docs.ultralytics.com/modes/track/#plotting-tracks-over-time


