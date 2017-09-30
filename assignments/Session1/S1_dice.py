##
# @author : Romain Francony, IT Student
# brief : Dice game


def dice_game():
    ##
    # Simple Dice game

    score_user = 0
    score_computer = 0
    step = 1

    print 'The dice game is gonna start'

    while score_user < 100 and score_computer < 100:
        print '---------------------------------'
        print 'Step {step} : you throw the dice'.format(step=step)
        score_user += dice_game_step_player()
        if score_user >= 100:
            break

        print 'The computer is going to play'
        score_computer += dice_game_step_computer()

        print '---------------------------------'
        print 'End of the round, the score is :'
        print 'You : {score}'.format(score=score_user)
        print 'Computer : {score}'.format(score=score_computer)
        step += 1

    print 'END OF THE GAME'
    if score_user > score_computer:
        print 'You win {score_user} - {score_computer}'.format(score_user=score_user, score_computer=score_computer)
        return True
    else:
        print 'You lose {score_user} - {score_computer}'.format(score_user=score_user, score_computer=score_computer)
        return False


from random import randint


def dice_game_step_player():
    ##
    # Dice game step when the user is playing
    keep_throwing = True
    score_total = 0
    while keep_throwing:
        score = randint(1, 6)

        if score == 1:
            print 'You got 1 ! Better luck next time.'
            score_total = 1
            keep_throwing = False
            break
        else:
            score_total += score

        print 'You obtain {score}, you now have {total} point(s)'.format(score=score, total=score_total)

        input = ''
        while input != 'o' and input != 'n':
            input = raw_input('Continue ? (o/n)')

        if input == 'n':
            keep_throwing = False

    return score_total


def dice_game_step_computer():
    ##
    # Dice game step when the computer is playing
    keep_throwing = True
    score_total = 0
    while keep_throwing:
        score = randint(1, 6)

        if score == 1:
            score_total = 1
            keep_throwing = False
            break
        else:
            score_total += score

    continuing = randint(0, 1)
    if continuing == 0:
        keep_throwing = False

    return score_total


"""
dice_game()
"""
