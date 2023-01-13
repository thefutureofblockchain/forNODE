# FIND YOUR DEBATE FORMAT
#### Video Demo:  <https://youtu.be/voyW1dBPnGQ>
#### Description: I ultimately decided on making this my project because i do speech and debate, and i dont frequenty see online communities or as much content about them as other areas i am interested in, therefore i was inspired.
The first file in this folder, is an image, and throughout this entire folder, there are collectively four images in total, and they’re the descriptions to the analysis that is made finally. (will explain about this in the following paragraphs)
The main project is a buzzfeed-adjacent personality quiz where you are asked 10 questions and based on those questions; you are at the end of the program, judged and told which of the four styles/formats (british parliamentary, model united nations, world schools debate and public forum) you are most suited for and then prompts you to enter y or n to either download a pdf or not download a pdf with detailed analysis. When and if you don’t choose to download the pdf, the program ends with a greeting and an ASCII art based firework animation in the terminal window.

However, when and if you do choose to download that pdf, the programs makes a pie chart of the percentages of each format that you fit under and saves that as an image (it’s called debate_analysis.png) and then further use that image and an image from the above mentioned four to present to you, a pdf, that contains, at the very top, the string “your results” and under it the image with the analysis written out. This was done using fpdf because i found fpdf to have wonderful functionality. Under the analysis is the previously mentioned pie chart and underneath all of this is the name of the format.

The two example.txt files are used to create the animation that is the fireworks at the end of the program.

When beginning, I debated as to which library to use. I wanted to use the stdscr.refresh of the curses library, but the getch() function puzzled me, and moreover so, it didn’t make sense for the program i was making. I was stuck with wanting a pretty terminal and wanting for it to reload, however when i learned that this could be done by combining the use of rich and the os module (and more specifically the os.system(‘clear’) function, i decided on using that instead of the aforementioned idea, even though i cycled through various libraries like curses (for example, pygame, textual etc.)


In the end, I was able to create a project that i am wholly proud of.



