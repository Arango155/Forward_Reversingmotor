from PIL import Image, ImageTk
import customtkinter
import os
import time

# Global variables
Q1 = False
Q2 = False
message_color = "skyblue"
message_color2 = "yellow"
image_motor = "Images/motor.png"
timer = 0

file_path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(file_path, image_motor)

# Open the image using PIL
motor_pil_image = Image.open(image_path)
motor_img = customtkinter.CTkImage(motor_pil_image, size=(200, 200))


message = ""
customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.geometry("650x550")
root.resizable(False,False)


def update_image():
    global motor_img, label_photo, image_motor
    image_path = os.path.join(file_path, image_motor)
    motor_pil_image = Image.open(image_path)
    motor_img = customtkinter.CTkImage(motor_pil_image, size=(200, 200))
    label_photo.configure(image=motor_img)


def forward():
    global Q1, Q2, message, image_motor

    if not Q1 and not Q2:
        time.sleep(timer)
        message = "Motor started moving forward"
        Q1 = True
        message_label.configure(text_color=message_color)
        message_label.configure(text=message)
        image_motor = "Images/motorforward.png"
        update_image()
    elif not Q1 and Q2:
        message = """Motor already started moving reverse
You have to stop it to change direction
Otherwise, you can create a shortcut."""
        message_label.configure(text_color=message_color2)
        message_label.configure(text=message)
    else:
        message = "Motor already started moving forward"
        message_label.configure(text_color=message_color)
        message_label.configure(text=message)


def stop():
    global Q1, Q2, message, image_motor

    if Q1 or Q2:

        message = "Motor stopped"
        message_label.configure(text_color=message_color)
        message_label.configure(text=message)
        image_motor = "Images/motor.png"
        update_image()
        Q1, Q2 = False, False
    else:
        message = "Motor already stopped"
        message_label.configure(text_color=message_color)
        message_label.configure(text=message)


def reverse():
    global Q1, Q2, message, image_motor
    if not Q1 and not Q2:
        time.sleep(timer)
        message = "Motor started moving in reverse"
        Q2 = True
        message_label.configure(text=message)
        message_label.configure(text_color=message_color)
        image_motor = "Images/motorreverse.png"
        update_image()
    elif Q1 and not Q2:
        message = """Motor already started moving forward
You have to stop it to change direction
Otherwise, you can create a shortcut."""
        message_label.configure(text_color=message_color2)
        message_label.configure(text=message)
    else:
        message = "Motor already started moving in reverse"
        message_label.configure(text_color=message_color)
        message_label.configure(text=message)


def exit_program():
    root.destroy()


def set_time():
    global message, timer
    try:
        timer_input_value = timer_input.get()
        if timer_input_value:
            timer = int(timer_input_value)
            message = f"Timer was set in {timer} seconds"
            message_label.configure(text=message)
            message_label.configure(text_color=message_color)
            timer_input.delete(0, "end")
        else:
            print("Input is empty")
    except ValueError:
        message = "Your input is not an integer"
        message_label.configure(text_color=message_color2)
        message_label.configure(text=message)


frame = customtkinter.CTkFrame(root)
label = customtkinter.CTkLabel(root, text="Control app Demo", font=("Arial", 20))
labele = customtkinter.CTkLabel(root, text="A simulation of how this code idea would work with a real motor",
                                font=("Arial", 14))
label_photo = customtkinter.CTkLabel(frame, text="", image=motor_img)
message_label = customtkinter.CTkLabel(root, text="You can set a timer in seconds for the motor start up (optional)", font=("Georgia", 15))

forwardButton = customtkinter.CTkButton(root, text="Move forward", command=forward, fg_color="#1CB903",
                                        hover_color="#007B0B", corner_radius=200)
stopButton = customtkinter.CTkButton(root, text="Stop", command=stop, fg_color="#B91C03", hover_color="#961501",
                                     corner_radius=200)
reverseButton = customtkinter.CTkButton(root, text="Reverse", command=reverse, corner_radius=200)

timer_input = customtkinter.CTkEntry(root)
send_time = customtkinter.CTkButton(root, text="Set timer", command=set_time, corner_radius=200)

# Print in the GUI area
label.pack(pady=10)
labele.pack(pady=5)
label_photo.pack(pady=10, padx=10)
frame.pack(pady=10)

message_label.pack(pady=10)
timer_input.pack(pady=10)
send_time.pack(side=customtkinter.LEFT,padx=10)

forwardButton.pack(side=customtkinter.LEFT, padx=10)
stopButton.pack(side=customtkinter.LEFT, padx=10)
reverseButton.pack(side=customtkinter.LEFT, padx=10)

root.mainloop()
