import os
import json
from dataclasses import dataclass, asdict

PATH = '/tmp/my_vars/'
RESULTS_PATH = '/tmp/my_vars/results/'

if not os.path.isdir(RESULTS_PATH):
	os.makedirs(RESULTS_PATH)

if not os.path.isdir(PATH):
	os.makedirs(PATH)

FILES = []

for file in os.listdir(PATH):
	FILES.append(os.path.join(PATH, file))

data = []

@dataclass
class Entry:
	address: str
	broadcast: str
	netmask: str
	network: str
	prefix: int
	public: str


@dataclass
class Server:
	private_ip: str
	public_ip: str
	subnet: str


@dataclass
class ServerConfig:
	name: str
	from_server: Server
	to_server: Server


for file in FILES:
	if not os.path.isfile(file):
		continue

	with open(file) as fl:
		public = os.path.splitext(os.path.basename(file))[0]
		content = json.load(fl)
		data.append(Entry(**content, public=public))


def create_config(pitcher_data, catcher_data, position="east", public=None):
	return ServerConfig(
		name = position,
		from_server = Server(
			private_ip = pitcher_data.address,
			public_ip = public,
			subnet = f'{pitcher_data.network}/{pitcher_data.prefix}'
		),
		to_server = Server(
			private_ip = catcher_data.address,
			public_ip = public,
			subnet = f'{catcher_data.network}/{catcher_data.prefix}'
		)
	)

dataset = [
	create_config(data[1], data[0], position="west", public=data[0].public),
	create_config(data[1], data[0], position="east", public=data[1].public)

	# create_config(data[1], data[0],public=data[0].public),
	# create_config(data[0], data[1], position="west", public=data[1].public)
]


for file in dataset:
	file_location = os.path.join(RESULTS_PATH, f'{file.from_server.public_ip}.json')
	with open(file_location, 'w') as fl:
		content = json.dumps(asdict(file), indent=4)
		fl.write(content)
