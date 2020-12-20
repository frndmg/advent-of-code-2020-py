from functools import partial, reduce, wraps


def compose(*F):
    return reduce(lambda f, g: lambda x: f(g(x)), F)


def fmap(f):
    return partial(map, f)


def ffilter(f):
    return partial(filter, f)


def fnone(func, default=None):
    @wraps(func)
    def _func(x):
        if x is not None:
            return func(x)

        return default

    return _func


def tupled(func):
    @wraps(func)
    def _func(x):
        return func(*x)

    return _func


def tuple_map(*fs):
    return compose(
        tuple,
        partial(
            map,
            tupled(lambda i, v: fs[i](v) if i < len(fs) and fs[i] else v),
        ),
        enumerate,
    )


def identity(x):
    return x


def apply(f, *args, **kwargs):
    return f(*args, **kwargs)


def length(xs):
    len_ = getattr(xs, '__len__', None)

    def default_len():
        return sum(1 for _ in xs)

    return compose(
        apply,
        fnone(identity, default=default_len)
    )(len_)
