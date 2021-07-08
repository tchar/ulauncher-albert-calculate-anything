#!/bin/bash
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

if [ "$1" == "ulauncher" ]; then
    ulauncher
    cmd="equal space"
    sleep_small=0.02
    sleep_big=2
elif [ "$1" == "albert" ]; then
    albert show
    cmd="equal space"
    sleep_small=0.02
    sleep_big=2
else
    exit
fi
sleep 0.05
clear_all
wmctrl -a "Ulauncher - Application Launcher"
sleep 4.4

# Currency
keys=( $cmd 5 0 0 space dollar )
run_xdotool
sleep $sleep_big

keys=( space t o space E U R comma space b i t c o i n comma space c a n a d i a n comma space m e x i c a n  )
run_xdotool
sleep $sleep_big
clear_all

# Time
old_cmd=$cmd
cmd=""

keys=($cmd t i m e space)
run_xdotool
sleep $sleep_big

keys=( a t space P a r i s comma space F r a n c e )
run_xdotool
sleep $sleep_big

keys=( BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace )
run_xdotool
keys=( p l u s space 2 space h o u r s space 3 space m i n space a t space P r a g u e )
run_xdotool
sleep $sleep_big

keys=( BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace minus space 2 space y e a r s space 5 space m o n t h s )
run_xdotool
sleep $sleep_big
clear_all

cmd=$old_cmd
# Units
keys=( $cmd 3 8 space c space t o  space f )
run_xdotool
sleep $sleep_big
clear_all

keys=( $cmd 1 0 space m space plus space 1 5 8 space c m )
run_xdotool
sleep $sleep_big

keys=( space t o space i n comma space c m comma space k m )
run_xdotool
sleep $sleep_big
clear_all

keys=( $cmd 6 0 space m p h space t o space k p h comma space m i l e s space p e r space m i n u t e comma space i n c h slash h )
run_xdotool
sleep $sleep_big
clear_all

keys=( $cmd 1 0 space m asciicircum space 2 space t o space i n c h space asciicircum space 2 comma space c m space asterisk space c m )
run_xdotool
sleep $sleep_big
clear_all

# Percentages
keys=( $cmd 1 0 0 space plus space 5 0 percent )
run_xdotool
sleep $sleep_big
clear_all

keys=( $cmd s q r t parenleft 2 parenright space plus space 5 0 percent )
run_xdotool
sleep $sleep_big
clear_all

keys=( $cmd 1 0 0 space a s space percent space o f space 2 0 0)
run_xdotool
sleep $sleep_big
clear_all

keys=( $cmd 5 0 percent space o f space 4 )
run_xdotool
sleep $sleep_big
clear_all

keys=( $cmd 5 0 percent space o f space 1 0 0 space plus space s q r t parenleft 2 parenright space plus space 1 period 5 )
run_xdotool
sleep $sleep_big
clear_all

# Calculator

keys=( $cmd 1 0 space plus space 2 space plus space s q r t parenleft 2 parenright space plus space c o s parenleft p i parenright space plus space s i n parenleft e parenright )
run_xdotool
sleep $sleep_big
clear_all

keys=( $cmd 5 space plus space 3 i space minus space 8 i )
run_xdotool
sleep $sleep_big

keys=( space plus space c o s parenleft 2 space plus space i parenright )
run_xdotool
sleep $sleep_big
clear_all

keys=( $cmd e asciicircum parenleft p i space asterisk space i parenright )
run_xdotool
sleep $sleep_big
clear_all

keys=( $cmd A n d space s o space m u c h space m o r e )
run_xdotool
