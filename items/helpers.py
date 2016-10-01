from items.item import *


def sell(item, store, player):
    """
    :param item A item the player wants to sell
    :param store The place that wants to buy the item
    :param player The player selling the item
    """
    if item in player.inventory:
        store.inventory += item
        player.inventory -= item
        player.money += item.Value


def buy(item, player, store):
    assert isinstance(item, Item)
    assert isinstance(item.Value, int)
    if item in store.inventory:
        store.inventory -= item
        player.inventory += item
        player.money -= item.Value
