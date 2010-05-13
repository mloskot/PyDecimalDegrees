# -*- coding: utf-8 -*-
"""
Example of PyDecimalDegrees usage.

Created by Mateusz Łoskot <mateusz@loskot.net>
Altered by Evan Wheeler <ewheeler@unicef.org>

"""

import decimaldegrees as dd

# Input coordinate in DMS format
coord = { "degrees": 121, "minutes": 8, "seconds": 6 }

# Convert coordinate from DMS to DD
d = dd.dms2decimal(coord["degrees"], coord["minutes"], coord["seconds"])
print d

# Convert coordinate DD to DM
dm = dd.decimal2dm(d)
print dm

# Convert coordinate from DD to back to DMS
dms = dd.decimal2dms(d)
print dms

