Author: Greg Kalaydjian

 					How to use textSearch.py
      
      (MUST HAVE SPECIAL ACCESS TO XSEDE FILE SYSTEM, russian-political-influence.zip file, FacebookAds.csv file)

1. Download russian-political-influence.zip file and extract the file.
2. Extract the FacebookAds.csv file, we will use this for our program.
3. In order to upload the .txt file and the .py file onto the XSEDE file system we will need to open the terminal and use the SFTP File Transfer Method.
4. Once terminal is open type in the following command: $sftp <username>@bridges.psc.edu
5. Login with your password
6. Once you login you should see a prompt like “sftp>” then type in the following command: put <textfile.txt> where <textfile.txt> is the following text file/csv file that you would like to TextSearch on. Do this as many times as possible in order to have all of your documents on the file system.
7. Also note that you may need to modify the TextSearch application in order to further analyze your results. You can do this by opening the textSearch.py file and changing the key words that will be searched.
8. Be sure to also include the textSearch.py file by typing in put textSearch.py.
9. End the sftp session and close the terminal once you are done uploading your files on the system.
10. Open Putty
11. For the host name: bridges.psc.edu using port 22 and use the SSH connection type.
12. Log in to XSEDE.
12a. Find <groupname> with the command $projects
13. Move the files uploaded into the correct directory. This is done with the command:
$scp -P 22 <file.csv> /pylon5/<groupname>/<username>/
14. To get to the directory you put the file use this command: $cd /pylon5/<groupname>/<username>/
15. In order to allocate yourself resources for pyspark use the following command: $module load spark
16. To run the textSearch.py file with the FacebookAds.csv file we will run the command:
$<textSearch.py> > <output.txt>
where FacebookAds.csv and the text to be searched is specified in the textSearch.py file.
17. Once the calculation is complete head back to SFTP connection using terminal and type in the command: $get <output.txt>
18. View the <output.txt> file, each string or cell within the .csv file that contains the searched word will be easily accessible in the output.txt file.
