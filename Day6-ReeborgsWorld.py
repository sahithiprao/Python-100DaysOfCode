#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# #draw square
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()

#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def hurdle_loop():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# for i in range(0,6):
#     i = hurdle_loop()

# num_hurdles = 6

# while num_hurdles > 0:
#     hurdle_loop()
#     num_hurdles -= 1
#     print(num_hurdles)

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def hurdle_loop():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while not at_goal():
#     if  wall_in_front():
#         hurdle_loop()
#     else:
#         move()

# 4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
        
# while not at_goal():
#     if wall_in_front():
#        jump()
#     else:
#         move()

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#     move()
# turn_left()
        
# while not at_goal():
#    if right_is_clear():
#         turn_right()
#         move()
#    elif front_is_clear():
#         move()
#    else:
#         turn_left()