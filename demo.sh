#!/bin/bash

sleep_small=0.1
sleep_big=1.5

run_xdotool () {
    for key in "${keys[@]}"
    do
        xdotool key $key
        sleep $sleep_small
    done
}

clear_all () {
    keys=( ctrl+a BackSpace )
    run_xdotool
}

ulauncher
sleep 0.05
wmctrl -a "Ulauncher - Application Launcher"
sleep 4.4

keys=( c a l c space 1 0 space dollar )
run_xdotool
sleep $sleep_big

keys=( space t o space E U R comma space b i t c o i n comma space c a n a d i a n comma space m e x i c a n  )
run_xdotool
sleep $sleep_big
clear_all

keys=( c a l c space 3 8 space c space t o  space f )
run_xdotool
sleep $sleep_big
clear_all

keys=( c a l c space 1 0 space m space plus space 1 5 8 space c m )
run_xdotool
sleep $sleep_big

keys=( space t o space i n comma space c m comma space k m )
run_xdotool
sleep $sleep_big
clear_all

keys=( c a l c space 6 0 space m p h space t o space k p h comma space m i l e s space p e r space m i n u t e comma space i n c h slash h )
run_xdotool
sleep $sleep_big
clear_all

keys=( c a l c space 1 0 m asciicircum 2 space t o space i n asciicircum 2 comma space c m asterisk c m )
run_xdotool
sleep $sleep_big
clear_all

keys=( c a l c space 1 0 space plus space 2 space plus space s q r t parenleft 2 parenright )
run_xdotool
sleep $sleep_big

keys=( space plus space c o s parenleft p i parenright space plus space s i n parenleft e parenright )
run_xdotool
sleep $sleep_big
clear_all

keys=( c a l c space 5 space plus space 3 i space minus space 8 i )
run_xdotool
sleep $sleep_big

keys=( space plus space c o s parenleft 2 space plus space i parenright )
run_xdotool
sleep $sleep_big
clear_all

keys=( c a l c space e asciicircum parenleft p i space asterisk space i parenright )
run_xdotool
sleep $sleep_big
clear_all

keys=( c a l c space A n d space s o space m u c h space m o r e )
run_xdotool
