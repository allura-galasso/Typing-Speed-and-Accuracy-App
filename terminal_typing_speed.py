import time
from random import randint
import json


easy_txt_options = ["The sun was bright today. I went outside for a short walk. The air felt warm and fresh. Birds were singing in the trees.\n"
                "It was a nice way to start the day.", 

                "She didn't understand how changed worked. When she looked at today compared to yesterday, there was nothing that she could see that was different.\n"
                "Yet, when she looked at today compared to last year, she couldn't see how anything was ever the same.",

                "My favorite meal is pizza. I like cheese and pepperoni the most. I also enjoy garlic bread on the side.\n"
                "After dinner, I usually drink cold water. It is a simple meal that makes me happy.",
                
                "I have a small backpack for school. It holds my books, pencils, and laptop.\n"
                "I try to keep it clean every week. A neat bag helps me stay organized. It also makes finding things easier.",
                
                "Rain began to fall in the afternoon. I watched the drops hit the windows. The sound was calm and relaxing.\n"
                "After a while, the sky became clear again. A rainbow appeared for a few minutes.",
                
                "Reading is a great hobby. Books can teach new ideas and tell fun stories.\n"
                "I enjoy reading before bed. It helps me relax after a busy day. Every book has something new to offer.",
                
                "My family likes to spend time together. We watch movies, cook dinner, and play games.\n"
                "Everyone laughs and tells stories. These moments are special to me. They create happy memories.",
                
                "Exercise is important for good health. A short walk or bike ride can improve your mood.\n"
                "Drinking enough water also helps your body. Small healthy habits make a big difference over time.",
                
                "The beach is one of my favorite places. I enjoy listening to the waves. Walking on the sand feels peaceful.\n"
                "The ocean breeze is cool and refreshing. Watching the sunset is the best part.",
                
                "Learning something new takes practice. At first, it may seem difficult. With patience, each day becomes a little easier.\n"
                "Mistakes help us improve. Success comes from not giving up."]

medium_txt_options = ["You're going to make a choice today that will have a direct impact on where you are five years from now.\n"
               "The truth is, you'll make choice like that every day of your life. The problem is that on most days,\n"
                "you won't know the choice you make will have such a huge impact on your life in the future.\n"
                "So if you want to end up in a certain place in the future, you need to be careful of the choices you make today.",
                
                "One of the best parts of traveling is experiencing a place through the eyes of the people who live there.\n"
                "Every city has its own traditions, favorite foods, and unique atmosphere that cannot be fully understood from photographs alone.\n"
                "Exploring new places often creates memories that last much longer than any souvenir.",
                
                "Technology has changed the way people communicate, learn, and work.\n"
                "Information that once required hours of research can now be found within seconds.\n"
                "Although these advances make life more convenient, they also encourage people to balance screen time with meaningful face-to-face conversations."
                
                "Many successful people explain that consistency is more valuable than motivation.\n"
                " Motivation can disappear when life becomes stressful or exhausting, but consistent habits continue to produce progress.\n"
                "Even small improvements made every day can lead to impressive results over the course of a year."
                
                "Reading regularly strengthens vocabulary, improves concentration, and encourages creative thinking.\n"
                "Whether someone enjoys mystery novels, biographies, or science fiction, every book offers an opportunity to learn something new.\n"
                "A few quiet minutes with a good book can be surprisingly refreshing after a busy day."
                
                "Exercise benefits both physical and mental health in ways that are often underestimated.\n"
                "Regular movement increases energy, reduces stress, and helps people sleep more comfortably at night.\n"
                "Finding an activity that is enjoyable makes it much easier to maintain a healthy routine.",
                
                "Weather has a surprising influence on people's daily routines and emotions.\n"
                "Bright, sunny mornings often encourage outdoor activities, while rainy afternoons provide the perfect excuse to stay inside with a warm drink and a favorite movie.\n"
                "Each season offers its own unique experiences and traditions."
                
                "Learning a new language requires patience, repetition, and the willingness to make mistakes.\n"
                "At first, remembering vocabulary and grammar rules can feel overwhelming, but confidence grows with regular practice.\n"
                "Eventually, conversations become more natural, and understanding another culture becomes much easier.",
                
                "Good time management does not mean filling every minute with work.\n"
                "Instead, it involves organizing responsibilities while leaving room for rest, hobbies, and unexpected events.\n"
                "Maintaining a balanced schedule often leads to greater productivity and a healthier lifestyle.",
                
                "Friendships become stronger through trust, honesty, and shared experiences rather than expensive gifts or constant attention.\n"
                "Supporting one another during difficult moments creates lasting connections that can survive distance and time.\n"
                "Simple acts of kindness often have the greatest impact."]

