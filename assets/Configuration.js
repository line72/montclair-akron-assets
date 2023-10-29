/* -*- Mode: rjsx -*- */

/*******************************************
 * Copyright (2018)
 *  Marcus Dillavou <line72@line72.net>
 *  http://line72.net
 *
 * Montclair:
 *  https://github.com/line72/montclair
 *  https://montclair.line72.net
 *
 * Licensed Under the GPLv3
 *******************************************/

import AvailtecParser from './AvailtecParser';

class Configuration {
    constructor() {
        // Akron, OH
        this.center = [41.084569, -81.515555];
        this.tileserver = {
            url: 'https://akron.gotransitapp.com/tiles/{z}/{x}/{y}.png',
            subdomains: ''
        };

        this.agencies = [
            {
                name: 'Routes',
                hideRouteNumber: true,
                parser: new AvailtecParser('https://akron.gotransitapp.com/api/no.php/InfoPoint')
            }
        ];
    }
}

export default Configuration;
