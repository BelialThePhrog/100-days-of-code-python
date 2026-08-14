import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # 1. Store the quiz_brain instance
        self.quiz = quiz_brain

        # 2. Window Setup
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # 3. Score Label
        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12))
        self.score_label.grid(row=0, column=1)

        # 4. Canvas & Question Text (Must assign to self.question_text)
        self.canvas = tk.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280, 
            text="Question Placeholder", 
            fill=THEME_COLOR, 
            font=("Arial", 14, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        # 5. Buttons & Images
        self.true_img = tk.PhotoImage(file="true.png")
        self.false_img = tk.PhotoImage(file="false.png")

        self.true_button = tk.Button(
            image=self.true_img, 
            highlightthickness=0, 
            bd=0, 
            command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)

        self.false_button = tk.Button(
            image=self.false_img, 
            highlightthickness=0, 
            bd=0, 
            command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)

        # 6. Load initial question
        self.get_next_question()

        # 7. Start the main event loop (keeps window open)
        self.window.mainloop()

    # --- UI & LOGIC METHODS ---
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, 
                text=f"You've completed the quiz!\nFinal Score: {self.quiz.score}/{len(self.quiz.question_list)}"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="#2ecc71")  # Green
        else:
            self.canvas.config(bg="#e74c3c")  # Red

        # Wait 1000ms (1 second) before showing the next question
        self.window.after(1000, self.get_next_question)
