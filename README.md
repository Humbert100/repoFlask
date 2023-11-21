# REPO FLASK
---
Este es un repo que hice para montar una vm instance y ejecutar app.py usando PUTTY (si planeas usarlo).
<br>
A continuación están los pasos que seguí (espero no se me olvide alguno).
<br>
Aclaro, sólo se encuentra NUESTRO modelo no otra cosa.
<br>
Los requirements originales están al inicio del repo.
<br>
Si quieres conectarte a la vm instance que tengo igual te puedo pasar la ipv4, el private key y user.
---
A) **Creación de vm Instance**
1. Creé una vm instance con estas características:
   <br>
   1.1 Image: Oracle Linux 8
   <br>
   ### **Me comentaron que uses mejor ubuntu y te ahorras tantos problemas, pero si aún sigues teniendo problemas quizas te ayude algo de aquí.**
   <br>
   1.2 Shape: VM.Standard.E2.1 (cambié el shape porque cuando traté de instalar, usando el shape por default, el torch se moría el proceso).
   <br>
   1.3 Si usas Putty, necesitas descargar un private key.
   <br>
3. Añadí reglas de seguridad para poder acceder a la instancia (si no más recuerdo son la de all ports):
   <br>
   2.1 Ingress Rules 
   <br>
   ![image](https://github.com/Humbert100/repoFlask/assets/93540685/dcd18478-f1f3-43b1-a18b-b0a36774fb9a)
   <br>
   2.2 Egress Rules
   <br>
   ![image](https://github.com/Humbert100/repoFlask/assets/93540685/d2e875df-08ad-4f17-8553-2816d269559a)
4. Probar (si quieres probar la conexión a tu vm instance)
   <br>
   Usa el comando en terminal: `ping <IPv4 address>`.
   
B) **Instalación y uso de Putty**
<br>
Para conectarte a la vm instance necesitarás que tu private key se encuentre en formato .ppk, para eso puedes hacer esto:
<br>
1. Abre Puttygen <br>
2. En "Load an existing private key file" carga la llave (elige todos los archivos). <br>
3. Te aparece un cuadro de diálogo, dale Aceptar. <br>
4. Da clic en "Save private key". <br>
5. Te aparece otro cuadro de diálogo, dale Sí. <br>
6. Ahora abre Putty. <br>
7. En "Session" pon tu IPV4 address. <br>
8. En "Data" (connection) pon opc.
9. En "Tunnels" (SSH):
   <br>
   9.1 En "Source port" pon 22.
   <br>
   9.2 En "Destination" pon tu `<IPv4 address:Port>`.
10. En "Credentials" (Auth) pon tu private key.
11. Si quieres (es deseable) guarda la sesión.
12. Abre tu sesión, te aparecerá otro cuadro de diálogo, dale que si de todos modos.
13. Ya estas adentro!
    
C) **Configuración de tu vm instance.**
1. Revisa tu versión de pthon y observarás que estás en python 3.6.8, para ultralytics necesitarás tener una versión mayor a 3.8.
2. Instala python 3.9 con `sudo yum install python39`.
3. Cambia a esa versión con `sudo update-alternatives --config python` y selecciona la versión.
4. Instala tu virtual environment, lo necesita tu Flask (si lo vas a ocupar) con `python3.9 -m venv <name of your venv>`.
5. Activa tu venv con `source myenv/bin/activate`.
6. Ya estás adentro!
7. Instala git con `sudo yum install git`.
8. Cona el repo (si lo vas a usar).
9. Instala mesa-libGL `sudo yum install mesa-libGL`, no recuerdo cual error me mostraba el requeriments pero lo necesitas.
10. Dentro de yolov5 instala los requeriments (estána modificados para que no tengas problemas porque los tuve).
11. Instala flask con `pip install Flask`.
12. Por alguna razón, siempre antes de correr flask, te muestra un error de que no encuentra pandas, lo tienes que instalar.
13. Corre tu flask con `flask run`.
14. Si corre,👌; si no, algo se me olvido 😥.
## Espero les ayude en algo.
