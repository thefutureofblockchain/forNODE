import os
import time
from rich import print
os.system('ls')
for _ in range(5):
    print(  " [yellow]                               .''.")
    print(" [yellow] .''.      .        *''*    :_\/_:     .")
    print("[yellow]  :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.")
    print("[yello].''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=::=-")
    print("[yellow]:_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'")
    print("[yellow]: /\ : :::::     *_\/_*     -=  =-  /)\    '  *")
    print(" [yellow]'..'  ':::'     * /\ *     .'/.\'.   '")
    print("[yellow] *            *..*         :")
    time.sleep(500/1000)

    print('\033[? 25l', end="")
    os.system("clear")
    print(  "  [purple]                              .''.")
    print(" [purple] .''.      .        *''*    :_\/_:     .")
    print("[purple]  :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.")
    print("[purple].''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=::=-")
    print("[purple]: /\ : :::::     *_\/_*     -=  =-  /)\    '  *")
    print("[purple] '..'  ':::'     * /\ *     .'/.\'.   '")
    '''                                .''.
       .''.      .        *''*    :_\/_:     .
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :'''

    time.sleep(500/1000)
    os.system('clear')
    #echo -e "\033[1K".


