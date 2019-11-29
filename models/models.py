from odoo import api, fields, models
import time

class Asset(models.Model):
    _name = 'management.asset'

    asset = fields.Char(string="Nama Asset", required=True, size=100)
    pemilik = fields.Many2one(comodel_name="hr.employee", string="SKPD/UKPD Pemilik/Penanggung jawab", required=True )
    jenis_perangkat = fields.Selection(
        selection =[
            ("DC", "DC"),
            ("NON DC", "NON DC"),
        ],
        string='Jenis Perangkat',
        required=True,
    )
    ruang = fields.Char(string="Ruang/Posisi", required=True,)
    name = fields.Char(string="No.Reg/SN/IP", readonly=True, default="New")
    merek = fields.Many2one(comodel_name="master.merek", string="Merk/Model/Tipe", required=True )
    spesifikasi = fields.Char(string="Spesifikasi")
    fungsi = fields.Char(String="Fungsi")
    visit = fields.Integer(string='Visit')
    note = fields.Text(string='Note')
    gambar = fields.Binary(string='Gambar')
    maintenances_ids = fields.One2many("management.maintenances", inverse_name="asset_id", string="Maintenances", required=False)

    @api.model
    def create(self, vals):
        if not vals.get('name', False) or vals['name'] == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('management.asset') or 'Error Number!!!'
        return super(Asset, self).create(vals)

class Capacity(models.Model):
    _name = 'management.capacity'
    _description = 'Description'

    ruang_id = fields.Many2one('master.ruang', string='Ruang', required=True)

class LANDitribution(models.Model):
    _name = 'management.landistribution'
    _description = 'Description'

    ruang = fields.Char(string='Ruang')
    posisi = fields.Char(string='Posisi')
    no_reg = fields.Char(string='No.Reg/SN', required=True,)
    merek = fields.Many2one(comodel_name="master.merek", string="Merk/Model/Tipe", required=True )
    fungsi = fields.Char(string='Fungsi')
    koneksi = fields.Char(string='Koneksi LAN')
    distribusi = fields.Integer(string='Distribusi')
    visit = fields.Integer(string='Visit')
    note = fields.Text(string='Note')

class Maintenances(models.Model):
    _name = 'management.maintenances'
    _description = 'Description'

    tgl_berkunjung = fields.Date(
        string='Tanggal Berkunjung',
        required=True,
        default=lambda self:time.strftime("%Y-%m-%d")
    )
    tiket = fields.Char(string='Tiket', required=True, size=100)
    tujuan = fields.Char(string='Tujuan')
    keterangan = fields.Text(string='Keterangan')
    status = fields.Char(string='Status')
    asset_id = fields.Many2one(
        comodel_name="management.asset",
        string="Asset",
        required=False,
    )

class PowerDistribution(models.Model):
    _name = 'management.powerdistribution'

    ruang = fields.Char(string='Ruang', required=True)
    posisi = fields.Char(string='Posisi')
    no_reg = fields.Char(string='No.Reg/SN', required=True,)
    merek = fields.Many2one(comodel_name="master.merek", string="Merk/Model/Tipe", required=True )
    fungsi = fields.Char(string='Fungsi')
    koneksi = fields.Char(string='Koneksi Listrik')
    distribusi = fields.Integer(string='Distribusi')
    visit = fields.Integer(string='Visit')
    note = fields.Text(string='Note')

class Layout(models.Model):
    _name = 'management.layout'
    _description = 'Description'

class Utilisasi(models.Model):
    _name = 'management.utilisasi'
    _description = 'Description'

# ================== MASTER ================== #
class Data_user(models.Model):
    _name = 'master.data_user'
    _description = 'Description'

    username 	= fields.Char(string='Username', required=True, size=100)
    identitas 	= fields.Integer(string='Identitas')
    name 		= fields.Char(string='Nama Lengkap')
    level 		= fields.Char(string='Level')
    blokir 		= fields.Selection(
    	selection =[
    		("Y", "Yes"),
    		("N", "No")
    	],
    	default="N",
        string='Blokir',
    )
    pemandu 	= fields.Selection(
        selection =[
            ('Y', 'Yes'),
            ('N', 'No'),
        ],
        string='Pemandu',
    )
    pengelola 	= fields.Selection(
    	selection =[
    		("Y", "Yes"),
    		("N", "No")
    	],
    	default="Y",
        string='Pengelola',
    )
    temp_admin 	= fields.Selection(
    	selection =[
    		("Y", "Yes"),
    		("N", "No")
    	],
        string='Temp Admin',
    )


class Kelompok_Perangkat(models.Model):
    _name = 'master.kelompok_perangkat'
    _description = 'Description'

    name 			= fields.Char(string='Nama Kelompok Perangkat', required=True, size=100)
    no_kelompok		= fields.Integer(string='No Kelompok', size=10)
    perangkat_id 	= fields.Many2one('master.kode_perangkat', string='Kode/Golongan Perangkat')


