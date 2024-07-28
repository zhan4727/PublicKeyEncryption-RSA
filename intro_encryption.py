from manim import *
class IntroEncryption(Scene):
	def construct(self):
		rectangle = RoundedRectangle(stroke_width = 8, stroke_color = WHITE, 
		fill_color = BLUE_B, width = 3.8, height = 1.5).shift(UP*2+LEFT*4)
		rectangle2 = RoundedRectangle(stroke_width = 8, stroke_color = WHITE, 
		fill_color = BLUE_B, width = 3.8, height = 2).shift(DOWN*2)

		message = MathTex("\\text{Hello, Amy!}").set_color_by_gradient(GREEN, PINK).set_height(0.5)
		message.move_to(rectangle.get_center())

		ciphertext = MathTex(
			r"& \text{A345DFE510}\\",
			r"& \text{C6DB34F8E7}\\"
		).set_color_by_gradient(GREEN, PINK)
		ciphertext.move_to(rectangle2.get_center())
		
		rect1 = Rectangle(height = 1.15, width = 4).shift(LEFT*4)
		rect2 = Rectangle(height = 1.15, width = 1.8).shift(RIGHT*4)
		christina = MathTex("\\text{Christina}").set_color(GREEN).set_height(0.6).shift(LEFT*4)
		amy = MathTex("\\text{Amy}").set_color(PINK).set_height(0.6).shift(RIGHT*4)
		christina.move_to(rect1.get_center())
		amy.move_to(rect2.get_center())

		self.play(Create(rect1), Write(christina), Create(rect2), Write(amy))
		self.wait(1)
		self.play(FadeIn(rectangle), Write(message))
		#self.play(Write(message))
		self.wait(1)
		self.play(rectangle.animate.shift(RIGHT*8), message.animate.shift(RIGHT*8), run_time = 2)
		self.wait(5)
		self.play(FadeOut(rect1), FadeOut(christina), FadeOut(rect2), FadeOut(amy))
		self.play(rectangle.animate.shift(LEFT*4), message.animate.shift(LEFT*4), run_time = 1)
		self.wait(2)
		down_arrow = Arrow(start=UP, end=DOWN)
		down_arrow.set_stroke(width=5)
		self.play(FadeIn(down_arrow))
		self.play(FadeIn(rectangle2), Write(ciphertext))
		self.wait(4)
		up_arrow = Arrow(start = DOWN, end = UP)
		up_arrow.set_stroke(width=5)
		self.play(FadeOut(down_arrow))
		self.play(FadeIn(up_arrow))
		self.wait(5)
		self.play(FadeOut(rectangle), FadeOut(message), FadeOut(rectangle2), FadeOut(ciphertext), FadeOut(up_arrow))
		