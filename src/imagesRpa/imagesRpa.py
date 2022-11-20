from decouple import config
from datetime import datetime
from imagesRpa.util.utils import  escreveNaImagem, cliclaImagem, existe_janela, existeImagem, fechaTudo, fechar_janelas

USUARIO = config('USUARIO')
PROCESS = config('PROCESS')
data_atual = datetime.now()
class imagesRpa:
    
    def __init__(self):
        

        escreveNaImagem()

    def teste():

        escreveNaImagem()