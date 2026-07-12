import random
import time
import customtkinter as ctk
import typing_speed

BG_PINK = "#F9BBD0"        # main background
SOFT_PINK = "#DBA1BA"      # buttons / borders
DARK_PINK = "#D6A6B5"   # main text
WHITE = "#FFFFFF"          # entry boxes / button text
HOVER_PINK = "#C78FA2"     # button hover

ctk.set_appearance_mode("light")      # "light", "dark", or "system"

window = ctk.CTk()
window.title("Typing Speed Test")
window.geometry("800x700")
window.configure(fg_color=BG_PINK)

def show_rules():
    clear_screen()

    title = ctk.CTkLabel(
        window,
        text= "Welcome to the Typing Speed Test!",
        font=("Times", 30, "bold"),
        text_color=WHITE,
        fg_color="transparent"
    )
    title.pack(pady=20)
    
    rules= ctk.CTkLabel(
        window,
        text=typing_speed.rules_text,
        font=("Times", 20),
        text_color=WHITE,
        fg_color="transparent",
        wraplength=420
    )
    rules.pack(pady=10)

    continue_button = ctk.CTkButton(
        window,
        text="I understand the rules, let's continue!",
        command=show_name_screen,
        fg_color=SOFT_PINK,
        hover_color=HOVER_PINK,
        text_color=WHITE,
        font=("Times", 20),
        corner_radius=15
    )
    continue_button.pack(pady=20)

def show_name_screen():
    clear_screen()

    global name_entry

    title_label = ctk.CTkLabel(
        window, 
        text="Typing Speed Test", 
        font=("Times", 30, "bold"), 
        fg_color=BG_PINK, 
        text_color="white"
        )
    title_label.pack(pady=20)

    name_label = ctk.CTkLabel(
        window, 
        text="Hey there! What's your name?", 
        font=("Times", 30), 
        fg_color=BG_PINK, 
        text_color="white"
    )
    name_label.pack()
    
    name_entry = ctk.CTkEntry(
        window,
        width = 300,
        height = 40,
        fg_color= SOFT_PINK,
        border_color=HOVER_PINK,
        border_width=2,
        corner_radius=12, 
        text_color=WHITE,
        font=("Times", 20)
    )
    name_entry.pack(pady=10)

    name_entry.bind("<Return>", save_name)

def save_name(event= None):

    global player_name

    player_name = name_entry.get().strip()

    if player_name == "":
        return

    show_difficulty_screen()

def show_difficulty_screen():
    clear_screen()

    title_label = ctk.CTkLabel(
        window,
        text=f"Welcome, {player_name}!\nChoose your difficulty level:", 
        text_color="white",
        font=("Times", 30, "bold")
        )
    title_label.pack(pady=20)


    easy_button = ctk.CTkButton(window, text="Easy", command=lambda: start_typing_screen("E"), fg_color=SOFT_PINK, hover_color=HOVER_PINK, text_color=WHITE, font=("Times", 20, "bold"), corner_radius=15)
    easy_button.pack(pady=5)

    medium_button = ctk.CTkButton(window, text="Medium", command=lambda: start_typing_screen("M"), fg_color=SOFT_PINK, hover_color=HOVER_PINK, text_color=WHITE, font=("Times", 20, "bold"), corner_radius=15)
    medium_button.pack(pady=5)

    hard_button = ctk.CTkButton(window, text="Hard", command=lambda: start_typing_screen("H"), fg_color=SOFT_PINK, hover_color=HOVER_PINK, text_color=WHITE, font=("Times", 20, "bold"), corner_radius=15)
    hard_button.pack(pady=5)

    if boss_unlocked():
        boss_button = ctk.CTkButton(
            window,
            text="Secret Boss Level",
            command=lambda: start_typing_screen("B"),
            fg_color=SOFT_PINK,
            hover_color=HOVER_PINK,
            text_color=WHITE,
            font=("Times", 20, "bold"),
            corner_radius=15
        )
        boss_button.pack(pady=5)

