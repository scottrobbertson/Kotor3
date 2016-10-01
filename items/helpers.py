def sell(item, store, player):
    if item in player.inventory:
        store.inventory += item
        player.inventory -= item
        player.money += item.Value


def buy(item, player, store):
    if item in store.inventory:
        store.inventory -= item
        player.inventory += item
        player.money -= item.Value
