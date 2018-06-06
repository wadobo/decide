Scripts para probar el cifrado
==============================

 * **test-encrypt.py**

Script que cifra un mensaje. Recibe como primer parámetro la clave pública
en formato "P,G,Y" y el mensaje en claro. Ha de ser un número entero.

```
$ python test-encrypt.py $(cat PK) 23
> 131,142
```

 * **test-decrypt.py**

Script que descifra un mensaje. Recibe como primer parámetro la clave
privada en formato "P,G,Y,X" y el mensaje cifrado "A,B". Devuelve el
mensaje descifrado.

```
$ python test-decrypt.py $(cat SK) 131,142
> 23
```

 * **js/index.html**

Web de ejemplo que cifra un mensaje usando una clave pública con
javascript. Se puede abrir directamente con el navegador:

```
$ firefox js/index.html
```

Se puede verificar que funciona correctamente con el script
`test-decrypt.py` parándole los parámetros que nos muestra la web y
verificando que el mensaje es correcto.