class Lokasi(models.Model):
    _name = 'master.lokasi'
    _description = 'Description'

    no_lokasi 	= fields.Integer(string='No Lokasi', size=10)
    name 		= fields.Char(string='Lokasi', required=True, size=100)


class Ruang(models.Model):
    _name = 'master.ruang'
    _description = 'Description'

    name 		= fields.Char(string='Nama Ruang', required=True, size=100)
    no_ruang 	= fields.Integer(string='No Ruang', size=10)
    lokasi 		= fields.Many2one('master.lokasi', string='Lokasi', required=True)


class Merek(models.Model):
    _name = 'master.merek'
    _description = 'Description'

    name 		= fields.Char(string="Merek", required=True, size=64)
    tgl_created = fields.Date(string='Created', default=lambda self:time.strftime("%Y-%m-%d"))
    gambar 		= fields.Binary(string='Logo')


class Kode_Perangkat(models.Model):
    _name = 'master.kode_perangkat'
    _description = 'Description'

    no_perangkat 	= fields.Integer(string='No. Perangkat')
    name 			= fields.Char(string='Golongan Perangkat', required=True, size=100 )


class SubRuang(models.Model):
    _name = 'master.subruang'
    _description = 'Description'

    ruang_id 		= fields.Many2one( 'master.ruang', string='Ruang', required=True, size=100, )
    no_subruang 	= fields.Integer( string='No. Sub Ruang' )
    nama_subruang 	= fields.Char( string='Nama Sub Ruang')


class Subunit(models.Model):
    _name = 'master.subunit'
    _description = 'Description'

    unit_id = fields.Many2one( 'master.unit', string='Kode/Golongan Perangkat' )
    name 	= fields.Char( string='Nama Sub Unit')
    no_sub 	= fields.Integer( string='No Sub Unit' )


class Unit(models.Model):
    _name = 'master.unit'
    _description = 'Description'

    no_unit = fields.Integer( string='No Unit', )
    name 	= fields.Char( string='Nama Unit', required=True, size=100)


# ================== Document ================== #
class Agenda(models.Model):
    _name = 'document.agenda'
    _description = 'Description'

    tema = fields.Char(string='Tema', required=True, size=100)
    tgl_mulai = fields.Date(
        string='Tgl.Mulai',
        required=True,
        default=lambda self:time.strftime("%Y-%m-%d")
    )
    tgl_selesai = fields.Date(
        string='Tgl.Selesai',
        required=True,
        default=lambda self:time.strftime("%Y-%m-%d")
    )

class BCP(models.Model):
    _name = 'document.bcp'
    _description = 'Description'

    kode = fields.Char(string='Kode')
    name = fields.Char(string='BPP Name')
    date_issued = fields.Date(
        string='Date Issued',
        required=True,
        default=lambda self:time.strftime("%Y-%m-%d")
    )
    date_review = fields.Date(
        string='Date Review',
        required=True,
        default=lambda self:time.strftime("%Y-%m-%d")
    )
    date_revised = fields.Date(
        string='Date Revised',
        required=True,
        default=lambda self:time.strftime("%Y-%m-%d")
    )

class Berita(models.Model):
    _name = 'document.berita'
    _description = 'Description'

    judul = fields.Char(string='Judul', size=100, required=True)
    tgl_posting = fields.Date(
        string='Tgl.Posting',
        required=True,
        default=lambda self:time.strftime("%Y-%m-%d")
    )
    publish = fields.Boolean(string='Publish')
    isi = fields.Text(string='Isi')

class Rekuitmen(models.Model):
    _name = 'document.rekuitmen'
    _description = 'Description'

    name = fields.Char(string='Nama', size=100)
    kode = fields.Boolean(string='Kode')
    kelamin = fields.Char(string='Kelamin')
    usia = fields.Integer(string='Usia')
    pendidikan = fields.Char(string='Pendidikan')
    telp = fields.Char(string='Telp/HP')
    email = fields.Char(string='Email')
    file = fields.Char(string='File')
    pengalaman = fields.Char(string='Pengalaman')
    catatan = fields.Text(string='Catatan')

class SOP(models.Model):
    _name = 'document.sop'
    _description = 'Description'

    kode = fields.Char(string='Kode')
    name = fields.Char(string='SOP Name')
    date_issued = fields.Date(
        string='Date Issued',
        required=True,
        default=lambda self:time.strftime("%Y-%m-%d"),
    )
    date_review = fields.Date(
        string='Date Review',
        required=True,
        default=lambda self:time.strftime("%Y-%m-%d"),
    )
    date_revised = fields.Date(
        string='Date Revised',
        required=True,
        default=lambda self:time.strftime("%Y-%m-%d"),
    )