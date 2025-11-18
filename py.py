import sys, os

# Caminho da pasta raiz (um nível acima de /sandbox)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT)

import numpy as np
from projeto.CB2325NumericaG4.integracao import integral_simpson, plot_integral_simpson
from projeto.CB2325NumericaG4.aproximacao import plot_regressao

print(integral_simpson(np.sin, 3, 6))
plot_integral_simpson(np.sin, 3, 6)
pontos = [(1, 2), (2, -2), (3, 5), (4, 7)]
plot_regressao(pontos=pontos, grau=2)
