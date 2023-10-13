#!/usr/bin/env python3

import importlib.resources
import sys

import frida
from rich import print


def on_message(message, data):
    print(f"msg: {message} data: {data}")


def main():
    package_files = importlib.resources.files(__package__)
    agent_dist_dir = package_files.joinpath("agent_dist")
    compiled_agent_js_str = agent_dist_dir.joinpath("konyutils_ng_ios.js").read_text()
    self_dev = frida.get_device("local")
    session = self_dev.attach("apfsd")

    bytecode = session.compile_script(compiled_agent_js_str)
    script = session.create_script_from_bytes(name="konyutils_ng_ios", data=bytecode)
    script.on("message", on_message)
    script.load()
    api = script.exports_sync
    hello_res = api.hello()
    print(f"hello: {hello_res}")
    script.unload()
    session.detach()
    return 0


if __name__ == "__main__":
    sys.exit(main())
