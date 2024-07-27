import cv2
import tkinter as tk
import customtkinter as ck
from PIL import Image, ImageTk
import mediapipe as mp
import numpy as np

def main():
    # do everything here
    # setup mp stuff
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    # setup cv2 stuff
    capture = video_setup()
    tk_window = tk_setup(capture)
    open_camera(capture, tk_window)

    tk_window.mainloop()

    # while capture.isOpened():
    #     ret, frame = capture.read()
    #     title = "test"
    #     cv2.imshow(title,frame)
    #     if cv2.waitKey(10) & 0xFF == ord("q"):
    #         capture.release()
        # if cv2.waitKey(10) & 0xFF == ord("1"):
        #         video_output(capture, "Deadlift")
        # if cv2.waitKey(10) & 0xFF == ord("2"):
        #         video_output(capture, "Squat")
        # if cv2.waitKey(10) & 0xFF == ord("3"):
        #         video_output(capture, "Bench")
        # if cv2.waitKey(10) & 0xFF == ord("q"):
        #         break
        #test which lift to calculate

    # setup video to save
    # calculate angles
    # angle/counter logic
    # save video frame 
    # quit video
    capture.release()
    cv2.destroyAllWindows()
    pass

def tk_setup(capture):
    window = tk.Tk()
    window.geometry("1280x720")
    window.title("Window")
    ck.set_appearance_mode("dark")

    button = ck.CTkButton(window, text="open camera", command=open_camera(capture, window), height=40, width=120, font=("Arial",20), text_color="black", fg_color="blue")
    button.place(x=10, y=600)
    return window

def open_camera(capture, window):
    _, frame = capture.read()
    title = "test"
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    captured_image = Image.fromarray(image)
    photo_image = ImageTk.PhotoImage(image=captured_image)

    label_widget = tk.Label(window)
    label_widget.photo_image = photo_image
    label_widget.configure(image=photo_image)
    label_widget.after(10, open_camera)
    # cv2.imshow(title,frame)
    # if cv2.waitKey(10) & 0xFF == ord("q"):
    #     capture.release()

def video_setup(capture_device = cv2.VideoCapture(0),
                frame_width = (3,1280),
                frame_height = (4, 720)
                ):
    capture_device.set(frame_width[0], frame_width[1])
    capture_device.set(frame_height[0], frame_height[1])
    return capture_device

def video_output(capture, title="Video Feed"):
        ret, frame = capture.read()
        cv2.imshow(title,frame)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            capture.release()

def video_writer():
    pass

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return int(angle)

if __name__ == "__main__":
     main()