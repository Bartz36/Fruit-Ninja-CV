from pynput import mouse
while True:
    controller = mouse.Controller()
    x, y = controller.position
    print("x: ", x, " y: ", y)

    # x = 1920
    # y = 1080

    