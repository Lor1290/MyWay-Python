from kivy.app import App as app
from kivy.uix.widget import Widget as widget

from kivy.properties import (
	NumericProperty, 
	ReferenceListProperty,
	ObjectProperty
)

from kivy.vector import Vector as vector
from kivy.clock import Clock as clock
from random import randint


class PongPaddle(widget):
	score = NumericProperty(0)
	
	def bounce(self, ball):
		if (self.y) == (ball.y + ball.height) or (self.y + self.height) == (ball.y):
			vy = ball.vel_y
			offset = (ball.center_y - self.center_y) / (self.height / 2)
			
			bounced = -1 * vy
			vel = bounced * 1.1
			ball.vel_y = vel
 
		if self.collide_widget(ball):
			vx, vy = ball.vel_tup
			offset = (ball.center_y - self.center_y) / (self.height / 2)
			bounced = vector(-1 * vx, vy)
			
			vel = bounced * 1.1
			ball.vel_tup = vel.x, vel.y + offset


class PongBall(widget):
	vel_x, vel_y = NumericProperty(5), NumericProperty(5)
	vel_tup = ReferenceListProperty(vel_x, vel_y)

	def move(self):
		self.pos = vector(*self.vel_tup) + self.pos


class PongGame(widget):
	ball = ObjectProperty(None)
	player1 = ObjectProperty(None)
	player2 = ObjectProperty(None)	
	
	def serve(self, vel=(4, 0)):
		self.ball.center = self.center
		self.ball.velocity = vel
		self.ball.vel_x, self.ball.vel_y = NumericProperty(5), NumericProperty(5)

	def update(self, dt):
		self.ball.move()
		
		self.player1.bounce(self.ball)
		self.player2.bounce(self.ball)


		if(self.ball.y < 0 or (self.ball.top > self.height)):
			self.ball.vel_y *= -1
		
		if self.ball.x < 0:
			self.player1.score += 1
			self.serve(vel=(4, 0))
		if self.ball.x > self.width:
			self.player2.score += 1
			self.serve(vel=(-4, 0)) 

	def on_touch_down(self, touch):
		if touch.x < self.width / 3:
			self.player1.center_y = touch.y
		if touch.x > (self.width- self.width/3):
			self.player2.center_y = touch.y




class PongApp(app):
	def build(self):
		game = PongGame()
		game.serve()

		clock.schedule_interval(game.update, 1.0/60.0)
		return game

if __name__ == '__main__':
	App = PongApp()
	App.run()	