hard_txt_options = [ "Curiosity is often the foundation of meaningful discovery because it encourages people to question assumptions rather than accept simple explanations.\n"
                "History demonstrates that many important breakthroughs resulted from individuals who refused to ignore unusual\n"
                "observations, choosing instead to investigate them with patience, determination, and careful analysis.",

                "Although modern technology has dramatically increased access to information, it has also created an environment in which distractions compete\n"
                "constantly for our attention. Developing the ability to concentrate deeply on a single task has therefore become an increasingly valuable skill,\n"
                "both academically and professionally.",

                "The natural world operates through countless interconnected systems, many of which remain only partially understood despite decades of\n"
                "scientific research. Even seemingly insignificant changes within one ecosystem can produce unexpected consequences elsewhere,\n"
                "illustrating the remarkable complexity and delicate balance of environmental processes.",

                "Success is rarely the result of extraordinary talent alone. Instead, it often emerges from disciplined preparation, thoughtful decision-making,\n"
                "and the willingness to learn from repeated failures. Individuals who embrace challenges instead of avoiding them generally develop greater\n"
                "confidence and resilience over time.",

                "Architecture reflects far more than engineering principles; it also reveals the priorities, traditions, and artistic values of the societies\n"
                "that constructed it. Ancient monuments, modern skyscrapers, and carefully preserved historical buildings each communicate stories about the\n"
                "cultures responsible for their creation.",

                "Artificial intelligence continues to reshape industries by automating repetitive tasks, assisting with complex analysis, and accelerating\n"
                "scientific research. Nevertheless, responsible implementation requires thoughtful consideration of ethical concerns, including privacy,\n"
                "transparency, accountability, and the appropriate role of human judgment.",

                "Financial responsibility extends beyond simply earning money because long-term stability depends upon careful budgeting, strategic saving,\n"
                "and informed investment decisions. Small, consistent financial habits often generate greater benefits than occasional attempts to make\n"
                "dramatic improvements all at once.",

                "Space exploration represents one of humanity's most ambitious scientific endeavors, combining advanced engineering, international collaboration,\n"
                "and decades of meticulous planning. Every successful mission expands our understanding of the universe while simultaneously inspiring\n"
                "future generations to pursue innovation and discovery.",

                "Effective communication requires more than selecting appropriate vocabulary; it also depends upon understanding context, interpreting tone,\n"
                "recognizing nonverbal cues, and adapting messages for different audiences. Misunderstandings frequently arise not because people fail to speak\n"
                "clearly, but because they fail to listen carefully.",

                "Throughout history, civilizations have risen and declined in response to countless political, economic, environmental,\n"
                "and cultural influences that interacted in remarkably complex ways. Studying these patterns reminds us that progress is seldom linear,\n"
                "certainty is often temporary, and thoughtful leadership frequently determines whether societies adapt successfully to changing circumstances."
                ]

