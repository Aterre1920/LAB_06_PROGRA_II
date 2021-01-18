from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '300')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from random import randrange
from kivy.clock import Clock

class Wid_Alfa(GridLayout):
    None
	
class GridRed(GridLayout):
	None

class GridBlue(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cont = 6
        self.racha = 0
        
    def Go(self):
        self.ids.pantalla5.text = str(0)
        Clock.schedule_interval(self.Contador, 1)

    def comparar_suma(self):
        suma = int(self.ids.pantalla2.text) + int(self.ids.pantalla3.text)
        if suma==int(self.ids.respuesta.text):
            self.racha = int(self.ids.pantalla5.text)
            self.ids.pantalla5.text = str(self.racha + 1)
            self.cont = 6
        if suma != int(self.ids.respuesta.text):
            self.cont=6
            self.racha=0
            self.ids.pantalla5.text = str(0)
        self.ids.respuesta.text=''
        
    def Contador(self,t):
        self.cont -= 1
        self.ids.pantalla4.text = 'Tiempo Restante: ' + str(self.cont)
        if self.cont == 0:
            self.cont=6
            self.racha=0
            self.ids.pantalla5.text = str(0)
        if self.cont==5:
            self.ids.pantalla2.text = str(randrange(10))
            self.ids.pantalla3.text = str(randrange(10))


class MainApp(App):
	def build(self):
		return Wid_Alfa()
		
if __name__ == '__main__':
	MainApp().run() 
