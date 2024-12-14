
maze=Group(Rect(35, 81, 15, 300, fill='slateGrey'), Rect(50, 366,310, 15, fill='slateGrey'), 
Rect(35, 27, 315, 15, fill='slateGrey'), Rect(89, 41, 15, 100, fill='slateGrey'), 
Rect(144, 80, 15, 170, fill='slateGrey'), Rect(159, 80, 145, 15, fill='slateGrey'),
Rect(89, 190, 15, 60, fill='slateGrey'), Rect(104, 235, 40, 15, fill='slateGrey'), 
Rect(89, 295, 15, 75, fill='slateGrey'), Rect(104, 295, 105, 15, fill='slateGrey'), 
Rect(194, 200, 15, 100, fill='slateGrey'), Rect(208, 251, 50, 15, fill='slateGrey'),
Rect(159, 200, 35, 15, fill='slateGrey'), Rect(202,40, 15, 1, fill='slateGrey'), 
Rect(255, 170, 15, 96, fill='slateGrey'), Rect(207, 157, 63, 15, fill='slateGrey'), 
Rect(207, 140, 15, 30, fill='slateGrey'), Rect(350, 27, 15, 290, fill='slateGrey'), 
Rect(304, 145, 15, 150, fill='slateGrey'), Rect(310, 280, 50, 15, fill='slateGrey'), 
Rect(254, 317, 15, 50, fill='slateGrey'))

Label('Start',17, 60)
Label('End', 362, 340)
player=Circle(40, 60, 10, fill='pink')
winGametext=Label('Winner!', 200, 200, visible=False, size=50)
gameOvertext=Label('Game Over!', 200, 200, visible=False, size=50)
def gameStops():
    app.stop()
    gameOvertext.visible=True
    
coin1=Circle(153, 268,8, fill='gold', border='goldenRod', visible=True)
coin2=Circle(183, 339,8, fill='gold', border='goldenRod', visible=True)
coin3=Circle(332, 218,8, fill='gold', border='goldenRod', visible=True)
coin4=Circle(190, 114,8, fill='gold', border='goldenRod', visible=True)

def onKeyHold(keys):
    if 'up'in keys:
        player.centerY-=1
    elif 'down' in keys:
        player.centerY+=1
    elif 'right' in keys:
        player.centerX+=1
    elif 'left'in keys:
        player.centerX-=1
    if player.hits(153, 268):
        coin1.visible=False
    if player.hits(183, 339):
        coin2.visible=False
    if player.hits(332, 218):
        coin3.visible=False
    if player.hits(190, 114):
        coin4.visible=False
    if player.hitsShape(maze):
        gameStops()
    if coin1.visible==False and coin2.visible==False and coin3.visible==False and coin3.visible==False and player.centerX>=365:
        winGametext.visible=True
        app.stop()
