#!/bin/csh

# Loop through potential law constant values, in units of 10^(-28)
foreach Kvalue ( 0.9 0.8 0.7 0.6 0.55 0.54 0.53 0.52 0.51 0.50 0.49 0.48 0.47 0.46 0.45 0.4 )

    echo $Kvalue
    python3.9 evolve.py -K $Kvalue -p0 10.0 > file$Kvalue

end
