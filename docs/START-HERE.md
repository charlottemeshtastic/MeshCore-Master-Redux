# Start here

Get from a new device to a first message in six steps. App screens and board procedures vary; follow the instructions for your exact hardware.

1. **Find a local network.** Use the [community directory](../README.md#communities) and [official map](https://map.meshcore.io/). Ask local operators which radio preset, channels and routing scopes they use. A map marker alone does not establish usable coverage.
2. **Choose a supported device and role.** Confirm the exact board and radio variant in the [official flasher](https://flasher.meshcore.io/) before buying. A companion connects to a phone or computer; a repeater supplies infrastructure; a room server stores messages; standalone firmware provides an on-device interface. Start with a companion for phone-based chat. See [hardware references](../README.md#hardware).
3. **Install the matching firmware.** Attach the correct antenna, power the board, and follow the flasher's board-specific instructions. For USB, use a data-capable cable and a browser supported by the flasher. Choose the companion transport your client needs. Save an existing configuration before an update; erase only when the board instructions require it.
4. **Choose and connect an app.** See the [app comparison](APP-COMPARISON.md). Install from the project's published download or store link, connect to your radio, and let contacts/channels synchronize. If pairing fails, use [troubleshooting](TROUBLESHOOTING.md).
5. **Match your community's configuration.** Confirm the radio parameters and channel configuration with local operators. The [official preset reference](https://docs.meshcore.io/radio_presets/) explains how presets are supplied. Community settings can differ from a national preset; routing scopes and channel keys serve different purposes. Set a recognizable node name and replace default Bluetooth/admin credentials where supported.
6. **Test a first message.** Send one short message to an agreed channel or a nearby known contact. For a direct message, check delivery status and ask the recipient to reply. If it fails, compare settings and test two companions nearby before troubleshooting a longer route. Improve antenna placement and seek local guidance before adding a repeater.

For an illustrated introduction, see the [official companion quick-start PDF](https://files.liamcottle.net/MeshCore/Documentation/MeshCore_Quick_Start_Guide.pdf). It may show older app screens; current device and app documentation takes precedence.

For repeater and room-server administration, use the [official CLI reference](https://docs.meshcore.io/cli_commands/) and [USB configuration tool](https://config.meshcore.io/).

Last reviewed: October 9, 2026. This guide summarizes linked documentation; it is not a hardware test report.
