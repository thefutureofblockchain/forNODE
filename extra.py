import time
while time.sleep == 0.1:
  tput cup $((RANDOM%LINES)) $((RANDOM%COLUMNS))
  print("*")
