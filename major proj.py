from tkinter import *

root = Tk(className="Python window")

# setting size of window
root.geometry("750x500")

bg = PhotoImage(file="background_major.png")

background = Label(root, image=bg)
background.place(x=0, y=0, relwidth=1, relheight=1)


# root.attributes("-alpha", 0.5)


def login(start_button):
    start_button.destroy()

    username_text = Label(root, width=15, borderwidth=5, font=('Helvetica', 16, 'bold'),
                          bg="light sky blue", fg="black", text="Enter username")
    username_text.pack()

    requested_username = Entry(root, width=15, borderwidth=5, bg="black", fg="lime green")
    requested_username.pack()
    password_text = Label(root, width=15, borderwidth=5, font=('Helvetica', 16, 'bold'),
                          bg="light sky blue", fg="black", text="Enter password")
    password_text.pack()

    requested_password = Entry(root, width=15, borderwidth=5, bg="black", fg="lime green")
    requested_password.pack()

    begin_button = Button(root, text="Sign in",
                          command=lambda: signIn(begin_button, requested_username, requested_password, username_text,
                                                 password_text))
    begin_button.pack()


def signIn(begin_button, requested_username, requested_password, username_text, password_text):
    checkUsername = requested_username.get()
    checkPassword = requested_password.get()

    username_text.forget()
    password_text.forget()

    requested_username.delete(0, END)
    requested_password.delete(0, END)
    if checkUser(checkUsername, checkPassword):
        begin_button.pack_forget()
        requested_username.pack_forget()
        requested_password.pack_forget()
        gameSelection()
    else:
        return False


def checkUser(checkUsername, checkPassword):
    for line in open("scratch.txt"):
        loginInfo = line.split()
        failLoginText = Label(root, text="Looks like you'll have to try again")
        failLoginText.pack_forget()
        if checkUsername == loginInfo[0] and checkPassword == loginInfo[1]:
            # testLabel = Label(root, text="Username: " + checkUsername + " Password: " + checkPassword)
            # testLabel.pack()
            failLoginText.pack_forget()
            return True

        else:
            failLoginText = Label(root, text="Looks like you'll have to try again")
            failLoginText.pack()

            return False


def gameSelection():
    selection_text = Label(root, width=30, borderwidth=5, bg="black", fg="lime green",
                           text="What level do you wish to complete?")
    selection_text.pack()
    level_one = Button(root, text="Level One", command=lambda: LevelOne(selection_text, level_one))
    level_one.pack()


def LevelOne(selection_text, level_one):
    # Level one function, firstly shows the required entry fields

    selection_text.pack_forget()
    level_one.pack_forget()

    title_text = Label(root, width=30, borderwidth=5, font=('Helvetica', 18, 'bold'), bg="black", fg="red",
                       text="LEVEL ONE")
    title_text.pack()

    instruction_text = Label(root, width=30, borderwidth=5, font=('Helvetica', 16, 'bold'), bg="black", fg="red",
                             text="Enter in the fields")
    instruction_text.pack()

    quote_entry = Entry(root, width=15, borderwidth=5, bg="black", fg="lime green")
    quote_entry.insert(0, "Enter quote")
    quote_entry.bind("<Button-1>", lambda event: clear_entry3(quote_entry))
    quote_entry.pack()

    author_entry = Entry(root, width=15, borderwidth=5, bg="black", fg="lime green")
    author_entry.insert(0, "Author name")
    author_entry.bind("<Button-1>", lambda event: clear_entry1(author_entry))
    author_entry.pack()

    source_entry = Entry(root, width=15, borderwidth=5, bg="black", fg="lime green")
    source_entry.insert(0, "Source")
    source_entry.bind("<Button-1>", lambda event: clear_entry2(source_entry))
    source_entry.pack()

    start_levelOne = Button(root, text="Begin", command=lambda: LevelOne2(source_entry, quote_entry,
                                                                          title_text, author_entry,
                                                                          start_levelOne.destroy()))
    start_levelOne.pack(padx=5, pady=5)


def LevelOne2(quote_entry, author_entry, source_entry, start_levelOne, title_text):
    # start_levelOne.destroy()
    # title_text.forget()

    print(source_entry)
    print(author_entry)
    print(quote_entry)

    quote_answer = quote_entry.get()
    author_answer = author_entry.get()
    # source_answer = source_entry.get()

    # quote_entry.pack_forget()
    # author_entry.pack_forget()
    # source_entry.pack_forget()

    test_text = Label(root, width=30, borderwidth=5, font=('Helvetica', 18, 'bold'), bg="black", fg="red",
                      text=quote_answer)
    test_text.pack()

    test_text1 = Label(root, width=30, borderwidth=5, font=('Helvetica', 18, 'bold'), bg="black", fg="red",
                       text=author_answer)
    test_text1.pack()

    test_text2 = Label(root, width=30, borderwidth=5, font=('Helvetica', 18, 'bold'), bg="black", fg="red",
                       text=source_entry)
    test_text2.pack()
    attempt = 1

    if attempt == 1:
        return True


def clear_entry1(author_entry):
    author_entry.delete(0, END)


def clear_entry2(source_entry):
    source_entry.delete(0, END)


def clear_entry3(quote_entry):
    quote_entry.delete(0, END)


# time.sleep(1000)

# test for miss

start_button = Button(root, text="Start", borderwidth=0, highlightthickness=0, bd=0,
                      font=('Helvetica', 16, 'bold'), height=5, width=10, command=lambda: login(start_button))
start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
