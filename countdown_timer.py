import tkinter as tk
from datetime import timedelta

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        master.title("Countdown Timer")  # Set the title of the window

        # Label to instruct users what to input
        self.label = tk.Label(master, text="Enter time in H:M:S", font=('Helvetica', 14))
        self.label.pack()  # Place the label in the window

        # Entry widget for users to input time
        self.entry = tk.Entry(master, justify='center')
        self.entry.pack()  # Place the entry field in the window

        # Label to display the countdown
        self.time_display = tk.Label(master, text="", font=('Helvetica', 48))
        self.time_display.pack()  # Place the time display label in the window

        # Button to start the countdown
        self.start_button = tk.Button(master, text="Start Countdown", command=self.start_timer)
        self.start_button.pack()  # Place the button in the window

        self.running = False  # This variable will control the countdown updates

    def start_timer(self):
        time_str = self.entry.get()  # Get the user input from the entry widget
        try:
            # Convert the input time from H:M:S to total seconds
            hours, minutes, seconds = map(int, time_str.split(':'))
            self.duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            self.remaining_seconds = self.duration.total_seconds()
            self.update_timer()  # Call the method to start updating the timer
        except ValueError:
            self.time_display.config(text="Invalid time format!")  # Show error if input is invalid

    def update_timer(self):
        if self.running:
            self.master.after_cancel(self.running)  # Cancel the previous after call
        if self.remaining_seconds > 0:
            # Update the label with remaining time
            self.time_display.config(text=str(timedelta(seconds=self.remaining_seconds)))
            self.remaining_seconds -= 1  # Decrement the remaining time
            # Call this method again after 1000 ms (1 second)
            self.running = self.master.after(1000, self.update_timer)
        else:
            self.time_display.config(text="Time's up!")  # Display this message when the countdown finishes

def main():
    root = tk.Tk()  # Create the main window
    timer = CountdownTimer(root)  # Create an instance of the CountdownTimer
    root.mainloop()  # Start the Tkinter event loop

if __name__ == "__main__":
    main()  # Run the main function



