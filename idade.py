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
        
        # Botão de verificação
        botao = Button(
            text="Verificar Idade", 
            size_hint=(1, None), 
            height=50,
            background_color=COR_BOTAO,
            background_normal='',  # Remove o estilo padrão para garantir a cor branca
            color=COR_FUNDO,
            bold=True
        )
        botao.bind(on_press=self.verificar_idade)
        layout.add_widget(botao)
        
        # Label para mensagens de erro (inicialmente vazia)
        self.label_erro = Label(text="", color=(1, 1, 1, 1), font_size=16)  # Branco
        layout.add_widget(self.label_erro)
        
        # Resultado
        self.label_resultado = Label(text="", color=COR_TEXTO, font_size=20)
        layout.add_widget(self.label_resultado)
        
        return layout

    def atualizar_fundo(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def verificar_idade(self, instance):
        # Limpa mensagens anteriores
        self.label_erro.text = ""
        self.label_resultado.text = ""
        
        nome = self.campo_nome.text.strip()
        idade_txt = self.campo_idade.text.strip()
        
        # Validação do nome
        if not nome:
            self.label_erro.text = "Por favor, digite seu nome."
            return
            
        # Verifica se o nome contém apenas números
        if nome.isdigit():
            self.label_erro.text = "Por favor, digite um nome válido (não apenas números)."
            return
            
        # Validação da idade
        if not idade_txt:
            self.label_erro.text = "Por favor, digite sua idade."
            return
            
        try:
            idade = int(idade_txt)
        except ValueError:
            self.label_erro.text = "Por favor, digite uma idade válida (apenas números)."
            return
            
        # Verifica se a idade é um valor razoável
        if idade < 0 or idade > 120:
            self.label_erro.text = "Por favor, digite uma idade entre 0 e 120 anos."
            return
        
        # Exibe o resultado baseado na idade
        if idade < 18:
            self.label_resultado.text = f"Olá, {nome}! Você é menor de idade."
        elif idade < 60:
            self.label_resultado.text = f"Olá, {nome}! Você é maior de idade."
        else:
            self.label_resultado.text = f"Olá, {nome}! Você já é uma pessoa de idade é merece muito respeito ❤️."

if __name__ == '__main__':
    IdadeApp().run()
