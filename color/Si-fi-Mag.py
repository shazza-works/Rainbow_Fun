
def nero_set():
	# Rainfade Provides a Smooth Transition In Between Each Set Of Color
	print " - Just Copy & Paste The Generated Messages - \n"
	colors = ["#ffff00","#e2571e","#ff7f00","#ffff00","#00ff00","#90bf33","#0000ff","#4b0082","#8b00ff"]
	s = 0
	new = ""
	msgb = ""
	while 1:
		msg = raw_input("Nero_Set: ").decode('utf8')
		if len(msg) >= 80:
			msgb = msg[80:]
			msg = msg[:80]
		msg = list(msg)
		for _ in msg:
			if s == len(colors):
				s = 0
			if _ == " ":
				new = new + " "
				s = s - 1
			else:
				new = new + colors[s].replace("#","[") + "]" + _
			s = s + 1
		print "[c][b]" + new + msgb + "\n"
		new = ""
		msgb = ""
		s = 0
nero_set()
