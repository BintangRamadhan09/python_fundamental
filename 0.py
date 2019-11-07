# => git add (nama file) = untuk add file di staging
# => git add . = untuk add semua file
# => git rm --cached (nama file) = remove file yang sudah di stagging
# => git commit -m "" = untuk menambah chackpoint(setip selesai satu fitur)
# => git log = untuk menecek status
# => git log --one line ( cek status yang penting aja )
# => git checkout (id commit) = kembali ke commit yang dituju
# => git checkout master = kembali(ngecek yang lalu)
# => git reset (id commit) = balikin lagi sebelum commit
# => git reset (id commit) --hard = balikin ke bener2 awal

class X :
    def __init__(self):
        self.nama = 'andi'
andi = X()
print(andi.nama)