from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = 300, 500

class speeddial(MDApp):

	data = {
		'Python': "language-python",
		'Java': "language-java",
		'HTML5': "language-html5",
		'JavaScript': "language-javascript"
	}

	def build(self):
		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_pallete = 'BlueGray'

	def callback(self, instance):
		self.root.ids.mylabel.text = f'You Pressed {instance.icon}'

	def open(self):
		self.root.ids.mylabel.text = 'Aberto!!!'
	def close(self):
		self.root.ids.mylabel.text = 'Fechado!!!'

speeddial().run()