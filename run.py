from engine2 import Engine
from distributions.circle import Circle
from distributions.gaussian import Gaussian
from distributions.rectangle import Rectangle
import pandas as pd
import numpy as np

Engine1 = Engine(300, Circle(50))
#lengths, angles, points, throws = Engine1.loadWriteGames()
Engine1.loadWriteGames()
#Circle100 = pd.DataFrame({'lengths':lengths, 'angles':angles, 'points':points, 'throws':throws})
#Circle100.to_csv('Circle50.csv')

# Engine2 = Engine(100, 300, Circle(50))
# lengths, angles, points, throws = Engine2.run()
# Circle50 = pd.DataFrame({'lengths':lengths, 'angles':angles, 'points':points, 'throws':throws})
# Circle50.to_csv('Circle50.csv')
#
# Engine3 = Engine(100, 300, Rectangle(125, 20, 10))
# lengths, angles, points, throws = Engine3.run()
# Rectangle = pd.DataFrame({'lengths':lengths, 'angles':angles, 'points':points, 'throws':throws})
# Rectangle.to_csv('Rectangle.csv')
#
# Engine4 = Engine(100, 300, Gaussian(100))
# lengths, angles, points, throws = Engine4.run()
# Gauss = pd.DataFrame({'lengths':lengths, 'angles':angles, 'points':points, 'throws':throws})
# Gauss.to_csv('Gauss.csv')
