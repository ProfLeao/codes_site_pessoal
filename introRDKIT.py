# Códigos do artigo: 
# Propriedades moleculares e formulas estruturais com RDKIT no Python

# Importndo o pacote Chem do RDKIT
from rdkit import Chem

# Declarando as moléculas
# Smile canônico para sacarose
sacarose =  Chem.MolFromSmiles("C(C1C(C(C(C(O1)OC2(C(C(C(O2)CO)O)O)CO)O)O)O)O")
# Smile canônico para clorato de potassio
clorato_potassio = Chem.MolFromSmiles("[O-]Cl(=O)=O.[K+]")

# Importando a função para extração do peso molecular
from rdkit.Chem.Descriptors import MolWt
print(f"Peso molecular da sacarose: {MolWt(sacarose)}")
print(f"Peso molecular do clorato de potássio: {MolWt(clorato_potassio)}")

# Importando o módulo Draw
from rdkit.Chem import Draw

Draw.MolToFile(sacarose, "sacarose.png")
Draw.MolToFile(clorato_potassio, "cloratodepotassio.png")