
*it can recognize only French, English or German text.*  
*accuracy depends how many characters are in text.*  

run:  
./tri.py corpus/eng.txt >eng.tri.txt  
./tri.py corpus/de.txt >de.tri.txt  
./tri.py corpus/fr.txt >fr.tri.txt  

and, for testing, run:  

./test.py eng.tri.txt fr.tri.txt de.tri.txt justtext.txt  

**and Voilà!**




