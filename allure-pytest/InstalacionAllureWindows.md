# Instalación de Allure en Windows con Scoop

## 1. Instalar Scoop

1. Abre PowerShell como administrador.

2. Ejecuta el siguiente comando para instalar Scoop:
```powershell
   iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
```
3. Configura la ejecución de scripts:

```powershell
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
```

## 2. Instalar Allure con Scoop
Ejecuta el siguiente comando para instalar Allure:

```powershell
scoop install allure
```

## 3. Verificar la instalacion
Ejecuta para verificar la instalación:

```powershell
allure --version
```