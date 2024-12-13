import re
class Game:
    a_button: tuple
    b_button: tuple
    score: tuple = (0, 0)
    prize: tuple

    def __init__(self, game_raw):
        [a_raw, b_raw, p_raw] = game_raw
        self.a_button = self._parse_raw(a_raw)
        self.b_button = self._parse_raw(b_raw)
        self.prize = self._parse_raw(p_raw)


    def _parse_raw(self, raw):
        [x_raw, y_raw] = re.findall("([XY][+=]\d+)", raw)
        x = int(x_raw[2:])
        y = int(y_raw[2:])

        return (x, y) 




def test():
    ex = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

    run(ex)

visited_scores = set()
def run(input: str):
    global visited_scores
    games = [g for g in input.split("\n\n")]
    games = [g.split("\n") for g in games]
    
    games = [Game(g) for g in games]
    score = 0
    for i, game in enumerate(games):
        visited_scores = set()
        score += play_game(game)

    print("1: ", score)

def play_game(game: Game):

    x,y = find_score(game, (0,0), game.prize, 0, 0)
    if x > 0:
        score = (x * 3) + (y * 1)
        return score
    return 0

def find_score(game, current, goal, acount,bcount):


    if current == goal:
        return acount, bcount
    
    elif current[0] < goal[0] and current[1] < goal[1] and current not in visited_scores:
        visited_scores.add(current)
        return max(find_score(game, press(game.a_button, current), goal, acount+1, bcount), find_score(game, press(game.b_button, current), goal,acount, bcount+1))
    
    elif current[0] > goal[0] or current[1] > goal[1]:
        return (0,0)
        
    return (0,0)

def press(button: tuple, score: tuple):
    return tuple(map(lambda x, y: x + y, button, score))