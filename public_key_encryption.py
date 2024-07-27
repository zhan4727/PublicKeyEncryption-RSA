from manim import *

class PublicKeyEncryption(Scene):
	def construct(self):
		mathtext1 = MathTex("\\text{Public-key Encryption}").shift(UP*3)
		msg = MathTex("\\text{Message}").shift(LEFT*5, DOWN * 0.25)
		encrmsg = MathTex("\\text{Ciphertext}").shift(RIGHT*4.5, DOWN * 0.25)
		silvermsg = MathTex("\\text{Alice's public key}").shift(DOWN * 2)
		goldmsg = MathTex("\\text{Alice's private key}").shift(DOWN * 2)
		bob = MathTex("\\text{Bob}").set_color(BLUE).shift(UP*2.5)
		alice = MathTex("\\text{Alice}").set_color(RED).shift(UP*2.5)
		msg.scale(1.25)
		encrmsg.scale(1.25)
		silvermsg.scale(1.3)
		goldmsg.scale(1.3)
		bob.scale(2)
		alice.scale(2)
		mathtextlistkeys = MathTex(
			r"& \text{1. Public key}\\",
			r"& \boxed{\text{Hello}}\ \Longrightarrow \ \boxed{\text{A7CEF687D5}}\\",
			r"& \\",
			r"& \text{2. Private key}\\",
			r"& \boxed{\text{A7CEF687D5}} \ \Longrightarrow \ \boxed{\text{Hello}}"
		)
		# mathtextlistkeys.shift(DOWN*1)
		# Create the key shape using VMobject
		private_key = VMobject()
		public_key = VMobject()
		private_key.set_points_as_corners([
			[-1.5, 0, 0], [2.5, 0, 0], [2.5, -0.5, 0], [2, -0.5, 0], [2, -1, 0],
			[1.5, -1, 0], [1.5, -0.5, 0], [1, -0.5, 0], [1, -1, 0], [0.5, -1, 0],
			[0.5, -0.5, 0], [-1.5, -0.5, 0], [-1.5, 0, 0]
		])
		public_key.set_points_as_corners([
			[-1.5, 0, 0], [2.5, 0, 0], [2.5, -0.5, 0], [2, -0.5, 0], [2, -1, 0],
			[1.5, -1, 0], [1.5, -0.5, 0], [1, -0.5, 0], [1, -1, 0], [0.5, -1, 0],
			[0.5, -0.5, 0], [-1.5, -0.5, 0], [-1.5, 0, 0]
		])
		#	[-1, 0, 0], [3, 0, 0], [3, -0.5, 0], [2.5, -0.5, 0], [2.5, -1, 0],
		#	[2, -1, 0], [2, -0.5, 0], [1.5, -0.5, 0], [1.5, -1, 0], [1, -1, 0],
		#	[1, -0.5, 0], [-1, -0.5, 0], [-1, 0, 0]
		#])
		# Create golden color gradient - private key
		golden_color = ["#FFD700", "#FFC700", "#FFB700", "#FFA700", "#FF9700"]

		# Create silver color gradient - public key
		silver_color = ["#C0C0C0", "#B0B0B0", "#A0A0A0", "#909090", "#808080"]

		private_key.set_color_by_gradient(*golden_color)
		private_key.set_fill(opacity=1)
		private_key.set_stroke(width=4, color=YELLOW)

		public_key.set_color_by_gradient(*silver_color)
		public_key.set_fill(opacity=1)
		public_key.set_stroke(width=4, color=BLUE)

		# Create the private key ring
		private_ring = Annulus(inner_radius=0.7, outer_radius=1.0, color=YELLOW, stroke_width=8)
		private_ring.set_color_by_gradient(*golden_color)
		private_ring.set_fill(opacity=1)
		private_ring.set_stroke(width=8, color=YELLOW)

		# Put the ring in the correct relative position
		private_ring.shift(LEFT * 2.25 + DOWN * 0.25)

		# Create the public key ring
		public_ring = Annulus(inner_radius=0.7, outer_radius=1.0, color=YELLOW, stroke_width=8)
		public_ring.set_color_by_gradient(*silver_color)
		public_ring.set_fill(opacity=1)
		public_ring.set_stroke(width=8, color=BLUE)

		# Put the ring in the correct relative position
		#public_ring.shift(LEFT * 1.75 + DOWN * 0.25)
		public_ring.shift(LEFT * 2.25 + DOWN * 0.25)
		
		# Intro to Public-key encryption	

		self.play(Write(mathtext1))
		self.wait(3)
		self.play(Write(mathtextlistkeys[0]))
		self.wait(1)
		self.play(Write(mathtextlistkeys[3]))
		self.wait(3)
		self.play(Write(mathtextlistkeys[1]))
		self.wait(2)
		self.play(Write(mathtextlistkeys[2]))
		self.wait(1)
		self.play(Write(mathtextlistkeys[4]))
		self.wait(3)
		#self.clear()
		self.play(FadeOut(mathtext1), FadeOut(mathtextlistkeys)) # Fade out all objects

		# Bob and Alice Example
		silvermsg.set_color_by_gradient(*silver_color)
		goldmsg.set_color_by_gradient(*golden_color)

		# Show the public key
		self.play(Write(bob), Write(msg), Write(public_key), Write(public_ring), Write(encrmsg), Write(silvermsg))
		self.wait(4)
		
		self.play(FadeOut(public_key), FadeOut(public_ring), FadeOut(bob), FadeOut(msg), FadeOut(encrmsg), FadeOut(silvermsg))
		self.wait(1)

		# Show the private key
		msg = MathTex("\\text{Message}").shift(RIGHT*4.5, DOWN * 0.25)
		encrmsg = MathTex("\\text{Ciphertext}").shift(LEFT*5, DOWN * 0.25)
		msg.scale(1.25)
		encrmsg.scale(1.25)
		self.play(Write(alice), Write(encrmsg), Write(private_key), Write(private_ring), Write(msg), Write(goldmsg))
		self.wait(4)

		self.play(FadeOut(alice), FadeOut(encrmsg), FadeOut(private_key), FadeOut(private_ring), FadeOut(msg), FadeOut(goldmsg))
		self.wait(1)

		self.wait(2)
