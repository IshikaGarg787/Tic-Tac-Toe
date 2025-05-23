def print_board(lst):
  st = '''
{}|{}|{}
------
{}|{}|{}
------
{}|{}|{}
'''.format(*lst)
  print(st)

#main code

choices = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
print('welcome to tic tac toe')
print_board(choices)
turns='0'

while ' ' in choices :
    mv=input(f'Its your turn{turns} , Your moves [0-8]')
    
    if not mv.isdigit() or not (0<= int(mv) <= 8):
      print('Invalid Move, please enter number between 0-8')
      continue
    mv=int(mv)

    if choices[mv] == ' ':
       choices[mv]=turns
    else:
      print('space is already occupied, Try Again')
      continue 

    print_board(choices)

    if choices[0]==choices[1]==choices[2]!=' ' :
      print(f'------{turns} is winner------')
      break
    elif choices[3]== choices[4]== choices[5]!=' ':
      print(f'------{turns} is winner------')
      break
    elif choices[6]==choices[7]==choices[8]!=' ':
      print(f'------{turns} is winner------')
      break
    elif choices[0]==choices[3]==choices[6]!=' ':
      print(f'------{turns} is winner------')
      break
    elif choices[1]==choices[4]==choices[7]!=' ':
      print(f'------{turns} is winner------')
      break
    elif choices[3]==choices[6]==choices[8]!=' ':
      print(f'------{turns} is winner------')
      break
    elif choices[0]==choices[4]==choices[8]!=' ':
      print(f'------{turns} is winner------')
      break
    elif choices[2]==choices[4]==choices[6]!=' ':
      print(f'------{turns} is winner------')
      break
    turns='X' if turns=='0' else '0'

else:
  if choices[0] != choices[1] != choices[2] != ' ':
      print(f'------Its a tie------')
  elif choices[3]!= choices[4]!= choices[5]!=' ':
      print(f'------Its a tie------')
  elif choices[6]!=choices[7]!=choices[8]!=' ':
      print(f'------Its a tie------')
  elif choices[0]!=choices[3]!=choices[6]!=' ':
      print(f'------Its a tie------')
  elif choices[1]!=choices[4]!=choices[7]!=' ':
      print(f'------Its a tie------')
  elif choices[3]!=choices[6]!=choices[8]!=' ':
      print(f'------Its a tie------')
  elif choices[0]!=choices[4]!=choices[8]!=' ':
      print(f'------Its a tie------')
  elif choices[2]!=choices[4]!=choices[6]!=' ':
      print(f'------Its a tie------')
      
