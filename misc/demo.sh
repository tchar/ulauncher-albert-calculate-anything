#!/bin/bash

setup_launcher() {
	launcher_info=$(xdotool search --onlyvisible --class "$launcher_class" getwindowgeometry --shell)
	eval $launcher_info
    # launcher_screen=$SCREEN
    launcher_id=$WINDOW
    launcher_x=$X
    launcher_y=$Y
    launcher_w=$WIDTH
    # launcher_h=$HEIGHT
}

setup_peek() {
    if [ "$use_peek" != "peek" ]; then
        return 0
    fi
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
    peek --start
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
    elif [ "$launcher_name" == "prompt_toolkit" ]; then
        use_peek="nopeek"
        RECORD=true python demo/prompt.py &
    else
        echo "No launcher provided"
        exit
    fi

    sleep_small=0.02
    sleep_big=2
    sleep 0.1
    setup_launcher
    setup_peek

    xdotool windowfocus $launcher_id
    sleep 3.5
}

finalize() {
    peek --stop
}

run_xdotool () {
    for (( i=0; i<${#keys}; i++ )); do
		key=${keys:$i:1}
        case $key in
            " ") xdotool_key="space";;
            "\t") xdotool_key="Tab";;
            "\n") xdotool_key="Return";;
            "\`") xdotool_key="grave";;
            "~") xdotool_key="asciitilde";;
            "!") xdotool_key="exclam";;
            "@") xdotool_key="at";;
            "#") xdotool_key="numbersign";;
            "$") xdotool_key="dollar";;
            "%") xdotool_key="percent";;
            "^") xdotool_key="asciicircum";;
            "&") xdotool_key="ampersand";;
            "*") xdotool_key="asterisk";;
            "(") xdotool_key="parenleft";;
            ")") xdotool_key="parenright";;
            "-") xdotool_key="minus";;
            "_") xdotool_key="underscore";;
            "=") xdotool_key="equal";;
            "+") xdotool_key="plus";;
            "[") xdotool_key="bracketleft";;
            "{") xdotool_key="braceleft";;
            "]") xdotool_key="bracketright";;
            "}") xdotool_key="braceright";;
            "\\") xdotool_key="backslash";;
            "|") xdotool_key="bar";;
            ";") xdotool_key="semicolon";;
            ":") xdotool_key="colon";;
            "'") xdotool_key="apostrophe";;
            "\"") xdotool_key="quotedbl";;
            ",") xdotool_key="comma";;
            "<") xdotool_key="less";;
            ".") xdotool_key="period";;
            ">") xdotool_key="greater";;
            "/") xdotool_key="slash";;
            "?") xdotool_key="question";;
            *)    xdotool_key=$key;;
        esac
		xdotool key $xdotool_key
        sleep 0.02
	done
}

clear_input () {
    if [ -z "$1" ]; then    
        xdotool key ctrl+a
        xdotool key Delete
        sleep $sleep_small
    else
        for (( c=1; c<=$1; c++ ));
        do
            xdotool key BackSpace
            sleep $sleep_small
        done
    fi
}

demo_currency(){
    keys="= 500 $"
    run_xdotool
    sleep $sleep_big

    keys=" to EUR, bitcoin, canadian, mexican"
    run_xdotool
    sleep $sleep_big
    clear_input
}

demo_time(){
    keys="time "
    run_xdotool
    sleep $sleep_big

    keys="at Paris France"
    run_xdotool
    sleep $sleep_big

    clear_input 15
    keys="+ 2 hours 3 min at Prague"
    run_xdotool
    sleep $sleep_big

    clear_input 9
    keys="- 2 years 5 months"
    run_xdotool
    sleep $sleep_big

    keys=" at Delhi"
    run_xdotool
    sleep $sleep_big
    clear_input

    keys="time until December 31 midnight"
    run_xdotool
    sleep $sleep_big
    clear_input

    keys="time until tomorrow afternoon"
    run_xdotool
    sleep $sleep_big
    clear_input
}

demo_units() {
    keys="= 38 c to f"
    run_xdotool
    sleep $sleep_big
    clear_input

    keys="= 10 m + 158 cm"
    run_xdotool
    sleep $sleep_big

    keys=" to in, cm, km"
    run_xdotool
    sleep $sleep_big
    clear_input

    keys="= 60 mph to kph, miles per minute, inch/h"
    run_xdotool
    sleep $sleep_big
    clear_input

    keys="= 10 m ^ 2 to inch ^ 2, cm ^ 2"
    run_xdotool
    sleep $sleep_big
    clear_input
}

demo_percentages() {
    keys="= 10 + 50%"
    run_xdotool
    sleep $sleep_big
    clear_input

    keys="= sqrt(2) + 50%"
    run_xdotool
    sleep $sleep_big
    clear_input

    keys="= 100 as % of 200"
    run_xdotool
    sleep $sleep_big
    clear_input

    keys="= 50% of 4"
    run_xdotool
    sleep $sleep_big
    clear_input

    keys="= 50 % of 100 + sqrt(2) + 1.5"
    run_xdotool
    sleep $sleep_big
    clear_input
}

demo_calculator() {    
    keys="= 10 + 2 + sqrt(2) + acosh(pi) + sin(e)"
    run_xdotool
    sleep $sleep_big
    clear_input

    keys="= 5 + 3i - 8i"
    run_xdotool
    sleep $sleep_big

    keys=" + tan(2 + i)"
    run_xdotool
    sleep $sleep_big
    clear_input

    keys="= e ^ (pi * i) + 1"
    run_xdotool
    sleep $sleep_big
    clear_input
}

demo_base_n_calculator() {
    keys="hex fa21 + ad10"
    run_xdotool
    sleep $sleep_big

    clear_input 11
    keys="#ff1234"
    run_xdotool
    sleep $sleep_big
    clear_input

    keys="bin (10001 xor 1111) ^ 10 + 10 mod 11"
    run_xdotool
    sleep $sleep_big
    clear_input
}

demo_exit() {
    keys="= And so much more"
    run_xdotool
    sleep $sleep_big
}

launcher_name=$1
use_peek=$2
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