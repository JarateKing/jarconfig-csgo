Buys = [
	"ak47",
	"aug",
	"awp",
	"bizon",
	"deagle",
	"decoy",
	"defuser",
	"elite",
	"famas",
	"fiveseven",
	"flashbang",
	"g3sg1",
	"galilar",
	"hegrenade",
	"incgrenade",
	"m249",
	"m4a1",
	"mac10",
	"mag7",
	"molotov",
	"mp7",
	"mp9",
	"negev",
	"nova",
	"p250",
	"p90",
	"revolver",
	"sawedoff",
	"scar20",
	"sg556",
	"smokegrenade",
	"ssg08",
	"taser",
	"tec9",
	"ump45",
	"vest",
	"vesthelm",
	"xm1014",
]

Combos = [
	[ "vesthelm", "vest" ],
	[ "ak47", "m4a1" ],
	[ "aug", "sg556" ],
	[ "famas", "galilar" ],
	[ "g3sg1", "scar20" ],
	[ "mac10", "mp9" ],
	[ "mag7", "sawedoff" ],
	[ "fiveseven", "tec9" ],
	[ "deagle", "revolver" ],
	[ "incgrenade", "molotov" ],
]

for wep in Buys:
	print('alias jar_buy_', wep, ' "buy ', wep, '"', sep='')

for weps in Combos:
	print('alias jar_buy_', weps[0], '+', weps[1], ' "buy ', weps[0], '; buy ', weps[1], '"', sep='')