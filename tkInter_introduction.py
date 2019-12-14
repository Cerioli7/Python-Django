import tkinter as tk

window = tk.Tk()
window.geometry("600x600")
window.title("Hello TkInter!")
#window.resizable(False, False)
#window.config(background="red")

def first_print():
    text = "Hello World!"
    text_output = tk.Label(window, text=text, fg="blue",font=("Arial", 15))
    text_output.grid(row=0, column=1, sticky="W")

def second_function():
    text = "Nuovo messaggio! Nuova funzione!"
    text_output = tk.Label(window, text=text, fg="green",font=("Arial", 15))
    text_output.grid(row=1, column=1, padx=20, sticky="W")

first__button = tk.Button(text="Saluta!!!", command=first_print)
first__button.grid(row=0, column=0, sticky="W")

second_button = tk.Button(text="Seconda Funzione", command=second_function)
second_button.grid(row=1, column=0, pady=20)


if __name__ == "__main__":
    window.mainloop()
