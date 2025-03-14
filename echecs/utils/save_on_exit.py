def save_on_exit(store_arg=0):
    """
    Décorateur qui sauvegarde les données à la fin de l'exécution d'une fonction.

    Args:
        store_arg: Position de l'argument (int) ou nom du keyword argument (str) contenant le store
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            # Récupérer le store selon sa position ou son nom
            if isinstance(store_arg, int) and len(args) > store_arg:
                store = args[store_arg]
            elif isinstance(store_arg, str) and store_arg in kwargs:
                store = kwargs[store_arg]
            else:
                raise ValueError(f"Impossible de trouver le store à la position {store_arg}")

            store.save_data()
            return result

        return wrapper

    return decorator
