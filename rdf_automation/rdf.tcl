# The reason why there is "; list" after many line is to suppress the return value displayed on the screen

######################### variable Initilizations #########################
###For user input
# puts -nonewline "Enter or drag an input file name: ";
# gets stdin filename; list
#
# puts -nonewline "Enter a number of types: "
# gets stdin numtype; list

# puts -nonewline "Enter an output file name: "
# gets stdin outfile

# puts "You can also change the script to avoid inputting everytime"

###For user input
set filename equil_770K.lammpstrj; list
set numtype 3 ; list
set outfile "rdf.txt"; list

# file validation
set ext [file extension $filename]; list
if {[catch {open $filename} fid]} {
  puts stderr "ERROR) $fid"
  quit
}

# file extension validation
if {$ext != ".lammpstrj"} {
  puts stderr "ERROR) file type must be .lammpstrj but the current file type\
  is $ext.\nThe LAMMPS trajectory type is necessary for assigning the dimension of\
  the unit cell structure automatically"
  quit
}

# version validation
set ver [vmdinfo version]; puts \n
if {$ver != "1.9.3"} {
  puts stderr "ERROR) This tcl was written in VMD version 1.9.3 but the current version is\
  $ver.\n Please update to ensure the compatability!"
  quit
}






## RDF constants
# delta r
set dr 0.1; list
# cut off radius
set maxr 10; list
# periodic boundary condition or not
set pbcflag true; list
# first time step
set tfirst 1; list
# last time step
set tlast -1; list
# stepsize
set tstep 1; list

######################### file setting #########################
# read file
mol new $filename autobonds no waitfor all; list

######################### atom select #########################
# initalizing dynamic array to store atom selection
array set sel {}; list
# set each atom types to selN
for {set i 1} {$i <= $numtype} {incr i} {
  set sel($i) [atomselect top "name $i"]
}; puts \n
# set sel1 [atomselect top {name 1}]
# set sel2 [atomselect top {name 2}]
# set sel3 [atomselect top {name 3}]

######################### RDF calculation #########################
# initalizing counter and dynamic array
set counter 1; list
set ctr 1; list
array set r {}; list
array set gr {}; list
array set integr {}; list

# open and start writing file
set outfileID [open $outfile "w"]; list
# Insert parameter for rdf for reference
puts $outfileID "delta_r $dr rmax $maxr PBC $pbcflag \
firsttimestep $tfirst lasttimsstep $tlast timestep $tstep"
# Loop through to calculate rdf for 1-1, 1-2, 1-3, 2-2, and so on
for {set i 1} {$i <= $numtype} {incr i} {
  for {set j $counter} {$j <= $numtype} {incr j} {
    # create heading for the rdf
    puts -nonewline $outfileID "r_$i$j g(r)_$i$j integ(r)_$i$j "
    # calculate rdf (data = nested list{{r}{g(r)}{integ(r)}{normalized}{timeframe}})
    set data [measure gofr $sel($i) $sel($j) \
    delta $dr rmax $maxr usepbc $pbcflag \
    first $tfirst last $tlast step $tstep]

    #redistribute the nested list to simple list
    set r($ctr) [lrange [lindex $data 0] 0 end]
    set gr($ctr) [lrange [lindex $data 1] 0 end]
    set integr($ctr) [lrange [lindex $data 2] 0 end]

    incr ctr
  }
  incr counter
}
puts -nonewline $outfileID \n; puts \n
######################### output #########################
# number of rows for rdf
set lsize [llength $r(1)]; list

set counter 1; list
set ctr 1; list

# Loop to write a value in nice format
# for each row
for {set row 0} {$row < $lsize} {incr row} {
  # for each type
  for {set i 1} {$i <= $numtype} {incr i} {
    for {set j $counter} {$j <= $numtype} {incr j} {
      # write to file
      puts -nonewline $outfileID "[lindex $r($ctr) $row] [lindex $gr($ctr) $row] [lindex $integr($ctr) $row] "
      incr ctr
    }
    incr counter
  }
  set ctr 1
  set counter 1
  puts -nonewline $outfileID \n
}

######################### cleaning #########################
# close file
close $outfileID
# release memory
mol delete all
# quit vmd
quit