secret_extra_lvl_options = ["Hypothetically, if quintessentially misunderstood quasiparticles unexpectedly coexisted with bioluminescent microorganisms\n"
                "inside an ultra-high-vacuum chamber, researchers would reluctantly acknowledge that conventional assumptions regarding equilibrium,\n"
                "electromagnetic fluctuations, and probabilistic interpretations required substantial reconsideration. Ironically, the equipment manual\n"
                "explicitly warned, \"Do not improvise.\"",
                
                "\"The juxtaposition,\" proclaimed the philosopher, \"between hyper-specialization and interdisciplinary collaboration is paradoxically advantageous.\"\n"
                " Nevertheless, the audience remained conspicuously unpersuaded, largely because Presentation_v14_FINAL_FINAL(2).pptx refused to open after\n"
                "someone accidentally renamed it Presentation_v14_FINAL_FINAL(2)_REAL_FINAL_v3.pptx.",
                
                "A bewilderingly heterogeneous assortment of hexadecimal values (0x1A3F, 0xBEEF, 0xDEADBEEF, and 0xCAFEBABE) appeared alongside binary\n"
                "sequences (101101001011), irrational constants (π, e, and φ), coordinate pairs (-73.9857, 40.7484), percentages (12.875%), semicolons; colons:\n"
                "commas, quotation marks, apostrophes, brackets [ ], braces { }, angle brackets < >, and enough parentheses (((like these))) to make proofreading\n"
                "feel mathematically hazardous.",
                
                "On Thursday, February 29, 2048 (which should immediately make you suspicious), Professor Maximilian Q. Wickersham-Jones III challenged exactly 1,024\n"
                "participants to transcribe the following sentence without committing a single typographical error: \"Pseudopseudohypoparathyroidism,\n"
                "floccinaucinihilipilification, antidisestablishmentarianism, and honorificabilitudinitatibus are unquestionably memorable, yet they remain\n"
                "astonishingly less intimidating than debugging somebody else's undocumented code at 3:17 a.m. while surviving exclusively on lukewarm coffee,\n"
                "stubborn optimism, and spectacularly misplaced confidence.\""
                
                "At exactly 11:58:47 p.m. on October 17, 2084, the bewildered committee unanimously concluded, \"Despite exhaustive testing, meticulous documentation,\n"
                "and seventeen consecutive revisions, nobody can adequately explain why the prototype functions perfectly on Tuesdays, catastrophically on Wednesdays,\n"
                "and suspiciously well whenever someone insists they 'didn't change anything.'\" Consequently, the emergency response team cross-referenced 14,782,391\n"
                "archived records, validated ERROR_CODE: 0xCAFEBABE, confirmed the coordinates (-73.985656, 40.748433), compared SHA-256 and SHA-512 checksums,\n"
                "alphabetized the words electroencephalographically, pseudopseudohypoparathyroidism, floccinaucinihilipilification, and thyroparathyroidectomized,\n"
                "restored the mysteriously renamed file FINAL_v31_REAL_FINAL_(2)_USE_THIS_ONE_FOR_REAL.docx, restarted the server exactly 17 times, and somehow\n"
                "discovered that the entire crisis had originated from a single misplaced comma, a missing quotation mark, and one spectacularly overconfident employee\n"
                "who confidently declared, \"Trust me, it'll be fine,\" approximately thirty seconds before everything failed in the most mathematically improbable,\n"
                "professionally embarrassing, and completely preventable fashion imaginable."]

rules_text = "The rules of this game is simple: \n 1. Choose your difficulty (Type E for easy, M for medium, and H for hard)\n" \
" 2. You'll be given a random paragraph that you will need to copy to the best of your ability as fast as you can. The faster you type and the more accurate you type," \
" the higher you will score!\n 3. Be sure to press the enter key before and after you type your text!\n 4. Test your luck at beating some of the highest scores on the "
"leaderboard! \n 5. Most importantly: HAVE FUN!\n"

level_prompting_txt = "Please select the level of difficulty you'd like to try! (As a reminder: Type E for easy, Type M for medium, and Type H for hard): "

secret_level_txt = "Woah you're a pro! You have reached top 3 on the leaderboard! For your accomplishes you have unlocked a secret boss level difficulty! " \
"To try it out, type B into the difficulty selection prompt!"

difficulty_names = {
    "E": "Easy Typing",
    "M": "Medium Typing",
    "H": "Hard Typing",
    "B": "Boss Typing"
}

