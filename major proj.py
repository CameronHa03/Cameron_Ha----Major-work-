from tkinter import *

root = Tk(className="Python window")

# setting size of window
root.geometry("750x500")

bg = PhotoImage(file="background_major.png")

background = Label(root, image=bg)
background.place(x=0, y=0, relwidth=1, relheight=1)

# this sets the background and size for the entire program


# root.attributes("-alpha", 0.5)


def login(start_button):
    # login function which allows the user to type username and password
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
    # on the click this button triggers a function which checks the users credentials


def signIn(begin_button, requested_username, requested_password, username_text, password_text):
    # takes the entries from the login function and changes them to strings to be checked
    checkUsername = requested_username.get()
    checkPassword = requested_password.get()

    username_text.forget()
    password_text.forget()

    requested_username.delete(0, END)
    requested_password.delete(0, END)

    if checkUser(checkUsername, checkPassword):
        # if the returned value is true the program continues
        begin_button.pack_forget()
        requested_username.pack_forget()
        requested_password.pack_forget()
        blank = True
        gameSelection(blank)
    else:
        return False


def checkUser(checkUsername, checkPassword):
    # Checks the username and password and returns a boolean value
    result = 0
    with open("scratch.txt") as f:
        for line in f:
            user, _, password = line.strip().partition(";")
            loginInfo = line.split(";")
            result = ((user == checkUsername) + (password == checkPassword)) or result
            failLoginText = Label(root, text="Looks like you'll have to try again")
            failLoginText.pack_forget()
            if result == 2:
                # testLabel = Label(root, text="Username: " + checkUsername + " Password: " + checkPassword)
                # testLabel.pack()
                failLoginText.pack_forget()
                return True

            else:
                failLoginText = Label(root, text="Looks like you'll have to try again")
                failLoginText.pack()

                return False


def gameSelection(blank):
    # Allows the user to choose which level they wish to do (currently only one)
    selection_text = Label(root, width=30, borderwidth=5, font=('Helvetica', 18, 'bold'),
                           bg="light sky blue", fg="black",
                           text="What level do you wish to complete?")
    selection_text.pack()
    # this button begins level one
    level_one = Button(root, text="Level One", command=lambda: LevelOne(selection_text, level_one))
    level_one.pack()


def LevelOne(selection_text, level_one):
    # Level one function, firstly shows the required entry fields

    selection_text.pack_forget()
    level_one.pack_forget()

    title_text = Label(root, width=50, borderwidth=5, font=('Helvetica', 18, 'bold'), bg="light sky blue", fg="black",
                       text="LEVEL ONE")
    title_text.pack()

    instruction_text = Label(root, width=50, borderwidth=5, font=('Helvetica', 16, 'bold'), bg="light sky blue",
                             fg="black", text="Enter in the fields")
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

    # Takes these entries and enters them into the next routine which is the  start of the questions
    start_levelOne = Button(root, text="Begin", command=lambda: LevelOne2(quote_entry, author_entry,
                                                                          source_entry, title_text.destroy(),
                                                                          start_levelOne.destroy(),
                                                                          instruction_text.destroy()))
    start_levelOne.pack(padx=5, pady=5)


def LevelOne2(quote_entry, author_entry, source_entry, title_text, start_levelOne, instruction_text):
    # takes the entries and converts them into strings which allows them to be checked

    quote_answer = quote_entry.get()
    author_answer = author_entry.get()
    source_answer = source_entry.get()

    quote_entry.pack_forget()
    author_entry.pack_forget()
    source_entry.pack_forget()

    finished = 0

    correct1 = False
    correct2 = False

    if finished == 0:
        display_text1 = Label(root, width=30, borderwidth=5, font=('Helvetica', 20, 'bold'), bg="light sky blue",
                              fg="black", text=source_answer)
        display_text1.pack()

        question_text = Label(root, width=40, borderwidth=5, font=('Helvetica', 16, 'bold'), bg="light sky blue",
                              fg="black", text="What is the quote associated with this source")
        question_text.pack()

        answer1 = Entry(root, width=30, borderwidth=5, bg="black", fg="lime green")
        answer1.insert(0, "Enter quote")
        answer1.bind("<Button-1>", lambda event: clear_entry4(answer1))
        answer1.pack()

        question_text1 = Label(root, width=40, borderwidth=5, font=('Helvetica', 16, 'bold'), bg="light sky blue",
                               fg="black", text='Who is the author associated with this source')
        question_text1.pack()

        answer2 = Entry(root, width=30, borderwidth=5, bg="black", fg="lime green")
        answer2.insert(0, "Enter author")
        answer2.bind("<Button-1>", lambda event: clear_entry5(answer2))
        answer2.pack()

        # on the click it begins the program that checks the answers
        submission_button = Button(root, text="Submit", command=lambda: submit1(answer1, answer2, quote_answer,
                                                                                author_answer, source_answer,
                                                                                finished,
                                                                                display_text1.destroy(),
                                                                                question_text.destroy(),
                                                                                question_text1.destroy(),
                                                                                submission_button.destroy()))
        submission_button.pack(padx=5, pady=5)

    else:
        finished = 2


