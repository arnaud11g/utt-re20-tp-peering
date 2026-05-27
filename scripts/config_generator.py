from jinja2 import Environment, FileSystemLoader
import json

env = Environment(loader=FileSystemLoader("templates"))

dataset = open

with open("dataset.json") as f:
    dataset = json.load(f)

for network in dataset["networks"]:

    # Generate C8200 initial config
    template = env.get_template("c8200/c8200_initial_config.j2")
    rendered_config = template.render(network)
    if network["id"] < 10:
        with open(
            f"../configuration_files/0{network["id"]} - {network["name"]}/c8200_initial_config_0{network["id"]}.cfg",
            "w",
        ) as f:
            f.write(rendered_config)
    else:
        with open(
            f"../configuration_files/{network["id"]} - {network["name"]}/c8200_initial_config_{network["id"]}.cfg",
            "w",
        ) as f:
            f.write(rendered_config)

    # Generate C8200 iBGP config
    template = env.get_template("c8200/c8200_ibgp_config.j2")
    rendered_config = template.render(network)
    if network["id"] < 10:
        with open(
            f"../configuration_files/0{network["id"]} - {network["name"]}/c8200_ibgp_config_0{network["id"]}.cfg",
            "w",
        ) as f:
            f.write(rendered_config)
    else:
        with open(
            f"../configuration_files/{network["id"]} - {network["name"]}/c8200_ibgp_config_{network["id"]}.cfg",
            "w",
        ) as f:
            f.write(rendered_config)

    # Generate C8200 peering interface
    template = env.get_template("c8200/c8200_peering_interface_config.j2")
    for device in network["devices"]:
        if device["name"] == f'c8200-{network["name_slug"]}':
            rendered_config = template.render(device)
            if network["id"] < 10:
                with open(
                    f"../configuration_files/0{network["id"]} - {network["name"]}/c8200_peering_interface_config_0{network["id"]}.cfg",
                    "w",
                ) as f:
                    f.write(rendered_config)
            else:
                with open(
                    f"../configuration_files/{network["id"]} - {network["name"]}/c8200_peering_interface_config_{network["id"]}.cfg",
                    "w",
                ) as f:
                    f.write(rendered_config)

    # Generate C8200 eBGP RS config
    template = env.get_template("c8200/c8200_ebgp_rs_config.j2")
    rendered_config = template.render(network)
    if network["id"] < 10:
        with open(
            f"../configuration_files/0{network["id"]} - {network["name"]}/c8200_ebgp_rs_config_0{network["id"]}.cfg",
            "w",
        ) as f:
            f.write(rendered_config)
    else:
        with open(
            f"../configuration_files/{network["id"]} - {network["name"]}/c8200_ebgp_rs_config_{network["id"]}.cfg",
            "w",
        ) as f:
            f.write(rendered_config)

    # Generate C9300 initial config
    template = env.get_template("c9300/c9300_initial_config.j2")
    rendered_config = template.render(network)
    if network["id"] < 10:
        with open(
            f"../configuration_files/0{network["id"]} - {network["name"]}/c9300_initial_config_0{network["id"]}.cfg",
            "w",
        ) as f:
            f.write(rendered_config)
    else:
        with open(
            f"../configuration_files/{network["id"]} - {network["name"]}/c9300_initial_config_{network["id"]}.cfg",
            "w",
        ) as f:
            f.write(rendered_config)

    # Generate C9300 iBGP config
    template = env.get_template("c9300/c9300_ibgp_config.j2")
    rendered_config = template.render(network)
    if network["id"] < 10:
        with open(
            f"../configuration_files/0{network["id"]} - {network["name"]}/c9300_ibgp_config_0{network["id"]}.cfg",
            "w",
        ) as f:
            f.write(rendered_config)
    else:
        with open(
            f"../configuration_files/{network["id"]} - {network["name"]}/c9300_ibgp_config_{network["id"]}.cfg",
            "w",
        ) as f:
            f.write(rendered_config)

    # Generate C9300 Loopback interfaces config
    template = env.get_template("common/common_loopback_config.j2")
    for device in network["devices"]:
        if device["name"] == f'c9300-{network["name_slug"]}':
            rendered_config = template.render(device)
            if network["id"] < 10:
                with open(
                    f"../configuration_files/0{network["id"]} - {network["name"]}/c9300_loopback_config_0{network["id"]}.cfg",
                    "w",
                ) as f:
                    f.write(rendered_config)
            else:
                with open(
                    f"../configuration_files/{network["id"]} - {network["name"]}/c9300_loopback_config_{network["id"]}.cfg",
                    "w",
                ) as f:
                    f.write(rendered_config)
