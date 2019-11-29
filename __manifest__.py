{
	"name"			: "Management Addons Latihan",
	"version"		: "1.0",
	"depends"		: [
						"base",
						"hr",
					],
	"author"		: "Arman",
	"category"		: "Management",
	"website"		: "vitraining.com",
	"description"	: "Sistem Management Version 1",
	"data"	: [
				"menu.xml",
				"asset.xml",
				"powerdistribution.xml",
				"landistribution.xml",
				"capacity.xml",
				"utilisasi.xml",
				"maintenances.xml",
				"document/rekuitmen.xml",
				"document/sop.xml",
				"document/bcp.xml",
				"document/berita.xml",
				"document/agenda.xml",
				"master/lokasi.xml",
				"master/ruang.xml",
				"master/subruang.xml",
				"master/merek.xml",
				"master/unit.xml",
				"master/subunit.xml",
				"master/kode_perangkat.xml",
				"master/kelompok_perangkat.xml",
				"master/data_user.xml",
				"security/group.xml",
				"security/ir.model.access.csv",
				"data/sequence.xml",
			],

	"installable": True,
	"auto_install": False,
	"application": True,
}