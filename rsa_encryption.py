from manim import *
class RSAEncryption(Scene):
	def construct(self):
		# Display title
		title = MathTex("\\text{The RSA Algorithm}").shift(UP*3)
		self.play(Write(title))
		self.wait(3)
		basic_info = MathTex(
			r"& \text{Find very large positive integers }e,d,n\text{ s.t.}\\",
			r"& (m^e)^d \equiv m \pmod{n}, \ \text{where }0 \leq m < n"
		).shift(UP*1)
		description = MathTex(
			r"& \text{Public key: }(e,n)\\",
			r"& \text{Private key: }d\\",
			r"& \text{Message: }m"
		).shift(DOWN*1.5)
		description2 = MathTex(
			r"& \text{Encryption: } m^e \bmod{n} = c\\",
			r"&\\",
			r"& \text{Decryption: } c^d \bmod{n} = (m^e)^d \bmod{n} = m"
		).shift(DOWN*1.5)

		# Display public key, private key, message
		self.play(Write(basic_info), run_time = 4)
		self.wait(12)
		self.play(Write(description[0]))
		self.wait(1)
		self.play(Write(description[1]))
		self.wait(1)
		self.play(Write(description[2]))
		self.wait(2)
		self.play(FadeOut(description))
		self.wait(1)

		# Display encryption, description
		self.play(Write(description2[0]), Write(description2[1]))
		self.wait(3)
		self.play(Write(description2[2]))
		self.wait(3)
		self.play(FadeOut(basic_info), FadeOut(description2), FadeOut(title))
		#self.play(FadeOut(title))

		# Explain key generation
		section = MathTex("\\text{Key generation}").shift(UP*3)
		steps = MathTex(
			r"& \text{1. Choose 2 large prime numbers }p \text{ and } q\\",
			r"& \quad \quad n=pq\\",
			r"& \text{2. Compute }\lambda(n)=\text{lcm}(p-1,q-1)\\",
			r"& \text{3. Choose }e\text{ s.t. }1<e<\lambda(n),\ \gcd(e,\lambda(n))=1\\",
			r"& \text{4. Find }d\text{ by solving }de\equiv 1 \pmod{\lambda(n)}"
		)
		self.play(Write(section))
		self.wait(1)
		self.play(Write(steps[0]))
		self.play(Write(steps[1]))
		self.wait(2)
		self.play(Write(steps[2]))
		self.wait(8)
		self.play(Write(steps[3]))
		self.wait(5)
		self.play(Write(steps[4]))
		self.wait(8)
		self.play(FadeOut(steps), FadeOut(section))
		self.wait(1)
		start_proof = MathTex("\\text{Proof of Correctness}").scale(1.5)
		self.play(Write(start_proof))
		self.wait(2)
		self.play(FadeOut(start_proof))

		# Show proof of correctness
		theorem = MathTex("(m^e)^d \equiv m \pmod{pq}").shift(UP*3)
		arrow = MathTex("\Longleftrightarrow").shift(UP*3)
		equiv = MathTex(
			r"& (m^e)^d \equiv m \pmod{p}\\",
			r"& (m^e)^d \equiv m \pmod{q}"
		).shift(UP*3, RIGHT*3)
		self.play(Write(theorem))
		self.wait(4)
		self.play(theorem.animate.shift(LEFT * 3))
		self.play(Write(arrow), Write(equiv))
		self.wait(5)
		proof1 = MathTex(
			r"& \text{1. }ed\equiv 1 \pmod{\text{lcm}(p-1,q-1)}\\",
			r"& \Longrightarrow ed - 1 = k_1(p-1)=k_2(q-1)\text{ for some }k_1,k_2\in\mathbb{Z}\\",
			r"& \text{2. }m\equiv 0 \pmod{p} \Longrightarrow (m^e)^d \equiv (0^e)^d \equiv 0 \pmod{p}\\",
			r"& \\",
			r"& \quad m\not\equiv 0 \pmod{p} \Longrightarrow \gcd(m,p)=1\\",
			r"& \quad \text{Use Fermat's Little Theorem: }m^{p-1} \equiv 1 \pmod{p}"
		).shift(DOWN*0.5)
		self.play(Write(proof1[0]), run_time = 3)
		self.play(Write(proof1[1]), run_time = 3)
		self.wait(4)
		self.play(Write(proof1[2]), run_time = 4)
		self.play(Write(proof1[3]))
		self.play(Write(proof1[4]), run_time = 2.5)
		self.play(Write(proof1[5]), run_time = 2.5)
		self.wait(2)
		self.play(FadeOut(proof1))
		#last_line = MathTex("\quad (m^{e})^d \equiv m^{ed} \equiv m^{ed-1}m").shift(UP*1.5, LEFT * 1)
		last_bunch = MathTex(
			r"(m^{e})^d \equiv m^{ed} & \equiv m^{ed-1}m\\",
			r"& \equiv m^{k_1(p-1)}m\\",
			r"& \equiv (m^{p-1})^{k_1}m\\",
			r"& \equiv 1^{k_1}m\\",
			r"& \equiv m \pmod{p}"
		).shift(DOWN * 0.5)
		proof2 = MathTex(
			r"& \text{3. }m\equiv 0 \pmod{q} \Longrightarrow (m^e)^d \equiv (0^e)^d \equiv 0 \pmod{q}\\",
			r"& \\",
			r"& \quad m\not\equiv 0 \pmod{q} \Longrightarrow \gcd(m,q)=1\\",
			r"& \quad \text{Use Fermat's Little Theorem: }m^{q-1} \equiv 1 \pmod{q}\\",
		).shift(DOWN*0.5)
		last_bunch2 = MathTex(
			r"(m^{e})^d \equiv m^{ed} &\equiv m^{ed-1}m\\",
			r"& \equiv m^{k_2(q-1)}m\\",
			r"& \equiv (m^{q-1})^{k_2}m\\",
			r"& \equiv 1^{k_2}m\\",
			r"& \equiv m \pmod{q}"
		).shift(DOWN*0.5)
		#self.play(Write(last_line))	
		#self.wait(1)
		self.play(Write(last_bunch[0]))
		self.play(Write(last_bunch[1]))
		self.play(Write(last_bunch[2]))
		self.play(Write(last_bunch[3]))
		self.play(Write(last_bunch[4]))
		self.wait(2)
		self.play(FadeOut(last_bunch))
		self.play(Write(proof2[0]))
		self.play(Write(proof2[1]))
		self.play(Write(proof2[2]))
		self.play(Write(proof2[3]))
		self.wait(3)
		self.play(FadeOut(proof2))
		self.play(Write(last_bunch2[0]))
		self.play(Write(last_bunch2[1]))
		self.play(Write(last_bunch2[2]))
		self.play(Write(last_bunch2[3]))
		self.play(Write(last_bunch2[4]))
		self.wait(3)
		self.play(FadeOut(last_bunch2), FadeOut(theorem), FadeOut(arrow), FadeOut(equiv))
		self.wait(1)
		