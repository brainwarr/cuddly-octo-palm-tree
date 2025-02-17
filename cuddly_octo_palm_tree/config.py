import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="cuddly_octo_palm_tree",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="cuddly_octo_palm_tree_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from cuddly_octo_palm_tree.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export cuddly_octo_palm_tree_KEY=value
export cuddly_octo_palm_tree_KEY="@int 42"
export cuddly_octo_palm_tree_KEY="@jinja {{ this.db.uri }}"
export cuddly_octo_palm_tree_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
cuddly_octo_palm_tree_ENV=production cuddly_octo_palm_tree run
```

Read more on https://dynaconf.com
"""