def difficulty_level():

    choice = input(level_prompting_txt).upper()

    if choice == "E":
        number = randint(0, len(easy_txt_options) - 1)
    
    elif choice == "M":
        number = randint(0, len(medium_txt_options) - 1)
    
    elif choice == "H":
        number = randint(0, len(hard_txt_options) - 1)

    elif choice == "B":
        number = randint(0, len(secret_extra_lvl_options) - 1)

    else:
        print("Invalid choice, try again.")
        return difficulty_level()
    
    return number, choice

def get_random_text(number, difficulty):

    if difficulty == "E":
        return easy_txt_options[number]
    
    elif difficulty == "M":
        return medium_txt_options[number]
    
    elif difficulty == "H":
        return hard_txt_options[number]
    
    elif difficulty == "B":
        return secret_extra_lvl_options[number]
    
    else:
        raise ValueError()
    
def typing_test():

    print("\n\nWelcome to the typing speed test! This is a fun game that will test your typing speed and accuracy!\n")
    print(rules_text)
    print("\nWhat's your name? (This will be used to save your score to the leaderboard!)\n")
    name = input("Enter your name here: ")

    print(f"\nHello {name}! It is so nice to meet you! Let's get started with the typing speed test!\n")

    number, difficulty = difficulty_level()
    random_text = get_random_text(number, difficulty)

    print(f"\nWell, {name}, I hope you're ready to put "
          f"your fingers to the test! Your random text to type is:\n\n{random_text}\n\n")
    input("Remember! Press Enter when you're ready to start typing and when you have finished...\n")

    start_time = time.time()

    user_input = input()

    end_time = time.time()

    elapsed_time = end_time - start_time

    total_words = len(random_text.split())

    correct_words = 0

    right_text = random_text.split()
    answered_text = user_input.split()

    for i in range(len(right_text)):
        if i < len(answered_text) and right_text[i] == answered_text[i]:
            correct_words = correct_words + 1
    
    accuracy = (correct_words / total_words) * 100

    print(f"\n\nTime taken: {elapsed_time:.2f} seconds\n")
    print(f"Accuracy: {accuracy:.2f}%\n")

    if accuracy >= 50 and accuracy < 75:
        print("You got about half correct!\n")

    elif accuracy >= 75 and accuracy < 90:
        print("Wow! You did really good, almost perfect!\n")

    elif accuracy >= 90:
        print("Holy cow! You're a pro, you're too good!\n")

    else:
        print("I am sure you tried your best! Try again to see if you can score higher!\n")
    
    return accuracy, elapsed_time, name, difficulty, random_text

