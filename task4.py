good = r"""
  ___ __ ___   _____ _ __ ___   __ _ _ __  
 / __/ _` \ \ / / _ \ '_ ` _ \ / _` | '_ \ 
| (_| (_| |\ V /  __/ | | | | | (_| | | | |
 \___\__,_| \_/ \___|_| |_| |_|\__,_|_| |_|
 """
bad = r"""
      __.
   ________/o |)
  {_______{_rs|




    .__
   (| o\________
    |rs_}_______}
    """




drawbridge_raised = True
if not drawbridge_raised:
    print(good)
    outcome = "Doom: How will I get out?"
else:
    print(bad)
    outcome = "Thunder: Great! Freedom is in sight."
print(outcome)