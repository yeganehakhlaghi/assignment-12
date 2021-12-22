import random
import arcade
import time
import math

SCREEN_WIDTH=800
SCREEN_HEIGHT=600

class StarShip(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.center_x=SCREEN_WIDTH//2
        self.center_y=32
        self.width = 48
        self.height = 48
        self.angle = 0
        self.change_angle = 0
        self.speed= 4
        self.bullet_list = []
        self.score = 3
        #self.image_S=arcade.load_texture(":resources:images/backgrounds/stars.png")

    
    def fire(self):
        self.bullet_list.append(Bullet(self))
        
    def rotate(self):
        self.angle += self.speed * self.change_angle


class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x=random.randint(0,SCREEN_WIDTH)
        self.center_y=SCREEN_HEIGHT + 24
        self.width = 48
        self.height = 48
        #self.change_y = 0
        self.speed= 3
        #self.angle = 0
        #self.change_angle = 0
        
        #self.bullet_list = []
        #self.score = 3
        
    def move(self):
        self.center_y -= self.speed 


class Bullet(arcade.Sprite):
    def __init__(self,host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.speed = 6
        self.angle = host.angle
        self.center_x= host.center_x
        self.center_y=host.center_y

    def move(self):
        a= math.radians(self.angle)
        self.center_x -= self.speed * math.sin(a)
        self.center_y += self.speed * math.cos(a)


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,"🚀")
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image=arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = StarShip()
        self.enemy_list = []
        self.start_time = time.time()




    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background_image)
        self.me.draw()
        for enemy in self.enemy_list:
            enemy.draw()

        for bullet in self.me.bullet_list:
            bullet.draw()


    def on_update(self, delta_time: float):
        self.end_time = time.time()

        if self.end_time - self.start_time > 3:
            self.enemy_list.append(Enemy())
            self.start_time=time.time()

        self.me.rotate()
        for enemy in self.enemy_list:
            enemy.move()

        for bullet in self.me.bullet_list:
            bullet.move()




    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.SPACE:
            self.me.fire()
        elif symbol == arcade.key.RIGHT:
            self.me.change_angle=-1
        elif symbol == arcade.key.LEFT:
            self.me.change_angle=+1
game=Game()
arcade.run()