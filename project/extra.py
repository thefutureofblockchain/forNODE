import os,time
os.system('clear')
filenames = ["example.txt","exampl2.txt"]
def fireworks (filenames,delay=1,repeat=10):
    frames = []
    for name in filenames:
        with open(name,"r") as f:
            frames.append(f.readlines())
    for _ in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(delay)
            os.system('clear')
fireworks(filenames, delay=1, repeat=10)

