# -*- mode: python -*-

import transmogrifier

CONFIG = transmogrifier.Config(
    build_dir = './build',
    repo = 'akron',
    package_name = 'montclair-akron',
    name = 'Go Akron',
    description = 'Real Time Tracking of the Buses for Akron, OH',
    url = 'https://akron.gotransitapp.com',
    logo_svg = 'assets/logo.svg',
    montclair_config = transmogrifier.MontclairConfig(
        version = '1.4.0',
        revision = 1,
        title = 'Go Akron',
        first_run_text = "Welcome to Akron, OH's Real Time Bus Tracker.<br /><br />Please select one or more routes to begin!",
        configuration_js_file = 'assets/Configuration.js'
    ),
    ios_config = transmogrifier.MontclairiOSConfig(
        version = '2.0.4',
        revision = 1,
        app_id = 'com.gotransitapp.akron',
        app_store_id = 'REPLACE_ME',
        app_store_url = 'https://apps.apple.com/us/app/go-akron/idREPLACE_ME'
    ),
    android_config = transmogrifier.MontclairAndroidConfig(
        version = '1.0.2',
        revision = 1,
        app_id = 'com.gotransitapp.akron',
        play_store_url = 'https://play.google.com/store/apps/details?id=com.gotransitapp.akron'
    )
)
