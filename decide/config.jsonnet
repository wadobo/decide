# Here you can find the configuration for the decide server. This is a jsonnet
# file, it's a data template language, to learn more go to:
# https://jsonnet.org/

local host = "localhost";
local port = "8000";
local db = {
    name: "decide",
    user: "decide",
    password: "decide",
};

{
    DEBUG: false,
    SECRET_KEY: "^##ydkswfu0+=ofw0l#$kv^8n)0$i(qd&d&ol#p9!b$8*5%j1+",
    KEYBITS: 256,
    ALLOWED_VERSIONS: ["v1", "v2"],
    DEFAULT_VERSION: "v1",
    BASEURL: "http://" + host + ":" + port,

    # Modules in use, commented modules that you won"t use
    MODULES: [
        "authentication",
        "base",
        "booth",
        "census",
        "mixnet",
        "postproc",
        "store",
        "visualizer",
        "voting",
    ],

    # Endpoint for each module, if the module is served by this instance you
    # can use localhost
    APIS: {
        "authentication": $["BASEURL"],
        "base": $["BASEURL"],
        "booth": $["BASEURL"],
        "census": $["BASEURL"],
        "mixnet": $["BASEURL"],
        "postproc": $["BASEURL"],
        "store": $["BASEURL"],
        "visualizer": $["BASEURL"],
        "voting": $["BASEURL"],
    },

    DATABASES: {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": db["name"],
            "USER": db["user"],
            "PASSWORD": db["password"],
            "HOST": host,
            "PORT": "5432",
        }
    }
}

