# Final Project Milestone #2

[Final Project Description](https://docs.google.com/document/d/1j3zgypVjPjzXl4pL1_Wpjvp3GLCW9zcFydkwUjNfNUA/edit?usp=sharing)

Complete this document in **your** portfolio (CH 6). 

Let's decide on our Final project. Select the idea from Milestone 1 that seems the most interesting to you.

Each class is a model of some real world object. We often refer to data classes as the ***models*** in a GUI program. Your models represent your application data.

Given what you have learned about classes on Chapter 6, describe the ***interface only*** of 3 classes you think you might need for your project.

*For example*, if you want to create a space invaders type game, you would need a class to represent the ship, which could have an interface such as: 

* class ship
    * moveLeft()
    * moveRight()
    * shoot()

***

Come up with interfaces fot 3 possible classes you think you may need. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1

class Player: 
  def __init__(self , player_num = 1):
    self.player_num = player_num
    self.lives = 3
    self.movement = keyboard 

## Class Interface 2

class Enemy: 
  def __init__(self):
    self.hits_to_kill = 1 
    self.postion = random 
    self.alive = True

## Class Interface 3

class Background:
  def __init__(self):
    self.grass = []
    self.color = 'green'
    self.treats = []