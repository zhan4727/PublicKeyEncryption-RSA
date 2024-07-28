from manim import *
class ConcludeEncryption(Scene):
	def construct(self):
		# Summarize video
		list = MathTex(
			r"& \text{1. Public-key encryption}\\",
			r"& \quad\quad -\text{public key for encryption}\\",
			r"& \quad\quad -\text{private key for decryption}\\",
			r"&\\",
			r"& \text{2. The RSA Algorithm}\\",
			r"& \quad \quad -\text{a public-key cryptosystem}"
		).shift(UP*1)
		self.play(Write(list[0]))
		self.play(Write(list[4]))
		self.wait(1)
		self.play(Write(list[1]))
		self.play(Write(list[2]), Write(list[3]))
		self.wait(2)
		self.play(Write(list[5]))
		self.wait(1)
		self.play(FadeOut(list))		

		# Replay part of the intro animation
		rectangle = RoundedRectangle(stroke_width = 8, stroke_color = WHITE, 
		fill_color = BLUE_B, width = 3.8, height = 1.5).shift(UP*2+LEFT*4)

		message = MathTex("\\text{Hello, Amy!}").set_color_by_gradient(GREEN, PINK).set_height(0.5)
		message.move_to(rectangle.get_center())
		
		rect1 = Rectangle(height = 1.15, width = 4).shift(LEFT*4)
		rect2 = Rectangle(height = 1.15, width = 1.8).shift(RIGHT*4)
		christina = MathTex("\\text{Christina}").set_color(GREEN).set_height(0.6).shift(LEFT*4)
		amy = MathTex("\\text{Amy}").set_color(PINK).set_height(0.6).shift(RIGHT*4)
		christina.move_to(rect1.get_center())
		amy.move_to(rect2.get_center())

		self.play(Create(rect1), Write(christina), Create(rect2), Write(amy))
		self.wait(1)
		self.play(FadeIn(rectangle), Write(message))
		self.wait(1)
		self.play(rectangle.animate.shift(RIGHT*8), message.animate.shift(RIGHT*8), run_time = 2)
		self.wait(3)
		self.play(FadeOut(rectangle), FadeOut(message), FadeOut(christina), FadeOut(amy), FadeOut(rect1), FadeOut(rect2))
		self.wait(1)