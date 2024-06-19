import pygame
import sys
import random



pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Sim")

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

class Ball:
	def __init__(self, x, y, radius, colour, dx, dy):
		self.x = x
		self.y = y
		self.radius = radius
		self.colour = colour
		self.dx = dx  # Horizontal velocity
		self.dy = dy  # Vertical velocity

	def draw(self,screen):
		pygame.draw.circle(screen, self.colour, (self.x,self.y), self.radius)

	def move(self):
		self.y += self.dy
		self.x += self.dx
  
		if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
			self.dx = -self.dx
		elif self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
			self.dy = -self.dy

	def checkCollision(self,other):
		if self.x == other.x and self.y == other.y:
			pass # TO DO: NEED TO FIGURE OUT HOW TO CALCULATE THE DIRECTION IT WAS ORIGINALLY HEADING IN. 


def main():
	ballOne = Ball(30,29, 20, red, -5,5)
	ballTwo = Ball(202, 222, 20, green, 5,-5)

	clock = pygame.time.Clock()
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		
		ballOne.move()
		ballTwo.move()
		
		ballOne.checkCollision(ballTwo)
		
		screen.fill(white)
		
		ballOne.draw(screen)
		ballTwo.draw(screen)
		
		pygame.display.flip()
		clock.tick(100)
		
	pygame.quit()
	sys.exit()


def experimental():
	balls = []

	for i in range (1,10):
		ball = Ball(random.randint(0,400),random.randint(0,400), 20, red, -5,5)
		balls.append(ball)
		
	clock = pygame.time.Clock()
	running = True
 
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		
		for ball in balls:
			ball.move()

		for Balli in balls:
			for Ballj in balls: 
				Balli.checkCollision(Ballj)
		
		screen.fill(white)
		
		for ball in balls:
			ball.draw(screen)
		
		pygame.display.flip()
		clock.tick(100)
		
	pygame.quit()
	sys.exit()
 
experimental()