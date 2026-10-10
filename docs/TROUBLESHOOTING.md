# Troubleshooting

Work through the symptom that matches your problem. Record the exact board, firmware version, app version and connection type before asking for help. Back up settings before resetting or reflashing.

| Symptom | Checks to try first |
| --- | --- |
| App cannot find or pair with radio | Confirm companion firmware supports BLE, enable Bluetooth and the app's required permissions, and disconnect any other client using the radio. Use the board's displayed/configured PIN rather than assuming a universal PIN. Restart the app and radio; follow the client's pairing instructions before resetting settings. |
| USB connection unavailable | Use a data cable, check the board's USB/bootloader instructions, select the correct serial device, and close any other app holding the port. Confirm USB companion firmware. For browser clients, check Web Serial support; MeshCore Open's web client requires a compatible Chromium browser. |
| No nearby nodes or map markers | Verify local radio parameters, antenna connection and placement. Give discovery time and compare with a known nearby operator. Contacts may lack coordinates; a public map may be stale or require uploads, so an empty map is not proof that the radio is broken. |
| Channel messages are not seen | Compare frequency, bandwidth, spreading factor, coding rate and channel key/configuration with the intended peer. Check region scope and the repeaters' forwarding rules. Matching channel names alone does not establish matching keys. |
| Direct messages fail | Refresh the recipient contact/advert, check route or path information, and test near the recipient. Distinguish an app's “sent” status from an acknowledged delivery. Check that the recipient is powered and connected to a usable route; avoid repeatedly flooding retries. |
| Firmware flash/update fails | Match the exact board and update method, use stable power and a data cable, and check bootloader/DFU instructions. USB flashing, Bluetooth DFU and Wi-Fi OTA are different procedures. Do not erase or load another board's image as a generic fix. |
| Repeater is invisible or will not forward | Verify its role, radio configuration, antenna, power and advert settings. Check routing scopes and allowed forwarding rules with local operators. Inspect status using the official USB config tool or CLI. Change one setting at a time and save the prior configuration. |
| Offline map is blank | Download the intended area while online and confirm the app's tile source/API-key requirements. Cached coverage and zoom levels vary; having offline messaging does not imply downloaded map tiles. |

Use the [official FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md), [CLI commands](https://docs.meshcore.io/cli_commands/) and [USB configuration tool](https://config.meshcore.io/) for current device guidance. See the [app comparison](APP-COMPARISON.md) for transport limitations.

When reporting a problem, include reproduction steps and expected/actual behavior. Remove channel secrets, private keys, admin credentials and precise private locations from logs or screenshots. Use the affected project's issue tracker for app/firmware bugs; this list's issue tracker is for resource and documentation corrections.

Last reviewed: October 9, 2026. These are diagnostic checks, not guaranteed fixes for every firmware or device.
