#border effect on hover
def onEnter(event, var):
    var.configure(border_color="white")

#border effect out on removing cursor
def onLeave(event, var):
    var.configure(border_color="black")

