
\version "2.22.0"
\language "français"
\layout {
  \context {
    \Score
    \omit BarNumber
  }
}
\relative {
\key ré \minor
\time 2/4
ré'8 ré ré ré | la'4 la | sib8 sib sib sib | la4 la | sol8 fa sol la | sib la sol fa | fa4 mi | ré2^\markup {
\italic "Fine"
}
\bar "||"
ré'8 ré ré ré | do si la si | do4 si | la2
la8 sib do la | sib sol la sib | la4 sol | fa2
fa8 sol la fa | sol4 sol | mi8 fa sol mi | fa4
mi 
\fermata
\bar ":|."
}
\addlyrics {
  \override StanzaNumber #'font-name = #"Times New Roman" 
  \override LyricText #'font-size = #-1
  \set stanza = "1. "
Ô Dieu de clé -- men -- ce, Viens par ta pré -- sen -- ce, Com -- bler nos dé -- sirs, A -- pai -- ser nos sou -- pirs. Sau -- veur se -- cou -- ra -- ble, Pa -- rais à nos yeux, À l'hom -- me cou -- pa -- ble Viens ou -- vrir les cieux ; Cé -- les -- te vic -- ti -- me, Fer -- me- -- lui l'a -- bî -- me.
}
