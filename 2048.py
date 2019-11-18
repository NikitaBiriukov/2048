from turtle import Turtle, Screen

class Game2048:
    def addNumber(self):
        for i in range(0, 4):
            for j in range(0, 4):
                if self.A[i][j] == 0:
                    self.A[i][j] = 2
                    return True
        return False

    def UpMove(self):
        self.offKeyHandler()
        for i in range(3, 0, -1):
            for j in range(0, 4):
                for k in range(i - 1, -1, -1):
                    if self.A[i][j] == self.A[k][j]:
                        self.A[k][j] *= 2
                        self.A[i][j] = 0
                    if self.A[k][j] == 0:
                        self.A[k][j] = self.A[i][j]
                        self.A[i][j] = 0
        if self.addNumber():
            self.draw_play_ground()
            self.onKeyHandler()
        else:
            print "You have lost"

    def DownMove(self):
        self.offKeyHandler()
        for i in range(0, self.n):
            for j in range(0, self.n):
                for k in range(i+1, self.n):
                    if self.A[i][j] == self.A[k][j]:
                        self.A[k][j] *= 2
                        self.A[i][j] = 0
                    if self.A[k][j] == 0:
                        self.A[k][j] = self.A[i][j]
                        self.A[i][j] = 0
        if self.addNumber():            
            self.draw_play_ground()
            self.onKeyHandler()
        else:
            print "You have lost"

    def LeftMove(self):
        self.offKeyHandler()
        for j in range(3, -1, -1):
            for i in range(0, self.n):
                for k in range(j - 1, -1, -1):
                    if self.A[i][j] == self.A[i][k]:
                        self.A[i][k] *= 2
                        self.A[i][j] = 0
                    if self.A[i][k] == 0:
                        self.A[i][k] = self.A[i][j]
                        self.A[i][j] = 0
        if self.addNumber():
            self.draw_play_ground()
            self.onKeyHandler()
        else:
            print "You have lost"

    def RightMove(self):
        self.offKeyHandler()
        for j in range(0, self.n):
            for i in range(0, self.n):
                for k in range(j+1, self.n):
                    if self.A[i][j] == self.A[i][k]:
                        self.A[i][k] *= 2
                        self.A[i][j] = 0
                    if self.A[i][k] == 0:
                        self.A[i][k] = self.A[i][j]
                        self.A[i][j] = 0
        if self.addNumber():
            self.draw_play_ground()
            self.onKeyHandler()
        else:
            print "You have lost"

    def draw_square(self, side_, tx):
        self.t.fillcolor(self.box_colors[tx])
        self.t.begin_fill()
        for s in range(4):
            self.t.forward(side_)
            self.t.left(90)
        self.t.end_fill()
        self.t.write(tx, font=("Arial", 18, "normal"))

    def draw_play_ground(self):
        self.t.clear()
        for i in range(self.n):
            for j in range(self.n):
                self.t.penup()
                self.t.goto(-self.side/2 + self.side*j / self.n , self.side/2 - i*self.side / self.n)
                self.t.pendown()
                self.draw_square(self.side/self.n, self.A[i][j])

    def onKeyHandler(self):
        # Handle key events
        self.screen.onkey(self.UpMove, "Up")
        self.screen.onkey(self.LeftMove, "Left")
        self.screen.onkey(self.RightMove, "Right")
        self.screen.onkey(self.DownMove, "Down")
        self.screen.listen()

    def offKeyHandler(self):
        self.screen.onkey(None, "Up")
        self.screen.onkey(None, "Left")
        self.screen.onkey(None, "Right")
        self.screen.onkey(None, "Down")

    def launch(self):
        self.draw_play_ground()
        self.onKeyHandler()
        self.screen.exitonclick()

    def __init__(self, side, n, title):
        self.n = n
        self.side = side        
        # Initialize turtle and screen
        self.screen = Screen()
        self.screen.setup(2 * side, 2 * side)
        self.screen.title(title)
        self.t = Turtle()
        self.t.speed(0)
        # Initialize playground values
        self.A = [[0] * n for i in range(n)]
        self.A[1][1] = 2
        self.A[2][2] = 2
        self.box_colors = { 0:"#b8cecd",  2:"#edf1ff", 4:"#fff49c", 8:"#ffc125", 16:"#ffa500", 32:"#b58e00", 64:"#ff9994", 128:"#ff7373", 256:"#cb8c9d", 512:"#a8659c", 1024:"#9365a8", 2048:"#943b5e"}

#https://www.color-hex.com/

# Call constructor
def main():
    g = Game2048(200, 4, "Game 2048")
    g.launch()   

if __name__ == "__main__":
    main()