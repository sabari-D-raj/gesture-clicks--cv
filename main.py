import cv2
import mediapipe as mp
import pyautogui
cap=cv2.VideoCapture(0)
screen_w,screen_h=pyautogui.size()
clicked=False
mp_hands=mp.solutions.hands
mp_draw=mp.solutions.drawing_utils
hands=mp_hands.Hands(static_image_mode=False,
                     max_num_hands=1,
                     min_detection_confidence=0.7,
                     min_tracking_confidence=0.7
                     )
while True:
    succes,frame=cap.read()
    h,w,_=frame.shape
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(rgb)
    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame,hand_landmark,mp_hands.HAND_CONNECTIONS)

        x=int(hand_landmark.landmark[8].x*w)
        y=int(hand_landmark.landmark[8].y*h)
        screem_x=screen_w/w*x
        screen_y=screen_h/h*y
        pyautogui.moveTo(screem_x,screen_y)
        thumb_x=(hand_landmark.landmark[4].x)
        thumb_y=(hand_landmark.landmark[4].y)
        index_x=(hand_landmark.landmark[8].x)
        index_y=(hand_landmark.landmark[8].y)
        distance=((thumb_x-index_x)**2+(thumb_y-index_y)**2)**0.5
        print(distance)
        if distance <0.08:
            if not clicked:
                pyautogui.click()
                print("clicked")
                clicked=True
        else:
            clicked=False
    if not succes:
        print("failed not working")
        break
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    cv2.imshow("click",frame)
cap.release()
cv2.destroyAllWindows()