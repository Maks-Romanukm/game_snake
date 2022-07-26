from pygame import mixer
from panel import InfoPanel
from settings import *
from snake import Snake, snake_moves
from body import *
from dead import *
import time
from menu import Menu
import global_storage
import logger
import high_score as hs
import GV


# file = open('best_score.txt', 'r+', encoding='utf-8')

# print(file.read())

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    game_screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.SysFont('Lucida Sans', 12)
    score = 0
    remain = 5
    fade_counter = 0
    sound = 'Start'
    remain_2 = 2
    high_score = hs.read()
    time.time()
    spawn = time.time() + 5
    pygame.init()
    pygame.font.init()
    run_game = True
    info_panel = InfoPanel(game_screen, font)
    menu = Menu(game_screen, font)
    menu.open_menu()
    clock = pygame.time.Clock()
    bg_sound = mixer.Sound('soung/bg_sound.wav')
    snake_tail = Snake()
    snake_head = snake_tail
    dead = Dead()
    snake_list = [snake_tail]
    food = Food()
    sprites = pygame.sprite.Group()
    sprites.add(snake_tail)
    sprites.add(food)
    pygame.display.update()
    sprites.update()
    sprites.draw(game_screen)
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if score > high_score:
                    hs.save(str(score))
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.stop(bg_sound)
                    sound ='Stop'
                    menu.open_menu()
                    sound = 'Start'
                if event.key in snake_moves:
                    new_direction = snake_moves[event.key]  # (0, -snake_step, 180)
                    if new_direction[0] + snake_head.direction[0] != 0 or new_direction[1] + snake_head.direction[
                        1] != 0:
                        snake_head.change_direction(new_direction)

        game_screen.fill(color=bg_color)
        sprites.update()
        for sprite in snake_list:
            if snake_head.rect.collidepoint(dead.rect.center) and 6 < score < 55:
                logger.info('Death reason: collide with grave')
                if score > high_score:
                    hs.save(score)
                pygame.mixer.Sound.stop(bg_sound)
                GV.game_over(fade_counter, 40, game_screen, score)
                menu.open_menu()
                sound = 'Start'
            if sprite.rect.collidepoint(food.rect.center):
                logger.debug('Common food eaten')
                score += food.score
                if score >= 55:
                    dead.kill()
                food.change_location()
                snakebody = SnakeBody(snake_tail)
                sprites.add(snakebody)
                snake_tail = snakebody
                snake_list.append(snake_tail)
                if score == remain:
                    global_storage.fps += 0.5
                    remain += 5
            if spawn < time.time() and 6 < score < 60:
                logger.debug('Special food eaten')
                sprites.add(dead)
                dead.change_location()
                spawn += 10
                if score >= 55:
                    dead.kill()
            if sprite.rect.collidepoint(snake_head.rect.center) and sprite is not snake_head:
                logger.info('Death reason: collide with snake body')
                if score > high_score:
                    hs.save(score)
                pygame.mixer.Sound.stop(bg_sound)
                GV.game_over(fade_counter, 40, game_screen, score)
                menu.open_menu()
                sound = 'Start'
        if sound == 'Start':
            bg_sound.play().set_volume(global_storage.music_volume / 10)
            sound = 'Stop'
        info_panel.draw(global_storage.fps, score)
        sprites.draw(game_screen)
        pygame.display.flip()
        clock.tick(global_storage.fps)
pygame.quit()