def levelOne3(quote_answer, source_answer, author_answer, win_screen, con_button):
    clear_label1(win_screen, con_button)

    # after LevelOne2 has been passed successfully then this sub-routine begins
    display_text1 = Label(root, width=30, borderwidth=5, font=('Helvetica', 20, 'bold'), bg="light sky blue",
                          fg="black", text=author_answer)
    display_text1.pack()

    question_text = Label(root, width=40, borderwidth=5, font=('Helvetica', 16, 'bold'), bg="light sky blue",
                          fg="black", text="What is the quote associated with this author")
    question_text.pack()

    answer1 = Entry(root, width=30, borderwidth=5, bg="black", fg="lime green")
    answer1.insert(0, "Enter quote")
    answer1.bind("<Button-1>", lambda event: clear_entry4(answer1))
    answer1.pack()

    question_text1 = Label(root, width=40, borderwidth=5, font=('Helvetica', 16, 'bold'), bg="light sky blue",
                           fg="black", text='Which source is associated with this author')
    question_text1.pack()

    answer2 = Entry(root, width=30, borderwidth=5, bg="black", fg="lime green")
    answer2.insert(0, "Enter source")
    answer2.bind("<Button-1>", lambda event: clear_entry5(answer2))
    answer2.pack()

    # on the click it begins the checking of the answers
    submission_button2 = Button(root, text="Submit", command=lambda: submit2(answer1, answer2, quote_answer,
                                                                             author_answer, source_answer,
                                                                             display_text1.destroy(),
                                                                             question_text.destroy(),
                                                                             question_text1.destroy(),
                                                                             submission_button2.destroy()))
    submission_button2.pack(padx=5, pady=5)


def levelOne4(quote_answer, author_answer, source_answer, con_button, correct_display):

    display_text = Label(root, width=40, borderwidth=10, font=('Helvetica', 20, 'bold'), bg="light sky blue",
                         fg="black", text="Complete each of the following to finish level one!")
    display_text.pack()


def submit1(answer1, answer2, quote_answer, author_answer, source_answer, finished, display_text1, question_text,
            question_text1, submission_button):
    # checks the answers
    answer_1 = answer1.get()
    answer_2 = answer2.get()

    answer1.destroy()
    answer2.destroy()

    correct1 = False
    correct2 = False

    if quote_answer == answer_1:
        correct1 = True
    if author_answer == answer_2:
        correct2 = True

    if correct1 & correct2 == True:
        # both are correct

        win_screen = Label(root, width=30, borderwidth=5, font=('Helvetica', 14, 'bold'), bg="light sky blue",
                           fg="black", text="WELL DONE")
        win_screen.pack()

        # allows user to continue to next stage
        con_button = Button(root, text="Continue", command=lambda: levelOne3(quote_answer, source_answer, author_answer,
                                                                             win_screen, con_button))
        con_button.pack(padx=5, pady=5)

    else:
        restart_button = Button(root, text="Restart", borderwidth=0, highlightthickness=0, bd=0,
                                font=('Helvetica', 16, 'bold'), height=5, width=10,
                                command=lambda: gameSelection(restart_button.destroy()))
        restart_button.place(relx=0.5, rely=0.5, anchor=CENTER)


def submit2(answer1, answer2, quote_answer, author_answer, source_answer, display_text1, question_text, question_text1,
            submission_button2):

    # Checks the answers submitted
    correct1 = False
    correct2 = False
    answer_1 = answer1.get()
    answer_2 = answer2.get()

    answer1.destroy()
    answer2.destroy()

    if answer_1 == quote_answer:
        correct1 = True
    elif answer_1 != quote_answer:
        correct1 = False
    else:
        correct1 = False

    if answer_2 == source_answer:
        correct2 = True
    elif answer_2 != source_answer:
        correct2 = False
    else:
        correct2 = False

    if correct1 == True & correct2 == True:
        # both are correct
        correct_display = Label(root, width=30, borderwidth=5, font=('Helvetica', 20, 'bold'), bg="light sky blue",
                                fg="black", text="Congratulations you got both correct!")
        correct_display.pack()

        # allows user to continue

        con_button = Button(root, text="Continue", command=lambda: levelOne4(quote_answer, author_answer, source_answer,
                                                                             con_button.destroy(),
                                                                             correct_display.destroy()))
        con_button.pack()
    else:
        # mistakes were made causing user to restart
        restart_button = Button(root, text="Restart", borderwidth=0, highlightthickness=0, bd=0,
                                font=('Helvetica', 16, 'bold'), height=5, width=10,
                                command=lambda: gameSelection(restart_button.destroy()))
        restart_button.place(relx=0.5, rely=0.5, anchor=CENTER)


def empty_textbox(incorrect_display):
    incorrect_display.destroy()


def clear_entry1(author_entry):
    author_entry.delete(0, END)


def clear_entry2(source_entry):
    source_entry.delete(0, END)


def clear_entry3(quote_entry):
    quote_entry.delete(0, END)


def clear_entry4(answer1):
    answer1.delete(0, END)


def clear_entry5(answer2):
    answer2.delete(0, END)


def clear_label1(win_screen, con_button):
    # removes text
    con_button.destroy()
    win_screen.destroy()


# use for later time.sleep(1000)

# this button allows the user to begin playing game
start_button = Button(root, text="Start", borderwidth=0, highlightthickness=0, bd=0,
                      font=('Helvetica', 16, 'bold'), height=5, width=10, command=lambda: login(start_button))
start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
