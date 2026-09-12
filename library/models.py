from django.db import models

class TheLoai(models.Model):
    ten = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Thể loại"
        verbose_name_plural = "Danh sách Thể loại"

    def __str__(self):
        return self.ten


class TacGia(models.Model):
    ho_ten = models.CharField(max_length=150)
    quoc_tich = models.CharField(max_length=100, default='Việt Nam')

    class Meta:
        verbose_name = "Tác giả"
        verbose_name_plural = "Danh sách Tác giả"

    def __str__(self):
        return self.ho_ten


class Sach(models.Model):
    tieu_de = models.CharField(max_length=255)
    nam_xuat_ban = models.IntegerField()
    so_trang = models.IntegerField()
    gia = models.DecimalField(max_digits=10, decimal_places=2)
    mo_ta = models.TextField(blank=True)
    
    the_loai = models.ForeignKey(
        TheLoai, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='sach_list'
    )
    
    tac_gia = models.ManyToManyField(TacGia, related_name='sach_list', blank=True)

    class Meta:
        verbose_name = "Sách"
        verbose_name_plural = "Danh sách Sách"

    def __str__(self):
        return self.tieu_de