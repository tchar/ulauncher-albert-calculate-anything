#!/bin/bash
run_xdotool () {
    for (( i=0; i<${#keys}; i++ )); do
		key=${keys:$i:1}
		if [ "$key" == " " ]; then
			xdotool_key="space"
		elif [ "$key" == "\t" ]; then
			xdotool_key="Tab"
		elif [ "$key" == "\n" ]; then
			xdotool_key="Return"
		elif [ "$key" == "\`" ]; then
			xdotool_key="grave"
		elif [ "$key" == "~" ]; then
			xdotool_key="asciitilde"
		elif [ "$key" == "!" ]; then
			xdotool_key="exclam"
		elif [ "$key" == "@" ]; then
			xdotool_key="at"
		elif [ "$key" == "#" ]; then
			xdotool_key="numbersign"
		elif [ "$key" == "$" ]; then
			xdotool_key="dollar"
		elif [ "$key" == "%" ]; then
			xdotool_key="percent"
		elif [ "$key" == "^" ]; then
			xdotool_key="asciicircum"
		elif [ "$key" == "\&" ]; then
			xdotool_key="ambersand"
		elif [ "$key" == "*" ]; then
			xdotool_key="asterisk"
		elif [ "$key" == "(" ]; then
			xdotool_key="parenleft"
		elif [ "$key" == ")" ]; then
			xdotool_key="parenright"
		elif [ "$key" == "-" ]; then
			xdotool_key="minus"
		elif [ "$key" == "_" ]; then
			xdotool_key="underscore"
		elif [ "$key" == "=" ]; then
			xdotool_key="equal"
		elif [ "$key" == "+" ]; then
			xdotool_key="plus"
		elif [ "$key" == "[" ]; then
			xdotool_key="bracketleft"
		elif [ "$key" == "{" ]; then
			xdotool_key="braceleft"
		elif [ "$key" == "]" ]; then
			xdotool_key="bracketright"
		elif [ "$key" == "}" ]; then
			xdotool_key="braceright"
		elif [ "$key" == "\\" ]; then
			xdotool_key="backslash"
		elif [ "$key" == "|" ]; then
			xdotool_key="bar"
		elif [ "$key" == ";" ]; then
			xdotool_key="semicolon"
		elif [ "$key" == ":" ]; then
			xdotool_key="colon"
		elif [ "$key" == "\'" ]; then
			xdotool_key="apostrophe"
		elif [ "$key" == "\"" ]; then
			xdotool_key="quotedbl"
		elif [ "$key" == "," ]; then
			xdotool_key="comma"
		elif [ "$key" == "<" ]; then
			xdotool_key="less"
		elif [ "$key" == "." ]; then
			xdotool_key="period"
		elif [ "$key" == ">" ]; then
			xdotool_key="greater"
		elif [ "$key" == "/" ]; then
			xdotool_key="slash"
		elif [ "$key" == "?" ]; then
			xdotool_key="question"
		else
			xdotool_key=$key
		fi
		xdotool key $xdotool_key
        sleep $sleep_small
	done
}

clear_launcher () {
    if [ -z "$1" ]; then    
        xdotool key ctrl+a
        xdotool key BackSpace
        sleep $sleep_small
    else
        for (( c=1; c<=$1; c++ ));
        do
            xdotool key BackSpace
            sleep $sleep_small
        done
    fi
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
    keys="= 500 $"
    run_xdotool
    sleep $sleep_big

    keys=" to EUR, bitcoin, canadian, mexican"
    run_xdotool
    sleep $sleep_big
    clear_launcher
}

demo_time(){
    keys="time "
    run_xdotool
    sleep $sleep_big

    keys="at Paris France"
    run_xdotool
    sleep $sleep_big

    clear_launcher 15
    keys="+ 2 hours 3 min at Prague"
    run_xdotool
    sleep $sleep_big

    clear_launcher 9
    keys="- 2 years 5 months"
    run_xdotool
    sleep $sleep_big

    keys=" at Delhi"
    run_xdotool
    sleep $sleep_big
    clear_launcher

    keys="time until December 31 midnight"
    run_xdotool
    sleep $sleep_big
    clear_launcher

    keys="time until tomorrow afternoon"
    run_xdotool
    sleep $sleep_big
    clear_launcher
}

demo_units() {
    cmd="equal space"

    keys="= 38 c to f"
    run_xdotool
    sleep $sleep_big
    clear_launcher

    keys="= 10 m + 158 cm"
    run_xdotool
    sleep $sleep_big

    keys=" to in, cm, km"
    run_xdotool
    sleep $sleep_big
    clear_launcher

    keys="= 60 mph to kph, miles per minute, inch/h"
    run_xdotool
    sleep $sleep_big
    clear_launcher

    keys="= 10 m ^ 2 to inch ^ 2, cm ^ 2"
    run_xdotool
    sleep $sleep_big
    clear_launcher
}

demo_percentages() {
    cmd="equal space"

    keys="= 10 + 50%"
    run_xdotool
    sleep $sleep_big
    clear_launcher

    keys="= sqrt(2) + 50%"
    run_xdotool
    sleep $sleep_big
    clear_launcher

    keys="= 100 as % of 200"
    run_xdotool
    sleep $sleep_big
    clear_launcher

    keys="= 50% of 4"
    run_xdotool
    sleep $sleep_big
    clear_launcher

    keys="= 50 % of 100 + sqrt(2) + 1.5"
    run_xdotool
    sleep $sleep_big
    clear_launcher
}

demo_calculator() {    
    keys="= 10 + 2 + sqrt(2) + acosh(pi) + sin(e)"
    run_xdotool
    sleep $sleep_big
    clear_launcher

    keys="= 5 + 3i - 8i"
    run_xdotool
    sleep $sleep_big

    keys=" + tan(2 + i)"
    run_xdotool
    sleep $sleep_big
    clear_launcher

    keys="= e ^ (pi * i) + 1"
    run_xdotool
    sleep $sleep_big
    clear_launcher
}

demo_base_n_calculator() {
    keys="hex fa21 + ad10"
    run_xdotool
    sleep $sleep_big

    clear_launcher 11
    keys="#ff1234"
    run_xdotool
    sleep $sleep_big
    clear_launcher

    keys="bin (10001 xor 1111) ^ 10 + 10 mod 11"
    run_xdotool
    sleep $sleep_big
    clear_launcher
}

demo_exit() {
    keys="= And so much more"
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