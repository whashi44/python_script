VMD RDF atutomation

Requirement: The dump file needs to be in .lammpstrj format because the cell size needs to be set automatically, and xyz do not provide that option.

Purpose: After getting annoyed by using GUI to calcuclate RDF for 5 different atom types, this scripts was created to automate the task
First, the tcl file will perform the following 
1. Open the file (You can also change script to allow you to perform user input) 
2. Calculate RDF 
3. Write result in nice format into the txt file.



Usage: $ vmd -dispdev text -e rdf.tcl
If the file name is "rdf.tcl"
you can simply run the vmd from command line by the above

This means that 
-dspdev text = do not provide any graphics display window
-e rdf.tcl = after initializatoin, execute the text commands in filename, and then resume normal operation. 


