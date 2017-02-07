from FeatureAdapterInterface import FeatureAdapterInterface
import sys
sys.path.insert(0, '../api/dto')
from api.dto.Suit import Suit

class SimplifyValueCard(FeatureAdapterInterface):
	"""Abstract class that contains the logic to convert the cards to values.
		Convert the cards not played yet into 4 options values.
	    4,5,6,7                -> 1
	    10,11,12,Anchos falsos -> 2
	    2,3                    -> 3
	    Los 7 y Anchos         -> 4
	"""
	def cardToFeature(self, card):
		if(card.value in [4,5,6] or (card.value == 7 and card.suit in [Suit.COUP, Suit.SWORD])):
			return [1]
		elif(card.value in [10,11,12] or (card.value == 1 and card.suit in [Suit.COUP, Suit.CLUB])):
			return [2]
		elif(card.value in [2,3]):
			return [3]
		else:
			return [4]
