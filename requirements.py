#INFO: install latest version main packages, stay up to date, freeze only for deployment

import sys
import os

PACKAGES=[
	'discord',
	'requests',
	'sqlmodel',
	'pydantic',
	'annotated-types',
	'email-validator',
	'SQLAlchemy',
	'aiosqlite', #U: we always include sqlite for testing, etc
]

if not '-nopg' in sys.argv:
	PACKAGES= PACKAGES+ ['asyncpg']

os.system('pip install --upgrade pip')
for pkg in PACKAGES:
	os.system(f"pip install {pkg}")
