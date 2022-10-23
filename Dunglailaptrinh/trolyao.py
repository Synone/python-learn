import speech_recognition
import pyttsx3
from datetime import date, datetime
robot_ear = speech_recognition.Recognizer()
robot_voice = pyttsx3.init()
robot_brain = ""

while True:
	with speech_recognition.Microphone() as mic:
		robot_ear.adjust_for_ambient_noise(mic) 
		print("Robot: I'm listening")
		audio = robot_ear.record(mic, duration=3)
	print ("Robot: ...")

	try:
		you = robot_ear.recognize_google(audio)
	except:
		you= ""

	print("You: " + you)


	if you == "":
		robot_brain = "I can't hear you, please try again"
	elif you == "hello":
		robot_brain = "Hello Sony"
	# VD thay: elif you = "today" bằng elif today in you.
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif you == "what can we do when everything is screwed up":
		robot_brain = "We just can try to be better"
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you:
		robot_brain = "Bye Sony"
		robot_voice.say(robot_brain)
		robot_voice.runAndWait()
		print("Robot: " + robot_brain)
		break
	else:
		robot_brain = "Stop asking nonsense questions"
	print("Robot: ...")
	print("Robot: " + robot_brain)
	robot_voice.say(robot_brain)
	robot_voice.runAndWait()

# để chương trình nghe được chữ trong câu, không cần đúng chính xác chữ đó
