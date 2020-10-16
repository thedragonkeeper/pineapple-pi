import inkyphat
from datetime import datetime
from PIL import Image, ImageFont, ImageDraw

class Notify(object):
	def __init__(self):
		inkyphat.set_colour('black')
		self.font = inkyphat.ImageFont.truetype(inkyphat.fonts.DejaVuSans,10)
		self.drawQ = []
		self.onlinetext = "\u2717"
		self.ip = "xxx.xxx.xxx.xxx"
		self.time = datetime.now()
		self.interface = ''

	def draw_text(self, position, text):
		x, y = position
		x = x+5
		w, h = self.font.getsize(text)
		mask = inkyphat.Image.new('1', (w, h))
		draw = inkyphat.ImageDraw.Draw(mask)
		draw.text((0, 0), text, 1, self.font)
		position = x,y
		inkyphat.paste(inkyphat.BLACK, position, mask)

	def draw_img(self, img):
		inkyphat.paste(inkyphat.Image.new('P', (inkyphat.WIDTH, inkyphat.HEIGHT)))
		img = Image.open(img)
		inkyphat.set_image(img)
		inkyphat.show()

	def draw_gui(self, title, text):
		try:
			inkyphat.paste(inkyphat.Image.new('P', (inkyphat.WIDTH, inkyphat.HEIGHT)))
			self.draw_text((0,0), str(title))
			self.draw_text((0,5), str("________________________________________"))
			self.draw_text((0,20), str(text[0]))
			self.draw_text((0,30), str(text[1]))
			self.draw_text((0,40), str(text[2]))
			self.draw_text((0,50), str(text[3]))
			self.draw_text((0,60), str(text[4]))
			self.draw_text((0,75), str("________________________________________"))
			bottombarlen = len("IP: "+self.ip+"  Online: "+self.onlinetext)
			dt_string = self.time.strftime("%d/%m %H:%M:%S")
			dtlen = len(dt_string)
			self.draw_text((0,90), "IP: "+self.ip+"  Online: "+self.onlinetext+""*int(40-bottombarlen-dtlen)+dt_string)
		except IndexError:
			pass
		inkyphat.show()

	def do_update(self):
		self.time = datetime.now()
		if len(self.drawQ) > 0:
			if self.drawQ[0][0] == "img":
				self.draw_img(self.drawQ[0][1])
			else:
				self.draw_gui(self.drawQ[0][0], self.drawQ[0][1])
			self.drawQ.pop(0)
