import cv2
import numpy as np
import supervision as sv
from roboflow import Roboflow

rf = Roboflow(api_key="gCnudHi6QN4Vui8aq1ne")
project = rf.workspace().project("anpr-vv2b2")
model = project.version(384).model

image_files = ["demo.jpg", "demo2.jpg", "demo3.jpg", "demo4.jpg"]

for image_file in image_files:
    result = model.predict(image_file).json()

    print(f"Processing {image_file}...")
    if not result["predictions"]:
        print("No detections found.")
        continue

    detections_xyxy = []
    class_ids = []
    labels = []
    confidences = []

    for prediction in result["predictions"]:
        x = prediction["x"]
        y = prediction["y"]
        width = prediction["width"]
        height = prediction["height"]
        class_name = prediction["class"]
        confidence = prediction["confidence"]

        x1 = x - width / 2
        y1 = y - height / 2
        x2 = x + width / 2
        y2 = y + height / 2

        detections_xyxy.append([x1, y1, x2, y2])
        class_ids.append(0)
        labels.append(class_name)
        confidences.append(confidence)

    xyxy = np.array(detections_xyxy, dtype=np.float32)
    class_ids = np.array(class_ids)
    confidences = np.array(confidences)

    detections = sv.Detections(xyxy=xyxy, class_id=class_ids, confidence=confidences)

    image = cv2.imread(image_file)
    label_annotator = sv.LabelAnnotator()
    bounding_box_annotator = sv.BoxAnnotator()

    annotated_image = bounding_box_annotator.annotate(
        scene=image, detections=detections
    )
    annotated_image = label_annotator.annotate(
        scene=annotated_image, detections=detections, labels=labels
    )

    sv.plot_image(image=annotated_image, size=(16, 16))
