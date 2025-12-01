# Guía de Configuración EmailJS - La Creativa

Esta guía te mostrará paso a paso cómo configurar el envío automático de emails con las facturas generadas.

## ⏱️ Tiempo estimado: 10-15 minutos

---

## Paso 1: Crear Cuenta en EmailJS

1. Ve a **https://www.emailjs.com/**
2. Haz clic en **"Sign Up"** (Registrarse)
3. Regístrate con tu email (puedes usar Google Sign-In)
4. Verifica tu email si es necesario

---

## Paso 2: Añadir Servicio de Email

1. Una vez dentro, ve a **"Email Services"** en el menú lateral
2. Haz clic en **"Add New Service"**
3. Selecciona **Gmail** (recomendado)
4. Sigue las instrucciones:
   - Haz clic en **"Connect Account"**
   - Selecciona tu cuenta de Gmail
   - Autoriza EmailJS para enviar emails
5. Dale un nombre al servicio (ej: "La Creativa Gmail")
6. **Guarda el Service ID** - lo necesitarás después
7. Haz clic en **"Create Service"**

> **Nota**: Si usas Gmail, puede que necesites activar "Acceso de aplicaciones menos seguras" o crear una "Contraseña de aplicación" en tu cuenta de Google.

---

## Paso 3: Crear Plantilla de Email

1. Ve a **"Email Templates"** en el menú lateral
2. Haz clic en **"Create New Template"**
3. Configura la plantilla:

### Configuración de la Plantilla:

**From Name:** `La Creativa`  
**From Email:** (tu email de Gmail)  
**Subject:** `Albarà La Creativa - {{client_name}}`

**Content (Mensaje del email):**
```
Hola {{client_name}},

Adjunto encontrarás el albarà número {{invoice_number}} por un importe de {{amount}}€.

Detalles de los productos:
{{products}}

Gracias por confiar en La Creativa.

Saludos,
La Creativa
Carrer del Bruc 1, 08600 Berga, Barcelona
Tel. 693 00 45 22 - 93 194 53 92
hola@lacreativaberga.cat
```

**To Email:** `{{to_email}}`

### Variables de la plantilla:
- `{{to_email}}` - Email del cliente (automático)
- `{{client_name}}` - Nombre del cliente
- `{{invoice_number}}` - Número de factura
- `{{amount}}` - Total de la factura
- `{{products}}` - Lista de productos

4. **Configurar adjunto PDF**:
   - En la sección "Attachments", añade:
   - **Attachment name:** `Factura_{{invoice_number}}.pdf`
   - **Attachment content:** `{{pdf_attachment}}`
   - **Encoding:** `base64`

5. Haz clic en **"Save"**
6. **Guarda el Template ID** - lo necesitarás después

---

## Paso 4: Obtener tu Public Key

1. Ve a **"Account"** → **"General"** en el menú
2. Busca **"API Keys"** o **"Public Key"**
3. **Copia tu Public Key**

---

## Paso 5: Actualizar script.js

Ahora que tienes las 3 claves, actualiza el archivo `script.js`:

1. Abre el archivo **`script.js`**
2. En las líneas 3-5, reemplaza los valores:

```javascript
const EMAILJS_PUBLIC_KEY = 'TU_PUBLIC_KEY_AQUI';     // Reemplaza con tu Public Key
const EMAILJS_SERVICE_ID = 'TU_SERVICE_ID_AQUI';      // Reemplaza con tu Service ID
const EMAILJS_TEMPLATE_ID = 'TU_TEMPLATE_ID_AQUI';    // Reemplaza con tu Template ID
```

3. Guarda el archivo

---

## Paso 6: Probar el Envío de Emails

1. Abre tu aplicación en el navegador (`index.html`)
2. Rellena el formulario de factura:
   - **Importante**: Usa un email válido (puede ser el tuyo para probar)
   - Rellena todos los campos obligatorios
3. Haz clic en **"Generar Factura"**
4. Deberías ver:
   - ✅ El PDF se descarga automáticamente
   - ✅ Mensaje de éxito: "Factura generada i enviada correctament"
5. Revisa tu bandeja de entrada (y spam por si acaso)

---

## 🎯 Resultado Esperado

Cuando todo esté configurado correctamente:
- El cliente recibirá un email con:
  - Asunto personalizado con su nombre
  - Detalles de la factura en el cuerpo del email
  - PDF de la factura adjunto
- Tú recibirás una copia en tu email (si lo configuras así en EmailJS)

---

## ❓ Solución de Problemas

### El email no se envía
1. Verifica que las 3 claves están correctamente copiadas en `script.js`
2. Abre la consola del navegador (F12) y busca errores
3. Verifica que autorizaste EmailJS en tu cuenta de Gmail
4. Revisa los límites del plan gratuito (200 emails/mes)

### El PDF no llega como adjunto
1. Verifica que en la plantilla de EmailJS configuraste:
   - Attachment name: `Factura_{{invoice_number}}.pdf`
   - Attachment content: `{{pdf_attachment}}`
   - Encoding: `base64`

### El email va a spam
1. Configura SPF/DKIM en EmailJS (opciones avanzadas)
2. Pide a los clientes que añadan tu email a contactos

---

## 📊 Límites del Plan Gratuito

- ✅ 200 emails/mes
- ✅ Plantillas ilimitadas
- ✅ Servicios ilimitados
- ✅ Sin tarjeta de crédito necesaria

Si necesitas más emails, hay planes de pago desde $7/mes.

---

## 🔐 Seguridad

⚠️ **Importante**: Las claves de EmailJS están en el frontend (`script.js`), por lo que son públicas. Esto es normal con EmailJS y no es un problema de seguridad porque:
- EmailJS tiene protecciones anti-spam
- Solo pueden enviar emails, no leer tu bandeja
- Puedes establecer límites y dominios permitidos en la configuración de EmailJS

---

## ✅ Checklist Final

- [ ] Cuenta EmailJS creada
- [ ] Servicio de Gmail configurado y conectado
- [ ] Plantilla de email creada con todas las variables
- [ ] Adjunto PDF configurado en la plantilla
- [ ] Public Key copiada
- [ ] Service ID copiado
- [ ] Template ID copiado
- [ ] `script.js` actualizado con las 3 claves
- [ ] Prueba realizada con éxito
- [ ] Email recibido con PDF adjunto

---

¡Listo! Ahora tu aplicación enviará automáticamente emails con las facturas generadas. 🎉
