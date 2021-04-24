import sys
input = sys.stdin.readline
team = int(input())
total_games = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
current_points = [0] * 5
games = int(input())
count = 0

for i in range(games):
    A, B, Sa, Sb = map(int, input().split())
    if (A, B) in total_games:
      total_games.remove((A, B))
    else:
      total_games.remove((B, A))

    if Sa > Sb:
        current_points[A] += 3
    elif Sb > Sa:
        current_points[B] += 3
    else:
        current_points[A] += 1
        current_points[B] += 1

def find_outcomes(teams, scores, points, index):
  global count
  A, B = teams 
  Sa, Sb = scores
  if Sa > Sb:
        points[A] += 3
  elif Sb > Sa:
      points[B] += 3
  else:
      points[A] += 1
      points[B] += 1
  
  if index == len(total_games)-1:
      winner = max(points)
      if winner == points[team]:

        temp = [points[i] for i in range(5)]
        temp.pop(team)
        if max(temp) < winner:
          count += 1
          return
      return
  
  next_game = total_games[index+1]
  
  find_outcomes(next_game, (1, 0), points.copy(), index+1)
  find_outcomes(next_game, (0, 1), points.copy(), index+1)
  find_outcomes(next_game, (1, 1), points.copy(), index+1)

next_game = total_games[0]
p = [current_points[i] for i in range(5)]
find_outcomes(next_game, (1, 0), p.copy(), 0)
find_outcomes(next_game, (0, 1), p.copy(), 0)
find_outcomes(next_game, (1, 1), p.copy(), 0)
print(count)
