import tkinter as tk
from gameLogic_final import Game

class GameGUI:
    def __init__(self, window):
        self.mainwindow = window
        self.mainwindow.title("NumberGuessingGame")
        self.mainwindow.geometry("275x200")
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
        self.choice.grid(row=2, column=0,pady=20, padx=30)

        #-----------------BUTTON-----------------
        self.enter_button = tk.Button(self.mainwindow,
                                      text="ENTER",
                                      command=self.logic_layer,
        )
        self.enter_button.grid(row=2, column=1, padx=7, pady=30)

        #----------------NUMBER-OF-LIFE--------------
        self.life_number = tk.Label(self.mainwindow,
                                    text=f"Remaining lifes: {self.backend.get_lifes()}",
                                    bg="lightblue"
                                    )
        self.life_number.grid(row=0, column=0, pady=20, padx=30)
        
        #-----------------WIN-LABEL----------------
        self.win_label = tk.Label(self.mainwindow,
                                  text="",
                                  bg="lightblue"
        )

        self.win_label.grid(row=1, column=0, pady=10)

        
        self.false_label = tk.Label(self.mainwindow,
                                  text="",
                                  bg="lightblue",
                                  fg="red"
        )

        self.false_label.grid(row=1, column=0, pady=10)
        
    def logic_layer(self):
        user_choice = self.choice.get()
        true_false_return = self.backend.true_false(user_choice)

        if true_false_return == True:
            self.win_label.configure(text="YOU WIN!",
                                     font=("Arial", 20),
                                     fg="black",
                                     )
            self.enter_button.config(state="disabled")   
        elif true_false_return == False:
            self.update_ui()

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


        
if __name__ == "__main__":
    root = tk.Tk()
    app = GameGUI(root)
    root.mainloop()