from turtle import  Turtle

# Initiate score traking
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

# Update score function
    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 25, "normal"))

# Game over function
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!!", align="center", font=("Arial", 25, "bold"))

# Increasing score each time snake gets food
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()