import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

flashcard_data = {
    "Alphabets": {
        "Hindi": [("अ", "A"), ("आ", "AA"), ("इ", "I"), ("ई", "EE"), ("उ", "U"),("ऊ", "UU"), ("ऋ", "RI"), ("ए", "E"),
    ("ऐ", "AI"), ("ओ", "O"), ("औ", "AU"), ("अं", "AM"),
    ("अः", "AH"),
    ("क", "KA"), ("ख", "KHA"), ("ग", "GA"), ("घ", "GHA"),
    ("ङ", "NGA"), ("च", "CHA"), ("छ", "CHHA"), ("ज", "JA"),
    ("झ", "JHA"), ("ञ", "NYA"), ("ट", "TA"), ("ठ", "THA"),
    ("ड", "DA"), ("ढ", "DHA"), ("ण", "NA"), ("त", "TA"),
    ("थ", "THA"), ("द", "DA"), ("ध", "DHA"), ("न", "NA"),
    ("प", "PA"), ("फ", "PHA"), ("ब", "BA"), ("भ", "BHA"),
    ("म", "MA"), ("य", "YA"), ("र", "RA"), ("ल", "LA"),
    ("व", "VA"), ("श", "SHA"), ("ष", "SHHA"), ("स", "SA"),
    ("ह", "HA"), ("क्ष", "KSH"), ("त्र", "TRA"), ("ज्ञ", "GYA")],
       
        "Spanish": [("A", "A"), ("E", "E"), ("I", "I"), ("O", "O"), ("U", "U"), 
    ("B", "B"), ("C", "C"), ("CH", "CH"), ("D", "D"), ("F", "F"),
    ("G", "G"), ("H", "H"), ("J", "J"), ("K", "K"), ("L", "L"), 
    ("LL", "LL"), ("M", "M"), ("N", "N"), ("Ñ", "Ñ"), ("P", "P"), 
    ("Q", "Q"), ("R", "R"), ("S", "S"), ("T", "T"), ("V", "V"),
    ("W", "W"), ("X", "X"), ("Y", "Y"), ("Z", "Z")],
        
        "French": [("A", "A"), ("E", "E"), ("I", "I"), ("O", "O"), ("U", "U"), ("Y", "Y"),
    ("B", "B"), ("C", "C"), ("CH", "CH"), ("D", "D"), ("F", "F"),
    ("G", "G"), ("H", "H"), ("J", "J"), ("K", "K"), ("L", "L"),
    ("M", "M"), ("N", "N"), ("P", "P"), ("Q", "Q"), ("R", "R"),
    ("S", "S"), ("T", "T"), ("V", "V"), ("W", "W"), ("X", "X"),
    ("Y", "Y"), ("Z", "Z")],

        "Telugu": [("అ", "A"), ("ఆ", "AA"), ("ఇ", "I"), ("ఈ", "II"), ("ఉ", "U"), ("ఊ", "UU"), ("ऋ", "R"), 
    ("ೠ", "RR"), ("ల", "L"), ("೤", "LL"), ("ఎ", "E"), ("10", "EE"), ("ఐ", "AI"), ("ఓ", "O"), 
    ("ఔ", "OU"), ("అం", "UM"), ("క", "K"), ("ఖ", "KH"), ("గ", "G"), ("ఘ", "GH"), ("ఙ", "NG"),
    ("చ", "CH"), ("ఛ", "CHH"), ("జ", "J"), ("ఝ", "JH"), ("ఞ", "NY"), ("ట", "T"), ("ఠ", "TH"),
    ("డ", "D"), ("ఢ", "DH"), ("ణ", "N"), ("త", "THA"), ("థ", "THHA"), ("ద", "DA"), ("ధ", "DHA"),
    ("న", "NA"), ("ప", "P"), ("ఫ", "PH"), ("బ", "B"), ("భ", "BH"), ("మ", "M"), ("య", "YA"),
    ("ర", "RA"), ("ల", "LA"), ("వ", "VA"), ("శ", "SHA"), ("ష", "SHHA"), ("స", "SA"), ("హ", "HA"),
    ("ళ", "LA"), ("క్ష", "KS"), ("ఱ", "R")],

        "German": [("A", "A"), ("Ä", "AE"), ("E", "E"), ("I", "I"), ("O", "O"), ("Ö", "OE"), ("U", "U"), 
    ("Ü", "UE"), ("Y", "Y"), ("B", "B"), ("C", "C"), ("CH", "CH"), ("D", "D"), ("F", "F"), 
    ("G", "G"), ("H", "H"), ("J", "Y"), ("K", "K"), ("L", "L"), ("M", "M"), ("N", "N"), 
    ("P", "P"), ("Q", "KW"), ("R", "R"), ("S", "S"), ("SCH", "SH"), ("T", "T"), ("V", "F"), 
    ("W", "V"), ("X", "X"), ("Z", "TS")],
    },
    "Numbers": {
        "Hindi": [("१", "1"), ("२", "2"), ("३", "3"), ("४", "4"), ("५", "5"), 
    ("६", "6"), ("७", "7"), ("८", "8"), ("९", "9"), ("१०", "10")],
        "Spanish": [("Uno", "1"), ("Dos", "2"), ("Tres", "3"), ("Cuatro", "4"), ("Cinco", "5"),
    ("Seis", "6"), ("Siete", "7"), ("Ocho", "8"), ("Nueve", "9"), ("Diez", "10")],
        "French": [("Un", "1"), ("Deux", "2"), ("Trois", "3"), ("Quatre", "4"), ("Cinq", "5"),
    ("Six", "6"), ("Sept", "7"), ("Huit", "8"), ("Neuf", "9"), ("Dix", "10")],
        "Telugu": [("ఒకటి", "1"), ("రెండు", "2"), ("మూడు", "3"), ("నాలుగు", "4"), ("ఐదు", "5"),
    ("ఆరు", "6"), ("ఏడు", "7"), ("ఎనిమిది", "8"), ("తొమ్మిది", "9"), ("పది", "10")],
        "German": [("Eins", "1"), ("Zwei", "2"), ("Drei", "3"), ("Vier", "4"), ("Fünf", "5"),
    ("Sechs", "6"), ("Sieben", "7"), ("Acht", "8"), ("Neun", "9"), ("Zehn", "10")],
    },
    "Greetings": {
        "Hindi": [("नमस्ते", "Hello"),
        ("सुप्रभात", "Good Morning"),
        ("शुभ संध्या", "Good Evening"),
        ("शुभ रात्रि", "Good Night"),
        ("कैसे हो?", "How are you?"),
        ("क्या हाल है?", "What's up?"),
        ("धन्यवाद", "Thank you"),
        ("माफ़ करें", "Excuse me / Sorry"),
        ("शुभकामनाएं", "Best wishes"),
        ("मुझे अच्छा लगा", "I liked it / It was nice"),
        ("क्या तुम ठीक हो?", "Are you okay?"),
        ("बधाई हो", "Congratulations"),
        ("क्या कर रहे हो?", "What are you doing?"),
        ("आराम से", "Take it easy"),
        ("ख्याल रखना", "Take care"),
        ("फिर मिलेंगे", "See you again"),
        ("जल्दी आना", "Come soon"),
        ("बैठो, आराम से", "Sit down, relax"),
        ("कोई बात नहीं", "It's nothing / No problem"),
        ("चलो, चलते हैं", "Let's go, let's move")],

        "Spanish": [("Hola", "Hello"),
        ("Buenos días", "Good Morning"),
        ("Buenas tardes", "Good Afternoon"),
        ("Buenas noches", "Good Night"),
        ("¿Cómo estás?", "How are you?"),
        ("¿Qué tal?", "What's up?"),
        ("Gracias", "Thank you"),
        ("Perdón", "Excuse me / Sorry"),
        ("Felicidades", "Congratulations"),
        ("Mucho gusto", "Nice to meet you"),
        ("¿Qué haces?", "What are you doing?"),
        ("Cuídate", "Take care"),
        ("Hasta luego", "See you later"),
        ("Nos vemos", "See you"),
        ("Te quiero", "I love you"),
        ("¡Venga!", "Come on! / Let's go!"),
        ("¿Todo bien?", "Is everything fine?"),
        ("¿Cómo te va?", "How’s it going?"),
        ("Bienvenido", "Welcome"),
        ("Disculpa", "Excuse me / Pardon me")],

        "French": [("Bonjour", "Good Morning / Hello"),
        ("Bonsoir", "Good Evening"),
        ("Bonne nuit", "Good Night"),
        ("Comment ça va?", "How are you?"),
        ("Ça va?", "How’s it going?"),
        ("Merci", "Thank you"),
        ("Excusez-moi", "Excuse me / Sorry"),
        ("Félicitations", "Congratulations"),
        ("Enchanté", "Nice to meet you"),
        ("Quoi de neuf?", "What's up?"),
        ("Comment tu vas?", "How are you?"),
        ("Prends soin de toi", "Take care"),
        ("À bientôt", "See you soon"),
        ("À demain", "See you tomorrow"),
        ("Bonne journée", "Have a nice day"),
        ("Bonne soirée", "Have a nice evening"),
        ("Bienvenue", "Welcome"),
        ("Ça marche", "It works / It’s fine"),
        ("D'accord", "Alright / Okay"),
        ("Je t’aime", "I love you")],

        "Telugu": [("నమస్కారం", "Hello"),
        ("శుభోదయం", "Good Morning"),
        ("శుభ సాయంత్రం", "Good Evening"),
        ("శుభ రాత్రి", "Good Night"),
        ("మీరు ఎలా ఉన్నారు?", "How are you?"),
        ("బాగున్నాను", "I’m good"),
        ("మీరు బాగున్నారా?", "Are you doing well?"),
        ("ధన్యవాదాలు", "Thank you"),
        ("మన్నించండి", "Excuse me / Sorry"),
        ("మీరు కధలు చెప్పగలరా?", "Can you tell me a story?"),
        ("మీరు ఎలా అనిపిస్తారు?", "How do you feel?"),
        ("మంచిది", "Good"),
        ("ఇంకా కలుద్దాం", "Let’s meet again"),
        ("ఆకర్షణగా ఉన్నారు", "You look great"),
        ("మంచి రోజులు ఉండాలి", "Have a good day"),
        ("పలుకరించేందుకు సంతోషం", "Nice to talk to you"),
        ("రేపు కలుద్దాం", "See you tomorrow"),
        ("ఇంకా మరొక రోజు కలుద్దాం", "Let’s meet another day"),
        ("ప్రతి రోజూ ఆనందంగా ఉండండి", "Stay happy every day"),
        ("మీతో మాట్లాడడం ఆనందంగా ఉంది", "It’s nice talking to you")],

        "German": [("Hallo", "Hello"),
        ("Guten Morgen", "Good Morning"),
        ("Guten Abend", "Good Evening"),
        ("Gute Nacht", "Good Night"),
        ("Wie geht's?", "How are you?"),
        ("Mir geht's gut", "I’m good"),
        ("Wie fühlst du dich?", "How do you feel?"),
        ("Danke", "Thank you"),
        ("Entschuldigung", "Excuse me / Sorry"),
        ("Wie war dein Tag?", "How was your day?"),
        ("Alles klar?", "All good?"),
        ("Schön dich zu sehen", "Nice to see you"),
        ("Lass uns wieder treffen", "Let’s meet again"),
        ("Bis später", "See you later"),
        ("Bis morgen", "See you tomorrow"),
        ("Haben Sie einen schönen Tag", "Have a nice day"),
        ("Viel Glück", "Good luck"),
        ("Gute Reise", "Safe journey"),
        ("Ich wünsche dir einen tollen Tag", "I wish you a great day"),
        ("Es war schön, mit dir zu sprechen", "It was nice talking to you")],
    },
}

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Learning App")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#ffecd2")

        self.category = tk.StringVar(value="")
        self.language = tk.StringVar(value="")
        self.flashcards = []
        self.current_index = 0
        self.flipped = False

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(
            self.root, text="Learn with Flashcards!", bg="#ffecd2", fg="#ff6f61", font=("Arial", 16, "bold")
        )
        self.title_label.pack(pady=10)

        self.category_label = tk.Label(self.root, text="Select Category:", bg="#ffecd2", font=("Arial", 12))
        self.category_label.pack(pady=5)
        self.category_menu = ttk.Combobox(
            self.root, textvariable=self.category, values=list(flashcard_data.keys()), state="readonly"
        )
        self.category_menu.pack(pady=5)
        self.category_menu.bind("<<ComboboxSelected>>", self.show_language_menu)

        self.language_label = tk.Label(self.root, text="Select Language:", bg="#ffecd2", font=("Arial", 12))
        self.language_menu = ttk.Combobox(self.root, textvariable=self.language, state="readonly")
        self.language_menu.bind("<<ComboboxSelected>>", self.load_flashcards)

        self.flashcard_label = tk.Label(
            self.root, text="", font=("Arial", 28, "bold"), bg="#f9d5e5", fg="#5d5c61", relief="raised", pady=20, padx=20
        )

        self.button_frame = tk.Frame(self.root, bg="#ffecd2")
        self.flip_button = tk.Button(
            self.button_frame, text="Flip", command=self.flip_card, bg="#ff6f61", fg="#ffffff", font=("Arial", 10, "bold")
        )
        self.prev_button = tk.Button(
            self.button_frame, text="Previous", command=self.prev_card, bg="#4caf50", fg="#ffffff", font=("Arial", 10, "bold")
        )
        self.next_button = tk.Button(
            self.button_frame, text="Next", command=self.next_card, bg="#2196f3", fg="#ffffff", font=("Arial", 10, "bold")
        )

    def show_language_menu(self, event=None):
        self.language_label.pack(pady=5)
        self.language_menu.pack(pady=5)

        selected_category = self.category.get()
        languages = list(flashcard_data[selected_category].keys())
        self.language_menu.config(values=languages)

    def load_flashcards(self, event=None):
        selected_category = self.category.get()
        selected_language = self.language.get()
        self.flashcards = flashcard_data[selected_category][selected_language]
        self.current_index = 0
        self.flipped = False

        self.flashcard_label.pack(pady=20)
        self.button_frame.pack(pady=10)
        self.flip_button.pack(side="left", padx=5)
        self.prev_button.pack(side="left", padx=5)
        self.next_button.pack(side="left", padx=5)

        self.update_flashcard()

    def update_flashcard(self):
        if not self.flashcards:
            self.flashcard_label.config(text="No flashcards available!")
            return
        front, _ = self.flashcards[self.current_index]
        self.flashcard_label.config(text=front)

    def flip_card(self):
        if not self.flashcards:
            return
        front, back = self.flashcards[self.current_index]
        self.flashcard_label.config(text=back if not self.flipped else front)
        self.flipped = not self.flipped

    def prev_card(self):
        if not self.flashcards:
            return
        self.current_index = (self.current_index - 1) % len(self.flashcards)
        self.flipped = False
        self.update_flashcard()

    def next_card(self):
        if not self.flashcards:
            return
        self.current_index = (self.current_index + 1) % len(self.flashcards)
        self.flipped = False
        self.update_flashcard()


class LandingPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Learning App")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f7fa")

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(
            self.root,
            text="HELLO NEW LEARNERS! 🎉",
            bg="#f5f7fa",
            fg="#4caf50",
            font=("Comic Sans MS", 18, "bold"),
        )
        self.title_label.pack(pady=20)

        self.subtitle_label = tk.Label(
            self.root,
            text="Dive into the world of flashcards\n& learn languages like never before!",
            bg="#f5f7fa",
            fg="#555555",
            font=("Arial", 12, "italic"),
        )
        self.subtitle_label.pack(pady=10)

        self.emoji_label = tk.Label(
            self.root, text="🌟 🚀 🌏", bg="#f5f7fa", fg="#ff6f61", font=("Arial", 20)
        )
        self.emoji_label.pack(pady=10)

        self.start_button = tk.Button(
            self.root,
            text="Start Learning Now ✨",
            command=self.start_app,
            bg="#4caf50",
            fg="#ffffff",
            font=("Arial", 12, "bold"),
            relief="raised",
            borderwidth=3,
        )
        self.start_button.pack(pady=10)

        self.explore_button = tk.Button(
            self.root,
            text="Explore More 🔍",
            command=self.explore_more,
            bg="#2196f3",
            fg="#ffffff",
            font=("Arial", 12, "bold"),
            relief="raised",
            borderwidth=3,
        )
        self.explore_button.pack(pady=5)

        self.footer_label = tk.Label(
            self.root,
            text="🌈 Learning made fun for Gen Z & everyone! 🌟",
            bg="#f5f7fa",
            fg="#555555",
            font=("Arial", 10, "italic"),
        )
        self.footer_label.pack(side="bottom", pady=10)

    def start_app(self):
        self.root.destroy()
        root = tk.Tk()
        app = FlashcardApp(root)
        root.mainloop()

    def explore_more(self):
        messagebox.showinfo(
            "Explore More",
            "Stay tuned! More features are coming soon.\nFollow us for updates! 🚀",
        )


if __name__ == "__main__":
    root = tk.Tk()
    landing_page = LandingPage(root)
    root.mainloop()
