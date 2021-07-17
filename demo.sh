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

#! /bin/bash

setup_peek() {
	launcher_info=$(xdotool search --onlyvisible --class "$launcher_class" getwindowgeometry --shell)
	eval $launcher_info
    launcher_screen=$SCREEN
    launcher_id=$WINDOW
    launcher_x=$X
    launcher_y=$Y
    launcher_w=$WIDTH
    launcher_h=$HEIGHT
    
	peek_id=$(xdotool search --onlyvisible --class Peek)
    if [ -z "$peek_id" ]; then
		peek &>/dev/null &
		sleep 0.1
    	peek_id=$(xdotool search --onlyvisible --class Peek)
	fi
	move_x=$((launcher_x - 720 / 2 + launcher_w / 2 ))
	move_y=$((launcher_y - pad_y ))
    xdotool windowsize $peek_id 720 480
    xdotool windowmove $peek_id $move_x $move_y
}

setup() {
    if [ "$launcher_name" == "ulauncher" ]; then
        ulauncher
        launcher_class="Ulauncher"
        pad_y=55
    elif [ "$launcher_name" == "albert" ]; then
        albert show
        launcher_class="albert"
        pad_y=70
    else
        echo "No launcher provided"
        exit
    fi

    sleep_small=0.02
    sleep_big=2
    sleep 0.1
    setup_peek

    xdotool windowfocus $launcher_id
    peek --start
    sleep 3.5
}

finalize() {
    peek --stop
}

demo_currency(){
    cmd="equal space"

    keys=( $cmd 5 0 0 space dollar )
    run_xdotool
    sleep $sleep_big

    keys=( space t o space E U R comma space b i t c o i n comma space c a n a d i a n comma space m e x i c a n  )
    run_xdotool
    sleep $sleep_big
    clear_all
}

demo_time(){
    cmd="t i m e space"

    keys=($cmd )
    run_xdotool
    sleep $sleep_big

    keys=( a t space P a r i s space F r a n c e )
    run_xdotool
    sleep $sleep_big

    keys=( BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace )
    run_xdotool
    keys=( p l u s space 2 space h o u r s space 3 space m i n space a t space P r a g u e )
    run_xdotool
    sleep $sleep_big

    keys=( BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace minus space 2 space y e a r s space 5 space m o n t h s )
    run_xdotool
    sleep $sleep_big

    keys=( space a t space D e l h i )
    run_xdotool
    sleep $sleep_big
    clear_all

    keys=( $cmd u n t i l space D e c e m b e r space 3 1  space m i d n i g h t )
    run_xdotool
    sleep $sleep_big
    clear_all

    keys=( $cmd u n t i l space t o m o r r o w space a f t e r n o o n )
    run_xdotool
    sleep $sleep_big
    clear_all
}

demo_units() {
    cmd="equal space"

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
}

demo_percentages() {
    cmd="equal space"

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
}

demo_calculator() {
    cmd="equal space"
    
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
}

demo_base_n_calculator() {
    cmd='h e x space'

    keys=( $cmd space f a 2 1 space plus space a 1 0 )
    run_xdotool
    sleep $sleep_big

    keys=( BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace BackSpace )
    run_xdotool
    keys=( numbersign f f 1 2 3 4 )
    run_xdotool
    sleep $sleep_big
    clear_all

    cmd='b i n space'
    keys=( $cmd parenleft 1 0 0 0 1 space x o r space 1 1 1 1 parenright space asciicircum space 1 space plus space 1 0 space m o d space 1 1 )
    run_xdotool
    sleep $sleep_big
    clear_all
}

demo_exit() {
    cmd="equal space"

    keys=( $cmd A n d space s o space m u c h space m o r e )
    run_xdotool
    sleep $sleep_big
}

launcher_name=$1
setup

# Currency
demo_currency

# Time
demo_time

# Units
demo_units

# Percentages
demo_percentages

# Calculator
demo_calculator

# Base N calculator
demo_base_n_calculator

# Exit
demo_exit

finalize