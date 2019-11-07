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
# => git branch (nama branch) = cara membuat branch
# => git branch  -a = mengecek ada branch apa aja
# => git branch -D (nama branch nya) = untuk menghapus branch yang dimaksud
# => git branch checkout (nama branch) = untuk masuk ke branch nya
# => git merged ( nama branch) = menggabungkan antar branch -> command harus dari master
# => git checkout -b (nama branch baru) = bikin branch baru sekaligus masuk ke branch itu
# => git clone (link di github) = mendownload project yang ada di git hub
# => git remote add = masuk ke project yang ada di github
class X :
    def __init__(self):
        self.nama = 'andi'
andi = X()
print(andi.nama)