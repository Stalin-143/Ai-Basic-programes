import cv2
tracker = cv2.TrackerCSRT_create()
video = cv2.VideoCapture(0)
if not video.isOpened():
    exit()
ret, frame = video.read()
if not ret:
    exit()
bbox = cv2.selectROI("Tracking", frame, False)
tracker.init(frame, bbox)
while True:
    ret, frame = video.read()
    if not ret:
        break
    success, bbox = tracker.update(frame)
    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Tracking", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Lost Track", (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow("Object Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
