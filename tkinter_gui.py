import tkinter as tk  # Import the tkinter library and alias it as 'tk' (to stop clashes)

root = tk.Tk()  # Create the main application window

root.title("GUI Title")  # Set the title of the window
root.geometry("300x200")  # Set the size of the window to 300x200 pixels

# Create a Label widget with the text "Enter your name:"
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)  # Add the label to the window with 10 pixels of vertical padding

# Create an Entry (UI) widget for user input
entry = tk.Entry(root)
entry.pack(
    pady=10
)  # Add the entry field to the window with 10 pixels of vertical padding


# Define a function to be called when the button is clicked
def on_button_click():
    user_input = entry.get()  # Retrieve the text entered in the entry field
    greeting_label.config(
        text=f"Hello, {user_input}!"
    )  # Update the greeting label with the user's input


# Create a Button widget that calls 'on_button_click' when clicked
button = tk.Button(root, text="Greet", command=on_button_click)
button.pack(pady=10)  # Add the button to the window with 10 pixels of vertical padding

# Create a Label widget to display the greeting message
greeting_label = tk.Label(root, text="")
greeting_label.pack(
    pady=10
)  # Add the greeting label to the window with 10 pixels of vertical padding

root.mainloop()  # Start the Tkinter event loop to run the application