def generate_points(accuracy, elapsed_time, difficulty, random_text):


    pts = 0

    x = (1.5*len(random_text))

    if difficulty == "E":

        if accuracy < 50 and elapsed_time > x:

            pts = pts + 2
        
        elif accuracy >= 50 and accuracy < 75 and elapsed_time <= x:

            pts = pts + 10
        
        elif accuracy >= 50 and accuracy < 75 and elapsed_time > x:

            pts = pts + 5
        
        elif accuracy >= 75 and accuracy < 90 and elapsed_time <= x:

            pts = pts + 20
        
        elif accuracy >= 75 and accuracy < 90 and elapsed_time > x:

            pts = pts + 4

        elif accuracy > 90 and elapsed_time <= x:

            pts = pts + 50

        elif accuracy > 90 and elapsed_time > x:

            pts = pts + 3

        else:

            pts = pts + 1
    
    elif difficulty == "M":

        if accuracy < 50 and elapsed_time > x:

            pts = pts + 5
        
        elif accuracy >= 50 and accuracy < 75 and elapsed_time <= x:

            pts = pts + 20
        
        elif accuracy >= 50 and accuracy < 75 and elapsed_time > x:

            pts = pts + 15
        
        elif accuracy >= 75 and accuracy < 90 and elapsed_time <= x:

            pts = pts + 50
        
        elif accuracy >= 75 and accuracy < 90 and elapsed_time > x:

            pts = pts + 14

        elif accuracy > 90 and elapsed_time <= x:

            pts = pts + 100

        elif accuracy > 90 and elapsed_time > x:

            pts = pts + 13

        else:

            pts = pts + 1
    
    elif difficulty == "H":

        if accuracy < 50 and elapsed_time > x:

            pts = pts + 10
        
        elif accuracy >= 50 and accuracy < 75 and elapsed_time <= x:

            pts = pts + 40
        
        elif accuracy >= 50 and accuracy < 75 and elapsed_time > x:

            pts = pts + 25
        
        elif accuracy >= 75 and accuracy < 90 and elapsed_time <= x:

            pts = pts + 100
        
        elif accuracy >= 75 and accuracy < 90 and elapsed_time > x:

            pts = pts + 30

        elif accuracy > 90 and elapsed_time <= x:

            pts = pts + 300

        elif accuracy > 90 and elapsed_time > x:

            pts = pts + 30

        else:

            pts = pts + 1

    elif difficulty == "B":

        if accuracy < 50 and elapsed_time > x:

            pts = pts + 30
        
        elif accuracy >= 50 and accuracy < 75 and elapsed_time <= x:

            pts = pts + 200
        
        elif accuracy >= 50 and accuracy < 75 and elapsed_time > x:

            pts = pts + 80
        
        elif accuracy >= 75 and accuracy < 90 and elapsed_time <= x:

            pts = pts + 400
        
        elif accuracy >= 75 and accuracy < 90 and elapsed_time > x:

            pts = pts + 60

        elif accuracy > 90 and elapsed_time <= x:

            pts = pts + 800

        elif accuracy > 90 and elapsed_time > x:

            pts = pts + 50

        else:

            pts = pts + 1

    else:
        raise ValueError()
    
    print(f"\nYou scored {pts} points! Your score will be saved to the leaderboard if you are in the top 10!\n")
    return pts

def show_leaderboard():
    try:
        with open("typing_leaderboard.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {"Easy Typing": {}, "Medium Typing": {}, "Hard Typing": {}}
    
def leaderboard(name, pts, difficulty):

    leaderboard = show_leaderboard()

    if difficulty not in leaderboard:
        leaderboard[difficulty] = {}

    if name not in leaderboard[difficulty] or pts > leaderboard[difficulty][name]:
        leaderboard[difficulty][name] = pts
    
    if name in leaderboard[difficulty] and pts > leaderboard[difficulty][name]:
        leaderboard[difficulty][name] = pts

    sorted_scores = sorted(leaderboard[difficulty].items(), key=lambda x: x[1], reverse=True)
    leaderboard[difficulty] = dict(sorted_scores[:10])

    with open("typing_leaderboard.json", "w") as file:
        json.dump(leaderboard, file, indent=4)

def display_leaderboard(difficulty):
    """Display the leaderboard for a given difficulty"""

    leaderboard = show_leaderboard()
    scores = leaderboard.get(difficulty, {})

    if not scores:
        print(f"\nNo leaderboard entries yet for {difficulty.title()}.\n")
        return

    print(f"\n\n🌟 Top 10 Leaderboard — {difficulty.title()} 🌟\n")
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for i, (name, score) in enumerate(sorted_scores, 1):
        print(f"{i}. {name} — {score} pts\n")
    
def reveal_secret_level(name):
    leaderboard = show_leaderboard()

    if name in leaderboard.get("Hard Typing", {}) and len(leaderboard["Hard Typing"]) >= 3:
        print(secret_level_txt)

def play_game():
    while True:

        accuracy, elapsed_time, name, difficulty, random_text = typing_test()

        pts = generate_points(accuracy, elapsed_time, difficulty, random_text)

        difficulty = difficulty_names[difficulty]

        leaderboard(name, pts, difficulty)

        reveal_secret_level(name)

        display_leaderboard(difficulty)

        continue_game = input("\nWould you like to continue playing? (Y/N): ").strip().lower()
        if continue_game == "y":
            continue
        else:
            display_leaderboard(difficulty)
            print("\nThanks for playing! Better luck next time!")
            break

if __name__ == "__main__":
    play_game()