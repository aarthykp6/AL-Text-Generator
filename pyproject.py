[[package]]
name = "aiohttp"
version = "3.8.1"
description = "Async http client/server framework (asyncio)"
category = "main"
optional = false
python-versions = ">=3.6"

[package.dependencies]
aiosignal = ">=1.1.2"
async-timeout = ">=4.0.0a3,<5.0"
attrs = ">=17.3.0"
charset-normalizer = ">=2.0,<3.0"
frozenlist = ">=1.1.1"
multidict = ">=4.5,<7.0"
yarl = ">=1.0,<2.0"

[package.extras]
speedups = ["aiodns", "brotli", "cchardet"]

[[package]]
name = "aiosignal"
version = "1.2.0"
description = "aiosignal: a list of registered asynchronous callbacks"
category = "main"
optional = false
python-versions = ">=3.6"

[package.dependencies]
frozenlist = ">=1.1.0"

[[package]]
name = "async-timeout"
version = "4.0.2"
description = "Timeout context manager for asyncio programs"