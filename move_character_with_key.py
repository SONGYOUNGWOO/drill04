from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('Daco.png')


def handle_events():
    global running , right, left, up, down
    global dirx, diry

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
                right = True

            elif event.key == SDLK_LEFT:
                dirx -= 1
                left = True
            elif event.key == SDLK_UP:
                diry += 1
                up = True
            elif event.key == SDLK_DOWN:
                diry -= 1
                down = True

            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
                right = False
            elif event.key == SDLK_LEFT:
                dirx += 1
                left = False
            elif event.key == SDLK_UP:
                diry -= 1
                up = False
            elif event.key == SDLK_DOWN:
                diry += 1
                down = False

running = True
right = False
up = False
down = False
left = False
keydown = False
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
dirx = 0
diry = 0

while running:

    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if x < 0:
        x = 0
    elif x > TUK_WIDTH:
        x = TUK_WIDTH

    if y < 0:
        y = 0
    elif y > TUK_HEIGHT:
        y = TUK_HEIGHT

    if (right):
        character.clip_draw(frame * 121, 120, 121, 120, x, y)
    elif (left):
        character.clip_draw(frame * 121, 0, 121, 120, x, y)
    elif (up):
        character.clip_draw(frame * 121, 121 * 3, 121, 120, x, y)
    elif (down):
        character.clip_draw(frame * 121, 121 * 2, 121, 120, x, y)
    else:
        character.clip_draw(121 * 2, 121 * 2, 121, 120, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dirx * 5
    y += diry * 5
    delay(0.01)

close_canvas()

