# -*- mode: python ; coding: utf-8 -*-

base_path = 'C:\\Users\\alzat\\Documents\\POO'

datas = [
    (f'{base_path}\\imagenes', 'imagenes'),
    (f'{base_path}\\adminGeneral.py', '.'),
    (f'{base_path}\\cocinero.py', '.'),
    (f'{base_path}\\database.py', '.'),
    (f'{base_path}\\facturacion.py', '.'),
    (f'{base_path}\\local.py', '.'),
    (f'{base_path}\\login.py', '.'),
    (f'{base_path}\\main.py', '.'),
    (f'{base_path}\\mesero.py', '.'),
    (f'{base_path}\\pedido.py', '.'),
    (f'{base_path}\\productos.py', '.'),
    (f'{base_path}\\reporteVentas.py', '.'),
    (f'{base_path}\\ventanaPrincipal.ui', '.'),
    (f'{base_path}\\venvD\\Lib\\site-packages\\PyQt5\\*', 'PyQt5'),
]

a = Analysis(
    ['main.py'],
    pathex=[base_path],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='FoodAlfaS.A',
    icon=r'C:\\Users\\alzat\\Documents\\POO\\imagenes\\icono.ico',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)