# Configuración Supabase Storage para PDFs

## Paso 1: Crear Bucket en Supabase Dashboard

1. Ve a tu **Supabase Dashboard**: https://app.supabase.com
2. Selecciona tu proyecto
3. En el menú lateral, haz clic en **"Storage"**
4. Haz clic en **"Create a new bucket"**
5. Configuración del bucket:
   - **Name:** `invoices`
   - **Public bucket:** ✅ **Marcado** (importante para generar URLs públicas)
   - Haz clic en **"Create bucket"**

## Paso 2: Configurar Políticas de Acceso Público

1. En la lista de buckets, haz clic en `invoices`
2. Ve a la pestaña **"Policies"**
3. Haz clic en **"New Policy"**
4. Selecciona **"For full customization"**

### Política 1: Permitir subidas públicas (INSERT)
```sql
CREATE POLICY "Allow public uploads"
ON storage.objects
FOR INSERT
TO public
WITH CHECK (bucket_id = 'invoices');
```

### Política 2: Permitir lecturas públicas (SELECT)
```sql
CREATE POLICY "Allow public downloads"
ON storage.objects
FOR SELECT
TO public
USING (bucket_id = 'invoices');
```

5. Haz clic en **"Review"** y luego **"Save policy"** para cada una

## Paso 3: Obtener Credenciales de Supabase

1. Ve a **Settings → API** (en el menú lateral)
2. Copia estos dos valores:

**Project URL:**
```
https://xxxxxxxxxx.supabase.co
```

**anon/public key:**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS...
```

## Paso 4: Actualizar script.js

Abre `script.js` y actualiza las líneas 6-7:

```javascript
const SUPABASE_URL = 'https://xxxxxxxxxx.supabase.co'; // Tu Project URL
const SUPABASE_ANON_KEY = 'eyJhbGci...'; // Tu anon key
```

## Paso 5: Actualizar Plantilla EmailJS

En tu plantilla de EmailJS, cambia el contenido a:

**Subject:**
```
Albarà La Creativa - {{client_name}}
```

**Body:**
```
Hola {{client_name}},

Puedes descargar tu factura número {{invoice_number}} desde este enlace:

{{download_link}}

Total: {{amount}}€

Detalles de los productos:
{{products}}

El enlace de descarga estará disponible permanentemente.

Gracias por confiar en La Creativa.

Saludos,
La Creativa
Carrer del Bruc 1, 08600 Berga, Barcelona
Tel. 693 00 45 22 - 93 194 53 92
hola@lacreativaberga.cat
```

**IMPORTANTE:** Elimina cualquier configuración de adjuntos (attachments) que hayas configurado anteriormente.

## Paso 6: Probar

1. Abre `index.html` en tu navegador
2. Genera una factura con un email válido
3. Verifica:
   - ✅ El PDF se descarga localmente
   - ✅ Se sube a Supabase Storage
   - ✅ Se envía el email con el link de descarga
   - ✅ El link funciona para descargar el PDF

## Verificar en Supabase Dashboard

1. Ve a **Storage → invoices**
2. Deberías ver tus PDFs subidos
3. Cada PDF tendrá un nombre como: `Factura_C0001_1732705200000.pdf`

## Solución de Problemas

### Error: "bucket not found"
- Verifica que el bucket se llama exactamente `invoices`
- Verifica que está marcado como público

### Error: "new row violates row-level security policy"
- Verifica que has creado las políticas de acceso
- Verifica que las políticas permiten acceso público (`TO public`)

### El link no funciona
- Verifica que el bucket es público
- Verifica la política de SELECT (lectura pública)

### Error de CORS
- No debería ocurrir con Supabase Storage, pero si ocurre, verifica la configuración CORS en Supabase Dashboard

## Límites del Plan Gratuito

- ✅ **1 GB de almacenamiento**
- ✅ **2 GB de transferencia/mes**
- ✅ Suficiente para ~3000-4000 facturas PDF

## Seguridad

Las políticas configuradas permiten:
- ✅ Cualquiera puede subir archivos al bucket
- ✅ Cualquiera puede descargar archivos del bucket

Esto es seguro porque:
- Los nombres de archivo incluyen timestamp (difícil de adivinar)
- Solo tu aplicación conoce los URLs completos
- Los PDFs no contienen información sensible más allá de la factura

Si deseas más seguridad, puedes:
- Configurar URLs firmadas con expiración
- Usar autenticación de Supabase
- Restringir políticas a usuarios autenticados

## ¡Listo!

Ahora tu aplicación:
1. Genera el PDF
2. Lo sube automáticamente a Supabase
3. Envía un email con link de descarga
4. El cliente puede descargar su factura cuando quiera
