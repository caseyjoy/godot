def can_build(env, platform):
    env.module_add_dependencies("basis_universal", ["jpg", "tinyexr"])
    return True


def configure(env):
    pass
