from Bot import *
import numpy as np

class Bot2023826(Bot):
	def __init__(self, settings):
		super().__init__(settings)
		self.setName('Gijstronomisch')
		self.moves_made_down_right = 0
		self.moves_made_down_left = 0 
		self.height_difference_clean_stain = 0        
	
	    
	def nextMove(self, currentCell, currentEnergy, vision, remainingStainCells):
		if not any('@' in sublist for sublist in vision):
			if self.height_difference_clean_stain > 0:
				self.height_difference_clean_stain -= 1
				return UP
			elif self.height_difference_clean_stain < 0:
				self.height_difference_clean_stain += 1
				return DOWN
		    
			if currentCell[0] <= self.sizeStains:
				return DOWN
			elif currentCell[1] <= self.sizeStains + 1:
				return RIGHT            
		    
			if currentCell[0] == self.nrRows - 2 - self.sizeStains and currentCell[1] == self.sizeStains + 2:
				return RIGHT
			elif currentCell[0] == self.nrRows - 2 - self.sizeStains and currentCell[1] == self.nrCols - 2 - self.sizeStains:
				return LEFT
			 
			elif self.moves_made_down_left == 0:
				if currentCell[0]%2 == 0 and currentCell[1] != self.nrCols - 2 - self.sizeStains:
					return RIGHT
			if self.moves_made_down_right < 3:
				self.moves_made_down_right += 1
				if currentCell[0]%2 == 0 and currentCell[1] >= self.nrCols - 2 - self.sizeStains:
					return DOWN 
				elif currentCell[0]%2 == 1 and currentCell[1] >= self.nrCols - 2 - self.sizeStains:
					return DOWN
			elif currentCell[0]%2 == 1 and currentCell[1] != self.sizeStains + 2:
				return LEFT
			elif self.moves_made_down_left < 3:
				self.moves_made_down_left += 1
				if currentCell[0]%2 == 1 and currentCell[1] <= self.sizeStains + 2:
					return DOWN 
				elif currentCell[0]%2 == 0 and currentCell[1] <= self.sizeStains + 2:
					return DOWN
			elif self.moves_made_down_left == 3:
				self.moves_made_down_right -= 3
				self.moves_made_down_left -= 3
		else:
			self.moves_made_down_left -= self.moves_made_down_left
			self.moves_made_down_right -= self.moves_made_down_right
			if vision[2][2] == '@' and vision[2][1] == '@' and vision[2][0] != '@':
				self.height_difference_clean_stain += 1
				return DOWN
			elif vision[2][0] == '@' and ('@' not in vision[1] and '@' not in vision[0]):
				return LEFT
			elif vision[0][2] == '@' and vision[1][2] == '@' and vision[2][2] == '@':
				self.height_difference_clean_stain -= 1
				return UP
			elif vision[0][2] != '@' and vision[1][2] == '@' and vision[2][2] == '@':
				return RIGHT
			elif vision[2][1] == '@' and vision[1][0] != '@':
				self.height_difference_clean_stain += 1
				return DOWN
			elif vision[2][1] != '@' and vision[1][2] == '@':
				return RIGHT
			elif vision[2][1] != '@' and vision[1][2] != '@' and vision[0][1] == '@':
				self.height_difference_clean_stain -= 1
				return UP
			elif vision[0][1] != '@' and vision[1][0] == '@':
				return LEFT
			elif vision[0][2] == '@' and vision[0][1] != '@' and vision[0][0] != '@' and '@' not in vision[1] and '@' not in vision[2]:
				self.height_difference_clean_stain -= 1
				return UP
            
            

