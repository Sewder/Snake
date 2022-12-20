import random


class Snake:
    
    def __init__(self) -> None:
        self.body=[[1,2],[1,1]]
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
                
       
        
        nexthead = [self.body[0][0] + dx, self.body[0][1] + dy]
        
        if self.check_collided(nexthead):
            print("game over")
            return False
        if nexthead in [[x,y] for x,y,_ in self.apple.apple]:
            if nexthead==self.apple.apple[0][:2]:
                self.body.append(self.body[-1])
            else:
                self.map.map[self.body[-1][0]][self.body[-1][1]] = '⬜'
                if len(self.body) > 2:
                    self.map.map[self.body[-2][0]][self.body[-2][1]] = '⬜'
                    self.body = self.body[:-1]
                    
        else:
            self.map.map[self.body[-1][0]][self.body[-1][1]] = '⬜'
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i-1]
        self.body[0]=nexthead    
        if nexthead in [[x,y] for x,y,_ in self.apple.apple]:
            if nexthead==self.apple.apple[0][:2]:
                self.apple.recreate_apple('red')
            else:
                self.apple.recreate_apple('other')
        return True
    
    def check_collided(self,body_part):
        return body_part in self.body or body_part[0] in [0, 9] or body_part[1] in [0, 9]
        
        
class Apple:
    apple_types = ['🍏', '🍐']
    def __init__(self,snake:Snake) -> None:
        self.apple=[[random.randint(2,5),random.randint(1,8),'🍎'],[random.randint(6,8),random.randint(1,8),random.choice(self.apple_types)]]
        self.snake = snake
        self.score = 0
        
    def draw_apple(self):
        for apple in self.apple:
            self.snake.map.map[apple[0]][apple[1]] = apple[2]
            
    
    def recreate_apple(self,red):
        if red=='red':
            self.snake.map.map[self.apple[0][0]][self.apple[0][1]] = '⬜'
            self.apple[0]=[random.randint(1,8),random.randint(1,8),'🍎']
            while self.apple[0][:2] in self.snake.body or self.apple[0][:2] == self.apple[1][:2]:
                self.apple[0] = [random.randint(1, 8), random.randint(1, 8), '🍎']
            self.score +=1
        else:
            self.snake.map.map[self.apple[0][0]][self.apple[0][1]] = '⬜'
            self.apple[1] = [random.randint(1, 8), random.randint(1, 8), random.choice(self.apple_types)]
            while (self.apple[1][:2] in self.snake.body) or (self.apple[1][:2] == self.apple[0][:2]):
                self.apple[1] = [random.randint(1, 8), random.randint(1, 8), random.choice(self.apple_types)]

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
        rows = [''.join(row) for row in self.map]
        print('\n'.join(rows))

snake = Snake()
wrong_direction=None
while True:
    snake.draw_snake()
    snake.apple.draw_apple()
    snake.map.draw_map()
    if wrong_direction:
        print('sadece w a s d argümanlrini alir')
        move=input(f'nereye gideceginizi secin    \nayrica skorunuz {snake.apple.print_score()}\n')
        wrong_direction=False
    else:
        move=input(f'nereye gideceginizi secin    \nayrica skorunuz {snake.apple.print_score()}\n')
    if move=='q':
        break
    if not move in ['w','a','s','d'] :
        wrong_direction=True
        continue
        
    if not snake.move(move):
        print(f'skorunuz şudur {snake.apple.print_score()}')
        d=input('devam etmek istiyor musunuz eger istiyorsaniz r yazin \n')
        if d=='r':
            snake=Snake()
        else:
            print('tesekkürler')
            break
    
            
