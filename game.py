import random


class Snake:
    
    def __init__(self) -> None:
        self.body=[(2,2),(2,3)]
        self.map=Map(10)
        self.apple = Apple(self)
        
        
    def draw_snake(self):
        for x,y in enumerate(self.body):
            if x==0:
                self.map.map[y[0]][y[1]]='🧑'
            else:
                self.map.map[y[0]][y[1]]='🍊'
                
                
    def move(self,move:str):
        direction = {'s': (1, 0), 'w': (-1, 0), 'a': (0, -1), 'd': (0, 1)}
        dx,dy=direction[move]
        
       
        
        nexthead = (self.body[0][0] + dx, self.body[0][1] + dy)
        
        if self.check_collided(nexthead):
            print("game over")
            return False
        if nexthead==self.apple.apple:
            self.body.append(self.body[-1])
       
        else:
            self.map.map[self.body[-1][0]][self.body[-1][1]] = '⬜'
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i-1]
        self.body[0]=nexthead    
        if nexthead==self.apple.apple:
            self.apple.recreate_apple()
        return True
    
    def check_collided(self,body_part):
        if body_part in self.body:
            return True
        elif body_part[0] in [0,9] or body_part[1] in [0,9]:
            return True
        else:
            return False
                
        
        
class Apple:
    
    def __init__(self,snake:Snake) -> None:
        self.apple=None
        self.snake = snake
        self.score = -1
        
    def draw_apple(self):
        if self.apple:
            self.snake.map.map[self.apple[0]][self.apple[1]] = '🍎'
        else:
            self.recreate_apple()
            
    
    def recreate_apple(self):
        if self.apple:
            self.snake.map.map[self.apple[0]][self.apple[1]] = '⬜'
        self.apple=random.randint(1,8),random.randint(1,8)
        while self.apple in self.snake.body:
            self.apple=random.randint(1,8),random.randint(1,8)
        self.draw_apple()
        self.score +=1

    def print_score(self):
        return self.score
    
                

class Map:
    
    
    def __init__(self,size) -> None:
        self.map= []
        for i in range(size):
            row = []
            for j in range(size):
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    row.append("⬛")
                else:
                    row.append("⬜")
            self.map.append(row)
        
    def draw_map(self):
        for row in self.map:
            print(''.join(row))

snake = Snake()
a=None
while True:
    snake.draw_snake()
    snake.apple.draw_apple()
    snake.map.draw_map()
    if a:
        print('sadece w a s d argümanlrini alir')
        move=input(f'nereye gideceginizi secin    \nayrica skorunuz {snake.apple.print_score()}\n')
        a=False
    else:
        move=input(f'nereye gideceginizi secin    \nayrica skorunuz {snake.apple.print_score()}\n')
    if move=='q':
        break
    if len(move) !=1:
        a=True
        continue
        
    if not snake.move(move):
        print(f'skorunuz şudur {snake.apple.print_score()}')
        d=input('devam etmek istiyor musunuz eger istiyorsaniz r yazin \n')
        if d=='r':
            snake=Snake()
        else:
            print('tesekkürler')
            break
    
            
