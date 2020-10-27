order = [4, 4, 6]
widgets = 8

def fillOrders(order, widgets):
    pedides = 0
    for o in order:
        if o <= widgets:
            pedides += 1
            widgets = widgets - o
    return pedides

result = fillOrders(order, widgets)

print(result)