
from ultralytics import YOLO
import ac_config
from PIL import Image

# CASE01
# 결과 비디오 저장
# model = YOLO("yolov8n.pt")
# results = model.track(source="https...", cof=0.3, iou=9.5, save=True)


# CASE02
# 결과값 generator 로 받기
# -> 웹페이지에 스트리밍하면됨
model = YOLO(ac_config.PRETRAINED_PATH)
source = 'https://youtu.be/LNwODJXcvt4'
results = model(source, stream=True)  # generator of Results objects

r = next(results)
im_array = r.plot()  # plot a BGR numpy array of predictions
im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
print(f'im:{im}')
im.save(f'results_1.jpg')  # save image

r = next(results)
im_array = r.plot()  # plot a BGR numpy array of predictions
im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
print(f'im:{im}')
im.save(f'results_2.jpg')  # save image

r = next(results)
im_array = r.plot()  # plot a BGR numpy array of predictions
im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
print(f'im:{im}')
im.save(f'results_3.jpg')  # save image


# for i, r in enumerate(results):
#     print(i)
#     im_array = r.plot()  # plot a BGR numpy array of predictions
#     im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
#     print(f'im:{im}')
#     # im.show()  # show image
#     im.save(f'results_{i}.jpg')  # save image


