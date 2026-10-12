import cv2
import mediapipe as mp
import math

mp_pose = mp.solutions.pose

count = 0
stage = "UP"


def angle(a, b, c):
    radians = math.atan2(c[1] - b[1], c[0] - b[0]) - \
              math.atan2(a[1] - b[1], a[0] - b[0])

    angle = abs(math.degrees(radians))

    if angle > 180:
        angle = 360 - angle

    return angle


cap = cv2.VideoCapture(0)

with mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as pose:

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.flip(frame, 1)

        h, w, _ = frame.shape

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = pose.process(rgb)

        if results.pose_landmarks:

            lm = results.pose_landmarks.landmark

            left_elbow = angle(
                (lm[11].x, lm[11].y),
                (lm[13].x, lm[13].y),
                (lm[15].x, lm[15].y)
            )

            right_elbow = angle(
                (lm[12].x, lm[12].y),
                (lm[14].x, lm[14].y),
                (lm[16].x, lm[16].y)
            )

            elbow = (left_elbow + right_elbow) / 2

            if elbow > 160:
                if stage == "DOWN":
                    count += 1

                stage = "UP"

            elif elbow < 90:
                stage = "DOWN"

            for p in lm:
                x = int(p.x * w)
                y = int(p.y * h)

                if 0 <= x < w and 0 <= y < h:
                    cv2.circle(
                        frame,
                        (x, y),
                        4,
                        (0, 255, 0),
                        -1
                    )

        cv2.putText(
            frame,
            f"Push-ups: {count}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("Push-Up Counter", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()