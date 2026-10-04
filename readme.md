# mirocard-plotly

A small [Plotly Dash](https://dash.plotly.com/) web app that plots the power consumption
of a MiroCard application run, recorded with the
[RocketLogger](https://rocketlogger.ethz.ch/) (ETH Zurich) and stored in
`data/mirocard_triggered_data_app.rld` (about 30 MB).

The app was contributed by [@Haptein](https://github.com/Haptein) (PR #1) and is set up
for deployment on Heroku (`Procfile`, `gunicorn app:server`).

## Run locally

```
$ pip3 install -r requirements.txt
$ gunicorn app:server     # then open http://127.0.0.1:8000
```

`app.py` only exposes `server` for gunicorn; it does not call `app.run_server()`, so
`python3 app.py` alone will not start a server.

## MiroCard project

Project website: <https://ansgomez.github.io/mirocard-website/>

The MiroCard is a batteryless, light-powered BLE smart card, designed by Andres Gomez
(Miromico AG) and inspired by the
[Transient BLE Node](https://gitlab.ethz.ch/tec/public/employees/sigristl/transient_ble_node)
project developed at ETH Zurich. It was presented in:

> Andres Gomez. 2020. *Demo Abstract: On-Demand Communication with the Batteryless MiroCard.*
> In The 18th ACM Conference on Embedded Networked Sensor Systems (SenSys '20).
> [doi:10.1145/3384419.3430440](https://doi.org/10.1145/3384419.3430440)

Related repositories:

| Repository | Contents |
| --- | --- |
| [mirocard-hardware](https://github.com/ansgomez/mirocard-hardware) | Hardware: datasheet, schematics and Altium PCB project (MiroCard V2.0) |
| [mirocard-contiki-ng](https://github.com/ansgomez/mirocard-contiki-ng) | Firmware: Contiki-NG fork with the MiroCard platform and example applications |
| [miroreader-app](https://github.com/ansgomez/miroreader-app) | Android app to receive and display MiroCard beacons |
| [mirocard-scanner-python](https://github.com/ansgomez/mirocard-scanner-python) | Python scripts to scan for and decode MiroCard beacons (bluepy) and discover devices (gattlib) |
| [mirocard-scanner-mqtt](https://github.com/ansgomez/mirocard-scanner-mqtt) | Node.js bridge forwarding MiroCard beacons to an MQTT broker |
| [mirocard-scanner-influx](https://github.com/ansgomez/mirocard-scanner-influx) | Node.js bridge storing MiroCard beacons in InfluxDB |
| [mirocard-webid](https://github.com/ansgomez/mirocard-webid) | Web Bluetooth demo page for identification and sensor readout |
| [mirocard-postprocessing](https://github.com/ansgomez/mirocard-postprocessing) | Jupyter notebook to post-process RocketLogger power measurements |
| **mirocard-plotly** (this repository) | Plotly Dash web app visualizing a RocketLogger measurement |

## License

BSD-3-Clause. Copyright (c) 2022, Andres Gomez and [@Haptein](https://github.com/Haptein), who wrote the Dash app (`app.py`). See [LICENSE](LICENSE).