player_name = ""

start_time = 0

difficulty_names = {
    "E": "Easy Typing",
    "M": "Medium Typing",
    "H": "Hard Typing",
    "B": "Boss Typing"
}

def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()

def boss_unlocked():
    leaderboard_data = typing_speed.show_leaderboard()
    hard_scores = leaderboard_data.get("Hard Typing", {})

    sorted_scores = sorted(hard_scores.items(), key=lambda x: x[1], reverse=True)
    top_three_names = [name for name, score in sorted_scores[:3]]

    return player_name in top_three_names

def start_typing_screen(difficulty):
    clear_screen()
    global submit_button, start_button

    if difficulty == "E":
        number = random.randint(0, len(typing_speed.easy_txt_options) - 1)
    elif difficulty == "M":
        number = random.randint(0, len(typing_speed.medium_txt_options) - 1)
    elif difficulty == "H":
        number = random.randint(0, len(typing_speed.hard_txt_options) - 1)
    elif difficulty == "B":
        number = random.randint(0, len(typing_speed.secret_extra_lvl_options) - 1)
    else:
        raise ValueError()

    random_text = typing_speed.get_random_text(number, difficulty)

    title = ctk.CTkLabel(
        window,
        text=difficulty_names[difficulty],
        font=("Times", 30, "bold"),
        text_color=WHITE,
        fg_color="transparent"
    )
    title.pack(pady=20)

    paragraph = random_text

    paragraph_label = ctk.CTkLabel(
        window,
        text=paragraph,
        font=("Times", 20),
        text_color=WHITE,
        fg_color="transparent",
        wraplength=420
    )
    paragraph_label.pack(pady=10)

    typing_box = ctk.CTkTextbox(
        window,
        width=400,
        height=120,
        fg_color=WHITE,
        text_color=DARK_PINK,
        border_color=SOFT_PINK,
        border_width=2,
        corner_radius=12
    )
    typing_box.pack(pady=15)

    submit_button = ctk.CTkButton(
        window,
        text="Submit",
        fg_color=SOFT_PINK,
        hover_color=HOVER_PINK,
        text_color=WHITE,
        font=("Times", 20, "bold"),
        corner_radius=15
    )
    submit_button.pack(pady=10)

    typing_box.configure(state="disabled")
    submit_button.configure(state="disabled")

    start_button = ctk.CTkButton(
        window,
        text="Start",
        command=lambda: start_timer(typing_box, submit_button, start_button),
        fg_color=SOFT_PINK,
        hover_color=HOVER_PINK,
        text_color=WHITE,
        font=("Times", 20, "bold"),
        corner_radius=15
    )
    start_button.pack(pady=10)

    submit_button.configure(command=lambda: submit_text(typing_box, paragraph, difficulty))

def start_timer(typing_box, submit_button, start_button):
    global start_time

    start_time = time.time()

    typing_box.configure(state="normal")
    typing_box.focus()

    submit_button.configure(state="normal")
    start_button.configure(state="disabled")

def submit_text(typing_box, paragraph, difficulty):
    end_time = time.time()
    elapsed_time = end_time - start_time

    user_input = typing_box.get("1.0", "end-1c")

    accuracy = typing_speed.calculate_accuracy(paragraph, user_input)

    pts = typing_speed.generate_points(
        accuracy,
        elapsed_time,
        difficulty,
        paragraph
    )

    difficulty_key = difficulty_names[difficulty]

    typing_speed.leaderboard(
        player_name,
        pts,
        difficulty_key
    )

    typing_box.configure(state="disabled")

    show_results_screen(accuracy, elapsed_time, pts, difficulty_key)

