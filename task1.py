good = r"""  _
            _/-\_
         .-`-:-:-`-.
        /-:-:-:-:-:-\
        \:-:-:-:-:-:/
         |`       `|
         |         |
    jgs  `\       /'
           `-._.-'
              """

bad = r"""
/MMMM=M\
MMMMMMMM
\MM"MMMMM/
    VMMMM
    IMMM/
    \MMM
     M="
"""

escaped = False
if not escaped:
    print(bad)
    outcome = "Doom: Wait, so we're stuck?..."
else:
    print(good)
    outcome = "Legend: We're free!"
print(outcome)