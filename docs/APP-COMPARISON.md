# App comparison

A starting shortlist, not an exhaustive ranking. These facts were checked against the projects' own README files on October 9, 2026. “Not documented” means the reviewed source did not establish support. Platform support in source code does not guarantee a downloadable build or identical features on every platform. All rows below publish source code; linked projects retain their own licenses.

| Client / source | Platforms described by project | Radio connections | Offline maps | Installation / important limits |
| --- | --- | --- | --- | --- |
| [MeshCore Open](https://github.com/zjs81/meshcore-open) | Android, iOS, Windows, Linux, macOS, web | Native: BLE and TCP; USB except iOS. Web: USB only through Web Serial | Yes; README specifies a configured Stadia Maps source and API key | Use the installation website linked from the README or its releases. Web requires compatible Chromium; no browser BLE/TCP. |
| [MeshCore TEAM](https://github.com/tmacinc/MeshCore-TEAM) | Android and iOS | BLE; USB/TCP not established by reviewed README | Yes; downloads and KMZ overlays | Use the project's installation links. Basic messaging works with stock firmware; smart forwarding and autonomous tracking require its custom firmware. |
| [MeshCore One](https://github.com/Avi0n/MeshCoreOne) | iOS, iPadOS and Apple Silicon Mac | Bluetooth and Wi-Fi; USB not established by reviewed README | Yes; offline download listed | App Store or unsigned IPA releases linked by the project. Check current OS requirements in its README. |
| [PommeCore](https://github.com/mbedworth/PommeCore) | iPhone, iPad, Mac; watchOS companion | BLE on iOS/macOS; TCP over Wi-Fi; USB serial on macOS | Not documented in reviewed README | Follow the project's build/distribution instructions; do not assume an App Store release. Apple Watch is a companion interface. |
| [Offband MeshCore](https://github.com/OffbandMesh/meshcore-client) | Android, Windows; source support also described for iOS, macOS, Linux and web | Native BLE/USB/TCP with platform limits; README marks iOS USB/TCP in progress | Yes; map tile downloads | README offers Android APK and Windows ZIP; iOS/macOS/Linux require source builds. Release candidate status; browser TCP requires a bridge. |
| [mesh-client](https://github.com/Colorado-Mesh/mesh-client) | Windows, macOS and Linux | MeshCore BLE, USB serial, TCP and MQTT | Yes; cached tiles and explicit region downloads | Use its published releases. Multi-protocol desktop suite; MQTT is an internet transport, separate from a direct radio connection. |

BLE means Bluetooth Low Energy. TCP generally means a network connection to a compatible radio or bridge; it does not turn every Bluetooth device into a Wi-Fi device. USB requires the correct companion firmware and platform support.

For the proprietary official companion app, its web distribution and other clients, see the [full client directory](../README.md#client). Confirm downloads through each project's own page rather than using third-party mirrors.
