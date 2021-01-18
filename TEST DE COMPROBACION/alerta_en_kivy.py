# importar módulo kivy
import kivy
kivy.require('1.9.0') #version requerida del kivy
# app: siempre se refiere a la instancia de su aplicación
from kivy.app import App
# El botón es una etiqueta con acciones asociadas que se activa cuando el botón Se presiona.
from kivy.uix.button import Button
# El GridLayout organiza a los cuadros en una matriz Toma el espacio disponible y
# lo divide en columnas y filas, luego agrega widgets a las "celdas" resultantes.
from kivy.uix.gridlayout import GridLayout
# El widget pupup se utiliza para crear ventanas emergentes.
# Por defecto, la ventana emergente cubrirá
# toda la ventana "principal".
# Al crear una ventana emergente,debe establecer al menos un Popup.title y Popup.content.
from kivy.uix.popup import Popup
# El widget label(etiqueta) es para renderizar texto.
from kivy.uix.label import Label

# Crea una aplicación derivando de la clase app proporcionada por kivy.
class Popup_ejemplo(App):
    # anula el método de compilación y devuelve el widget raíz de este App

    def build(self):
        # Defina un diseño de cuadrícula para esta aplicación
        self.layout = GridLayout(cols=1, padding=0)

        # Agregar un botón
        self.button = Button(text="CLICK PARA MOSTRAR ALARMA")
        self.layout.add_widget(self.button)

        # Adjuntar una devolución de llamada para el evento de pulsación de botón
        self.button.bind(on_press=self.onButtonPress)

        return self.layout

# ---Al presionar el botón: crea un cuadro de diálogo emergente con una etiqueta y un botón de cierre---

    def onButtonPress(self, button):

        layout = GridLayout(cols=1, padding=10)

        popupLabel = Label(text="ERROR EN EL SISTEMA 505")
        closeButton = Button(text="cerrar alarma")

        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)

        # Crear una instancia de la ventana emergente modal y mostrar
        popup = Popup(title='!!! ALERTA ¡¡¡',
                      content=layout,
                      size_hint=(None, None), size=(400, 200))
        popup.open()

        # Adjuntar presionar el botón de cierre con la acción popup.dismiss
        closeButton.bind(on_press=popup.dismiss)

    # Ejecuta la aplicación con el metodo.run
if __name__ == '__main__':
    Popup_ejemplo().run()