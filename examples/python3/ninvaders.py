import os
import random
import time

WIDTH = 40
HEIGHT = 20

class Entity:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_char():
    if os.name != 'nt':
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    else:
        import msvcrt
        ch = msvcrt.getch().decode('utf-8')
    return ch

def draw_game(player, bullets, invaders, score):
    screen = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    screen[player.y][player.x] = player.char
    
    for bullet in bullets:
        if 0 <= bullet.y < HEIGHT:
            screen[bullet.y][bullet.x] = bullet.char
    
    for inv in invaders:
        if inv.y > 0:
            screen[inv.y][inv.x] = inv.char
    
    clear_screen()
    print(f"Score: {score}")
    print('-' * WIDTH)
    for row in screen:
        print(''.join(row))
    print('-' * WIDTH)

def update_game(player, bullets, invaders, score):
    # Move bullets
    for bullet in bullets:
        bullet.y -= 1
    bullets = [b for b in bullets if b.y >= 0]  # Remove off-screen bullets
    
    # Move invaders
    for inv in invaders:
        if inv.y > 0 and random.random() < 0.1:
            inv.y += 1
    
    # Check for collisions
    for bullet in bullets[:]:  # Create a copy of the list to iterate over
        for inv in invaders:
            if inv.y > 0 and bullet.x == inv.x and bullet.y == inv.y:
                inv.y = 0
                bullets.remove(bullet)
                score += 10
                break
    
    return bullets, score

def game_over(invaders):
    return any(inv.y >= HEIGHT - 1 for inv in invaders if inv.y > 0)

def play_game():
    player = Entity(WIDTH // 2, HEIGHT - 1, 'A')
    bullets = []
    invaders = [Entity(i * 4, 2, 'W') for i in range(10)]
    score = 0
    shoot_cooldown = 0
    cooldown_time = 5  # Adjust this to control shooting speed (higher = slower)
    
    while not game_over(invaders) and score < 100:
        draw_game(player, bullets, invaders, score)
        bullets, score = update_game(player, bullets, invaders, score)
        
        ch = get_char()
        
        if ch == 'a' and player.x > 0:
            player.x -= 1
        elif ch == 'd' and player.x < WIDTH - 1:
            player.x += 1
        elif ch == ' ' and shoot_cooldown == 0:
            bullets.append(Entity(player.x, player.y - 1, '|'))
            shoot_cooldown = cooldown_time
        elif ch == 'q':
            return False, score
        
        if shoot_cooldown > 0:
            shoot_cooldown -= 1
        
        time.sleep(0.1)
    
    return True, score  # Return True if the game wasn't quit early

def main():
    while True:
        completed, score = play_game()
        
        if completed:
            if score >= 100:
                print(f"Congratulations! You won with a score of {score}!")
            else:
                print(f"Game Over! Final Score: {score}")
        
        print("\nDo you want to play again? (y/n)")
        if get_char().lower() != 'y':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
