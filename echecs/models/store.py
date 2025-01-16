from echecs.models.storePlayer import StorePlayer


class Store:

    def __init__(self, storage_file="data.json"):
        self.players = StorePlayer()
