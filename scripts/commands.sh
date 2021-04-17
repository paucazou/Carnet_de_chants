#!/bin/zsh
# Please enter `source commands.sh`
# Launch every command from the main dir

songs=songs
scripts=scripts

__check_name_entered () {
    if [[ $1 == '' ]]; then
        print 0
    else
        print 1
    fi
}

__check_file_does_not_exist () {
    if [[ -a $1 ]]; then
        print 1
    else
        print 0
    fi
}



new_song () {
    if [[ `__check_name_entered $1` == 1 ]]; then
        if [[ `__check_file_does_not_exist $1.ly` == 0 ]]; then
    name=$1
    touch $songs/$name.txt # lyrics
    print '\
\\version "2.22.0"
\\language "français"
\\relative {
\key 
\time 
}
\\addlyrics {
}
' >> $songs/$name.ly
    print $1 created
    git add $songs/$name.txt
    git add $songs/$name.ly
    git commit $songs/$name.txt $songs/$name.ly -m "Added $name"
    update
else
    print $1 already exists
        fi
    else
        print No name entered
    fi

}

update () {
    # update the index
    scripts/check_songs.py
    print Index updated
}

compile_ly () {
    lilypond  --output=$songs $1
    update
}

compile_and_pdf () {
    compile_ly $1
    xdg-open ${1%.ly}.pdf
    update
}

finish () {
    if [[ `__check_file_does_not_exist $1` == 1 ]]; then
        code_line="import scripts.update_status as sus; sus.update_status(\"$1\",1)"
        python -c $code_line
        update
    else
        print No file.
    fi
}
unfinish () {
    if [[ `__check_file_does_not_exist $1` == 1 ]]; then
        python -m "import scripts.update_status as sus; sus.update_status($1,0)"
        update
    else
        print No file.
    fi
}





