# In this project, I learnt using module and library.
import pyjokes
print("Do you want to get a joke?")
answer= input("\nResponse in y for 'yes' and n for 'no'.  ")
if answer== str('y') :
    print('\n',pyjokes.get_joke())
else :
    print('\nok then....')
