from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

# Cores personalizadas
COR_FUNDO = (94/255, 5/255, 30/255, 1)    # Vinho escuro
COR_TEXTO = (212/255, 6/255, 75/255, 1)   # Rosa vibrante
COR_BOTAO = (1, 1, 1, 1)                  # Branco

class IdadeApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        # Fundo colorido
        with layout.canvas.before:
            Color(*COR_FUNDO)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        
        # Atualizar fundo ao redimensionar
        layout.bind(size=self.atualizar_fundo, pos=self.atualizar_fundo)
        
        # Título
        titulo = Label(text="Verificador de Idade", font_size=24, bold=True, color=COR_TEXTO)
        layout.add_widget(titulo)
        
        # Campo de nome
        self.campo_nome = TextInput(
            hint_text="Digite seu nome", 
            size_hint=(1, None), 
            height=50,
            foreground_color=COR_TEXTO, 
            background_color=(1, 1, 1, 0.9)
        )
        layout.add_widget(self.campo_nome)
        
        # Campo de idade
        self.campo_idade = TextInput(
            hint_text="Digite sua idade", 
            size_hint=(1, None), 
            height=50,
            input_filter="int",
            foreground_color=COR_TEXTO, 
            background_color=(1, 1, 1, 0.9)
        )
        layout.add_widget(self.campo_idade)
        
        # Botão de verificação (AGORA BRANCO)
        botao = Button(
            text="Verificar Idade", 
            size_hint=(1, None), 
            height=50,
            background_color=COR_BOTAO,  # Botão branco
            color=COR_FUNDO,             # Texto do botão na cor de fundo
            bold=True
        )
        botao.bind(on_press=self.verificar_idade)
        layout.add_widget(botao)
        
        # Resultado
        self.label_resultado = Label(text="Preencha seus dados acima", color=COR_TEXTO, font_size=20)
        layout.add_widget(self.label_resultado)
        
        return layout

    def atualizar_fundo(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def verificar_idade(self, instance):
        nome = self.campo_nome.text.strip()
        idade_txt = self.campo_idade.text.strip()
        
        if not nome:
            self.label_resultado.text = "Digite seu nome!"
            return
        
        if not idade_txt:
            self.label_resultado.text = "Digite uma idade válida!"
            return
        
        idade = int(idade_txt)
        
        if idade < 18:
            self.label_resultado.text = f"Olá, {nome}! Você ainda é de menor então não ta podendo."
        elif idade < 60:
            self.label_resultado.text = f"Olá, {nome}! Você já é de maior então já ta podendo."
        else:
            self.label_resultado.text = f"Olá, {nome}! ta ficando velho em irmão ta precisando tomar omega três 😁👍."

if __name__ == '__main__':
    IdadeApp().run()