def show_results_screen(accuracy, elapsed_time, pts, difficulty_key):
    clear_screen()

    title = ctk.CTkLabel(
        window,
        text=f"Great job, {player_name}!",
        font=("Times", 30, "bold"),
        text_color=WHITE,
        fg_color="transparent"
    )
    title.pack(pady=20)

    results = ctk.CTkLabel(
        window,
        text=(
            f"Difficulty: {difficulty_key}\n"
            f"Accuracy: {accuracy:.2f}%\n"
            f"Time Taken: {elapsed_time:.2f} seconds\n"
            f"Points Earned: {pts}"
        ),
        font=("Times", 22),
        text_color=WHITE,
        fg_color="transparent"
    )
    results.pack(pady=20)

    leaderboard_button = ctk.CTkButton(
        window,
        text="View Leaderboard",
        command=lambda: show_leaderboard_screen(difficulty_key),
        fg_color=SOFT_PINK,
        hover_color=HOVER_PINK,
        text_color=WHITE,
        font=("Times", 20, "bold"),
        corner_radius=15
    )
    leaderboard_button.pack(pady=10)

def show_leaderboard_screen(difficulty_key):
    clear_screen()

    title = ctk.CTkLabel(
        window,
        text=f"{difficulty_key} Leaderboard",
        font=("Times", 30, "bold"),
        text_color=WHITE,
        fg_color="transparent"
    )
    title.pack(pady=20)

    leaderboard_data = typing_speed.show_leaderboard().get(difficulty_key, {})

    if not leaderboard_data:
        no_data_label = ctk.CTkLabel(
            window,
            text="No data available.",
            font=("Times", 20),
            text_color=WHITE,
            fg_color="transparent"
        )
        no_data_label.pack(pady=10)
    else:
        for i, (name, points) in enumerate(leaderboard_data.items(), start=1):
            entry_label = ctk.CTkLabel(
                window,
                text=f"{i}. {name} - {points} points",
                font=("Times", 20),
                text_color=WHITE,
                fg_color="transparent"
            )
            entry_label.pack(pady=5)
    
    if boss_unlocked() and difficulty_key == "Hard Typing":
        congratulations_label = ctk.CTkLabel(
        window,
        text=typing_speed.secret_level_txt,
        font=("Times", 20, "bold"),
        text_color=WHITE,
        fg_color="transparent"
        )
        congratulations_label.pack(pady=10)

    play_again_button = ctk.CTkButton(
        window,
        text="Play Again as the same player",
        command=show_difficulty_screen,
        fg_color=SOFT_PINK,
        hover_color=HOVER_PINK,
        text_color=WHITE,
        font=("Times", 20, "bold"),
        corner_radius=15
    )
    play_again_button.pack(pady=20)

    play_again_new_button = ctk.CTkButton(
        window,
        text="Play Again as a new player",
        command=show_name_screen,
        fg_color=SOFT_PINK,
        hover_color=HOVER_PINK,
        text_color=WHITE,
        font=("Times", 20, "bold"),
        corner_radius=15
    )
    play_again_new_button.pack(pady=10)

    exit_game_button = ctk.CTkButton(
        window,
        text="Exit Game",
        command=show_exit_screen,
        fg_color=SOFT_PINK,
        hover_color=HOVER_PINK,
        text_color=WHITE,
        font=("Times", 20, "bold"),
        corner_radius=15
    )
    exit_game_button.pack(pady=10)

def show_exit_screen():
    clear_screen()

    exit_label = ctk.CTkLabel(
        window,
        text="Thanks for playing! Better luck next time!",
        font=("Times", 30, "bold"),
        text_color=WHITE,
        fg_color="transparent"
    )
    exit_label.pack(pady=20)

    exit_button = ctk.CTkButton(
        window,
        text="Bye bye!",
        command=window.destroy,
        fg_color=SOFT_PINK,
        hover_color=HOVER_PINK,
        text_color=WHITE,
        font=("Times", 20, "bold"),
        corner_radius=15
    )
    exit_button.pack(pady=20)


show_rules()
window.mainloop()