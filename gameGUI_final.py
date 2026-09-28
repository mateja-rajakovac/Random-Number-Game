import tkinter as tk
from gameLogic_final import Game

class GameGUI:
    def __init__(self, window):
        self.mainwindow = window
        self.mainwindow.title("NumberGuessingGame")
        self.mainwindow.geometry("275x220")
        self.mainwindow.resizable(False, False)
        self.mainwindow.config(bg="lightblue")
        self.backend = Game()
        self.entry_var = tk.StringVar()
        self.app_icon = tk.PhotoImage(file="Random_Number.png")
        self.mainwindow.iconphoto(True, self.app_icon)

        #-----------------ENTRY------------------
        self.choice = tk.Entry(self.mainwindow,
                               textvariable=self.entry_var,
                               bg="white"
                               )
        self.choice.grid(row=2, column=0,pady=15, padx=30)

        #-----------------BUTTON-----------------
        self.enter_button = tk.Button(self.mainwindow,
                                      text="ENTER",
                                      command=self.logic_layer,
        )
        self.enter_button.grid(row=2, column=1, padx=7, pady=25)

        #----------------NUMBER-OF-LIFE--------------
        self.life_number = tk.Label(self.mainwindow,
                                    text=f"Remaining lives: {self.backend.get_lifes()}",
                                    bg="lightblue"
                                    )
        
        self.life_number.grid(row=0, column=0, pady=20, padx=30)
        
        #-----------------WIN-LABEL----------------
        self.win_label = tk.Label(self.mainwindow,
                                  text="",
                                  bg="lightblue"
        )

        self.win_label.grid(row=1, column=0, pady=10)

        
        self.game_over_label = tk.Label(self.mainwindow,
                                  text="",
                                  bg="lightblue",
                                  fg="red"
        )

        self.game_over_label.grid(row=1, column=0, pady=10)

        #-----------------INVALID-LABEL--------------------

        self.invalid_label = tk.Label(self.mainwindow,
                                    text="",
                                    bg="lightblue",
                                    fg="red",
                                    )

        self.invalid_label.grid(row=3, column=0, )
        
    def logic_layer(self):
        user_choice = self.choice.get()
        true_false_return = self.backend.true_false(user_choice)

        if true_false_return == "CHOICE_WON":
            self.win_label.configure(text="YOU WIN!",
                                     font=("Arial", 20),
                                     fg="black",
                                     )
            self.enter_button.config(state="disabled")
        
        if true_false_return == "FALSE_INPUT":
            self.update_ui()
            self.update_ui_false()
        
        if true_false_return == "INVALID_INPUT":
            self.update_ui_invalid()

        if self.backend.game_over(user_choice) == True:
            self.win_label.config(text='Game Over :(',
                                    font=("Arial", 20),
                                        fg="red",
                                        )
            self.enter_button.config(state="disabled")
        
        self.entry_var.set("")

        
    def update_ui(self):
        life_count = self.backend.get_lifes()
        self.life_number.config(text=f"Remaining lifes: {life_count}")

    def update_ui_invalid(self):
        self.invalid_label.config(text="INVALID INPUT")
        self.mainwindow.after(3000, lambda: self.invalid_label.config(text=""))

    def update_ui_false(self):
        self.invalid_label.config(text="False number... try again")
        self.mainwindow.after(3000, lambda: self.invalid_label.config(text=""))
        
if __name__ == "__main__":
    root = tk.Tk()
    app = GameGUI(root)
    root.mainloop()