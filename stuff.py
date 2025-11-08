import pprint
import sys
from pathlib import Path

import typeshed_client

context = typeshed_client.SearchContext(
    typeshed=(typeshed := Path("./typeshed/stdlib")),
    search_path=[],
    version=sys.version_info[:2],
    platform="linux"
)

stdlib_modules = set(sys.stdlib_module_names)

for full_name, path in typeshed_client.get_all_stub_files(search_context=context):
    name, nested, rest = full_name.partition(".")
    if nested:
        continue
    stdlib_modules.discard(name)

pprint.pprint(stdlib_modules)
