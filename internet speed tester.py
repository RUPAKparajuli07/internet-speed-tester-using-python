import speedtest
import tkinter as tk
import random

# Define a list of colors
colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF",
          "#FFA500", "#800080", "#008000", "#FFC0CB", "#800000", "#008080"]

def check_internet_speed():
    # Create a SpeedtestClient instance
    st = speedtest.Speedtest()

    # Perform the speed test
    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6  # Convert to Mbps

    # Update the label text with the speed results
    download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
    upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")

def update_speed():
    # Call the check_internet_speed function to update the speed values
    check_internet_speed()
    # Schedule the next update after 5 seconds (5000 milliseconds)
    window.after(5000, update_speed)

def change_background_color():
    # Choose a random color from the list
    color = random.choice(colors)
    # Update the background color of the window
    window.configure(bg=color)
    # Schedule the next color change after 3 seconds (3000 milliseconds)
    window.after(3000, change_background_color)

# Create the main window
window = tk.Tk()
window.title("Internet Speed Checker")

# Create labels to display speed results
download_label = tk.Label(window, text="Download Speed: -- Mbps")
download_label.pack()
upload_label = tk.Label(window, text="Upload Speed: -- Mbps")
upload_label.pack()

# Call the update_speed function to start updating the speed values
update_speed()

# Call the change_background_color function to start changing the background color
change_background_color()

# Run the GUI main loop
window.mainloop()
