def sneak(label):
    def _sneak(x):
        print(f'{label} {x!r}')

        return x

    return _sneak
