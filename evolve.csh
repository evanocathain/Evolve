#!/bin/csh

# Loop through potential law constant values, in units of 10^(-28)
#foreach Kvalue ( 0.9 0.8 0.7 0.6 0.55 0.54 0.53 0.52 0.51 0.50 0.49 0.48 0.47 0.46 0.45 0.4 )
#foreach Kvalue ( 0.3 0.2 0.1 0.05 0.02 0.01 )
foreach Kvalue ( 0.005 0.002 0.001 0.0005 0.0002 0.0001 )

    echo $Kvalue
    python3.10 evolve.py -K $Kvalue -p0 10.0 > file$Kvalue

end
