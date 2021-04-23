import psutil

drives = ['C:\\', 'D:\\', 'E:\\', 'G:\\', 'H:\\', 'I:\\', ]
obj_drives = []

def GetDriveSpace():
    print("-GETTING HARD DRIVE SPACE")

    disk_c = psutil.disk_usage('C:\\')
    disk_c_gb = [int(disk_c.total / (1024.0 ** 3)), int(disk_c.used / (1024.0 ** 3)), int(disk_c.free / (1024.0 ** 3))]
    disk_h = psutil.disk_usage('H:\\')
    disk_h_gb = [int(disk_h.total / (1024.0 ** 3)), int(disk_h.used / (1024.0 ** 3)), int(disk_h.free / (1024.0 ** 3))]
    disk_i = psutil.disk_usage('I:\\')
    disk_i_gb = [int(disk_i.total / (1024.0 ** 3)), int(disk_i.used / (1024.0 ** 3)), int(disk_i.free / (1024.0 ** 3))]

    data_return = [disk_c, disk_h, disk_i, disk_c_gb, disk_h_gb, disk_i_gb]

    return data_return