# ✅ Credenciales de Supabase Configuradas

Las credenciales de Supabase ya están en `script.js`:
- ✅ **Project URL:** https://tpnycyjwqnfqqpwukplb.supabase.co
- ✅ **Anon Key:** Configurada

---

## ⚠️ IMPORTANTE: Aún faltan las credenciales de EmailJS

Para que funcione el envío de emails, necesitas configurar **3 credenciales más** de EmailJS en `script.js` (líneas 2-4):

```javascript
const EMAILJS_PUBLIC_KEY = 'YOUR_PUBLIC_KEY';     // ← Reemplazar
const EMAILJS_SERVICE_ID = 'YOUR_SERVICE_ID';      // ← Reemplazar  
const EMAILJS_TEMPLATE_ID = 'YOUR_TEMPLATE_ID';    // ← Reemplazar
```

---

## 📋 Cómo obtener las credenciales de EmailJS

### 1. Public Key (Línea 2)
1. Ve a https://dashboard.emailjs.com/
2. Click en **"Account"** (arriba derecha)
3. Busca **"API Keys"** o **"Public Key"**
4. Copia el valor (ejemplo: `user_xxxxxxxxxx` o similar)

### 2. Service ID (Línea 3)  
1. En EmailJS Dashboard → **"Email Services"**
2. Verás el servicio que configuraste (Gmail)
3. Copia el **"Service ID"** (ejemplo: `service_xxxxxx`)

### 3. Template ID (Línea 4)
1. En EmailJS Dashboard → **"Email Templates"**
2. Busca la plantilla que creaste
3. Copia el **"Template ID"** (ejemplo: `template_xxxxxx`)

---

## 🎯 Próximo Paso

**Opción A:** Dame las 3 credenciales de EmailJS y las configuro yo  
**Opción B:** Actualizalas tú mismo en `script.js` líneas 2-4

Cuando estén configuradas, probamos el sistema completo generando una factura de prueba.

---

## 🧪 Cómo Probar (cuando tengas las credenciales)

1. Abre `index.html` en Chrome/Firefox
2. Rellena el formulario:
   - Cliente: "Test Cliente"
   - Email: **TU EMAIL PERSONAL**
   - Teléfono: "600000000"  
   - Producto 1: "Prueba", Precio: 10, Cantidad: 1
3. Click **"Generar i Enviar Factura"**

**Deberías ver:**
- ✅ PDF se descarga
- ✅ "Pujant PDF a Supabase..."
- ✅ "Enviant correu..."
- ✅ "✓ Factura generada i enviada correctament"

4. Revisa tu email → Click en el link → Descarga el PDF

---

¿Tienes ya las credenciales de EmailJS o necesitas ayuda para obtenerlas?
