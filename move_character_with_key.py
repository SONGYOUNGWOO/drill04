from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('Daco.png')


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


while running:

    clear_canvas()
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dirx * 5
    y += diry * 5
    delay(0.01)


close_canvas()
