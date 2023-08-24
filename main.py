from tkinter import *
from words import hangman_words
import random
from stages import stages
from tkinter import messagebox

random_category = random.choice(list(hangman_words.items()))
random_category_name = random_category[0]
lives = 7
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

used_letters = []


def random_word():
    random_value = random.choice(random_category[1])
    return random_value


current_random_word = random.choice(random_category[1])
current_random_word_list = list(current_random_word)
current_secure_word = ["_" for _ in current_random_word]


def return_value():
    value = letter_entry.get().lower()
    if value in used_letters:
        messagebox.showinfo("Info", "You've already used this letter!")
        letter_entry.delete(0, END)
    elif len(value) > 1 or len(value) < 1:
        messagebox.showinfo("Info", "Insert only one sign!")
        letter_entry.delete(0, END)
    elif value not in alphabet:
        messagebox.showinfo("Info", "Invalid sign. A sign has to be a letter from the English alphabet.")
        letter_entry.delete(0, END)
    elif value not in current_random_word_list and value in alphabet:
        messagebox.showinfo("Info", "A sign does not match!")
        used_letters.append(value)
        reduce_lives()
        letter_entry.delete(0, END)
    else:
        for index, letter in enumerate(current_random_word_list):
            if letter == value:
                current_secure_word[index] = value
        updated_word()
        used_letters.append(value)
        letter_entry.delete(0, END)
    if lives > 0 and "_" not in current_secure_word:
        if messagebox.askyesno("Play Again?", "You won! Congratulations! Do you want to play again?"):
            restart_game()
        else:
            window.quit()
    elif lives == 0:
        if messagebox.askyesno("Play Again?", "You lost! :( Do you want to play again?"):
            restart_game()
        else:
            window.quit()


def updated_word():
    updated_word_text = " ".join(current_secure_word)
    canvas.itemconfig(word, text=updated_word_text)


def reduce_lives():
    global lives
    lives -= 1
    lives_label.config(text=f"Lives: {lives}")
    canvas.itemconfig(hangman, text=stages[lives])


def restart_game():
    global lives, used_letters, current_random_word, current_random_word_list, current_secure_word, random_category_name
    random_cat = random.choice(list(hangman_words.items()))
    random_category_name = random_cat[0]
    lives = 7
    used_letters = []
    current_random_word = random.choice(random_cat[1])
    current_random_word_list = list(current_random_word)
    current_secure_word = ["_" for _ in current_random_word]
    updated_word()
    lives_label.config(text=f"Lives: {lives}")
    label_category_name.config(text=f"Category: {random_category_name}")
    canvas.itemconfig(hangman, text="")


window = Tk()
window.title("Hangman")

lives_label = Label()
lives_label.config(text=f"Lives: {lives} ", font=("Comic Sans MS", 30, "normal"))
lives_label.grid(row=0, column=0)

label_category_name = Label()
label_category_name.config(text=f"Category: {random_category_name}", font=("Comic Sans MS", 30, "normal"))
label_category_name.grid(column=1, row=0)

canvas = Canvas(width=1920, height=1080)
canvas.grid(column=0, row=1, columnspan=2)

hangman = canvas.create_text(370, 260, text="", font=("Comic Sans MS", 30, "normal"))
word = canvas.create_text(1410, 260, text=" ".join(current_secure_word), font=("Comic Sans MS", 100, "normal"))
letter_entry = Entry(width=30, font=("Comic Sans MS", 30, "normal"))
letter_entry.grid(column=0, row=1)

button_type_letter = Button(text="Click to guess a letter", font=("Comic Sans MS", 30, "normal"), cursor="hand2",
                            command=return_value)
button_type_letter.grid(column=1, row=1)

window.mainloop()
