from ultralytics import YOLO

# Load a model
model = YOLO("/content/drive/MyDrive/PrinceResnetYoloCode/yolov8l.yaml")  # build a new model from scratch ye model ki file ??? han yaha se model buld hoga dfir train ager backbone fegafult rehne dega to train start ho jata hau 
results = model.train(data='/content/drive/MyDrive/PrinceResnetYoloCode/data.yaml', epochs=300, imgsz=640, batch=4)

