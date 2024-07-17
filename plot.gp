set term x11
set term postscript enhanced color solid
set output "trajectory.ps"
set logscale xy

set ylabel "Period Derivative (s/s)"
set format y '%1.1E'
set xlabel "Period (s)"

set label "Evolutionary Laws of the form ~{P}{1.1..} = kQP^{-2}" at 0.01,2.0e-13

set key bottom left box

plot [0.005:10.0][1.0e-17:3.0e-13]"file0.51" u 1:2 wi li title "Example bound-type trajectory", "file0.49" wi li title "Example open-type trajectory"

