import pygame, sys
from time import sleep
from bricks import Bricks


def check_keydown_events(event, paddle, ball):
    if event.key == pygame.K_RIGHT:
        paddle.moving_right = True
    elif event.key == pygame.K_LEFT:
        paddle.moving_left = True
    elif event.key == pygame.K_SPACE:
        if not ball.ball_in_game:
            if not paddle.moving_right and not paddle.moving_left:
                ball.speed_factorx = ball.speed_factor
            elif paddle.moving_right:
                ball.speed_factorx = ball.speed_factorx
            elif paddle.moving_left:
                ball.speed_factorx *= -1
            ball_action(ball)


def check_keyup_events(event, paddle):
    if event.key == pygame.K_RIGHT:
        paddle.moving_right = False
    elif event.key == pygame.K_LEFT:
        paddle.moving_left = False


def check_events(settings, screen, stats, play_button, paddle, sb, bricks, ball):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, play_button, paddle, sb, bricks, mouse_x, mouse_y, ball)

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle, ball)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle)


def check_play_button(settings, screen, stats, play_button, paddle, sb, bricks, mouse_x, mouse_y, ball):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_level()
        sb.prep_high_score()
        sb.prep_heart()

    bricks.empty()

    create_bricks(settings, screen, paddle, bricks)

    screen_rect = screen.get_rect()
    ball.rect.centerx = screen_rect.centerx
    ball.rect.bottom = paddle.rect.top
    paddle.center_paddle()


def create_bricks(settings, screen, paddle, bricks):
    brick = Bricks(settings, screen)
    number_aliens_x = get_number_brick_x(settings, brick.rect.width)
    number_rows = get_number_rows(settings, paddle.rect.height, brick.rect.height)
    for row_number in range(number_rows):
        for brick_number in range(number_aliens_x):
            create_brick(settings, screen, bricks, brick_number, row_number)


def get_number_brick_x(settings, brick_width):
    available_space_x = settings.width - brick_width
    number_bricks_x = int(available_space_x / (1.5 * brick_width))
    return number_bricks_x


def get_number_rows(settings, paddle_height, brick_height):
    available_space_y = (settings.height - (brick_height + paddle_height))
    number_rows = int(available_space_y / (2.5 * brick_height))
    return number_rows


def create_brick(settings, screen, bricks, brick_number, row_number):
    brick = Bricks(settings, screen)
    brick_width = brick.rect.width
    brick.x = 0.75 * brick_width + 1.5 * brick_width * brick_number
    brick.rect.x = brick.x
    brick.rect.y = 1.5 * brick.rect.height + 1.5 * brick.rect.height * row_number
    bricks.add(brick)


def ball_action(ball):
    ball.ball_in_game = True


def check_ball_bottom(stats, screen, paddle, sb, bricks, ball):
    screen_rect = screen.get_rect()
    if ball.rect.bottom >= screen_rect.bottom:
        ball_out(stats, screen, paddle, sb, ball, bricks)


def check_ball_collisions(settings, stats, paddle, sb, bricks, ball):
    collisions = pygame.sprite.spritecollide(ball, bricks, True)
    collision = pygame.sprite.collide_rect(paddle, ball)
    if collisions:
        hit_rect = collisions[0].rect
        if hit_rect.top:
            ball.speed_factory *= -1
        elif hit_rect.bottom:
            ball.speed_factory *= -1
        elif hit_rect.left:
            ball.speed_factorx *= -1
        elif hit_rect.right:
            ball.speed_factorx *= -1

        stats.score += settings.brick_points
        sb.prep_score()
        check_high_score(stats, sb)

    if collision:
        ball.speed_factory *= -1

    if len(bricks) == 0:
        paddle.center_paddle()
        ball.center_ball()
        # вывести счет на экран
        ball.ball_in_game = False
        stats.game_active = False


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def ball_out(stats, screen, paddle, sb, ball, bricks):
    ball.ball_in_game = False
    stats.heart_left -= 1
    if stats.heart_left > 0:

        sb.prep_heart()

        screen_rect = screen.get_rect()
        ball.rect.centerx = screen_rect.centerx
        ball.rect.bottom = paddle.rect.top
        paddle.center_paddle()

        sleep(1.0)

    else:
        bricks.empty()

        paddle.center_paddle()
        screen_rect = screen.get_rect()
        ball.rect.centerx = screen_rect.centerx
        ball.rect.bottom = paddle.rect.top
        # вывести счет на экран
        ball.ball_in_game = False
        stats.game_active = False


def update_bricks(bricks):
    bricks.update()


def update_ball(settings, screen, stats, paddle, sb, bricks, ball):
    ball.update()
    check_ball_collisions(settings, stats, paddle, sb, bricks, ball)
    check_ball_bottom(stats, screen, paddle, sb, bricks, ball)


def update_screen(settings, screen, stats, sb, paddle, bricks, ball, play_button):
    screen.blit(settings.bg_img, (0, 0))  # картинка на фон

    paddle.blitme()

    ball.blitme()

    sb.show_score()
    bricks.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()  # отрисовка экрана по каждому тику
