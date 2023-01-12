import os, time

os.system('cls')

filenames = ["example.txt","exampl2.txt"]





def animator(filenames,delay = 1, repeat = 10):
    frames = []
    for name in filenames:
        with open (name,"r",encoding="utf8") as f:
		    frames.append(f.readlines())
	for i in range(repeat):
	    for frame in frames:
		    print("".join(frame))
	time.sleep(delay)
	os.system('clear')
animator(filenames,delay = 0.1,  repeat = 5)