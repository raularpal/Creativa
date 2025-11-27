# Checklist: Configuración de envío de emails

## ✅ Completado
- [x] Plantilla de EmailJS creada
- [x] Código implementado en script.js
- [x] Supabase JS añadido a index.html

## ⏳ Pendiente (30 minutos)

### 1. Configurar Supabase Storage (10 min)

#### Paso 1.1: Crear Bucket
1. Ve a https://app.supabase.com
2. Selecciona tu proyecto
3. Menú lateral → **Storage**
4. Click **"Create a new bucket"**
5. Configuración:
   - **Name:** `invoices`
   - **Public bucket:** ✅ **MARCAR**
   - Click **"Create bucket"**

#### Paso 1.2: Configurar Políticas de Acceso
1. Click en el bucket `invoices`
2. Pestaña **"Policies"**
3. Click **"New Policy"** → **"For full customization"**

**Política 1 - Permitir uploads:**
```sql
CREATE POLICY "Allow public uploads"
ON storage.objects
FOR INSERT
TO public
WITH CHECK (bucket_id = 'invoices');
```
Click **"Review"** → **"Save policy"**

**Política 2 - Permitir descargas:**
```sql
CREATE POLICY "Allow public downloads"
ON storage.objects
FOR SELECT
TO public
USING (bucket_id = 'invoices');
```
Click **"Review"** → **"Save policy"**

---

### 2. Obtener Credenciales de Supabase (2 min)

1. En Supabase Dashboard → **Settings** → **API**
2. Copia estos dos valores:

**Project URL:**
```
https://xxxxxxxxxxx.supabase.co
```
(Guarda este valor - lo necesitarás en el siguiente paso)

**anon/public key:**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ey...
```
(Guarda este valor - lo necesitarás en el siguiente paso)

---

### 3. Actualizar script.js con TODAS las credenciales (3 min)

Abre `/Users/arpal/.gemini/antigravity/scratch/creativa_dades/script.js`

**Líneas 3-5 (EmailJS):**
```javascript
const EMAILJS_PUBLIC_KEY = 'TU_PUBLIC_KEY_EMAILJS';
const EMAILJS_SERVICE_ID = 'TU_SERVICE_ID_EMAILJS';
const EMAILJS_TEMPLATE_ID = 'TU_TEMPLATE_ID_EMAILJS';
```

**Líneas 6-7 (Supabase):**
```javascript
const SUPABASE_URL = 'https://xxxxxxxxxxx.supabase.co'; // Del paso 2
const SUPABASE_ANON_KEY = 'eyJhbGci...'; // Del paso 2
```

**IMPORTANTE:** Reemplaza TODOS los valores. Necesitas 5 claves en total:
- ✅ 3 de EmailJS (public key, service ID, template ID)
- ✅ 2 de Supabase (URL, anon key)

---

### 4. Probar el Sistema Completo (5 min)

1. Abre `index.html` en tu navegador
2. Rellena el formulario:
   - Cliente: "Prueba Test"
   - Email: **TU EMAIL** (para recibir la prueba)
   - Teléfono: "600000000"
   - Al menos 1 producto
3. Click **"Generar i Enviar Factura"**

**Deberías ver:**
- ✅ PDF se descarga automáticamente
- ✅ Mensaje: "Pujant PDF a Supabase..."
- ✅ Mensaje: "Enviant correu..."
- ✅ Mensaje final: "✓ Factura generada i enviada correctament"

4. **Verifica el email:**
   - Revisa tu bandeja de entrada (y spam)
   - Debe llegar un email con el link de descarga
   - Click en el link → Debe descargar el PDF

5. **Verifica Supabase:**
   - Ve a Supabase Dashboard → Storage → invoices
   - Deberías ver el PDF subido

---

## 🆘 Si algo falla

### No se sube el PDF a Supabase
- Abre consola del navegador (F12)
- Mira errores en rojo
- Verifica que el bucket se llama exactamente `invoices`
- Verifica que tiene las 2 políticas configuradas

### No se envía el email
- Verifica que las 3 claves de EmailJS están correctas
- Abre consola del navegador para ver errores
- Verifica que la plantilla existe en EmailJS

### El link del email no funciona
- Verifica que el bucket es público
- Verifica la política de SELECT

---

## ✅ Cuando todo funcione

Habrás completado el sistema de envío de facturas por email. Cada vez que generes una factura:
1. Se descargará el PDF localmente
2. Se subirá a Supabase automáticamente
3. Se enviará un email al cliente con el link de descarga

**¿Por dónde quieres empezar? Te recomiendo seguir el orden:**
1. Primero → Supabase Storage (pasos 1.1 y 1.2)
2. Segundo → Copiar credenciales (paso 2)
3. Tercero → script.js (paso 3)
4. Cuarto → Probar (paso 4)

Dime cuando completes el paso 1 (Supabase Storage) y te ayudo con el siguiente.
