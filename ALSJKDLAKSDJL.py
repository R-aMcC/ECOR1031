def rps_winner():
  p1 = input("Player 1, please enter your choice: ")
  p2 = input("Player 2, please enter your choice: ")
  print(f"""Player 1: {p1} 
Player 2: {p2} 
Player 1 wins: {"s" in p1 and "p" in p2 or "p" in p1 and "k" in p2 or "k" in p1 and "s" in p2}
Player 2 wins: {"s" in p2 and "p" in p1 or "p" in p2 and "k" in p1 or "k" in p2 and "s" in p1}
Draw: {p1 == p2}""")
  
