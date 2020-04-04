import scraper  # Our file that will alow us to get back data
import tkinter  # GUI Library
from time import sleep


class trackerApp:
    def __init__(self, master):
        self.casesLabel = tkinter.Label(text="Cases\n", foreground="gray", font=("Verdana Bold", 28), pady=25,
                                        width=500, background="white")
        self.deathsLabel = tkinter.Label(text="Deaths\n", foreground="red", font=("Verdana Bold", 28), padx=32.5,
                                         height=100, background="white")
        self.recoveredLabel = tkinter.Label(text="Recovered\n", foreground="green", font=("Verdana Bold", 28),
                                            padx=32.5, height=100, background="white")

        self.casesLabel.pack()
        self.deathsLabel.pack(side=tkinter.LEFT)
        self.recoveredLabel.pack(side=tkinter.LEFT)

    def update(self):
        self.casesLabel.config(text=f"Cases\n{scraper.requestInformation()[0]}")
        self.deathsLabel.config(text=f"Deaths\n{scraper.requestInformation()[1]}")
        self.recoveredLabel.config(text=f"Recovered\n{scraper.requestInformation()[2]}")


root = tkinter.Tk()
root.title("COVID-19 Tracker")
root.geometry("500x300")
root.resizable(False, False)
root["bg"] = "#FFFFFF"

tracker = trackerApp(root)

while True:  # Custom version of 'root.mainloop', includes update method for the app
    root.update()
    tracker.update()
    sleep(1)  # Give rest
