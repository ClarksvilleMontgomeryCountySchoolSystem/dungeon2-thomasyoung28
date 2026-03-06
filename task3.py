good = r"""
-|
               -' |
             -'   | __
        ==wkm=====|'\/           ()
                                 /|
                                 `O
                                 /`
                                :
                               /\
                               \ \
                               ` `
        ____________________________________
        ///\\\///\\\///\\\///\\\///\\\///\\\
        """
bad = r"""
\|/
            .-*-         
           / /|\         
          _L_            
        ,"   ".          
    (\ /  O O  \ /)      
     \|    _    |/       
       \  (_)  /         
       _/.___,\_         
      (_/ alf \_)         
      """






guard_awake = True
if guard_awake:
    print(good)
    outcome = "Shadow: Get through quick!"
else:
    print(bad)
    outcome = "Doom: You're caught..."
print(outcome)